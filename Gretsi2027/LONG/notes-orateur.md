# Notes d'orateur — version longue (51 planches, ≈ 45 min)

Ce document est le conducteur complet de l'exposé : il donne, planche par planche, ce qu'il faut dire, la phrase qui amène la suivante, et ce qu'on garde en réserve.

## Avant de commencer

- **Durée** : ouverture et cadrage, planches 1 à 6, jusqu'à 5 min 30 ; l'ère du pixel, planches 7 à 16, jusqu'à 15 min ; le contexte spatial et les champs de Markov, planches 17 à 24, jusqu'à 24 min 30 ; représentations et énergies, planches 25 à 32, jusqu'à 33 min ; apprentissage profond et modèles de fondation, planches 33 à 41, jusqu'à 42 min 30 ; conclusion, planches 42 à 44, jusqu'à 45 min. Le remerciement et les six annexes sont hors minutage.
- **Le fil directeur en une phrase** : l'histoire de la segmentation sémantique en télédétection est celle de l'intégration progressive de niveaux croissants de contexte — information spectrale locale, cohérence spatiale, frontières et régions et objets, apprentissage de représentations, modèles de fondation.
- **Trois idées à faire passer coûte que coûte** :
  1. Le domaine n'a jamais avancé par simple importation de la vision par ordinateur ; il résulte de la convergence de plusieurs traditions — statistique, markovienne, variationnelle, morphologique, orientée objet, puis profonde.
  2. Un même principe traverse tout : un terme d'attache aux données plus une régularisation, des champs de Markov à Mumford–Shah et jusqu'aux fonctions de perte des réseaux profonds.
  3. L'apprentissage profond et les modèles de fondation ne suppriment pas les questions anciennes — contexte, échelles, fusion, généralisation — ils les apprennent au lieu de les construire.
- **Si vous êtes en retard**, sacrifiez dans cet ordre : planche 27 (morphologie mathématique, 1 min 10, l'illustration est jolie mais la planche 28 suffit) ; planche 23 (optimisation, 1 min 20, c'est un catalogue d'algorithmes) ; planche 36 (contexte, échelles, modalités, 1 min 20, encore un catalogue) ; planche 16 (bilan de l'ère « pixel », 1 min, si le fil est déjà clair) ; planche 30 (contours actifs, 1 min 20, on peut entrer directement dans Mumford–Shah). Ne jamais sacrifier les planches 6, 22, 32, 37 et 43 : ce sont les cinq nœuds du récit.

## Déroulé

### Planche 1 — Segmentation sémantique en télédétection · 1 min · 1 min
**À dire.** Merci de m'accueillir. Je voudrais vous raconter comment la segmentation sémantique s'est construite en télédétection, c'est-à-dire comment on est passé, en une cinquantaine d'années, de la décision prise pixel par pixel sur une signature spectrale aux modèles de fondation géospatiaux d'aujourd'hui. Cet exposé s'appuie sur un article écrit avec Martina Pastorino et Gabriele Moser, de l'Università di Genova, à paraître dans Traitement du Signal et des Images.
**Transition.** Le plan de l'exposé est très exactement celui de l'article ; le voici.
**En réserve.** L'article est d'ores et déjà disponible comme rapport de recherche Inria, RR-9631, sur HAL, hal-05742224, depuis septembre 2026.

### Planche 2 — Sommaire · 30 s · 1 min 30
**À dire.** Onze sections, dans l'ordre chronologique de l'histoire du domaine : la classification statistique pixel à pixel, les méthodes discriminantes, les méthodes d'ensemble, le contexte spatial, les champs de Markov, les méthodes spectro-spatiales et variationnelles, puis l'apprentissage profond et les modèles de fondation. Gardez à l'esprit que ce n'est pas un catalogue : c'est une seule histoire, avec un fil.
**Transition.** Commençons par dire de quoi nous parlons exactement.

### Planche 3 — Introduction · 10 s · 1 min 40
**À dire.** Premier volet : ce qu'est la segmentation sémantique, ce qui rend la télédétection particulière, et le fil directeur de tout l'exposé.
**Transition.** Et d'abord, la définition.

### Planche 4 — De l'image à la carte thématique · 1 min 30 · 3 min 10
**À dire.** La segmentation sémantique consiste à associer à chaque pixel d'une image une étiquette prise dans un ensemble prédéfini de classes. Le mot s'est imposé avec l'apprentissage profond, au milieu des années 2010, mais le problème est étudié depuis des décennies en télédétection sous les noms de classification supervisée, pixel à pixel ou contextuelle — vous les trouverez déjà chez Duda et Hart en 1973, Swain et Davis en 1978, Richards en 1986. Le résultat est une carte dense : chaque pixel reçoit une interprétation, et c'est ce qui distingue cette tâche de la segmentation dite de bas niveau, qui se contente de partitionner l'image en régions homogènes sans leur donner de sens. En télédétection, l'enjeu est de transformer les observations satellitaires en cartes d'occupation et d'utilisation du sol : en bas de la planche, à gauche l'image aérienne, à droite la carte de segmentation.
**Transition.** Reste à comprendre pourquoi ce problème, en télédétection, ne se résout pas comme ailleurs.
**En réserve.** L'image et la carte viennent du jeu de données Zeebruges, publié par le comité technique d'analyse d'image et de fusion de données, l'IADF, de l'IEEE GRSS ; images et vérité terrain ont été fournies par l'Académie royale militaire belge et l'ONERA.

### Planche 5 — Ce qui distingue la télédétection · 1 min 10 · 4 min 20
**À dire.** Nos images ne sont pas des images naturelles. Elles peuvent venir de capteurs optiques, de radars à synthèse d'ouverture ou de LiDAR ; leurs résolutions spatiales sont très variables ; elles sont acquises à des dates différentes et combinent souvent plusieurs modalités. Et elles décrivent des scènes géographiques complexes, dont les propriétés changent selon les régions, selon les saisons, selon les conditions d'acquisition. C'est pour cette raison que l'évolution du domaine ne se réduit pas à une adaptation des avancées de la vision par ordinateur : elle résulte d'une convergence entre reconnaissance statistique des formes, traitement du signal et des images, modélisation probabiliste, morphologie mathématique, géométrie stochastique, analyse orientée objet et, plus récemment seulement, apprentissage profond.
**Transition.** Posons maintenant le problème de façon formelle, et je vous donnerai le fil de l'exposé.

### Planche 6 — Formalisation et fil directeur · 1 min 10 · 5 min 30
**À dire.** Formellement, une image de télédétection est une fonction I définie sur le domaine spatial oméga, à valeurs dans R puissance d, où d est le nombre de variables disponibles : une bande panchromatique, des bandes multispectrales ou hyperspectrales, des polarisations radar, des mesures LiDAR, mais aussi des indices spectraux, des modèles numériques de terrain ou d'autres données auxiliaires. Segmenter sémantiquement, c'est estimer une seconde fonction f, qui va du même domaine spatial vers C, l'ensemble fini des classes sémantiques. Et voici le fil que je vous propose de suivre : toute l'histoire du domaine peut se lire comme l'intégration progressive de niveaux croissants de contexte — l'information spectrale locale, puis la cohérence spatiale, puis les frontières, les régions et les objets, puis l'apprentissage des représentations, et enfin les modèles de fondation. Retenez cette frise : nous la retrouverons en conclusion.
**Transition.** Revenons donc au tout début de cette histoire, quand il n'y avait que le pixel.
**En réserve.** Un second fil, plus discret, traverse tout l'exposé : une attache aux données plus une régularisation. Il apparaîtra avec les champs de Markov, puis dans les modèles variationnels, et jusque dans les fonctions de perte des réseaux profonds.

### Planche 7 — Classification statistique pixel à pixel · 10 s · 5 min 40
**À dire.** Deuxième section : les premières approches, celles qui ne regardent qu'un pixel à la fois.
**Transition.** Tout commence avec les premiers satellites.

### Planche 8 — Les premières approches (années 1970–1980) · 1 min 20 · 7 min
**À dire.** Tout part des premiers satellites d'observation de la Terre : le programme Landsat, en optique, au début des années 1970, et SeaSat, en radar, à la fin de la même décennie. Ces capteurs créent un besoin nouveau, celui de méthodes automatiques capables de produire des cartes d'occupation du sol. On s'appuie alors sur les fondements de la reconnaissance statistique des formes : chaque pixel devient un vecteur d'observations — réponses radiométriques dans les différentes bandes, intensités radar, indices, données auxiliaires — et l'on attribue à ce pixel la classe la plus probable, selon une règle de décision bayésienne. Sous l'hypothèse que les observations de chaque classe suivent une loi gaussienne multivariée, on obtient le classifieur du maximum a posteriori, qui restera la méthode de référence pendant plusieurs décennies.
**Transition.** Sa réussite a tenu longtemps ; ses limites, elles, sont apparues avec les progrès des capteurs.
**En réserve.** Le classifieur MAP est souvent appelé, de manière informelle, classifieur du maximum de vraisemblance, le MLC des articles anglophones. Son succès s'explique par trois choses : une interprétation probabiliste simple, une mise en œuvre peu coûteuse et des performances satisfaisantes.

### Planche 9 — Deux limites structurelles · 1 min 10 · 8 min 10
**À dire.** Deux limites, et elles sont structurelles. La première, c'est la malédiction de la dimension, le phénomène décrit par Hughes dès 1968 : ajouter des variables spectrales n'améliore pas les performances dès lors que le nombre d'échantillons d'apprentissage reste limité — autrement dit, les signatures spectrales seules ne suffisent pas. La seconde, c'est l'hypothèse d'indépendance des observations : chaque pixel est décidé isolément, sans que l'on exploite son voisinage, alors que les objets géographiques sont fortement corrélés spatialement — une parcelle agricole, une forêt, une zone urbaine, un réseau routier. La conséquence est immédiate : des cartes bruitées, et d'autant plus bruitées que la résolution spatiale augmente.
**Transition.** Plutôt que de vous le dire, laissez-moi vous le montrer.

### Planche 10 — Le résultat : des cartes bruitées · 1 min 20 · 9 min 30
**À dire.** À gauche, une image IKONOS à 4 mètres de résolution, en fausses couleurs ; à droite, la classification pixel à pixel de cette même image. Prenez le temps de regarder le bruit de la carte : c'est l'effet « poivre et sel », signature visuelle de l'hypothèse d'indépendance. Ce que cette image dit, c'est que la décision ne peut plus dépendre de la seule radiométrie d'un pixel : il lui faut son environnement spatial. C'est ici, historiquement, que le problème cesse d'être une classification spectrale pour devenir un problème d'interprétation spatiale des scènes — et c'est ce basculement qui ouvre la voie à Geman et Geman en 1984, à Besag en 1986, à Solberg et ses collègues en 1996.
**Transition.** Avant d'en venir au contexte spatial, il faut raconter une autre branche de l'histoire, celle où l'on cherche à améliorer non pas la représentation, mais le classifieur lui-même.
**En réserve.** La composition fausses couleurs utilise l'infrarouge voisin, le rouge et le bleu ; les cartes viennent des travaux de Gabriele Moser et de ses collègues, publiés dans les Proceedings of the IEEE en 2013. Nous reverrons cette image planche 19, avec la carte contextuelle en plus.

### Planche 11 — Méthodes discriminantes et à noyaux · 10 s · 9 min 40
**À dire.** Troisième section : on cesse de modéliser la loi des observations pour estimer directement la frontière entre les classes.
**Transition.** L'outil emblématique de ce déplacement, ce sont les machines à vecteurs de support.

### Planche 12 — Estimer la frontière plutôt que la distribution · 1 min 20 · 11 min
**À dire.** À partir de la fin des années 1990, l'intérêt se déplace vers les méthodes discriminantes, dont l'objectif est d'estimer directement les frontières de décision entre classes plutôt que de modéliser la distribution statistique des observations. C'est une réponse à deux difficultés bien identifiées : des hypothèses gaussiennes souvent peu réalistes, et une dimension des données qui ne cesse de croître. Parmi ces approches, les machines à vecteurs de support s'imposent très vite comme une référence pour la classification supervisée des images de télédétection. Issues de la théorie de l'apprentissage statistique — Cortes et Vapnik en 1995, Vapnik en 1998 — elles reposent sur la maximisation de la marge entre classes, ce qui leur donne d'excellentes capacités de généralisation même quand les échantillons d'apprentissage sont peu nombreux devant la dimension des données. En télédétection, où l'annotation coûte cher, cette propriété compte énormément.
**Transition.** Mais comment traiter les problèmes non linéaires sans rien perdre de ce qui fait la force de cette formulation ?

### Planche 13 — Noyaux : la non-linéarité sans perdre la convexité · 1 min 30 · 12 min 30
**À dire.** Les méthodes à noyaux étendent naturellement ce cadre aux problèmes non linéaires : on construit des frontières de décision complexes tout en conservant une formulation convexe du problème d'optimisation. Au cours des années 2000, les SVM deviennent ainsi l'un des classifieurs les plus utilisés en télédétection — en multispectral, en hyperspectral, en multisources — au point que l'on développe des noyaux spécifiquement adaptés aux caractéristiques des observations géospatiales. J'insiste sur un point, parce qu'il commande toute la suite : les SVM améliorent la fonction de décision, pas la représentation ; appliqués directement aux vecteurs d'observations, ils restent des classifieurs pixel à pixel et n'intègrent pas les dépendances spatiales entre étiquettes. C'est pourquoi, à partir de ce moment, deux directions de recherche avancent largement en parallèle : de nouveaux classifieurs d'un côté, des représentations spatiales de plus en plus riches de l'autre.
**Transition.** Suivons d'abord la piste des classifieurs, avec les méthodes d'ensemble.
**En réserve.** Sur les noyaux, la référence de fond est le livre de Schölkopf et Smola, en 2002 ; pour la télédétection, l'ouvrage de Camps-Valls et Bruzzone en 2009, et la revue de Mountrakis, Im et Ogole dans l'ISPRS Journal en 2011.

### Planche 14 — Méthodes d'ensemble · 10 s · 12 min 40
**À dire.** Quatrième section : pendant que les méthodes à noyaux occupent une grande partie des travaux sur la classification supervisée, une autre direction se développe en parallèle, avec une idée très différente.
**Transition.** Et dans cette famille, une méthode va s'imposer presque aussi vite que les SVM.

### Planche 15 — Forêts aléatoires · 1 min 20 · 14 min
**À dire.** Le principe de l'apprentissage d'ensemble est simple : plutôt que de perfectionner un classifieur unique, on en combine plusieurs, et l'on gagne en robustesse et en généralisation. Les forêts aléatoires, proposées par Leo Breiman en 2001, construisent un ensemble d'arbres de décision appris chacun sur des sous-ensembles tirés au hasard — et le hasard joue deux fois, sur les observations et sur les variables — puis agrègent leurs prédictions par vote majoritaire. Cette stratégie limite le surapprentissage tout en conservant une forte capacité à modéliser des relations non linéaires. Ce qui explique leur diffusion très rapide, c'est surtout leur commodité : peu de réglages, robustesse au bruit, un grand nombre de variables sans difficulté, et des mesures d'importance qui aident réellement à interpréter le modèle. Les premières applications, chez Gislason, Benediktsson et Sveinsson en 2006, portent sur le multispectral et l'hyperspectral ; elles deviennent ensuite un outil de référence pour la cartographie de l'occupation du sol, la détection de changements et la fusion multisources.
**Transition.** Comme les SVM, pourtant, les forêts aléatoires restent indépendantes de la représentation qu'on leur donne : le moment est venu de faire le bilan.
**En réserve.** La revue de Belgiu et Drăguț, en 2016, fait le tour des usages. Cette neutralité vis-à-vis de la représentation leur donne une longue vie : nous les avons nous-mêmes utilisées, avec Martina Pastorino et Gabriele Moser, comme ensembles d'arbres de décision à l'intérieur d'un cadre markovien hiérarchique causal, en 2021.

### Planche 16 — Bilan de l'ère « pixel » · 1 min · 15 min
**À dire.** Arrêtons-nous un instant, parce que nous sommes à une charnière de l'exposé. Les méthodes discriminantes et les méthodes d'ensemble apportent des gains considérables, mais ces gains portent sur le classifieur, et seulement sur lui : elles restent indépendantes de la représentation, qu'elle soit spectrale, texturale, morphologique ou spectro-spatiale. La limitation fondamentale des approches pixel à pixel, elle, demeure intacte : l'organisation spatiale de la scène n'est toujours pas prise en compte explicitement. À partir de là, deux réponses complémentaires vont structurer tout le reste de l'exposé : régulariser les étiquettes — ce sera le contextuel, le markovien, le variationnel — ou enrichir les descripteurs — ce sera le spectro-spatial et l'orienté objet.
**Transition.** Prenons d'abord la première de ces deux voies : faire entrer le contexte spatial dans la décision elle-même.
**En réserve.** Ces deux directions ne se succèdent pas, elles évoluent largement en parallèle tout au long des années 2000 : c'est pour la clarté de l'exposé que je les présente l'une après l'autre.

### Planche 17 — Classification contextuelle · 10 s · 15 min 10
**À dire.** Cinquième section : la classification contextuelle et les premiers modèles spatiaux. C'est ici que le pixel cesse d'être seul.
**Transition.** Le point de départ est une observation de bon sens, formulée dès les années 1980.

### Planche 18 — Trois niveaux de contexte · 1 min 50 · 17 min
**À dire.** L'idée est simple, et on la trouve déjà dans les manuels des années 1980, chez John Richards par exemple : dans une scène de télédétection, les objets géographiques présentent une forte cohérence spatiale, si bien qu'un pixel a beaucoup plus de chances d'appartenir à la classe de ses voisins immédiats qu'à une classe totalement différente. L'information pertinente ne réside donc plus seulement dans la réponse radiométrique locale, mais aussi dans les relations de voisinage et dans les structures régionales. La communauté distingue alors trois niveaux : le contexte local, les interactions entre pixels voisins et les fenêtres de taille limitée, chez Haralick et Shapiro en 1985 ; le contexte régional, qui décrit des ensembles de pixels par leur texture, leur forme, leur taille et l'homogénéité des régions segmentées ; et le contexte global, qui intègre l'organisation générale de la scène, les relations entre objets et les connaissances a priori sur leur disposition. Le contexte régional annonce déjà l'analyse orientée objet, dont Thomas Blaschke fera la synthèse en 2010. Cette hiérarchie restera un principe structurant jusqu'aux architectures profondes contemporaines : on la retrouve chez Azencott et Graffigne, en 1992, et encore dans la revue de Csurka et ses collègues, en 2023.
**Transition.** Et ce n'est pas seulement une idée séduisante : l'apport du contexte se mesure, sur la même image.
**En réserve.** Ce qui déclenche ce virage est très concret : améliorer le classifieur ne suffisait pas à faire disparaître les artefacts en poivre et sel. Il fallait s'attaquer au modèle, pas seulement à la règle de décision.

### Planche 19 — L'apport mesurable du contexte · 1 min 30 · 18 min 30
**À dire.** Vous reconnaissez l'image de tout à l'heure : IKONOS, 4 mètres, trois bandes en composition fausses couleurs. Au centre, la carte pixel à pixel que nous avions déjà vue ; à droite, la carte obtenue en intégrant le contexte spatial, d'après les travaux de Gabriele Moser, Sebastiano Serpico et Jón Atli Benediktsson publiés dans les Proceedings of the IEEE en 2013. Je vous laisse quelques secondes pour regarder : le bruit disparaît, les parcelles redeviennent des parcelles, les structures urbaines redeviennent lisibles. Ces gains ont été documentés en multispectral, en multitemporel et en multisources — Solberg, Taxt et Jain en 1996, Bruzzone et Serpico en 1997 puis en 1999 — et ce qu'ils disent au fond, c'est que la classification cesse d'être une succession de décisions indépendantes : les étiquettes doivent être estimées conjointement.
**Transition.** Reste à donner à cette intuition un cadre théorique rigoureux — et ce cadre, ce sont les champs de Markov.
**En réserve.** Si l'on me demande pourquoi la même image revient : c'est délibéré, c'est la seule façon de rendre la comparaison honnête.

### Planche 20 — Modèles markoviens et bayésiens · 10 s · 18 min 40
**À dire.** Sixième section : les modèles markoviens et bayésiens. Nous entrons dans le cœur théorique de l'exposé.
**Transition.** C'est ici que l'intuition du contexte devient une formulation probabiliste générale.

### Planche 21 — Les champs de Markov : la première formalisation · 1 min 30 · 20 min 10
**À dire.** Les champs de Markov constituent la première formalisation probabiliste générale de cette idée, et ils deviennent très vite l'un des cadres théoriques les plus influents pour la segmentation et la classification d'image. Le principe tient en une phrase : les étiquettes ne sont plus des variables indépendantes, ce sont des variables aléatoires définies sur un graphe de voisinage. Sous les hypothèses de Markov, et grâce à l'équivalence entre champs de Markov et distributions de Gibbs — c'est l'appareillage que mettent en place Stuart et Donald Geman en 1984, et que Julian Besag reprend en 1986 du côté de l'analyse statistique — la recherche de la carte de classes optimale s'écrit comme une estimation au sens du maximum a posteriori. Et c'est là que le théorème de Bayes fait tout le travail : maximiser la probabilité a posteriori des étiquettes est exactement équivalent à minimiser une fonction d'énergie, X désignant les observations et Y l'ensemble des étiquettes à estimer.
**Transition.** Voyons maintenant ce qu'il y a dans cette énergie : c'est, à mon sens, l'équation la plus importante de l'exposé.
**En réserve.** Pour qui veut le détail complet du cadre, Zoltan Kato et moi-même en avons publié une synthèse en 2012 dans Foundations and Trends in Signal Processing.

### Planche 22 — Attache aux données + régularisation · 1 min 50 · 22 min
**À dire.** Voilà l'équation que je voudrais vraiment que vous emportiez avec vous. L'énergie se décompose en deux termes seulement : le premier, U indice d, c'est l'attache aux données, généralement dérivée de la vraisemblance des observations, et c'est lui qui porte tout ce que la radiométrie nous apprend sur le pixel ; le second, U indice r, c'est la régularisation spatiale, qui introduit une contrainte favorisant la cohérence entre pixels voisins. Entre les deux, le paramètre bêta, qui n'est rien d'autre que le curseur entre fidélité aux observations et régularité de la solution. À droite, vous voyez les systèmes de voisinage, définis au premier ou au second ordre, et les cliques associées : les potentiels de clique pénalisent certaines configurations d'étiquettes, typiquement les changements de classe entre pixels adjacents. L'intérêt majeur de cette formulation, c'est qu'elle intègre dans un cadre unique les observations radiométriques et les interactions spatiales.
**Transition.** Écrire l'énergie est une chose ; la minimiser en est une autre, et c'est beaucoup moins confortable.
**En réserve.** Retenez la forme de cette équation : nous allons la retrouver presque à l'identique dans la fonctionnelle de Mumford–Shah, puis dans les formulations sur graphes, et finalement dans les fonctions de perte des réseaux profonds.

### Planche 23 — Optimiser : un problème difficile · 1 min 20 · 23 min 20
**À dire.** Trouver la configuration d'étiquettes qui minimise cette énergie est un problème d'optimisation combinatoire difficile ; en pratique on ne l'atteint pas exactement, et l'on travaille donc avec des stratégies sous-optimales. Les premières sont les modes conditionnels itérés, l'ICM, puis le recuit simulé, chez Kirkpatrick en 1984, et l'échantillonneur de Gibbs, chez Geman et Geman. Viennent ensuite les coupes de graphes, avec Boykov, Veksler et Zabih en 2001, et la propagation de croyance avec boucles, chez Tanaka et ses collègues en 2003. Les applications couvrent tout le champ : cohérence spatiale des classifications, segmentation multisource, restauration, détection de changements, fusion optique, radar et LiDAR. Mais l'apport des champs de Markov dépasse très largement ces applications particulières : ils fournissent au domaine une formulation probabiliste générale de la régularisation spatiale, et c'est cela qui va durer.
**Transition.** Cette famille connaît d'ailleurs un prolongement direct, qui la rapproche de l'apprentissage supervisé.
**En réserve.** Il existe de très beaux exemples où les deux directions du premier tiers se rejoignent : Gabriele Moser et Sebastiano Serpico ont proposé en 2013 un cadre intégré combinant machines à vecteurs de support et champs de Markov pour la classification contextuelle.

### Planche 24 — Des MRF aux CRF · 1 min 10 · 24 min 30
**À dire.** Les champs conditionnels aléatoires prolongent naturellement cette famille : plutôt que de modéliser la loi jointe des observations et des étiquettes, ils représentent directement la distribution conditionnelle de Y sachant X — Lafferty, McCallum et Pereira, en 2001. L'avantage est immédiat : on peut y faire entrer des caractéristiques discriminantes complexes, et les modèles entièrement connectés de Krähenbühl et Koltun, en 2011, préservent mieux les contours des objets. Puis les CRF entrent dans les réseaux profonds, d'abord comme modules de raffinement, ensuite comme couches différentiables, et c'est exactement le terrain de nos travaux avec Martina Pastorino et Gabriele Moser, jusqu'à CRFNet, en 2024. Au-delà de ces modèles, retenez l'idée qui traverse tout le domaine : une carte d'occupation du sol ne doit pas seulement être compatible avec les observations locales, elle doit l'être aussi avec l'organisation spatiale de la scène.
**Transition.** Nous avons régularisé les étiquettes ; revenons à l'autre branche de l'alternative, et enrichissons cette fois la représentation.
**En réserve.** Zheng et ses collègues montrent dès 2015 qu'un CRF peut se lire comme un réseau récurrent ; dans CRFNet, c'est un réseau convolutif profond qui en apprend les potentiels. Et dans la même veine, avec Aurélie Voisin, Vladimir Krylov, Gabriele Moser et Sebastiano Serpico, nous avons classé des images RSO de très haute résolution en zone urbaine à l'aide de copules et de texture dans un champ de Markov hiérarchique, en 2013.

### Planche 25 — Méthodes spectro-spatiales · 10 s · 24 min 40
**À dire.** Septième section, et changement de levier : jusqu'ici nous avons régularisé les étiquettes ; nous allons maintenant enrichir la représentation elle-même.
**Transition.** Ce qui a rendu ce virage nécessaire, c'est la montée en résolution des capteurs.

### Planche 26 — Enrichir la représentation, pas les étiquettes · 1 min 10 · 25 min 50
**À dire.** Les modèles contextuels améliorent la cohérence des cartes, mais ils ne changent rien à la représentation des observations. Une démarche complémentaire consiste donc à enrichir directement les caractéristiques utilisées par le classifieur, en combinant l'information spectrale avec des descripteurs spatiaux : c'est le paradigme spectro-spatial, qui s'installe au cours des années 2000 et qui va jouer un rôle majeur dans l'évolution du domaine. Ce qui le rend nécessaire, c'est la montée en résolution, spatiale et spectrale, des capteurs : les premières générations d'images étaient caractérisées essentiellement par leurs signatures radiométriques, alors que les images à plus haute résolution révèlent la structure interne des objets géographiques. Une même classe peut alors présenter une forte variabilité spectrale, et des objets différents avoir des signatures très proches. C'est pour cela que la texture, la forme, la taille, l'organisation spatiale et les relations de voisinage deviennent des informations aussi discriminantes que les valeurs spectrales elles-mêmes.
**Transition.** Les premiers outils de cet enrichissement viennent de l'analyse de texture et de la morphologie mathématique.
**En réserve.** L'idée d'intégrer intensité et information texturale est déjà à l'œuvre en radar chez Dellepiane, Giusto, Serpico et Vernazza, en 1991. La référence de fond sur la chaîne multispectrale complète reste le livre de Landgrebe, en 2003.

### Planche 27 — Morphologie mathématique · 1 min 10 · 27 min
**À dire.** Les premières approches spectro-spatiales exploitent des statistiques locales et des descripteurs texturaux — les caractéristiques de Haralick, Shanmugam et Dinstein datent de 1973 — puis les opérateurs de la morphologie mathématique : l'érosion, la dilatation et leurs compositions, dans la lignée de Serra en 1982 et de Soille en 2003. Vous en avez ici une illustration directe : au centre l'image satellite originale en RVB, à gauche son érosion, à droite sa dilatation. Notez bien la différence de nature avec ce que nous venons de voir : les modèles markoviens introduisent une régularisation spatiale au niveau des étiquettes, alors que ces opérateurs enrichissent les vecteurs de caractéristiques, en amont, avant la phase de classification.
**Transition.** Ces opérateurs, il a fallu ensuite les organiser pour décrire une scène à toutes ses échelles à la fois.

### Planche 28 — Profils morphologiques et profils d'attributs · 1 min 30 · 28 min 30
**À dire.** L'étape importante est franchie avec les profils morphologiques étendus, les EMP, introduits par Benediktsson, Palmason et Sveinsson en 2005, puis avec les profils d'attributs de Dalla Mura et ses collègues en 2010 : ils décrivent simultanément les propriétés spectrales et la structure spatiale des scènes, à différentes échelles d'observation. Ces représentations deviennent très vite des références pour la classification hyperspectrale et, plus généralement, pour la haute et la très haute résolution spatiale. Associées aux machines à vecteurs de support, elles obtiennent des performances remarquables, et c'est largement ce qui a diffusé les approches spectro-spatiales ; mais le principe est plus général — forêts aléatoires, réseaux de neurones et d'autres méthodes discriminantes peuvent exploiter les mêmes descripteurs. Retenez que les gains observés proviennent alors autant de la qualité de la représentation que des performances du classifieur. Plusieurs travaux proposent enfin de prendre les régions segmentées, plutôt que les pixels individuels, comme unités d'analyse : la cohérence spatiale des cartes augmente et le bruit diminue.
**Transition.** Après la régularisation des étiquettes et l'enrichissement des descripteurs, voici une troisième voie : s'attaquer directement à la géométrie des frontières.
**En réserve.** L'objectif n'a jamais été d'exploiter un plus grand nombre de bandes spectrales, mais de construire une représentation intégrant toutes les informations pertinentes qui décrivent la scène. Sur les vues d'ensemble : Plaza et ses collègues en 2009, Camps-Valls, Tuia, Bruzzone et Benediktsson en 2014 ; sur les unités-régions, Tarabalka, Benediktsson et Chanussot en 2009.

### Planche 29 — Méthodes variationnelles · 10 s · 28 min 40
**À dire.** Huitième section : la segmentation formulée comme un problème de minimisation d'énergie, sans loi de probabilité explicite sur les étiquettes.
**Transition.** Tout part des contours actifs, à la fin des années 1980.

### Planche 30 — Segmenter en minimisant une énergie · 1 min 20 · 30 min
**À dire.** À partir de la fin des années 1980, en parallèle des champs de Markov, une autre famille de méthodes développe une idée très voisine mais dans un autre langage. Les méthodes variationnelles ne cherchent plus à modéliser explicitement une distribution de probabilité sur les étiquettes : elles cherchent la partition de l'image qui réalise le meilleur compromis entre la fidélité aux observations et la régularité, spatiale ou géométrique. Les premiers développements concernent les contours actifs — les snakes de Kass, Witkin et Terzopoulos, en 1988 : les frontières des objets y sont des courbes déformables, qui évoluent sous l'action de forces internes assurant la régularité du contour et de forces externes dérivées des informations contenues dans l'image. Ces modèles introduisent une représentation explicite des contours, et ils ouvrent la voie à toute une famille de méthodes fondées sur la minimisation d'énergie.
**Transition.** Le modèle qui a le plus marqué cette famille tient en trois termes ; le voici.

### Planche 31 — La fonctionnelle de Mumford–Shah · 1 min 30 · 31 min 30
**À dire.** Voici la fonctionnelle proposée par Mumford et Shah en 1989, qui constitue encore aujourd'hui l'un des modèles variationnels les plus influents en traitement des images. On y cherche simultanément deux choses : une approximation régulière u de l'image observée I, et un ensemble K de discontinuités, qui sont les contours des objets. Le premier terme mesure la fidélité de la solution aux observations ; le deuxième, pondéré par le paramètre mu, favorise une représentation régulière à l'intérieur des régions ; le troisième, pondéré par nu, pénalise la mesure des contours, c'est-à-dire leur complexité géométrique. Regardez bien la structure de cette énergie : c'est très exactement, dans un autre langage, ce que nous avions écrit planche 22 pour les champs de Markov — un ajustement aux données, et de la régularité.
**Transition.** Restait à rendre tout cela numériquement robuste, et à l'amener sur des images satellitaires.

### Planche 32 — Robustesse numérique et applications · 1 min 30 · 33 min
**À dire.** Deux avancées ont rendu ces modèles véritablement utilisables. D'abord les surfaces de niveau, les level sets d'Osher et Sethian en 1988 : le contour n'est plus décrit explicitement mais au moyen d'une fonction de niveau, ce qui permet de gérer automatiquement les changements de topologie au cours de l'évolution de la segmentation. Ensuite, quelques années plus tard, les modèles régionaux — les contours actifs sans contours de Chan et Vese, en 2001 — qui s'appuient sur les statistiques des régions plutôt que sur les seuls gradients de l'image, et qui sont donc bien plus robustes sur des images bruitées ou faiblement contrastées. À droite, une image SPOT du CNES et, juste à côté, sa segmentation par la méthode variationnelle que nous avions proposée avec Christophe Samson, Laure Blanc-Féraud et Gilles Aubert en 2000, et qui unifie classification et restauration dans une même fonctionnelle. Et c'est ici le point d'orgue de cette première moitié d'exposé : modèles bayésiens, champs de Markov, méthodes variationnelles et formulations fondées sur les graphes sont différentes expressions d'un même principe — un terme d'attache aux données, combiné à une régularisation spatiale ou géométrique.
**Transition.** Retenez cette phrase, parce que l'apprentissage profond, que nous abordons maintenant, ne l'abolit pas : il la déplace.
**En réserve.** Ces méthodes sont aussi un pont vers les approches modernes : formulations énergétiques, contraintes de régularité et compromis entre fidélité aux données et cohérence spatiale réapparaissent aujourd'hui dans les fonctions de perte, dans les procédures d'optimisation et dans des architectures hybrides.

### Planche 33 — Apprentissage profond · 10 s · 33 min 10
**À dire.** Neuvième section : le moment où les descripteurs cessent d'être conçus et où les représentations se mettent à être apprises.
**Transition.** Cette bascule a une date précise.

### Planche 34 — 2012 : la bascule · 1 min 20 · 34 min 30
**À dire.** 2012, le challenge ImageNet : le réseau AlexNet, de Krizhevsky, Sutskever et Hinton, démontre une amélioration spectaculaire des performances en classification d'images naturelles. Ce que ce résultat établit, c'est qu'il est possible d'apprendre automatiquement des représentations hiérarchiques directement à partir des données, sans conception manuelle de descripteurs spectraux, texturaux ou géométriques ; la qualité des performances ne dépend donc plus seulement du classifieur, mais de la capacité du réseau à apprendre conjointement une représentation pertinente et la fonction de décision. La transposition à la télédétection est rapide — Chen et ses collègues en 2014 sur l'hyperspectral, Castelluccio et ses collègues en 2015 sur l'utilisation du sol — avec deux constats convergents : les réseaux convolutifs apprennent des représentations plus discriminantes que les descripteurs construits manuellement, et le transfert de modèles pré-entraînés sur les grandes bases d'images naturelles fonctionne sur les images aériennes et satellitaires. Autrement dit, les approches spectro-spatiales que nous venons de voir passent de représentations conçues à des représentations apprises.
**Transition.** Classer une image entière, pourtant, n'est pas la segmenter : il fallait encore produire une prédiction dense, pixel par pixel.

### Planche 35 — Prédiction dense : FCN et encodeur–décodeur · 1 min 30 · 36 min
**À dire.** L'étape décisive, ce sont les réseaux entièrement convolutifs, les FCN de Long, Shelhamer et Darrell en 2015, dont vous voyez l'architecture à droite. En supprimant les couches entièrement connectées au profit d'opérations exclusivement convolutionnelles, on produit directement une prédiction dense à l'échelle du pixel, et l'on apprend de bout en bout une fonction de segmentation, sans extraction explicite de caractéristiques et sans post-traitement obligatoire. Les architectures encodeur-décodeur complètent très vite cette formulation, et U-Net, de Ronneberger, Fischer et Brox, la même année, en est l'exemple le plus représentatif : ses connexions de saut réinjectent dans le décodeur les informations de localisation perdues lors des sous-échantillonnages, ce qui améliore la délimitation des contours et la segmentation des petits objets. Par leur simplicité et leur efficacité, ces architectures deviennent des références pour de nombreuses applications en télédétection : cartographie de l'occupation du sol, extraction de bâtiments, de routes, de réseaux hydrographiques.
**Transition.** Trois questions, cependant, que la prédiction dense ne règle pas : le contexte, les échelles et la diversité des capteurs.
**En réserve.** La figure est tirée de notre article de revue avec Martina Pastorino, Gabriele Moser et Sebastiano Serpico, paru dans IEEE Signal Processing Magazine en 2026 ; l'exemple porte sur les images aériennes de la base ISPRS 2D Semantic Labeling Challenge, à Potsdam. Sur les applications, voir Audebert, Le Saux et Lefèvre en 2018, Zhang et ses collègues en 2018 pour les routes, Isikdogan et ses collègues en 2017 pour les surfaces en eau.

### Planche 36 — Contexte, échelles, modalités · 1 min 20 · 37 min 20
**À dire.** L'évolution des réseaux profonds s'accompagne alors d'un effort important pour mieux représenter le contexte spatial et les objets observés à différentes échelles. Les réseaux résiduels, de He et ses collègues en 2016, facilitent l'apprentissage de modèles plus profonds en limitant la disparition du gradient. Les architectures DeepLab introduisent les convolutions dilatées et les modules d'agrégation multi-échelle, l'ASPP, qui augmentent le champ réceptif sans dégrader la résolution spatiale des prédictions. Et dans le même esprit, les pyramides de caractéristiques améliorent la représentation d'objets de tailles très variables — une propriété particulièrement importante chez nous, puisqu'une même scène peut contenir simultanément des véhicules, des bâtiments, des parcelles agricoles et des massifs forestiers. Enfin, l'intégration de données multimodales devient un axe majeur : les réseaux profonds apprennent désormais des représentations communes à partir de l'optique, du radar à synthèse d'ouverture, du LiDAR, des modèles numériques de terrain ou de données géographiques auxiliaires.
**Transition.** Vous aurez reconnu, sous ces noms d'architectures, des questions déjà rencontrées ; c'est précisément ce que je voudrais expliciter.

### Planche 37 — Ce que l'apprentissage profond ne supprime pas · 1 min 10 · 38 min 30
**À dire.** Voici ce qu'il faut retenir de cette section : l'apprentissage profond ne fait pas disparaître les concepts développés au cours des décennies précédentes, il les reformule dans un cadre d'apprentissage de bout en bout. Le contexte spatial, la représentation multi-échelle, la fusion de données, la hiérarchie des objets — que l'on décrivait auparavant au moyen de modèles probabilistes, variationnels ou géométriques — sont désormais appris directement par les architectures profondes. Cela dit, et malgré des performances remarquables, les réseaux convolutifs conservent trois limites : leur apprentissage repose sur de grandes quantités d'annotations pixel à pixel, dont la production est particulièrement coûteuse en télédétection ; leur capacité de généralisation entre capteurs, entre régions géographiques et entre modalités d'acquisition reste limitée ; et ils modélisent mal les dépendances spatiales à très longue portée. Ce sont exactement ces trois limites qui ouvrent la voie à la suite.
**Transition.** La suite, ce sont les mécanismes d'attention, puis les modèles de fondation géospatiaux.

### Planche 38 — Transformers et modèles de fondation · 10 s · 38 min 40
**À dire.** Dixième section : les transformers et les modèles de fondation. Ce sont les limites que je viens d'énoncer qui nous y conduisent, et non une mode.
**Transition.** Commençons par le mécanisme lui-même : l'attention.

### Planche 39 — L'attention en segmentation · 1 min 30 · 40 min 10
**À dire.** Les limites des architectures convolutives, et tout particulièrement leur difficulté à modéliser des dépendances spatiales à longue portée, conduisent progressivement à introduire des mécanismes d'attention en segmentation sémantique. Les transformers ont été développés pour le traitement automatique du langage naturel — c'est l'article de Vaswani et ses collègues, en 2017 — et leur propriété essentielle est de modéliser directement les relations entre éléments distants d'une séquence, sans les faire transiter par un voisinage local. Leur adaptation à la vision, par Dosovitskiy et ses collègues en 2021, ouvre une nouvelle étape. Deux architectures sont particulièrement représentatives : Swin Transformer, de Liu et ses collègues, et SegFormer, de Xie et ses collègues, toutes deux en 2021, qui combinent une représentation hiérarchique de l'image avec une modélisation plus globale du contexte. Cette propriété nous intéresse au premier chef, parce qu'en télédétection l'identification d'un bâtiment, d'une route ou d'une parcelle agricole ne repose pas uniquement sur son apparence locale, mais sur son organisation au sein de la scène.
**Transition.** Un second mouvement se développe en parallèle, et il répond à un problème encore plus concret pour nous : celui des annotations.
**En réserve.** Souvenez-vous des trois niveaux de contexte de la planche 18 : local, régional, global. C'est le troisième, le plus difficile à formaliser explicitement, que l'attention permet enfin d'aborder de front.

### Planche 40 — Apprendre sans annotation · 1 min 10 · 41 min 20
**À dire.** En parallèle, l'apprentissage auto-supervisé devient un axe majeur de recherche. Les autoencodeurs masqués — je pense aux travaux de He et ses collègues, en 2022 — montrent qu'il est possible d'apprendre des représentations visuelles riches à partir de très grandes quantités de données non annotées. Cette évolution répond directement à un déséquilibre propre à notre domaine : les archives satellitaires sont abondantes et s'accumulent depuis des décennies, alors que les annotations pixel à pixel restent rares et coûteuses à produire. Autrement dit, ce n'est pas seulement une avancée importée de la vision par ordinateur ; c'est une réponse à une contrainte que nous connaissons bien.
**Transition.** De ces deux mouvements combinés, l'attention et l'auto-supervision, naissent les modèles de fondation géospatiaux.
**En réserve.** Le coût des annotations figurait déjà, à la planche 37, parmi les limites persistantes des réseaux convolutifs ; il reviendra dans les perspectives. C'est sans doute le problème le plus tenace de tout l'exposé.

### Planche 41 — Modèles de fondation géospatiaux · 1 min 10 · 42 min 30
**À dire.** Ces travaux conduisent à l'émergence des modèles de fondation géospatiaux, dont vous voyez le principe à droite : pré-entraînés sur de très grands volumes de données, puis adaptés à des tâches très différentes — classification, segmentation, détection d'objets, détection de changements. L'objectif n'est plus d'optimiser une architecture pour un jeu de données particulier, mais d'apprendre des représentations génériques, transférables entre capteurs, entre régions géographiques et entre applications. Le revers, j'y insiste, c'est un coût de pré-entraînement très élevé, en calcul comme en ressources matérielles et énergétiques, qui soulève de vraies questions d'empreinte environnementale et d'accessibilité pour la communauté. Et surtout, ce n'est pas une rupture : les mêmes questions traversent toute l'histoire que je viens de raconter, à ceci près qu'elles sont désormais apprises à partir de très grands volumes de données plutôt que construites explicitement.
**Transition.** Nous voici au bout du parcours ; il est temps de prendre du recul.
**En réserve.** Les jalons à citer si on me le demande : SatMAE, de Cong et ses collègues en 2022 ; les travaux de Jakubik et ses collègues et de Wang et ses collègues en 2023 ; Segment Anything, de Kirillov et ses collègues la même année ; et tout récemment AlphaEarth Foundations, de Brown et ses collègues en 2025. Sur la figure, le principe est toujours le même : un pré-entraînement unique, puis des adaptations légères.

### Planche 42 — Conclusion · 10 s · 42 min 40
**À dire.** Onzième et dernière section : je voudrais terminer en revenant au fil que je vous avais annoncé au début.
**Transition.** Et la première chose à dire, c'est que cette histoire n'est pas linéaire.

### Planche 43 — Une histoire non linéaire · 1 min 20 · 44 min
**À dire.** L'histoire de la segmentation sémantique en télédétection ne suit pas une trajectoire linéaire qui irait simplement des classifieurs statistiques aux réseaux profonds ; elle résulte plutôt de plusieurs traditions scientifiques qui se sont progressivement rejointes — classification statistique, méthodes à noyaux, méthodes d'ensemble, modèles contextuels, champs de Markov, méthodes variationnelles, géométrie stochastique, apprentissage profond et modèles de fondation. Voici de nouveau la frise du début, et vous pouvez maintenant la lire comme un récit : les premières approches exploitent l'information spectrale locale ; les modèles contextuels et markoviens introduisent la cohérence spatiale ; les méthodes variationnelles et les processus ponctuels marqués modélisent les frontières, les régions et les objets ; les réseaux profonds apprennent automatiquement ces représentations ; et les transformers et les modèles de fondation cherchent aujourd'hui à construire des représentations géospatiales générales, multimodales et transférables. Et sous cette progression, un principe récurrent que vous avez vu réapparaître de planche en planche : une attache aux données plus une régularisation, des champs de Markov aux fonctions de perte des réseaux profonds.
**Transition.** Terminons par ce qui n'est pas résolu — et il y a de quoi faire.
**En réserve.** Les connexions mathématiques entre modèles graphiques probabilistes et apprentissage profond sont précisément l'objet de la synthèse publiée avec Martina Pastorino, Gabriele Moser et Sebastiano Serpico dans IEEE Signal Processing Magazine en 2026.

### Planche 44 — Perspectives · 1 min · 45 min
**À dire.** Les défis actuels restent nombreux, et je les énumère sans les hiérarchiser : la généralisation géographique, c'est-à-dire la capacité d'un modèle appris ici à fonctionner ailleurs ; le manque d'annotations, dont nous venons de parler ; la fusion des données optiques, radar et LiDAR ; la prise en compte de la temporalité, alors que nos archives sont par nature des séries ; l'interprétabilité des modèles ; et la robustesse opérationnelle, qui est la condition pour que tout cela serve réellement. Ces questions montrent que la segmentation sémantique en télédétection demeure un domaine ouvert, situé à l'intersection du traitement du signal et des images, de la modélisation probabiliste, de la géométrie, de la vision par ordinateur et de l'intelligence artificielle, dans un contexte géospatial. C'est, je crois, ce qui en fait encore aujourd'hui un très beau sujet de recherche.
**Transition.** Je vous remercie de votre attention.
**En réserve.** Cette intersection de disciplines n'est pas une formule de conclusion : c'est ce qui explique que le domaine n'ait jamais avancé par simple importation de la vision par ordinateur, comme je le disais dès la planche 5.

### Planche 45 — Merci de votre attention. · hors minutage · 45 min
**À dire.** Merci de votre attention — et merci à Martina Pastorino et Gabriele Moser, de l'Università di Genova, avec qui ce travail a été mené. Je suis à votre disposition pour vos questions.
**En réserve.** Les planches suivantes sont des annexes : la bibliographie complète et les crédits des figures ; je peux y revenir si une référence précise vous intéresse.

### Planche 46 — Références I · annexe · —
**À dire.** Voici la bibliographie complète de l'exposé, telle qu'elle figure dans l'article : soixante-dix-neuf entrées, dans l'ordre d'apparition, en commençant par l'article source lui-même et les ouvrages fondateurs des années 1970 et 1980.
**En réserve.** Cette première planche couvre les références 1 à 20, de l'article source et Duda et Hart jusqu'à Gislason, Benediktsson et Sveinsson.

### Planche 47 — Références II · annexe · —
**À dire.** Suite de la bibliographie : les forêts aléatoires, la texture, le contexte, puis les champs de Markov et leur optimisation.
**En réserve.** Références 21 à 36, de Belgiu et Drăguț à Krähenbühl et Koltun.

### Planche 48 — Références III · annexe · —
**À dire.** Suite : les CRF profonds, nos propres travaux avec Martina Pastorino et Gabriele Moser, puis la morphologie mathématique et les méthodes spectro-spatiales.
**En réserve.** Références 37 à 51, de Zheng et ses collègues à Mumford et Shah.

### Planche 49 — Références IV · annexe · —
**À dire.** Suite : les méthodes variationnelles, les contours actifs et les level sets, puis la bascule de 2012 et les premières architectures profondes.
**En réserve.** Références 52 à 66, de Samson, Blanc-Féraud, Aubert et Zerubia à Chen et ses collègues.

### Planche 50 — Références V · annexe · —
**À dire.** Fin de la bibliographie : les architectures multi-échelles, les transformers, l'apprentissage auto-supervisé et les modèles de fondation géospatiaux.
**En réserve.** Références 67 à 79, de Chen et ses collègues à Kirillov et ses collègues.

### Planche 51 — Crédits des figures · annexe · —
**À dire.** Dernière planche de secours : les crédits des sept figures de l'exposé, qui sont toutes celles de l'article — en particulier le jeu de données Zeebruges du comité technique IADF de l'IEEE GRSS, avec images et vérité terrain fournies par l'Académie royale militaire belge et l'ONERA, et l'image SPOT, copyright CNES.
**En réserve.** Les crédits figurent déjà sous chaque figure au fil de l'exposé ; cette planche ne fait que les récapituler, au cas où la question serait posée.

## Questions probables

**Les modèles de fondation rendent-ils tout le reste obsolète ?**
Non, et c'est même le cœur de ma conclusion. Ils prolongent des questions qui traversent toute l'histoire du domaine — intégrer des données hétérogènes, représenter le contexte spatial, généraliser à de nouvelles régions, tirer parti de modalités complémentaires — à ceci près qu'elles sont apprises plutôt que construites. Et leur coût de pré-entraînement, en calcul comme en énergie, pose de vraies questions d'empreinte environnementale et d'accessibilité.

**Les champs de Markov servent-ils encore à quelque chose ?**
Oui, et par deux voies. Les CRF sont entrés dans les réseaux profonds, d'abord comme modules de raffinement, puis comme couches différentiables — Zheng et ses collègues montrent en 2015 qu'un CRF se lit comme un réseau récurrent. Et nos travaux avec Martina Pastorino et Gabriele Moser vont jusqu'à CRFNet, en 2024, où un réseau convolutif profond apprend les potentiels du CRF.

**Comment règle-t-on le paramètre bêta, ou mu et nu chez Mumford–Shah ?**
Ce sont les curseurs entre fidélité aux observations et régularité de la solution : plus on les augmente, plus la carte est lisse, et moins elle suit le détail des données. Le compromis dépend de la résolution de l'image et de la taille des objets que l'on veut conserver. Pour le détail du cadre markovien, je renvoie à la synthèse de Zoltan Kato et moi-même, en 2012.

**SVM ou forêts aléatoires ?**
La comparaison n'est pas vraiment le sujet, parce que les deux améliorent la fonction de décision et restent indépendantes de la représentation qu'on leur donne. Les SVM généralisent remarquablement bien quand les échantillons d'apprentissage sont rares devant la dimension des données ; les forêts aléatoires demandent très peu de réglages, tolèrent le bruit et fournissent des mesures d'importance des variables utiles à l'interprétation.

**Pourquoi un modèle appris sur une région ne fonctionne-t-il pas ailleurs ?**
C'est la généralisation géographique, et c'est l'un des défis que je cite en perspectives. Les scènes de télédétection ont des propriétés qui varient selon les régions, les saisons et les conditions d'acquisition, et les réseaux convolutifs généralisent mal entre capteurs, entre régions et entre modalités. C'est précisément l'une des motivations des représentations transférables.

**Pourquoi les annotations sont-elles à ce point un goulot d'étranglement ?**
Parce que l'apprentissage supervisé de la segmentation demande des annotations pixel à pixel, dont la production est particulièrement coûteuse en télédétection. Le déséquilibre est frappant : les archives satellitaires sont abondantes et s'accumulent depuis des décennies, les annotations restent rares. C'est exactement ce que vise l'auto-supervision, avec les autoencodeurs masqués de He et ses collègues en 2022.

**Où sont passés les processus ponctuels marqués et la géométrie stochastique ?**
Ils figurent dans la lecture unifiée de la conclusion, dans la famille qui modélise explicitement les frontières, les régions et les objets, aux côtés des méthodes variationnelles. Faute de temps, je ne les développe pas ici, mais ils font partie des traditions qui ont convergé.

**Que reste-t-il de l'analyse orientée objet ?**
Beaucoup, en réalité. Le contexte régional identifié dès les années 1980 l'annonce directement, et Thomas Blaschke en fait la synthèse en 2010. Et l'idée de prendre les régions segmentées plutôt que les pixels comme unités d'analyse — Tarabalka, Benediktsson et Chanussot, en 2009 — améliore la cohérence spatiale des cartes tout en réduisant le bruit.

## Repères à ne pas se tromper

**L'exposé et ses auteurs**
- Article source : Martina Pastorino, Gabriele Moser, Josiane Zerubia, « Segmentation sémantique en télédétection », Traitement du Signal et des Images (TSI), GRETSI, 2027. Également rapport de recherche Inria RR-9631, HAL hal-05742224, septembre 2026.
- Josiane Zerubia, Centre Inria d'Université Côte d'Azur, équipe Ayana ; Martina Pastorino et Gabriele Moser, Università di Genova, DITEN.
- 51 planches, 11 sections, 79 références, 7 figures.

**Capteurs, données et figures**
- Landsat, optique, début des années 1970 ; SeaSat, radar, fin des années 1970.
- Jeu de données Zeebruges : comité technique IADF de l'IEEE GRSS ; images et vérité terrain de l'Académie royale militaire belge et de l'ONERA.
- Image IKONOS, 4 m, 3 bandes, fausses couleurs (infrarouge voisin, rouge, bleu).
- Image satellitaire SPOT, © CNES.
- Base ISPRS 2D Semantic Labeling Challenge, Potsdam.

**Sigles**
- MAP : maximum a posteriori ; MLC : maximum likelihood classifier. SVM : machines à vecteurs de support. RF : forêts aléatoires.
- MRF : champs de Markov ; CRF : champs conditionnels aléatoires ; ICM : modes conditionnels itérés.
- EMP : profils morphologiques étendus. FCN : réseaux entièrement convolutifs. ASPP : agrégation multi-échelle des architectures DeepLab.
- RSO : radar à synthèse d'ouverture. LiDAR. IADF : comité technique d'analyse d'image et de fusion de données de l'IEEE GRSS.

**Dates et noms, dans l'ordre de l'exposé**
- Duda et Hart, 1973 · Swain et Davis, 1978 · Richards, 1986 · Hughes, 1968 · Haralick, Shanmugam et Dinstein, 1973.
- Cortes et Vapnik, 1995 · Vapnik, 1998 · Schölkopf et Smola, 2002 · Camps-Valls et Bruzzone, 2009 · Mountrakis, Im et Ogole, 2011.
- Breiman, 2001 · Gislason, Benediktsson et Sveinsson, 2006 · Belgiu et Drăguț, 2016.
- Haralick et Shapiro, 1985 · Azencott et Graffigne, 1992 · Blaschke, 2010 · Csurka et ses collègues, 2023.
- Geman et Geman, 1984 · Besag, 1986 · Solberg, Taxt et Jain, 1996 · Bruzzone et Serpico, 1997 et 1999 · Moser, Serpico et Benediktsson, Proceedings of the IEEE, 2013 · Kato et Zerubia, 2012.
- Kirkpatrick, 1984 · Boykov, Veksler et Zabih, 2001 · Tanaka et ses collègues, 2003.
- Lafferty, McCallum et Pereira, 2001 · Krähenbühl et Koltun, 2011 · Zheng et ses collègues, 2015 · Pastorino et ses collègues, 2021, puis CRFNet, 2024 · Voisin, Krylov, Moser, Serpico et Zerubia, 2013.
- Dellepiane, Giusto, Serpico et Vernazza, 1991 · Serra, 1982 · Soille, 2003 · Landgrebe, 2003 · Benediktsson, Palmason et Sveinsson, 2005 · Dalla Mura et ses collègues, 2010 · Tarabalka, Benediktsson et Chanussot, 2009.
- Kass, Witkin et Terzopoulos, 1988 · Mumford et Shah, 1989 · Osher et Sethian, 1988 · Chan et Vese, 2001 · Samson, Blanc-Féraud, Aubert et Zerubia, 2000.
- Krizhevsky, Sutskever et Hinton, 2012 · Chen et ses collègues, 2014 · Castelluccio et ses collègues, 2015 · Long, Shelhamer et Darrell, 2015 · Ronneberger, Fischer et Brox, 2015 · He et ses collègues, 2016.
- Vaswani et ses collègues, 2017 · Dosovitskiy et ses collègues, 2021 · Liu et ses collègues (Swin), 2021 · Xie et ses collègues (SegFormer), 2021 · He et ses collègues (autoencodeurs masqués), 2022.
- Cong et ses collègues (SatMAE), 2022 · Jakubik et ses collègues, 2023 · Wang et ses collègues, 2023 · Kirillov et ses collègues (Segment Anything), 2023 · Brown et ses collègues (AlphaEarth Foundations), 2025.
- Pastorino, Moser, Serpico et Zerubia, IEEE Signal Processing Magazine, 2026.
