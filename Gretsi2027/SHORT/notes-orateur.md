# Notes d'orateur — version courte (24 planches, ≈ 20 min)

Document à garder sous les yeux pendant l'exposé : pour chaque planche, ce qu'il y a à dire, la phrase qui amène la suivante, et ce qu'on ne sort que si on a le temps.

## Avant de commencer

- **Durée** : six blocs, 20 minutes pleines, hors questions.
  - Introduction (planches 1 à 5) — 4 min 30 au compteur.
  - Du pixel au contexte (planches 6 à 9) — 9 min.
  - Modèles markoviens et bayésiens (planches 10 à 13) — 13 min 05.
  - Représentations spectro-spatiales et variationnelles (planches 14 à 16) — 15 min 40.
  - Apprentissage profond et modèles de fondation (planches 17 et 18) — 18 min.
  - Défis ouverts, conclusion et remerciements (planches 19 à 21) — 20 min.
  - Planches 22 à 24 : bibliographie, hors minutage, uniquement sur question.

- **Le fil directeur en une phrase** : l'histoire de la segmentation sémantique en télédétection est celle d'une intégration progressive de niveaux croissants de contexte, et sous cette progression un même principe revient de bout en bout — une attache aux données plus une régularisation.

- **Trois idées à faire passer coûte que coûte**
  1. Ce n'est ni un catalogue de méthodes ni une trajectoire linéaire : plusieurs traditions scientifiques se sont progressivement rejointes.
  2. Une même forme traverse cinquante ans de travaux : attache aux données plus régularisation, des champs de Markov aux fonctions de perte des réseaux profonds.
  3. L'apprentissage profond ne supprime pas les concepts antérieurs, comme le contexte spatial, le multi-échelle, la fusion ou la hiérarchie des objets : il les apprend au lieu de les construire à la main.

- **Si vous êtes en retard**, sacrifier dans cet ordre :
  1. Planche 15, morphologie mathématique (45 s) — la planche 14 suffit à porter l'idée spectro-spatiale.
  2. Planche 12, optimisation des MRF (50 s) — enchaîner directement de l'énergie aux CRF.
  3. Planche 8, méthodes discriminantes et d'ensemble (1 min 10) — en garder une phrase : elles améliorent la décision, pas la représentation.
  4. Planche 4, ce qui distingue la télédétection (1 min) — replier l'essentiel sur la planche 3.
  Ne jamais sacrifier les planches 5, 11 et 20 : ce sont le fil, l'équation et la conclusion.

## Déroulé

### Planche 1 — Segmentation sémantique en télédétection · 45 s · 45 s
**À dire.** Merci de m'accueillir dans cette session historique. En vingt minutes, je voudrais vous raconter comment la segmentation sémantique s'est construite en télédétection : comment, en une cinquantaine d'années, on est passé de la décision prise pixel par pixel sur une signature spectrale aux modèles de fondation géospatiaux d'aujourd'hui. Cet exposé s'appuie sur un article écrit avec Martina Pastorino et Gabriele Moser, de l'Università di Genova, à paraître dans Traitement du Signal et des Images.
**Transition.** Voici le chemin que je vous propose de suivre.
**En réserve.** L'article est également disponible comme rapport de recherche Inria, le RR-9631, déposé sur HAL sous la référence hal-05742224 depuis septembre 2026.

### Planche 2 — Sommaire · 30 s · 1 min 15
**À dire.** Six étapes, dans l'ordre chronologique : après une courte introduction, nous irons du pixel au contexte, puis aux modèles markoviens et bayésiens, aux représentations spectro-spatiales et variationnelles, à l'apprentissage profond et aux modèles de fondation, et nous finirons sur les défis ouverts. Je vous demande de ne pas y voir un catalogue de méthodes : c'est une seule histoire, avec un fil que je vous donnerai dans trois planches.
**Transition.** Commençons par dire précisément de quoi nous parlons.

### Planche 3 — De l'image à la carte thématique · 1 min 15 · 2 min 30
**À dire.** La segmentation sémantique consiste à associer à chaque pixel d'une image une étiquette prise dans un ensemble prédéfini de classes. Le mot lui-même s'est imposé avec l'essor de l'apprentissage profond, au milieu des années 2010, mais le problème, lui, est étudié depuis des décennies en télédétection sous les noms de classification supervisée, de classification pixel à pixel ou de classification contextuelle — on les trouve déjà chez Duda et Hart en 1973, chez Swain et Davis en 1978, chez Richards en 1986. Ce qu'on produit, c'est une carte dense : chaque pixel reçoit une interprétation, et c'est exactement ce qui distingue cette tâche de la segmentation dite de bas niveau, qui se contente de partitionner l'image en régions homogènes sans leur donner de sens. En télédétection, l'enjeu est de transformer les observations satellitaires en cartes d'occupation et d'utilisation du sol, comme sur l'exemple que vous voyez ici.
**Transition.** Reste à comprendre pourquoi ce problème, chez nous, ne se pose pas comme ailleurs.
**En réserve.** L'image aérienne et la carte viennent du jeu de données Zeebruges, publié par le comité technique d'analyse d'image et de fusion de données, l'IADF, de l'IEEE GRSS ; les images et la vérité terrain ont été fournies par l'Académie royale militaire belge et l'ONERA.

### Planche 4 — Ce qui distingue la télédétection · 1 min · 3 min 30
**À dire.** Nos images ne sont pas des images naturelles. Elles peuvent venir de capteurs optiques, de radars à synthèse d'ouverture ou de LiDAR ; leurs résolutions spatiales et spectrales sont très variables ; elles sont acquises à des dates différentes et combinent souvent plusieurs modalités. Et elles décrivent des scènes géographiques complexes, dont les propriétés changent selon les régions, selon les saisons, selon les conditions d'acquisition. C'est pour cette raison que l'évolution du domaine ne se réduit pas à une adaptation des avancées de la vision par ordinateur : elle résulte d'une convergence entre la reconnaissance statistique des formes, le traitement du signal et des images, la modélisation probabiliste et, plus récemment seulement, l'apprentissage profond.
**Transition.** Posons maintenant le problème de façon formelle, et je vous donnerai le fil de l'exposé.
**En réserve.** À cette liste, l'article ajoute encore la morphologie mathématique, la géométrie stochastique et l'analyse orientée objet : sept traditions scientifiques au total, qui se sont progressivement rejointes.

### Planche 5 — Fil directeur · 1 min · 4 min 30
**À dire.** Formellement, une image de télédétection est une fonction I définie sur le domaine spatial, noté grand oméga, à valeurs dans R puissance d, où d est le nombre de variables disponibles : des bandes spectrales, mais aussi des polarisations radar, des mesures LiDAR, des indices, des modèles numériques de terrain ou d'autres données auxiliaires. Segmenter sémantiquement, c'est estimer une seconde fonction f, qui va du même domaine spatial vers l'ensemble fini des classes sémantiques. Et voici le fil que je vous demande de retenir : toute l'histoire du domaine peut se lire comme une intégration progressive de niveaux croissants de contexte — l'information spectrale locale, puis la cohérence spatiale, puis les frontières, les régions et les objets, puis l'apprentissage des représentations, et enfin les modèles de fondation. Nous retrouverons cette frise à l'identique en conclusion.
**Transition.** Revenons donc au tout début de cette histoire, quand il n'y avait que le pixel.
**En réserve.** Un second fil, plus discret, traverse également tout l'exposé : celui d'une énergie en deux morceaux, l'un qui colle aux observations, l'autre qui impose de la régularité. Il apparaîtra avec les champs de Markov et ne nous quittera plus.

### Planche 6 — Les premières approches : pixel à pixel · 1 min 10 · 5 min 40
**À dire.** Tout part des premiers satellites d'observation de la Terre : le programme Landsat, en optique, au début des années 1970, et SeaSat, en radar, à la fin de la même décennie. Ces capteurs créent un besoin nouveau, celui de méthodes automatiques capables de produire des cartes d'occupation du sol à partir d'images multispectrales ou radar. On s'appuie alors sur les fondements de la reconnaissance statistique des formes : chaque pixel devient un vecteur d'observations — les réponses radiométriques dans les différentes bandes, les intensités radar, des indices, des données auxiliaires — et on lui attribue la classe la plus probable selon une règle de décision bayésienne. Sous l'hypothèse que les observations de chaque classe suivent une loi gaussienne multivariée, on obtient le classifieur du maximum a posteriori, qui restera la méthode de référence pendant plusieurs décennies.
**Transition.** Cette réussite a duré longtemps ; ses limites, elles, sont apparues avec les progrès des capteurs.
**En réserve.** Ce classifieur MAP est souvent appelé, de manière informelle, classifieur du maximum de vraisemblance — le MLC des articles anglophones. Son succès s'explique par trois choses : une interprétation probabiliste simple, une mise en œuvre peu coûteuse et des performances satisfaisantes.

### Planche 7 — Deux limites : dimension et indépendance · 1 min 10 · 6 min 50
**À dire.** Deux limites, et elles sont structurelles. La première, c'est la malédiction de la dimension, le phénomène décrit par Hughes dès 1968 : ajouter des variables spectrales ne garantit pas de meilleures performances dès lors que le nombre d'échantillons d'apprentissage reste limité — autrement dit, les signatures spectrales seules ne suffisent pas. La seconde, c'est l'hypothèse d'indépendance des observations : chaque pixel est décidé isolément, sans qu'on exploite son voisinage, alors même que les objets géographiques sont fortement corrélés spatialement — une parcelle agricole, une forêt, une zone urbaine, un réseau routier. La conséquence est sous vos yeux, à droite : des cartes bruitées, l'effet « poivre et sel », et d'autant plus marqué que la résolution spatiale augmente.
**Transition.** C'est ce constat qui va progressivement déplacer le problème d'une classification spectrale vers une interprétation spatiale des scènes.
**En réserve.** La carte de droite est issue des travaux de Gabriele Moser, Sebastiano Serpico et Jón Atli Benediktsson, publiés dans les Proceedings of the IEEE en 2013.

### Planche 8 — Méthodes discriminantes et d'ensemble · 1 min 10 · 8 min
**À dire.** À partir de la fin des années 1990, une autre branche de l'histoire se développe : plutôt que de modéliser la loi des observations, on estime directement les frontières de décision entre classes. Les machines à vecteurs de support s'imposent très vite — Cortes et Vapnik en 1995, Vapnik en 1998 — grâce au principe de maximisation de la marge, qui leur donne d'excellentes capacités de généralisation même en grande dimension ; les méthodes à noyaux étendent ensuite ce cadre aux problèmes non linéaires sans perdre la convexité. En parallèle, les forêts aléatoires de Breiman, en 2001, agrègent par vote des arbres appris sur des sous-ensembles aléatoires d'observations et de variables : peu de réglages, une bonne robustesse au bruit, et des mesures d'importance des variables très utiles pour interpréter les modèles. Mais je voudrais insister sur un point, parce qu'il commande toute la suite : appliquées directement aux vecteurs d'observations, ces méthodes améliorent la fonction de décision, pas la représentation — elles restent essentiellement des classifieurs pixel à pixel.
**Transition.** Reste donc entière la question qu'aucune d'elles ne traite : l'organisation spatiale de la scène.
**En réserve.** Des noyaux spécifiquement adaptés aux observations géospatiales ont été développés ensuite : la référence de fond est le livre de Schölkopf et Smola en 2002, et pour la télédétection l'ouvrage de Camps-Valls et Bruzzone en 2009 et la revue de Mountrakis, Im et Ogole dans l'ISPRS Journal en 2011. Pour les forêts aléatoires en télédétection, Gislason, Benediktsson et Sveinsson en 2006.

### Planche 9 — L'apport du contexte spatial · 1 min · 9 min
**À dire.** Regardez ces trois images. À gauche, une image IKONOS à 4 mètres de résolution, en fausses couleurs ; au centre, la classification pixel à pixel ; à droite, la classification contextuelle de la même scène. Dès les années 1980-1990, une part importante de la recherche s'oriente vers l'introduction du contexte spatial, en partant d'une idée très simple : dans une scène de télédétection, un pixel a beaucoup plus de chances d'appartenir à la même classe que ses voisins immédiats qu'à une classe totalement différente. La classification cesse alors d'être une succession de décisions indépendantes : les étiquettes doivent être estimées conjointement, pour produire une représentation cohérente de la scène.
**Transition.** Restait à donner à cette intuition un cadre théorique rigoureux — ce sera l'objet de la section suivante.
**En réserve.** L'article distingue trois niveaux de contexte : le contexte local, entre pixels voisins ou dans des fenêtres de taille limitée ; le contexte régional, qui décrit des ensembles de pixels par leur texture, leur forme, leur taille, et qui annonce les approches orientées objet ; et le contexte global, qui porte sur l'organisation générale de la scène. Cette hiérarchie restera structurante jusqu'aux architectures profondes contemporaines.

### Planche 10 — Les champs de Markov : première formalisation · 1 min 10 · 10 min 10
**À dire.** Les champs de Markov constituent la première formalisation probabiliste générale de cette idée, et ils deviennent très vite l'un des cadres théoriques les plus influents du domaine — Geman et Geman en 1984, Besag en 1986. Le principe : les étiquettes ne sont plus des variables indépendantes, mais un ensemble de variables aléatoires définies sur un graphe de voisinage. Sous les hypothèses de Markov, et grâce à l'équivalence entre champs de Markov et distributions de Gibbs, la recherche de la carte optimale s'écrit comme une estimation au sens du maximum a posteriori — et, par le théorème de Bayes, cette maximisation devient équivalente à la minimisation d'une fonction d'énergie. C'est cette équivalence qui donne aux champs de Markov leur portée : un cadre unique pour relier les données locales et la cohérence spatiale.
**Transition.** Regardons maintenant de plus près ce que contient cette énergie, parce que c'est là que se trouve le fil de tout l'exposé.
**En réserve.** Pour une présentation d'ensemble des champs de Markov en segmentation, nous renvoyons à la monographie que j'ai écrite avec Zoltan Kato, parue dans Foundations and Trends in Signal Processing en 2012.

### Planche 11 — Attache aux données + régularisation · 1 min · 11 min 10
**À dire.** Voici, à mon sens, l'équation la plus importante de cet exposé. L'énergie se décompose en deux termes : un terme d'attache aux données, dérivé de la vraisemblance des observations, et un terme de régularisation spatiale, qui favorise la cohérence entre pixels voisins ; le paramètre bêta contrôle le compromis entre fidélité aux observations et régularité de la solution. Concrètement, on définit un système de voisinage — du premier ou du second ordre, comme sur les deux figures de droite — et les potentiels de clique pénalisent certaines configurations d'étiquettes, typiquement les changements de classe entre pixels adjacents. Retenez cette forme : attache aux données plus régularisation. Nous allons la retrouver dans les méthodes variationnelles, et jusque dans les fonctions de perte des réseaux profonds.
**Transition.** Reste une difficulté pratique, et elle est sérieuse : trouver la configuration qui minimise cette énergie.
**En réserve.** La segmentation résulte ainsi d'un compromis entre l'information apportée par les données et une hypothèse explicite de cohérence spatiale — c'est-à-dire, en termes bayésiens, entre la vraisemblance et l'a priori.

### Planche 12 — Optimisation et usages des MRF · 50 s · 12 min
**À dire.** Minimiser cette énergie est un problème d'optimisation combinatoire difficile, et une part importante des travaux a donc porté sur des stratégies sous-optimales, mais exploitables en pratique : l'algorithme ICM, le recuit simulé, l'échantillonneur de Gibbs, puis les coupes de graphes de Boykov, Veksler et Zabih en 2001 et la propagation de croyance avec boucles. Ces modèles sont ensuite devenus un outil de référence pour la classification contextuelle, la segmentation multisource, la restauration, la détection de changements et la fusion de données optiques, radar ou LiDAR. Mais leur apport dépasse largement ces applications : ils fournissent une formulation probabiliste générale de la régularisation spatiale, et c'est à ce titre qu'ils ont durablement influencé tout ce qui a suivi.
**Transition.** Y compris, et c'est ce que je voudrais vous montrer maintenant, l'apprentissage profond lui-même.
**En réserve.** Le recuit simulé renvoie à Kirkpatrick en 1984, l'échantillonneur de Gibbs à Geman et Geman en 1984, la propagation de croyance avec boucles à Tanaka, Inoue et Titterington en 2003. Côté fusion et applications : Solberg, Taxt et Jain en 1996, Derin et Elliott en 1987, Moser et Serpico en 2013 — ce dernier travail combinant précisément SVM et champs de Markov dans un même cadre.

### Planche 13 — Des MRF aux CRF : un pont vers le profond · 1 min 05 · 13 min 05
**À dire.** Les champs conditionnels aléatoires prolongent naturellement cette famille : au lieu de décrire la loi jointe des observations et des étiquettes, ils représentent directement la distribution conditionnelle de la carte sachant les observations — Lafferty, McCallum et Pereira, en 2001. Ce déplacement, qui paraît technique, autorise des caractéristiques discriminantes complexes et s'intègre bien plus naturellement aux méthodes d'apprentissage supervisé. Les modèles entièrement connectés de Krähenbühl et Koltun, en 2011, préservent mieux les contours des objets ; puis les CRF entrent dans les architectures profondes, comme modules de raffinement ou comme couches différentiables — Zheng et ses collègues, en 2015 —, et c'est là que s'inscrivent nos travaux avec Martina Pastorino et Gabriele Moser, sur les cadres markoviens hiérarchiques et sur les CRF dont un réseau apprend les potentiels. Retenez de tout ce bloc markovien une idée qui va traverser le reste de l'exposé : une carte d'occupation du sol doit être compatible avec les observations locales, mais aussi avec l'organisation spatiale de la scène.
**Transition.** Jusqu'ici, nous avons régularisé les étiquettes ; une autre famille de méthodes va plutôt s'attaquer à ce que le classifieur reçoit en entrée.
**En réserve.** Les connexions mathématiques entre modèles graphiques probabilistes et apprentissage profond sont précisément l'objet de la synthèse que nous avons publiée avec Martina Pastorino, Gabriele Moser et Sebastiano Serpico dans IEEE Signal Processing Magazine en 2026.

### Planche 14 — Enrichir la représentation, pas seulement les étiquettes · 50 s · 13 min 55
**À dire.** Voici la distinction que je voudrais que vous gardiez de cette planche : les modèles contextuels régularisent les étiquettes, alors que les méthodes spectro-spatiales enrichissent les descripteurs, en amont, avant même la classification. Ce paradigme se développe dans les années 2000, porté par l'amélioration des résolutions : sur des images à haute résolution, on voit la structure interne des objets géographiques, une même classe peut présenter une forte variabilité spectrale, tandis que des objets différents ont parfois des signatures radiométriques très proches. Les signatures radiométriques seules ne suffisent donc plus : la texture, la forme, la taille, l'organisation spatiale et les relations de voisinage deviennent des informations aussi discriminantes que les valeurs spectrales elles-mêmes. Et cette logique-là prépare directement les représentations multi-échelles que les réseaux profonds apprendront ensuite d'eux-mêmes.
**Transition.** L'outil le plus emblématique de cette démarche nous vient de la morphologie mathématique.
**En réserve.** Sur l'intégration de l'intensité et de l'information texturale en imagerie radar, la référence ancienne est Dellepiane, Giusto, Serpico et Vernazza, en 1991 ; et la synthèse de Blaschke en 2010 fait le lien avec l'analyse orientée objet.

### Planche 15 — Morphologie mathématique et profils multi-échelles · 45 s · 14 min 40
**À dire.** Les opérateurs de base viennent de la morphologie mathématique — érosion, dilatation, ouvertures, fermetures — dont Serra puis Soille ont donné les traités de référence. Vous voyez ici, autour de l'image originale, ce que produisent une érosion et une dilatation : on ne change pas les étiquettes, on change ce que l'image donne à voir. L'étape décisive vient des profils morphologiques étendus de Benediktsson et ses collègues, en 2005, puis des profils d'attributs de Dalla Mura et ses collègues, en 2010 : ils décrivent la forme, la taille et le contraste des structures à plusieurs échelles. Associés à des machines à vecteurs de support — Fauvel et ses collègues, en 2008 —, ils deviennent une référence pour l'hyperspectral et la très haute résolution.
**Transition.** Une troisième famille, développée en parallèle, va exprimer la même exigence de cohérence spatiale, mais dans un langage continu.
**En réserve.** Ces descripteurs sont indépendants du classifieur : on peut les donner à des SVM, à des forêts aléatoires ou à des réseaux de neurones. Les gains observés viennent donc autant de la qualité de la représentation que du classifieur utilisé.

### Planche 16 — Méthodes variationnelles : régulariser la solution · 1 min · 15 min 40
**À dire.** À partir de la fin des années 1980, une autre famille d'approches développe une idée très proche de celle des champs de Markov, mais sans modéliser explicitement une loi de probabilité sur les étiquettes : on cherche la partition de l'image qui réalise le meilleur compromis entre la fidélité aux observations et la régularité spatiale ou géométrique de la solution. L'un des modèles fondateurs, c'est la fonctionnelle de Mumford et Shah, en 1989, qui recherche simultanément une approximation régulière de l'image et l'ensemble des discontinuités correspondant aux contours des objets. Regardez la forme de l'énergie écrite ici et comparez-la à celle de la planche 11 : c'est exactement le même principe, avec un paramètre qui règle le compromis. Cette proximité est aujourd'hui largement reconnue : modèles bayésiens, champs de Markov, méthodes variationnelles et formulations sur graphes ne sont souvent que différentes expressions d'un même principe.
**Transition.** Nous arrivons au moment où l'histoire change de régime, et ce moment porte une date.
**En réserve.** Avec Christophe Samson, Laure Blanc-Féraud et Gilles Aubert, nous avons proposé en 2000 une fonctionnelle qui unifie dans une même formulation la classification, la segmentation et la restauration — l'un des ponts directs entre approches probabilistes et modèles variationnels. En amont, il y a toute la lignée des contours actifs, puis les surfaces de niveau, qui gèrent automatiquement les changements de topologie, et enfin les modèles régionaux, plus robustes que les seuls gradients dans les images bruitées.

### Planche 17 — Apprendre profond · 1 min 10 · 16 min 50
**À dire.** 2012, c'est la bascule : lors du challenge ImageNet, le réseau AlexNet — Krizhevsky, Sutskever et Hinton — démontre une amélioration spectaculaire des performances en classification d'images naturelles. Le changement de fond n'est pas l'architecture, c'est le principe : on apprend conjointement la représentation et la fonction de décision, directement à partir des données, sans concevoir manuellement des descripteurs spectraux, texturaux ou géométriques. Trois architectures structurent la suite, à commencer par les réseaux entièrement convolutifs de Long, Shelhamer et Darrell, en 2015, qui produisent directement une prédiction dense à l'échelle du pixel : c'est celle que vous voyez à droite, appliquée aux images aériennes de Potsdam. Viennent ensuite U-Net, la même année, dont les connexions de saut réinjectent l'information de localisation perdue au sous-échantillonnage et améliorent ainsi les contours et les petits objets, puis DeepLab, dont les convolutions dilatées et l'agrégation multi-échelle élargissent le champ réceptif sans dégrader la résolution des prédictions. Retenez surtout ceci : l'apprentissage profond ne fait pas disparaître les concepts des décennies précédentes, contexte spatial, multi-échelle, fusion, hiérarchie des objets ; il les reformule dans un cadre d'apprentissage de bout en bout.
**Transition.** Deux obstacles subsistaient pourtant, et ce sont eux qui ouvrent le dernier chapitre.
**En réserve.** La figure vient de la base de données ISPRS 2D Semantic Labeling Challenge sur Potsdam. Deux autres éléments comptent dans cette période : le transfert de modèles pré-entraînés sur de grandes bases d'images naturelles vers les images aériennes et satellitaires, et la fusion multimodale apprise directement par le réseau, à laquelle Audebert, Le Saux et Lefèvre ont contribué en 2018.

### Planche 18 — Transformers, auto-supervisé et modèles de fondation · 1 min 10 · 18 min
**À dire.** Les réseaux convolutifs restent limités par deux choses : leur appétit en annotations pixel à pixel, très coûteuses à produire en télédétection, et leur difficulté à modéliser des dépendances spatiales à très longue portée. Les mécanismes d'attention répondent à la seconde : développés d'abord pour le traitement du langage — Vaswani et ses collègues en 2017 — puis adaptés à la vision par Dosovitskiy et ses collègues en 2021, les transformers modélisent directement les relations entre éléments distants, et cela nous intéresse au premier chef, car identifier un bâtiment ou une parcelle ne repose pas seulement sur l'apparence locale, mais sur l'organisation dans la scène. L'apprentissage auto-supervisé répond à la première : les autoencodeurs masqués, He et ses collègues en 2022, apprennent des représentations riches sur des données non annotées — et nos archives satellitaires sont précisément abondantes, quand les annotations, elles, sont rares. De la combinaison des deux naissent les modèles de fondation géospatiaux, dont le principe général est schématisé à droite : l'objectif n'est plus d'optimiser une architecture pour un jeu de données particulier, mais d'apprendre des représentations générales, multimodales et transférables entre capteurs, entre régions et entre applications.
**Transition.** Ce n'est évidemment pas la fin de l'histoire, et je voudrais terminer par ce qui reste ouvert.
**En réserve.** Il faut dire le revers : le coût de pré-entraînement de ces modèles est très élevé, en temps de calcul comme en ressources matérielles et énergétiques, ce qui pose de vraies questions d'empreinte environnementale et d'accessibilité pour la communauté scientifique. Et ce n'est pas une rupture : intégrer des données hétérogènes, représenter le contexte, généraliser à de nouvelles régions — ce sont les questions de tout l'exposé ; la différence est qu'elles sont désormais apprises plutôt que construites explicitement.

### Planche 19 — Défis ouverts · 40 s · 18 min 40
**À dire.** Les défis restent nombreux, et je vous les donne sans les hiérarchiser. La généralisation d'abord : entre régions, entre saisons, entre capteurs, entre résolutions — un modèle appris ici ne fonctionne pas nécessairement ailleurs. Le manque d'annotations ensuite, avec le coût des vérités terrain, le déséquilibre entre classes et des étiquettes souvent imparfaites. Puis la fusion multimodale — optique, radar, LiDAR, séries temporelles, données auxiliaires —, la robustesse face aux changements de distribution, aux nuages, au bruit, aux artefacts, aux événements rares, et enfin l'interprétabilité, c'est-à-dire notre capacité à comprendre et à contrôler des modèles de plus en plus grands.
**Transition.** Permettez-moi maintenant de reprendre le fil depuis le début.
**En réserve.** La prise en compte de la temporalité mérite une mention particulière : nos archives sont par nature des séries, et nous les traitons encore trop souvent comme des images isolées.

### Planche 20 — Conclusion : une histoire non linéaire · 1 min 20 · 20 min
**À dire.** Ce que je voudrais que vous reteniez, c'est d'abord que cette histoire n'est pas linéaire : elle ne va pas des classifieurs statistiques aux réseaux profonds, elle résulte de plusieurs traditions qui se sont progressivement rejointes — la classification statistique, les méthodes à noyaux, les méthodes d'ensemble, les modèles contextuels, les champs de Markov, les méthodes variationnelles, la géométrie stochastique, l'apprentissage profond et les modèles de fondation. Voici de nouveau la frise du début, et vous pouvez maintenant la lire comme un récit : l'information spectrale locale des premières approches, la cohérence spatiale des modèles contextuels et markoviens, les frontières, les régions et les objets des méthodes variationnelles et des processus ponctuels marqués, puis l'apprentissage des représentations, et aujourd'hui les modèles de fondation. Et sous cette progression, un principe récurrent, que vous avez vu réapparaître de planche en planche : une attache aux données plus une régularisation, des champs de Markov jusqu'aux fonctions de perte des réseaux profonds. C'est, je crois, ce qui fait l'unité de ce domaine — et ce qui en fait encore aujourd'hui un très beau sujet de recherche, à l'intersection du traitement du signal et des images, de la modélisation probabiliste, de la géométrie, de la vision par ordinateur et de l'intelligence artificielle.
**Transition.** Je vous remercie de votre attention.
**En réserve.** Si l'on ne devait retenir qu'une phrase : ce n'est pas l'histoire d'un remplacement de méthodes, c'est l'histoire de l'intégration progressive de niveaux croissants de contexte.

### Planche 21 — Merci de votre attention. · hors minutage · 20 min
**À dire.** Merci de votre attention — et merci à Martina Pastorino et Gabriele Moser, de l'Università di Genova, avec qui ce travail a été mené. Je suis à votre disposition pour vos questions.
**En réserve.** Les trois planches suivantes sont la bibliographie complète ; je peux y revenir si une référence précise vous intéresse.

### Planche 22 — Références I · annexe · —
**À dire.** La bibliographie complète de l'exposé, en commençant par l'article source lui-même, disponible comme rapport de recherche Inria RR-9631 sur HAL.
**En réserve.** Cette planche couvre les références 1 à 21 : de Duda et Hart en 1973 à Blaschke en 2010, en passant par Hughes, Geman et Geman, Besag, Solberg, Vapnik, Breiman et Gislason.

### Planche 23 — Références II · annexe · —
**À dire.** Suite de la bibliographie : les champs de Markov et leur optimisation, les CRF, puis nos travaux avec Martina Pastorino et Gabriele Moser, et le début de la morphologie mathématique.
**En réserve.** Références 22 à 38 : de Kato et Zerubia en 2012 à Benediktsson, Palmason et Sveinsson en 2005, en passant par Kirkpatrick, Boykov, Lafferty, Krähenbühl et Koltun, Zheng, CRFNet et Voisin.

### Planche 24 — Références III · annexe · —
**À dire.** Fin de la bibliographie : les profils d'attributs, les méthodes variationnelles, la bascule de 2012 et les architectures profondes, puis les transformers, l'auto-supervision et les modèles de fondation.
**En réserve.** Références 39 à 54 : de Dalla Mura à Segment Anything de Kirillov et ses collègues en 2023. La référence 45 est notre synthèse dans IEEE Signal Processing Magazine, en 2026.

## Questions probables

**Les champs de Markov sont-ils dépassés à l'ère des modèles de fondation ?**
Non, et c'est même l'un des points de l'exposé. Les CRF sont entrés dans les architectures profondes comme modules de raffinement ou comme couches différentiables, depuis les travaux de Zheng et ses collègues en 2015, et nous avons nous-mêmes travaillé sur des cadres markoviens hiérarchiques et sur des CRF dont les potentiels sont appris par un réseau. Les connexions mathématiques entre modèles graphiques probabilistes et apprentissage profond font l'objet de notre synthèse dans IEEE Signal Processing Magazine en 2026.

**Quelle est la différence exacte entre segmentation sémantique et segmentation tout court ?**
La segmentation sémantique produit une carte dense dans laquelle chaque pixel reçoit une étiquette prise dans un ensemble prédéfini de classes, donc une interprétation. La segmentation dite de bas niveau se contente de partitionner l'image en régions homogènes, sans leur associer de signification. C'est la présence de l'ontologie de classes qui fait toute la différence.

**Pourquoi ne pas simplement transposer les avancées de la vision par ordinateur ?**
Parce que nos images ne sont pas des images naturelles : capteurs optiques, radar à synthèse d'ouverture ou LiDAR, résolutions spatiales et spectrales très variables, acquisitions multitemporelles et multimodales, et des scènes géographiques dont les propriétés changent avec la région, la saison et les conditions d'acquisition. Le domaine s'est donc construit par convergence de plusieurs traditions — reconnaissance statistique des formes, traitement du signal et des images, modélisation probabiliste, morphologie mathématique, géométrie stochastique, analyse orientée objet — et, plus récemment seulement, apprentissage profond.

**Les SVM et les forêts aléatoires ont-ils encore un intérêt aujourd'hui ?**
Ils ont fortement amélioré la fonction de décision, mais pas la représentation : appliqués aux vecteurs d'observations, ils restent des classifieurs pixel à pixel. Leur force est d'être indépendants de la représentation, ce qui permet de les associer à des descripteurs texturaux, morphologiques ou spectro-spatiaux. L'association profils morphologiques et SVM, chez Fauvel et ses collègues en 2008, en est l'exemple le plus connu.

**Comment fait-on avec si peu d'annotations ?**
C'est justement ce à quoi répond l'apprentissage auto-supervisé : les autoencodeurs masqués, He et ses collègues en 2022, montrent qu'on peut apprendre des représentations riches sur des données non annotées, et nos archives satellitaires sont abondantes alors que les vérités terrain restent rares et coûteuses. Cela ne clôt pas la question pour autant : le coût des annotations, le déséquilibre entre classes et l'imperfection des étiquettes figurent toujours parmi les défis ouverts.

**Quel est le coût réel des modèles de fondation ?**
Le pré-entraînement est particulièrement coûteux, en temps de calcul comme en ressources matérielles et énergétiques. Cela soulève des questions d'empreinte environnementale, mais aussi d'accessibilité pour la communauté scientifique, qui n'a pas toujours les moyens de pré-entraîner ces modèles. C'est un point que l'article mentionne explicitement, et qui me paraît devoir être discuté.

**Où sont passées la géométrie stochastique et la dimension temporelle ?**
Ce sont deux victimes du format court. La géométrie stochastique et les processus ponctuels marqués font partie des traditions qui ont convergé, et ils interviennent précisément au niveau de la modélisation des frontières, des régions et des objets. Quant à la temporalité, elle figure parmi les défis ouverts : nos archives sont par nature des séries, et l'intégration des séries temporelles reste un axe majeur.

## Repères à ne pas se tromper

**Capteurs et programmes**
- Landsat, optique, **début** des années 1970 — SeaSat, radar, **fin** des années 1970. Ne pas inverser.
- IKONOS, image de la planche 9 : 4 mètres de résolution, 3 bandes, composition en fausses couleurs.
- Jeux de données cités : Zeebruges (comité technique IADF de l'IEEE GRSS ; images et vérité terrain de l'Académie royale militaire belge et de l'ONERA) ; Potsdam (ISPRS 2D Semantic Labeling Challenge).

**Dates et noms, dans l'ordre chronologique**
- Hughes, 1968 — malédiction de la dimension, dite phénomène de Hughes.
- Duda et Hart, 1973 ; Swain et Davis, 1978 ; Richards, 1986.
- Serra, 1982 ; Soille, 2003 — morphologie mathématique.
- Geman et Geman, 1984 — champs de Markov, distributions de Gibbs, échantillonneur de Gibbs.
- Kirkpatrick, 1984 — recuit simulé.
- Besag, 1986 ; Derin et Elliott, 1987.
- Mumford et Shah, 1989 — fonctionnelle variationnelle fondatrice.
- Dellepiane, Giusto, Serpico et Vernazza, 1991.
- Cortes et Vapnik, 1995 ; Vapnik, 1998 — machines à vecteurs de support.
- Solberg, Taxt et Jain, 1996.
- Samson, Blanc-Féraud, Aubert et Zerubia, 2000.
- Breiman, 2001 — forêts aléatoires ; Boykov, Veksler et Zabih, 2001 — coupes de graphes ; Lafferty, McCallum et Pereira, 2001 — CRF. Trois références de 2001, ne pas les confondre.
- Schölkopf et Smola, 2002 ; Tanaka, Inoue et Titterington, 2003.
- Benediktsson, Palmason et Sveinsson, 2005 — profils morphologiques étendus.
- Gislason, Benediktsson et Sveinsson, 2006 ; Fauvel et ses collègues, 2008 ; Camps-Valls et Bruzzone, 2009.
- Dalla Mura et ses collègues, 2010 — profils d'attributs ; Blaschke, 2010 — analyse orientée objet.
- Krähenbühl et Koltun, 2011 — CRF entièrement connectés ; Mountrakis, Im et Ogole, 2011.
- Kato et Zerubia, 2012 ; Krizhevsky, Sutskever et Hinton, 2012 — AlexNet.
- Moser, Serpico et Benediktsson, 2013, Proceedings of the IEEE ; Moser et Serpico, 2013 ; Voisin et ses collègues, 2013.
- Long, Shelhamer et Darrell, 2015 — FCN ; Ronneberger, Fischer et Brox, 2015 — U-Net ; Zheng et ses collègues, 2015 — CRF comme réseau récurrent. Trois références de 2015.
- Vaswani et ses collègues, 2017 — transformers.
- Audebert, Le Saux et Lefèvre, 2018 ; Chen et ses collègues, 2018 — DeepLab.
- Dosovitskiy et ses collègues, 2021 — transformers en vision ; Pastorino et ses collègues, 2021.
- He et ses collègues, 2022 — autoencodeurs masqués ; Pastorino, Moser, Serpico et Zerubia, 2022.
- Kirillov et ses collègues, 2023 — Segment Anything ; Pastorino, Moser, Serpico et Zerubia, 2024 — CRFNet.
- Xiao et ses collègues, 2025 — état de l'art des modèles de fondation.
- Pastorino, Moser, Serpico et Zerubia, 2026 — IEEE Signal Processing Magazine.

**Sigles**
- RSO : radar à synthèse d'ouverture (SAR en anglais).
- MAP : maximum a posteriori. MLC : maximum likelihood classifier, nom informel du même classifieur sous hypothèse gaussienne.
- MRF : champs de Markov. CRF : champs conditionnels aléatoires. ICM : iterated conditional modes.
- SVM : machines à vecteurs de support. RF : forêts aléatoires.
- EMP : profils morphologiques étendus. MNT : modèle numérique de terrain.
- FCN : réseaux entièrement convolutifs.
- IADF : comité technique d'analyse d'image et de fusion de données de l'IEEE GRSS.

**Chiffres et identifiants**
- 24 planches, 20 minutes, 54 références.
- Article source : Pastorino, Moser et Zerubia, Traitement du Signal et des Images, GRETSI ; également Inria RR-9631, HAL hal-05742224, septembre 2026.
- Affiliation : Centre Inria d'Université Côte d'Azur, équipe Ayana ; Martina Pastorino et Gabriele Moser, Università di Genova, Diten.
