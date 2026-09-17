#!/usr/bin/env python3
"""Génère les PDF des notes d'orateur à partir des quatre fichiers markdown.

    python3 tools/notes-pdf.py

Prérequis : pandoc et pdfLaTeX (avec titlesec, fancyhdr, enumitem, needspace).
Les PDF sont déposés à côté des PDF de planches : ceux des versions anglaises
dans le dossier de leur version française, comme le reste du projet.
"""
import os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER = os.path.join(ROOT, 'tools', 'notes-pdf-header.tex')

JOBS = [
    dict(md='LONG/notes-orateur.md', lang='fr',
         out='LONG/Notes_Orateur_Segmentation_Semantique_Teledetection_LONG.pdf',
         run="Notes d'orateur — Segmentation sémantique en télédétection — version longue"),
    dict(md='SHORT/notes-orateur.md', lang='fr',
         out='SHORT/Notes_Orateur_Segmentation_Semantique_Teledetection_SHORT.pdf',
         run="Notes d'orateur — Segmentation sémantique en télédétection — version courte"),
    dict(md='LONG/EN/speaker-notes.md', lang='en',
         out='LONG/Speaker_Notes_Semantic_Segmentation_Remote_Sensing_LONG.pdf',
         run='Speaker notes — Semantic segmentation in remote sensing — long version'),
    dict(md='SHORT/EN/speaker-notes.md', lang='en',
         out='SHORT/Speaker_Notes_Semantic_Segmentation_Remote_Sensing_SHORT.pdf',
         run='Speaker notes — Semantic segmentation in remote sensing — short version'),
]

# Étiquettes de conduite, mises en couleur dans le PDF
LABELS = ['À dire.', 'Transition.', 'En réserve.', 'Say.', 'In reserve.']


def build(job, workdir):
    src = open(os.path.join(ROOT, job['md']), encoding='utf-8').read()
    m = re.match(r'#\s+(.*?)\n', src)
    if not m:
        raise SystemExit(f"{job['md']} : pas de titre de niveau 1 en tête")
    title, body = m.group(1).strip(), src[m.end():].lstrip('\n')

    # « À dire » / « Transition » / « En réserve » sont sur des lignes
    # consécutives : markdown les fondrait en un seul paragraphe. On les sépare,
    # pour qu'à l'oral l'œil trouve chaque étiquette d'un coup.
    body = re.sub(r'\n(\*\*(?:Transition\.|En réserve\.|In reserve\.)\*\*)', r'\n\n\1', body)

    base = os.path.splitext(os.path.basename(job['out']))[0]
    md_tmp, tex_tmp = f'{workdir}/{base}.md', f'{workdir}/{base}.tex'
    hdr_tmp = f'{workdir}/{base}.header.tex'
    open(md_tmp, 'w', encoding='utf-8').write(body)
    open(hdr_tmp, 'w', encoding='utf-8').write(
        f"\\newcommand{{\\runninghead}}{{{job['run']}}}\n"
        + open(HEADER, encoding='utf-8').read())

    subprocess.run(['pandoc', md_tmp, '-s', '-o', tex_tmp,
                    '-M', f'title={title}', '-V', f'lang={job["lang"]}',
                    '-V', 'documentclass=article', '-V', 'fontsize=10pt',
                    '-V', 'papersize=a4',
                    '-V', 'geometry:margin=2.1cm', '-V', 'geometry:top=2.3cm',
                    '--shift-heading-level-by=-1', '-H', hdr_tmp], check=True)

    tex = open(tex_tmp, encoding='utf-8').read()
    for lab in LABELS:
        tex = tex.replace('\\textbf{%s}' % lab, '\\notelabel{%s}' % lab)
    open(tex_tmp, 'w', encoding='utf-8').write(tex)

    for _ in range(2):        # deux passes : table des matières interne, renvois
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            os.path.basename(tex_tmp)],
                           cwd=workdir, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"ÉCHEC {base}", file=sys.stderr)
        print('\n'.join(l for l in r.stdout.split('\n') if l.startswith('!'))[:1500],
              file=sys.stderr)
        return False
    shutil.copyfile(f'{workdir}/{base}.pdf', os.path.join(ROOT, job['out']))
    print(f"{job['out']}")
    return True


def main():
    for tool in ('pandoc', 'pdflatex'):
        if shutil.which(tool) is None:
            raise SystemExit(f'{tool} est introuvable.')
    with tempfile.TemporaryDirectory() as workdir:
        ok = all(build(j, workdir) for j in JOBS)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
