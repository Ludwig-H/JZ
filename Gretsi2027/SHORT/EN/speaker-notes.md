# Speaker notes — short version (24 slides, ≈ 20 min)

Keep this in front of you during the talk: for each slide, what there is to say, the sentence that brings on the next one, and what to use only if there is time.

## Before you start

- **Length**: six blocks, a full 20 minutes, questions not included.
  - Introduction (slides 1 to 5) — 4 min 30 on the clock.
  - From pixel to context (slides 6 to 9) — 9 min.
  - Markov and Bayesian models (slides 10 to 13) — 13 min 05.
  - Spectral-spatial and variational representations (slides 14 to 16) — 15 min 40.
  - Deep learning and foundation models (slides 17 and 18) — 18 min.
  - Open challenges, conclusion and thanks (slides 19 to 21) — 20 min.
  - Slides 22 to 24: bibliography, off the clock, only if someone asks.

- **The storyline in one sentence**: the history of semantic segmentation in remote sensing is the history of a progressive integration of increasing levels of context, and under this progression the same principle comes back from end to end — a data term plus a regularization.

- **Three ideas to get across, whatever happens**
  1. This is neither a catalog of methods nor a linear trajectory: several scientific traditions came together step by step.
  2. The same form runs through fifty years of work: data term plus regularization, from Markov random fields to the loss functions of deep networks.
  3. Deep learning does not remove the earlier concepts — spatial context, multiscale, fusion, object hierarchy — it learns them instead of building them by hand.

- **If you are running late**, cut in this order:
  1. Slide 15, mathematical morphology (45 s) — slide 14 is enough to carry the spectral-spatial idea.
  2. Slide 12, optimization of MRFs (50 s) — go straight from the energy to CRFs.
  3. Slide 8, discriminative and ensemble methods (1 min 10) — keep one sentence: they improve the decision, not the representation.
  4. Slide 4, what sets remote sensing apart (1 min) — fold the essential into slide 3.
  Never cut slides 5, 11 and 20: they are the storyline, the equation and the conclusion.

## Slide by slide

### Slide 1 — Semantic segmentation in remote sensing · 45 s · 45 s
**Say.** Thank you for having me in this historical session. In twenty minutes, I would like to tell you how semantic segmentation was built in remote sensing: how, in some fifty years, we went from a decision made pixel by pixel on a spectral signature to today's geospatial foundation models. This talk is based on a paper written with Martina Pastorino and Gabriele Moser, from Università di Genova, to appear in Traitement du Signal et des Images.
**Transition.** Here is the path I suggest we follow.
**In reserve.** The paper is also available as an Inria research report, RR-9631, deposited on HAL under the reference hal-05742224 since September 2026.

### Slide 2 — Outline · 30 s · 1 min 15
**Say.** Six steps, in chronological order: after a short introduction, we will go from pixel to context, then to Markov and Bayesian models, to spectral-spatial and variational representations, to deep learning and foundation models, and we will end on open challenges. Please do not see this as a catalog of methods: it is a single story, with a storyline that I will give you three slides from now.
**Transition.** Let us start by saying precisely what we are talking about.

### Slide 3 — From image to thematic map · 1 min 15 · 2 min 30
**Say.** Semantic segmentation means assigning to every pixel of an image a label from a predefined set of classes. The word itself took hold with the rise of deep learning, in the mid-2010s, but the problem has been studied for decades in remote sensing under the names supervised classification, per-pixel classification and contextual classification — we already find them in Duda and Hart in 1973, in Swain and Davis in 1978, in Richards in 1986. What we produce is a dense map: every pixel gets an interpretation, and that is exactly what sets this task apart from so-called low-level segmentation, which only partitions the image into homogeneous regions without attaching any meaning to them. In remote sensing, the goal is to turn satellite observations into land-cover and land-use maps, as in the example you see here.
**Transition.** It remains to understand why this problem, in our field, is not posed the way it is elsewhere.
**In reserve.** The aerial image and the map come from the Zeebruges dataset, released by the Image Analysis and Data Fusion Technical Committee, the IADF, of the IEEE GRSS; the imagery and the ground truth were provided by the Belgian Royal Military Academy and ONERA.

### Slide 4 — What sets remote sensing apart · 1 min · 3 min 30
**Say.** Our images are not natural images. They can come from optical sensors, from synthetic aperture radar or from LiDAR; their spatial and spectral resolutions vary widely; they are acquired at different dates and often combine several modalities. And they describe complex geographical scenes, whose properties change from region to region, from season to season, with the acquisition conditions. That is why the evolution of the field is not just an adaptation of the advances of computer vision: it comes from a convergence between statistical pattern recognition, signal and image processing, probabilistic modeling and, only more recently, deep learning.
**Transition.** Let us now state the problem formally, and I will give you the storyline of the talk.
**In reserve.** To this list the paper adds mathematical morphology, stochastic geometry and object-based analysis: seven scientific traditions in all, which came together step by step.

### Slide 5 — Storyline · 1 min · 4 min 30
**Say.** Formally, a remote sensing image is a function I defined on the image domain Omega, with values in R to the power d, where d is the number of available variables: spectral bands, but also SAR polarizations, LiDAR measurements, indices, digital terrain models or other ancillary data. Semantic segmentation means estimating a second function f, which goes from the same image domain to C, the finite set of semantic classes. And here is the storyline I would ask you to remember: the whole history of the field can be read as a progressive integration of increasing levels of context — local spectral information, then spatial coherence, then boundaries, regions and objects, then representation learning, and finally foundation models. We will see this same timeline again, exactly as it is, in the conclusion.
**Transition.** So let us go back to the very beginning of this history, when there was only the pixel.
**In reserve.** A second thread, more discreet, also runs through the whole talk: an energy in two pieces, one that sticks to the observations, one that imposes regularity. It will appear with Markov random fields and never leave us.

### Slide 6 — The first approaches: per-pixel · 1 min 10 · 5 min 40
**Say.** It all starts with the first Earth observation satellites: the Landsat program, optical, in the early 1970s, and SeaSat, radar, at the end of the same decade. These sensors create a new need: automatic methods able to produce land-cover maps from multispectral or radar images. The field then builds on the foundations of statistical pattern recognition: each pixel becomes an observation vector — the radiometric responses in the different bands, the SAR intensities, indices, ancillary data — and it is assigned the most probable class under a Bayesian decision rule. Under the assumption that the observations of each class follow a multivariate Gaussian distribution, we get the MAP classifier, maximum a posteriori, which will remain the reference method for several decades.
**Transition.** This success lasted a long time; its limits appeared as the sensors improved.
**In reserve.** This MAP classifier is often called, informally, the maximum likelihood classifier — the MLC of the English-language papers. Its success comes from three things: a simple probabilistic interpretation, a cheap implementation and satisfactory performance.

### Slide 7 — Two limitations: dimensionality and independence · 1 min 10 · 6 min 50
**Say.** Two limitations, and they are structural. The first is the curse of dimensionality, the phenomenon described by Hughes as early as 1968: adding spectral variables does not guarantee better performance when the number of training samples stays limited — in other words, spectral signatures alone are not enough. The second is the independence assumption on the observations: each pixel is decided in isolation, without using its neighborhood, even though geographical objects are strongly spatially correlated — an agricultural field, a forest, an urban area, a road network. The consequence is in front of you, on the right: noisy maps, the salt-and-pepper effect, and all the more marked as spatial resolution increases.
**Transition.** It is this observation that will progressively move the problem from a spectral classification to a spatial interpretation of the scenes.
**In reserve.** The map on the right comes from the work of Gabriele Moser, Sebastiano Serpico and Jón Atli Benediktsson, published in the Proceedings of the IEEE in 2013.

### Slide 8 — Discriminative and ensemble methods · 1 min 10 · 8 min
**Say.** From the late 1990s, another branch of the history develops: rather than modeling the distribution of the observations, the decision boundaries between classes are estimated directly. Support vector machines take hold very fast — Cortes and Vapnik in 1995, Vapnik in 1998 — thanks to the principle of margin maximization, which gives them excellent generalization even in high dimension; kernel methods then extend this framework to nonlinear problems without losing convexity. In parallel, Breiman's random forests, in 2001, learn decision trees on random subsets of the observations and of the variables, then combine them by a majority vote: little tuning, good robustness to noise, and variable importance measures that help interpret the models. But I would like to insist on one point, because it governs everything that follows: applied directly to the observation vectors, these methods improve the decision function, not the representation — they remain essentially per-pixel classifiers.
**Transition.** So the question that none of them addresses is still fully open: the spatial organization of the scene.
**In reserve.** Kernels specifically suited to geospatial observations will be developed: the background reference is the book by Schölkopf and Smola in 2002, and for remote sensing the book by Camps-Valls and Bruzzone in 2009 and the review by Mountrakis, Im and Ogole in the ISPRS Journal in 2011. For random forests in remote sensing, Gislason, Benediktsson and Sveinsson in 2006.

### Slide 9 — The contribution of spatial context · 1 min · 9 min
**Say.** Look at these three images. On the left, an IKONOS image at 4 meters resolution, in false color; in the middle, the per-pixel classification; on the right, the contextual classification of the same scene. From the 1980s and 1990s on, a large part of the research turns to introducing spatial context, starting from a very simple idea: in a remote sensing scene, a pixel is much more likely to belong to the same class as its immediate neighbors than to a completely different class. Classification then stops being a series of independent decisions: the labels must be estimated jointly, to produce a consistent representation of the scene.
**Transition.** What remained was to give this intuition a rigorous theoretical framework — that is what the next section is about.
**In reserve.** The paper distinguishes three levels of context: local context, between neighboring pixels or within windows of limited size; regional context, which describes sets of pixels by their texture, their shape, their size, and which announces object-based approaches; and global context, which concerns the overall organization of the scene. This hierarchy will keep structuring the field up to today's deep architectures.

### Slide 10 — Markov random fields: the first formalization · 1 min 10 · 10 min 10
**Say.** Markov random fields are the first general probabilistic formalization of this idea, and they very quickly become one of the most influential theoretical frameworks in the field — Geman and Geman in 1984, Besag in 1986. The principle: the labels are no longer independent variables, but a set of random variables defined on a neighborhood graph. Under the Markov assumptions, and thanks to the equivalence between Markov random fields and Gibbs distributions, the search for the optimal map is written as a maximum a posteriori estimation — and, by Bayes' theorem, this maximization becomes strictly equivalent to an energy minimization. It is this equivalence that gives Markov random fields their reach: a single framework linking local data and spatial consistency.
**Transition.** Let us now look more closely at what this energy contains, because that is where the storyline of the whole talk lies.
**In reserve.** For an overview of Markov random fields in segmentation, we refer to the monograph I wrote with Zoltan Kato, published in Foundations and Trends in Signal Processing in 2012.

### Slide 11 — Data term + regularization · 1 min · 11 min 10
**Say.** Here is, to my mind, the most important equation of this talk. The energy splits into two terms: a data term, derived from the likelihood of the observations, and a spatial regularization term, which promotes consistency between neighboring pixels; the parameter beta controls the trade-off between fidelity to the observations and regularity of the solution. Concretely, a neighborhood system is defined — first or second order, as in the two figures on the right — and the clique potentials penalize certain label configurations, typically class changes between adjacent pixels. Remember this form: data term plus regularization. We will find it again in variational methods, and all the way into the loss functions of deep networks.
**Transition.** One practical difficulty remains, and it is a serious one: finding the configuration that minimizes this energy.
**In reserve.** Segmentation thus results from a trade-off between the information carried by the data and an explicit assumption of spatial consistency — that is, in Bayesian terms, between the likelihood and the prior.

### Slide 12 — Optimization and uses of MRFs · 50 s · 12 min
**Say.** Minimizing this energy is a hard combinatorial optimization problem, so a large part of the work has gone into suboptimal strategies that are usable in practice: the ICM algorithm, simulated annealing, the Gibbs sampler, then the graph cuts of Boykov, Veksler and Zabih in 2001 and loopy belief propagation. These models then became a reference tool for contextual classification, multisource segmentation, restoration, change detection and the fusion of optical, radar or LiDAR data. But their contribution goes well beyond these applications: they provide a general probabilistic formulation of spatial regularization, and it is on that account that they have durably influenced everything that followed.
**Transition.** Including, and this is what I would like to show you now, deep learning itself.
**In reserve.** Simulated annealing refers to Kirkpatrick in 1984, the Gibbs sampler to Geman and Geman in 1984, loopy belief propagation to Tanaka, Inoue and Titterington in 2003. On fusion and applications: Solberg, Taxt and Jain in 1996, Derin and Elliott in 1987, Moser and Serpico in 2013 — this last work combining precisely SVMs and Markov random fields in a single framework.

### Slide 13 — From MRFs to CRFs: a bridge to deep learning · 1 min 05 · 13 min 05
**Say.** Conditional random fields extend this family naturally: instead of describing the joint distribution of the observations and the labels, they model directly the conditional distribution of the map given the observations — Lafferty, McCallum and Pereira, in 2001. This shift, which looks technical, allows complex discriminative features and fits far more naturally with supervised learning methods. The fully connected models of Krähenbühl and Koltun, in 2011, preserve object boundaries much better. Then CRFs enter deep architectures, as refinement modules or as differentiable layers — Zheng and colleagues, in 2015 — and this is where our work with Martina Pastorino and Gabriele Moser fits in, on hierarchical Markov frameworks and on CRFs whose potentials are learned by a network. From this whole Markov block, remember one idea that will run through the rest of the talk: a land-cover map must be consistent with the local observations, but also with the spatial organization of the scene.
**Transition.** So far we have regularized the labels; another family of methods will instead work on what the classifier receives as input.
**In reserve.** The mathematical connections between probabilistic graphical models and deep learning are precisely the subject of the overview we published with Martina Pastorino, Gabriele Moser and Sebastiano Serpico in IEEE Signal Processing Magazine in 2026.

### Slide 14 — Enriching the representation, not only the labels · 50 s · 13 min 55
**Say.** Here is the distinction I would like you to keep from this slide: contextual models regularize the labels, whereas spectral-spatial methods enrich the features, upstream, before classification. This paradigm develops in the 2000s, driven by improving resolutions: on high-resolution images, the internal structure of geographical objects becomes visible, one class can show strong spectral variability, while different objects sometimes have very close radiometric signatures. Radiometric signatures alone are therefore no longer enough: texture, shape, size, spatial organization and neighborhood relations become as discriminative as the spectral values themselves. And this rationale paves the way directly for the multiscale representations that deep networks will learn on their own some fifteen years later.
**Transition.** The most emblematic tool of this approach comes from mathematical morphology.
**In reserve.** On integrating intensity and texture information in radar imaging, the early reference is Dellepiane, Giusto, Serpico and Vernazza, in 1991; and Blaschke's 2010 review makes the link with object-based analysis.

### Slide 15 — Mathematical morphology and multiscale profiles · 45 s · 14 min 40
**Say.** The basic operators come from mathematical morphology — erosion, dilation, openings, closings — for which Serra and then Soille wrote the reference books. You see here, around the original image, what an erosion and a dilation produce: we do not change the labels, we change what the image shows. The decisive step comes with the extended morphological profiles of Benediktsson and colleagues, in 2005, then the attribute profiles of Dalla Mura and colleagues, in 2010: they describe the shape, the size and the contrast of structures at several scales. Combined with support vector machines — Fauvel and colleagues, in 2008 — they become a reference for hyperspectral and very high resolution data.
**Transition.** A third family, developed in parallel, will express the same requirement of spatial consistency, but in a continuous language.
**In reserve.** These features are independent of the classifier: they can be fed to SVMs, to random forests or to neural networks. The gains observed therefore come as much from the quality of the representation as from the classifier used.

### Slide 16 — Variational methods: regularizing the solution · 1 min · 15 min 40
**Say.** From the late 1980s, another family of approaches develops an idea very close to that of Markov random fields, but without explicitly modeling a probability distribution on the labels: we look for the partition of the image that achieves the best trade-off between fidelity to the observations and the spatial or geometric regularity of the solution. One of the founding models is the Mumford and Shah functional, in 1989, which looks at the same time for a regular approximation of the image and for the set of discontinuities corresponding to object boundaries. Look at the form of the energy written here and compare it with the Markov energy we saw a few slides ago: it is exactly the same principle, with a parameter that sets the trade-off. This closeness is now widely recognized — Bayesian models, Markov random fields, variational methods and graph-based formulations are often different expressions of the same idea.
**Transition.** We now reach the moment when the history changes regime, and that moment has a date.
**In reserve.** With Christophe Samson, Laure Blanc-Féraud and Gilles Aubert, we proposed in 2000 a functional that unifies classification, segmentation and restoration in a single formulation — one of the direct bridges between probabilistic approaches and variational models. Around this functional runs the whole line of active contours, which come before it, then level sets, which handle topology changes automatically, and later the region-based models, more robust than gradients alone in noisy images.

### Slide 17 — Going deep · 1 min 10 · 16 min 50
**Say.** 2012 is the turning point: at the ImageNet challenge, the AlexNet network — Krizhevsky, Sutskever and Hinton — demonstrates a dramatic improvement in natural-image classification. The real change is not the architecture, it is the principle: the representation and the decision function are learned jointly, directly from the data, without hand-designing spectral, textural or geometric features. Three architectures structure what follows: the fully convolutional networks of Long, Shelhamer and Darrell, in 2015, which directly produce a dense prediction at the pixel level, and whose architecture you see on the right, applied to the Potsdam aerial images. Then U-Net, the same year, whose skip connections restore the spatial information lost in downsampling, and DeepLab, whose dilated convolutions and multiscale representations enlarge the receptive field without degrading the resolution of the predictions. I would like to insist on one point: deep learning does not make the concepts of the previous decades disappear — spatial context, multiscale, fusion, object hierarchy — it reformulates them in an end-to-end learning framework.
**Transition.** Two obstacles remained, however, and they are what opens the last chapter.
**In reserve.** The aerial images in that figure come from the ISPRS 2D Semantic Labeling Challenge dataset on Potsdam. Two other things matter in this period: the transfer of models pre-trained on large natural-image datasets to aerial and satellite images, and multimodal fusion learned directly by the network, to which Audebert, Le Saux and Lefèvre contributed in 2018.

### Slide 18 — Transformers, self-supervision and foundation models · 1 min 10 · 18 min
**Say.** Convolutional networks remain limited by two things: their appetite for pixel-level annotations, which are very costly to produce in remote sensing, and their difficulty in modeling very long-range spatial dependencies. Attention mechanisms answer the second: transformers, developed first for language processing by Vaswani and colleagues in 2017, then adapted to vision by Dosovitskiy and colleagues in 2021, model directly the relations between distant elements. This matters to us, because identifying a building or a field does not rest only on local appearance, but on the organization within the scene. Self-supervised learning answers the first: masked autoencoders, He and colleagues in 2022, learn rich representations on unlabeled data — and our satellite archives are precisely abundant, while annotations are rare. From the combination of the two come the geospatial foundation models, whose principle is sketched on the right: the goal is no longer to optimize an architecture for one particular dataset, but to learn general, multimodal representations that transfer between sensors, between regions and between applications.
**Transition.** This is obviously not the end of the history, and I would like to end on what remains open.
**In reserve.** The other side has to be said: the pre-training cost of these models is very high, in computing time as well as in hardware and energy resources, which raises real questions of environmental footprint and of accessibility for the scientific community. And this is not a break: integrating heterogeneous data, representing context, generalizing to new regions — these are the questions of the whole talk; the difference is that they are now learned rather than built explicitly.

### Slide 19 — Open challenges · 40 s · 18 min 40
**Say.** The challenges are still many, and I give them to you without ranking them. Generalization first: across regions, across seasons, across sensors, across resolutions — a model learned here does not necessarily work elsewhere. Then the lack of annotations, with the cost of ground-truth data, class imbalance and labels that are often noisy. Then multimodal fusion — optical, SAR, LiDAR, time series, ancillary data — and robustness to distribution shift, to clouds, to noise, to artifacts, to rare events. And finally interpretability, that is, our ability to understand and control increasingly large models.
**Transition.** Allow me now to pick up the storyline from the beginning.
**In reserve.** Taking time into account deserves a special mention: our archives are series by nature, and we still treat them too often as isolated images.

### Slide 20 — Conclusion: a nonlinear history · 1 min 20 · 20 min
**Say.** What I would like you to remember is, first, that this history is not linear: it does not go from statistical classifiers to deep networks, it comes from several traditions that came together step by step — statistical classification, kernel methods, ensemble methods, contextual models, Markov random fields, variational methods, stochastic geometry, deep learning and foundation models. Here again is the timeline from the beginning, and you can now read it as a story: the local spectral information of the first approaches, the spatial coherence of contextual and Markov models, the boundaries, regions and objects of variational methods and marked point processes, then representation learning, and today foundation models. And under this progression, one recurring principle, which you have seen come back slide after slide: a data term plus a regularization, from Markov random fields to the loss functions of deep networks. That, I believe, is what makes the unity of this field — and what still makes it, today, a very fine research subject, at the intersection of signal and image processing, probabilistic modeling, geometry, computer vision and artificial intelligence.
**Transition.** Thank you for your attention.
**In reserve.** If only one sentence were to be kept: this is not the history of methods replacing one another, it is the history of the progressive integration of increasing levels of context.

### Slide 21 — Thank you for your attention. · off the clock · 20 min
**Say.** Thank you for your attention — and thank you to Martina Pastorino and Gabriele Moser, from Università di Genova, with whom this work was carried out. I am happy to take your questions.
**In reserve.** The next three slides are the full bibliography; I can go back to them if a particular reference is of interest.

### Slide 22 — References I · appendix · —
**Say.** The full bibliography of the talk, in order of appearance, starting with the source paper itself, available as Inria research report RR-9631 on HAL.
**In reserve.** This slide covers references 1 to 21: from Duda and Hart in 1973 to Blaschke's object-based analysis in 2010, by way of Hughes, Geman and Geman, Besag, Solberg, Vapnik, Breiman and Gislason.

### Slide 23 — References II · appendix · —
**Say.** Continuation of the bibliography: Markov random fields and their optimization, CRFs, then our work with Martina Pastorino and Gabriele Moser, and the beginning of mathematical morphology.
**In reserve.** References 22 to 38: from Kato and Zerubia in 2012 to Benediktsson, Palmason and Sveinsson in 2005, by way of Kirkpatrick, Boykov, Lafferty, Krähenbühl and Koltun, Zheng, CRFNet and Voisin.

### Slide 24 — References III · appendix · —
**Say.** End of the bibliography: attribute profiles, variational methods, the 2012 turning point and deep architectures, then transformers, self-supervision and foundation models.
**In reserve.** References 39 to 54: from Dalla Mura to Segment Anything by Kirillov and colleagues in 2023. Reference 45 is our overview in IEEE Signal Processing Magazine, in 2026.

## Likely questions

**Are Markov random fields outdated in the age of foundation models?**
No, and that is even one of the points of the talk. CRFs have entered deep architectures as refinement modules or as differentiable layers, since the work of Zheng and colleagues in 2015, and we have ourselves worked on hierarchical Markov frameworks and on CRFs whose potentials are learned by a network. The mathematical connections between probabilistic graphical models and deep learning are the subject of our overview in IEEE Signal Processing Magazine in 2026.

**What exactly is the difference between semantic segmentation and segmentation as such?**
Semantic segmentation produces a dense map in which every pixel gets a label from a predefined set of classes, so an interpretation. So-called low-level segmentation only partitions the image into homogeneous regions, without attaching any meaning to them. It is the presence of the class ontology that makes all the difference.

**Why not simply carry over the advances of computer vision?**
Because our images are not natural images: optical sensors, synthetic aperture radar or LiDAR, widely varying spatial and spectral resolutions, multitemporal and multimodal acquisitions, and geographical scenes whose properties change with the region, the season and the acquisition conditions. The field was therefore built by the convergence of several traditions — statistical pattern recognition, signal and image processing, probabilistic modeling, mathematical morphology, stochastic geometry, object-based analysis — and, only more recently, deep learning.

**Are SVMs and random forests still of interest today?**
They improved the decision function a great deal, but not the representation: applied to the observation vectors, they remain per-pixel classifiers. Their strength is that they are independent of the representation, which makes it possible to combine them with textural, morphological or spectral-spatial features. The pairing of morphological profiles and SVMs, in Fauvel and colleagues in 2008, is the best-known example.

**How do we cope with so few annotations?**
That is exactly what self-supervised learning answers: masked autoencoders, He and colleagues in 2022, show that rich representations can be learned on unlabeled data, and our satellite archives are abundant while ground-truth data remains rare and costly. This does not close the question, though: the cost of annotations, class imbalance and noisy labels are still among the open challenges.

**What is the real cost of foundation models?**
Pre-training is particularly expensive, in computing time as well as in hardware and energy resources. This raises questions of environmental footprint, but also of accessibility for the scientific community, not all of which has the means to pre-train such models. It is a point the paper mentions explicitly, and one that I think has to be discussed.

**What happened to stochastic geometry and to the time dimension?**
They are two victims of the short format. Stochastic geometry and marked point processes are among the traditions that converged, and they act precisely at the level of modeling boundaries, regions and objects. As for time, it is among the open challenges: our archives are series by nature, and the integration of time series remains a major line of work.

## Facts to get right

**Sensors and programs**
- Landsat, optical, **early** 1970s — SeaSat, radar, **late** 1970s. Do not swap them.
- IKONOS, the image on slide 9: 4 meters resolution, 3 bands, false-color composite.
- Datasets cited: Zeebruges (IADF Technical Committee of the IEEE GRSS; imagery and ground truth from the Belgian Royal Military Academy and ONERA); Potsdam (ISPRS 2D Semantic Labeling Challenge).

**Dates and names, in chronological order**
- Hughes, 1968 — curse of dimensionality, known as the Hughes phenomenon.
- Duda and Hart, 1973; Swain and Davis, 1978 — the founding textbooks.
- Serra, 1982 — mathematical morphology.
- Geman and Geman, 1984 — Markov random fields, Gibbs distributions, Gibbs sampler.
- Kirkpatrick, 1984 — simulated annealing.
- Richards, 1986; Besag, 1986; Derin and Elliott, 1987.
- Mumford and Shah, 1989 — one of the founding variational functionals.
- Dellepiane, Giusto, Serpico and Vernazza, 1991.
- Cortes and Vapnik, 1995 — support vector machines; Solberg, Taxt and Jain, 1996; Vapnik, 1998.
- Samson, Blanc-Féraud, Aubert and Zerubia, 2000.
- Breiman, 2001 — random forests; Boykov, Veksler and Zabih, 2001 — graph cuts; Lafferty, McCallum and Pereira, 2001 — CRFs. Three references from 2001, do not mix them up.
- Schölkopf and Smola, 2002; Soille, 2003 — mathematical morphology; Tanaka, Inoue and Titterington, 2003.
- Benediktsson, Palmason and Sveinsson, 2005 — extended morphological profiles.
- Gislason, Benediktsson and Sveinsson, 2006; Fauvel and colleagues, 2008; Camps-Valls and Bruzzone, 2009.
- Dalla Mura and colleagues, 2010 — attribute profiles; Blaschke, 2010 — object-based analysis.
- Krähenbühl and Koltun, 2011 — fully connected CRFs; Mountrakis, Im and Ogole, 2011.
- Kato and Zerubia, 2012; Krizhevsky, Sutskever and Hinton, 2012 — AlexNet.
- Moser, Serpico and Benediktsson, 2013, Proceedings of the IEEE; Moser and Serpico, 2013; Voisin and colleagues, 2013.
- Long, Shelhamer and Darrell, 2015 — FCN; Ronneberger, Fischer and Brox, 2015 — U-Net; Zheng and colleagues, 2015 — CRF as a recurrent network. Three references from 2015.
- Vaswani and colleagues, 2017 — transformers.
- Audebert, Le Saux and Lefèvre, 2018; Chen and colleagues, 2018 — DeepLab.
- Dosovitskiy and colleagues, 2021 — transformers in vision; Pastorino and colleagues, 2021.
- He and colleagues, 2022 — masked autoencoders; Pastorino, Moser, Serpico and Zerubia, 2022.
- Kirillov and colleagues, 2023 — Segment Anything; Pastorino, Moser, Serpico and Zerubia, 2024 — CRFNet.
- Xiao and colleagues, 2025 — state of the art on foundation models.
- Pastorino, Moser, Serpico and Zerubia, 2026 — IEEE Signal Processing Magazine.

**Acronyms**
- SAR: synthetic aperture radar (RSO in French).
- MAP: maximum a posteriori. MLC: maximum likelihood classifier, the informal name of the same classifier under the Gaussian assumption.
- MRF: Markov random fields. CRF: conditional random fields. ICM: iterated conditional modes.
- SVM: support vector machines. RF: random forests.
- EMP: extended morphological profiles. DTM: digital terrain model.
- FCN: fully convolutional networks.
- IADF: the Image Analysis and Data Fusion Technical Committee of the IEEE GRSS.

**Numbers and identifiers**
- 24 slides, 20 minutes, 54 references.
- Source paper: Pastorino, Moser and Zerubia, Traitement du Signal et des Images, GRETSI; also Inria RR-9631, HAL hal-05742224, September 2026.
- Affiliation: Inria Centre at Université Côte d'Azur, Ayana project-team; Martina Pastorino and Gabriele Moser, Università di Genova, Diten.
