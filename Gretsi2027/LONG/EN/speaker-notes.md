# Speaker notes — long version (51 slides, ~45 min)

This document is the full script of the talk. Slide by slide, it gives what to say, the sentence that leads into the next one, and what to keep in reserve.

## Before you start

- **Timing**: opening and framing, slides 1 to 6, up to 5 min 30; the pixel era, slides 7 to 16, up to 15 min; spatial context and Markov random fields, slides 17 to 24, up to 24 min 30; representations and energies, slides 25 to 32, up to 33 min; deep learning and foundation models, slides 33 to 41, up to 42 min 30; conclusion, slides 42 to 44, up to 45 min. The thank-you slide and the six appendix slides are off the clock.
- **The storyline in one sentence**: the history of semantic segmentation in remote sensing is the history of the progressive integration of increasing levels of context — local spectral information, spatial coherence, boundaries and regions and objects, representation learning, foundation models.
- **Three ideas to get across no matter what**:
  1. The field never moved forward by simply importing computer vision. It is the convergence of several traditions — statistical, Markov, variational, morphological, object-based, then deep.
  2. One principle runs through all of it: a data term plus a regularization, from Markov random fields to Mumford–Shah and all the way to the loss functions of deep networks.
  3. Deep learning and foundation models do not remove the old questions — context, scales, fusion, generalization. They learn them instead of building them.
- **If you are running late**, cut in this order: slide 27 (mathematical morphology, 1 min 10, the illustration is nice but slide 28 is enough); slide 23 (optimizing, 1 min 20, it is a catalog of algorithms); slide 36 (context, scales, modalities, 1 min 20, another catalog); slide 16 (the pixel era, 1 min, if the storyline is already clear); slide 30 (active contours, 1 min 20, you can go straight into Mumford–Shah). Never cut slides 6, 22, 32, 37 and 43: they are the five key points of the story.

## Slide by slide

### Slide 1 — Semantic segmentation in remote sensing · 1 min · 1 min
**Say.** Thank you for having me. I would like to tell you how semantic segmentation was built in remote sensing — that is, how we went, in about fifty years, from a decision taken pixel by pixel on a spectral signature to today's geospatial foundation models. This talk is based on a paper written with Martina Pastorino and Gabriele Moser, from Università di Genova, to appear in Traitement du Signal et des Images.
**Transition.** The outline of the talk is exactly the outline of the paper. Here it is.
**In reserve.** The paper is already available as an Inria research report, RR-9631, on HAL, hal-05742224, since September 2026.

### Slide 2 — Outline · 30 s · 1 min 30
**Say.** Eleven sections, in the chronological order of the history of the field: per-pixel statistical classification, discriminative methods, ensemble methods, spatial context, Markov random fields, spectral-spatial and variational methods, then deep learning and foundation models. Keep in mind that this is not a catalog. It is one single story, with a storyline.
**Transition.** Let us start by saying exactly what we are talking about.

### Slide 3 — Introduction · 10 s · 1 min 40
**Say.** First part: what semantic segmentation is, what sets remote sensing apart, and the storyline of the whole talk.
**Transition.** And first, the definition.

### Slide 4 — From image to thematic map · 1 min 30 · 3 min 10
**Say.** Semantic segmentation means assigning to every pixel of an image a label from a predefined set of classes. The word came into use with deep learning, in the mid-2010s, but the problem has been studied for decades in remote sensing under the names supervised, per-pixel and contextual classification — you will already find them in Duda and Hart in 1973, Swain and Davis in 1978 and Richards in 1986. The result is a dense map: every pixel receives an interpretation. That is what distinguishes this task from so-called low-level segmentation, which only partitions the image into homogeneous regions without attaching any meaning to them. In remote sensing, the goal is to turn satellite observations into land-cover and land-use maps, as in this example.
**Transition.** What remains is to understand why this problem, in remote sensing, is not solved the way it is elsewhere.
**In reserve.** The image and the map come from the Zeebruges dataset, released by the Image Analysis and Data Fusion Technical Committee, the IADF, of the IEEE GRSS. Imagery and ground truth were provided by the Belgian Royal Military Academy and ONERA.

### Slide 5 — What sets remote sensing apart · 1 min 10 · 4 min 20
**Say.** Our images are not natural images: they can come from optical sensors, from synthetic aperture radar or from LiDAR. Their spatial resolutions vary widely, they are acquired at different dates, and they often combine several modalities. And they describe complex geographical scenes, whose properties change with the region, with the season, with the acquisition conditions. This is why the evolution of the field is not a mere adaptation of advances in computer vision. It is a convergence between statistical pattern recognition, signal and image processing, probabilistic modeling, mathematical morphology, stochastic geometry, object-based image analysis and, only recently, deep learning.
**Transition.** Let us now state the problem formally, and I will give you the storyline of the talk.

### Slide 6 — Formalization and storyline · 1 min 10 · 5 min 30
**Say.** Formally, a remote sensing image is a function I defined on the image domain omega, with values in R to the power d, where d is the number of variables available: a panchromatic band, multispectral or hyperspectral bands, SAR polarizations, LiDAR measurements, but also spectral indices, digital terrain models or other ancillary data. Semantic segmentation means estimating a second function f, which goes from the same image domain to C, the finite set of semantic classes. And here is the storyline I propose to follow: the whole history of the field can be read as the progressive integration of increasing levels of context — local spectral information, then spatial coherence, then boundaries, regions and objects, then representation learning, and finally foundation models. Remember this timeline. We will see it again in the conclusion.
**Transition.** So let us go back to the very beginning of this story, when there was only the pixel.
**In reserve.** A second, quieter thread runs through the whole talk: a data term plus a regularization. It will appear with Markov random fields, then in variational models, and all the way into the loss functions of deep networks.

### Slide 7 — Per-pixel statistical classification · 10 s · 5 min 40
**Say.** Second section: the first approaches, the ones that look at one pixel at a time.
**Transition.** It all starts with the first satellites.

### Slide 8 — The first approaches (1970s–1980s) · 1 min 20 · 7 min
**Say.** It all starts with the first Earth observation satellites: the Landsat program, optical, in the early 1970s, and SeaSat, radar, at the end of the same decade. These sensors create a new need, the need for automatic methods able to produce land-cover maps. The field then builds on the foundations of statistical pattern recognition. Each pixel becomes an observation vector — radiometric responses in the different bands, SAR intensities, indices, ancillary data — and the pixel is assigned the most probable class, following a Bayesian decision rule. Under the assumption that the observations of each class follow a multivariate Gaussian distribution, we obtain the MAP classifier, which will remain the reference method for several decades.
**Transition.** Its success lasted a long time. Its limitations appeared with the progress of the sensors.
**In reserve.** The MAP classifier is often called, informally, the maximum likelihood classifier, the MLC of the English-language literature. Its success comes from three things: a simple probabilistic interpretation, a cheap implementation and satisfactory performance.

### Slide 9 — Two structural limitations · 1 min 10 · 8 min 10
**Say.** Two limitations, and they are structural. The first is the curse of dimensionality, the phenomenon described by Hughes as early as 1968: adding spectral variables does not improve performance when the number of training samples remains limited. In other words, spectral signatures alone are not enough. The second is the independence assumption on the observations: each pixel is decided in isolation, without using its neighborhood, whereas geographical objects are strongly spatially correlated — an agricultural field, a forest, an urban area, a road network. The consequence is immediate: noisy maps, all the more so as spatial resolution increases.
**Transition.** Rather than telling you, let me show you.

### Slide 10 — The result: noisy maps · 1 min 20 · 9 min 30
**Say.** On the left, an IKONOS image at 4 meters resolution, in false color; on the right, the per-pixel classification of the same image. Take a moment to look at the noise in the map: this is the salt-and-pepper effect, the visual signature of the independence assumption. What this image says is that the decision can no longer depend on the radiometry of a single pixel alone: it needs its spatial environment. Historically, this is where the problem stops being a spectral classification and becomes one of spatial interpretation of scenes. And it is this shift that opens the way to Geman and Geman in 1984, to Besag in 1986, to Solberg and colleagues in 1996.
**Transition.** Before we come to spatial context, we need to tell another branch of the story, the one where the aim is to improve not the representation, but the classifier itself.
**In reserve.** The false-color composite uses near infrared, red and blue. The maps come from the work of Gabriele Moser and colleagues, published in the Proceedings of the IEEE in 2013. We will see this image again on slide 19, with the contextual map added.

### Slide 11 — Discriminative and kernel methods · 10 s · 9 min 40
**Say.** Third section: we stop modeling the distribution of the observations and estimate the boundary between classes directly.
**Transition.** The emblematic tool of this shift is support vector machines.

### Slide 12 — Estimating the boundary rather than the distribution · 1 min 20 · 11 min
**Say.** From the late 1990s, interest shifts to discriminative methods, whose aim is to estimate the decision boundaries between classes directly rather than to model the statistical distribution of the observations. This is a response to two well identified difficulties: Gaussian assumptions that are often unrealistic, and a dimensionality of the data that keeps growing. Among these approaches, support vector machines very quickly become a reference for the supervised classification of remote sensing images. They arise from statistical learning theory — Cortes and Vapnik in 1995, Vapnik in 1998 — and they rely on margin maximization between classes. That gives them excellent generalization even when the training samples are few compared with the dimension of the data, and in remote sensing, where annotation is expensive, this property matters enormously.
**Transition.** But how do we handle nonlinear problems without losing what makes this formulation strong?

### Slide 13 — Kernels: nonlinearity without losing convexity · 1 min 30 · 12 min 30
**Say.** Kernel methods extend this framework naturally to nonlinear problems: we build complex decision boundaries while preserving a convex formulation of the optimization problem. During the 2000s, SVMs become one of the most widely used classifiers in remote sensing — multispectral, hyperspectral, multisource — to the point that kernels tailored to the characteristics of geospatial observations are developed. Let me insist on one point, because it governs everything that follows: SVMs improve the decision function, not the representation. Applied directly to observation vectors, they remain per-pixel classifiers, and they do not integrate spatial dependencies between labels. This is why, from that moment on, two research directions largely evolve in parallel: new classifiers on one side, richer and richer spatial representations on the other.
**Transition.** Let us follow the classifier track first, with ensemble methods.
**In reserve.** On kernels, the background reference is the book by Schölkopf and Smola, in 2002. For remote sensing, the book by Camps-Valls and Bruzzone in 2009, and the review by Mountrakis, Im and Ogole in the ISPRS Journal in 2011.

### Slide 14 — Ensemble methods · 10 s · 12 min 40
**Say.** Fourth section: while kernel methods take up a large part of the work on supervised classification, another direction develops in parallel, with a very different idea.
**Transition.** And in this family, one method will catch on almost as fast as SVMs.

### Slide 15 — Random forests · 1 min 20 · 14 min
**Say.** The principle of ensemble learning is simple: rather than perfecting a single classifier, we combine several, and we gain in robustness and in generalization. Random forests, proposed by Leo Breiman in 2001, build a set of decision trees, each learned on randomly drawn subsets — and randomness plays twice, on the observations and on the variables — then aggregate their predictions by majority vote. This strategy limits overfitting while keeping a strong ability to model nonlinear relations. What explains how fast they spread is above all how convenient they are: little tuning, robustness to noise, a large number of variables without difficulty, and importance measures that really help interpret the model. The first applications, by Gislason, Benediktsson and Sveinsson in 2006, deal with multispectral and hyperspectral data, and random forests then become a reference tool for land-cover mapping, change detection and multisource data fusion.
**Transition.** Like SVMs, however, random forests remain independent of the representation they are given. It is time to take stock.
**In reserve.** The review by Belgiu and Drăguț, in 2016, surveys the uses. This neutrality with respect to the representation gives them a long life. We have used them ourselves, with Martina Pastorino and Gabriele Moser, as ensembles of decision trees inside a hierarchical causal Markov framework, in 2021.

### Slide 16 — The pixel era: takeaways · 1 min · 15 min
**Say.** Let us stop for a moment, because we are at a hinge of the talk. Discriminative methods and ensemble methods bring considerable gains, but these gains are on the classifier, and on the classifier only. They remain independent of the representation, be it spectral, textural, morphological or spectral-spatial. The fundamental limitation of per-pixel approaches remains intact: the spatial organization of the scene is still not taken into account explicitly. From here on, two complementary responses will structure the rest of the talk: regularize the labels — that will be the contextual, the Markov, the variational — or enrich the features — that will be the spectral-spatial and the object-based.
**Transition.** Let us take the first of these two paths: bringing spatial context into the decision itself.
**In reserve.** These two directions do not follow one another. They largely evolve in parallel throughout the 2000s. I present them one after the other for the clarity of the talk.

### Slide 17 — Contextual classification · 10 s · 15 min 10
**Say.** Fifth section: contextual classification and the first spatial models. This is where the pixel stops being alone.
**Transition.** The starting point is a common-sense observation, stated as early as the 1980s.

### Slide 18 — Three levels of context · 1 min 50 · 17 min
**Say.** The idea is simple, and it is already in the textbooks of the 1980s, in John Richards for instance: in a remote sensing scene, geographical objects show strong spatial coherence, so a pixel is much more likely to belong to the class of its immediate neighbors than to a completely different one. The relevant information therefore no longer lies in the local radiometric response alone, but also in neighborhood relations and in regional structures. The community then gradually distinguishes three levels. Local context is the interactions between neighboring pixels and small fixed-size windows, in Haralick and Shapiro in 1985; regional context describes sets of pixels by their texture, their shape, their size and the homogeneity of the segmented regions, and already foreshadows object-based image analysis, of which Thomas Blaschke will give the synthesis in 2010; global context seeks to integrate the overall organization of the scene, the relations between objects and prior knowledge about their layout. This hierarchy will remain a structuring principle for forty years, from the multi-level Markov random fields of Azencott and Graffigne, in 1992, all the way into contemporary deep architectures, where the review by Csurka and colleagues, in 2023, takes it up as it is.
**Transition.** And this is not just an attractive idea: the contribution of context can be measured, on the same image.
**In reserve.** What triggers this turn is very concrete. Improving the classifier was not enough to make the salt-and-pepper artifacts disappear. The model had to be addressed, not only the decision rule.

### Slide 19 — The measurable contribution of context · 1 min 30 · 18 min 30
**Say.** You recognize the image from earlier: IKONOS, 4 meters, three bands in a false-color composite, and in the center the per-pixel map we had already seen. On the right, the map obtained by integrating spatial context, after the work of Gabriele Moser, Sebastiano Serpico and Jón Atli Benediktsson published in the Proceedings of the IEEE in 2013. I will give you a few seconds to look: the noise disappears, fields become fields again, urban structures become readable again. These gains have been documented on multispectral, multitemporal and multisource data — Solberg, Taxt and Jain in 1996, Bruzzone and Serpico in 1997 and then in 1999. And what they say, fundamentally, is that classification stops being a series of independent decisions: labels must be estimated jointly.
**Transition.** What remains is to give this intuition a rigorous theoretical framework, and that framework is Markov random fields.
**In reserve.** If I am asked why the same image comes back: it is deliberate, it is the only way to make the comparison honest.

### Slide 20 — Markov and Bayesian models · 10 s · 18 min 40
**Say.** Sixth section: Markov and Bayesian models. We are entering the theoretical core of the talk.
**Transition.** This is where the intuition of context becomes a general probabilistic formulation.

### Slide 21 — Markov random fields: the first formalization · 1 min 30 · 20 min 10
**Say.** Markov random fields are the first general probabilistic formalization of this idea, and they very quickly become one of the most influential theoretical frameworks for image segmentation and classification. The principle fits in one sentence: labels are no longer independent variables, they are random variables defined on a neighborhood graph. Under the Markov assumptions, and thanks to the equivalence between Markov random fields and Gibbs distributions — this is the machinery set up by Stuart and Donald Geman in 1984, and taken up by Julian Besag in 1986 on the statistical analysis side — the search for the optimal class map is written as a maximum a posteriori estimation. And this is where Bayes' theorem does all the work: maximizing the posterior probability of the labels is exactly equivalent to minimizing an energy function, with X the observations and Y the labels to be estimated.
**Transition.** Let us now see what is inside this energy. To my mind, it is the most important equation of the talk.
**In reserve.** For anyone who wants the full detail of the framework, Zoltan Kato and I published a survey in 2012 in Foundations and Trends in Signal Processing.

### Slide 22 — Data term + regularization · 1 min 50 · 22 min
**Say.** Here is the equation I would really like you to take away with you: the energy splits into two terms only. The first, U subscript d, is the data term, generally derived from the likelihood of the observations, and it carries everything the radiometry tells us about the pixel. The second, U subscript r, is the spatial regularization, which promotes consistency between neighboring pixels, and between the two sits the parameter beta, the trade-off between fidelity to the observations and regularity of the solution. On the right, you see the neighborhood systems, defined at first or second order, and the associated cliques: clique potentials penalize certain label configurations, typically class changes between adjacent pixels. The major interest of this formulation is that it brings radiometric observations and spatial interactions together in a single framework.
**Transition.** Writing the energy is one thing. Minimizing it is another, and much less comfortable.
**In reserve.** Remember the form of this equation. We are going to find it again, almost identical, in the Mumford–Shah functional, then in graph-based formulations, and finally in the loss functions of deep networks.

### Slide 23 — Optimizing: a hard problem · 1 min 20 · 23 min 20
**Say.** Finding the label configuration that minimizes this energy is a hard combinatorial optimization problem, so in practice we do not reach it exactly and we work with suboptimal strategies. The first ones are iterated conditional modes, ICM, simulated annealing, in Kirkpatrick in 1984, and the Gibbs sampler of Geman and Geman. Then come methods based on graph cuts, with Boykov, Veksler and Zabih in 2001, and loopy belief propagation, in Tanaka and colleagues in 2003. The applications cover the whole field: spatial consistency of classifications, multisource segmentation, restoration, change detection, optical, radar and LiDAR fusion. But the contribution of Markov random fields goes far beyond these particular applications: they give the field a general probabilistic formulation of spatial regularization, and that is what will last.
**Transition.** This family also has a direct extension, which brings it closer to supervised learning.
**In reserve.** There are very nice examples where the two directions of the first third meet. Gabriele Moser and Sebastiano Serpico proposed in 2013 an integrated framework combining support vector machines and Markov random fields for contextual classification.

### Slide 24 — From MRFs to CRFs · 1 min 10 · 24 min 30
**Say.** Conditional random fields extend this family naturally: rather than modeling the joint distribution of the observations and the labels, they represent the conditional distribution of Y given X directly — Lafferty, McCallum and Pereira, in 2001. The advantage is immediate: complex discriminative features can be brought in, and the fully connected models of Krähenbühl and Koltun, in 2011, preserve object boundaries much better. Then CRFs enter deep networks, first as refinement modules, then as differentiable layers, and this is exactly the ground of our work with Martina Pastorino and Gabriele Moser, up to CRFNet, in 2024. Beyond these models, remember the idea that runs through the whole field: a land-cover map must not only be consistent with the local observations, it must also be consistent with the spatial organization of the scene.
**Transition.** We have regularized the labels. Let us come back to the other branch of the alternative, and this time enrich the representation.
**In reserve.** Zheng and colleagues show as early as 2015 that a CRF can be read as a recurrent network. In CRFNet, it is a deep convolutional network that learns its potentials. And in the same vein, with Aurélie Voisin, Vladimir Krylov, Gabriele Moser and Sebastiano Serpico, we classified very high resolution SAR images over urban areas using copulas and texture in a hierarchical Markov random field, in 2013.

### Slide 25 — Spectral-spatial methods · 10 s · 24 min 40
**Say.** Seventh section, and a change of lever: so far we have regularized the labels; we are now going to enrich the representation itself.
**Transition.** What made this turn necessary is the increasing resolution of sensors.

### Slide 26 — Enriching the representation, not the labels · 1 min 10 · 25 min 50
**Say.** Contextual models improve the consistency of the maps, but they change nothing in the representation of the observations, so a complementary approach is to enrich directly the features used by the classifier, by combining spectral information with spatial descriptors. This is the spectral-spatial paradigm, which takes hold during the 2000s and which will play a major role in the evolution of the field. What makes it necessary is the increasing resolution of sensors, both spatial and spectral. The first generations of images were characterized essentially by their radiometric signatures, whereas higher resolution images reveal the internal structure of geographical objects: a single class can exhibit strong spectral variability, and different objects can have very similar signatures. This is why texture, shape, size, spatial organization and neighborhood relations become as discriminative as the spectral values themselves.
**Transition.** The first tools of this enrichment come from texture analysis and mathematical morphology.
**In reserve.** The idea of combining intensity and textural information is already at work in radar in Dellepiane, Giusto, Serpico and Vernazza, in 1991. The background reference on the complete multispectral chain remains the book by Landgrebe, in 2003.

### Slide 27 — Mathematical morphology · 1 min 10 · 27 min
**Say.** The first spectral-spatial approaches use local statistics and textural features — the features of Haralick, Shanmugam and Dinstein date from 1973 — then the operators of mathematical morphology: erosion, dilation and their compositions, following Serra in 1982 and Soille in 2003. You have a direct illustration here: in the center the original RGB satellite image, on the left its erosion, on the right its dilation. Note the difference in nature with what we have just seen. Markov models introduce a spatial regularization at the level of the labels, whereas these operators enrich the feature vectors, upstream, before the classification stage.
**Transition.** These operators then had to be organized to describe a scene at all its scales at once.

### Slide 28 — Morphological profiles and attribute profiles · 1 min 30 · 28 min 30
**Say.** The important step is taken with extended morphological profiles, EMPs, introduced by Benediktsson, Palmason and Sveinsson in 2005, then with the attribute profiles of Dalla Mura and colleagues in 2010, which describe spectral properties and the spatial structure of scenes simultaneously, at several scales of observation. These representations very quickly become reference methods for hyperspectral data and for very high spatial resolution. Combined with support vector machines they obtain remarkable performance, and that is largely what spread the spectral-spatial approaches, but the principle is general: random forests, neural networks and other discriminative methods can use the same features. The same years bring dimensionality reduction, subspace-based methods and multisource data fusion, and several works propose to take the segmented regions, rather than individual pixels, as analysis units, which increases the spatial consistency of the maps while reducing noise. What should be remembered is that the gains observed then come as much from the quality of the representation as from the performance of the classifier.
**Transition.** After regularizing the labels and enriching the features, here is a third path: addressing the geometry of the boundaries directly.
**In reserve.** The aim was never to use a larger number of spectral bands, but to build a representation integrating all the relevant information that describes the scene. On the overviews: Plaza and colleagues in 2009, Camps-Valls, Tuia, Bruzzone and Benediktsson in 2014. On region units, Tarabalka, Benediktsson and Chanussot in 2009.

### Slide 29 — Variational methods · 10 s · 28 min 40
**Say.** Eighth section: segmentation formulated as an energy minimization problem, with no explicit probability distribution on the labels.
**Transition.** It all starts with active contours, at the end of the 1980s.

### Slide 30 — Segmenting by minimizing an energy · 1 min 20 · 30 min
**Say.** From the late 1980s, in parallel with Markov random fields, another family of methods develops a very close idea, but in a different language. Variational methods no longer seek to model an explicit probability distribution on the labels; they search for the partition of the image that achieves the best trade-off between fidelity to the observations and regularity, spatial or geometric. The first developments concern active contours — the snakes of Kass, Witkin and Terzopoulos, in 1988. There, object boundaries are deformable curves, which evolve under the action of internal forces ensuring contour regularity and of external forces derived from the information contained in the image. This is the first time the boundary is represented explicitly, and it is the starting point of a whole family of energy-minimization methods.
**Transition.** The model that marked this family the most holds in three terms. Here it is.

### Slide 31 — The Mumford–Shah functional · 1 min 30 · 31 min 30
**Say.** Here is the functional proposed by Mumford and Shah in 1989, which is still today one of the most influential variational models in image processing. Two things are sought simultaneously: a smooth approximation u of the observed image I, and a set K of discontinuities, which are the boundaries of the objects. The first term measures the fidelity of the solution to the observations, and the second, weighted by the parameter mu, promotes a smooth representation inside the regions. The third, weighted by nu, penalizes the measure of the boundaries, that is, their geometric complexity. Look carefully at the structure of this energy: it is exactly, in a different language, what we wrote a few slides ago for Markov random fields — a data term, and a regularization.
**Transition.** What remained was to make all this numerically robust, and to bring it to satellite images.

### Slide 32 — Numerical robustness and applications · 1 min 30 · 33 min
**Say.** Two advances made these models really usable. First, level sets, from Osher and Sethian in 1988: the contour is no longer described explicitly but by means of a level set function, which makes it possible to handle topology changes automatically during the evolution of the segmentation. Then, a few years later, region-based models — the active contours without edges of Chan and Vese, in 2001 — which rely on region statistics rather than on image gradients alone, and which are therefore far more robust on noisy or low-contrast images. On the right, a SPOT image from CNES and the segmentation obtained with the variational method we proposed with Christophe Samson, Laure Blanc-Féraud and Gilles Aubert in 2000, which unifies classification and restoration in a single functional. And this is the high point of this first half of the talk: Bayesian models, Markov random fields, variational methods and graph-based formulations are different expressions of the same principle — a data term, combined with a spatial or geometric regularization.
**Transition.** Remember this sentence, because deep learning, which we come to now, does not abolish it. It displaces it.
**In reserve.** These methods are also a bridge to modern approaches: energy formulations, regularity constraints and the trade-off between data fidelity and spatial consistency reappear today in loss functions, in optimization procedures and in hybrid architectures.

### Slide 33 — Deep learning · 10 s · 33 min 10
**Say.** Ninth section: the moment when features stop being designed and representations start being learned.
**Transition.** This shift has a precise date.

### Slide 34 — 2012, the turning point · 1 min 20 · 34 min 30
**Say.** 2012, the ImageNet challenge: the AlexNet network, from Krizhevsky, Sutskever and Hinton, demonstrates a dramatic improvement in natural-image classification. What this result establishes is that hierarchical representations can be learned automatically, directly from the data, without hand-crafted design of spectral, textural or geometric features. Performance therefore no longer depends on the classifier alone, but on the ability of the network to learn jointly a relevant representation and the decision function. The transfer to remote sensing is rapid — Chen and colleagues in 2014 on hyperspectral data, Castelluccio and colleagues in 2015 on land use — with two converging observations: convolutional networks learn more discriminative representations than hand-crafted features, and the transfer of models pretrained on large datasets of natural images works on aerial and satellite images. In other words, the spectral-spatial approaches we have just seen shift from hand-crafted to learned representations.
**Transition.** Classifying a whole image, however, is not segmenting it. A dense, pixel-level prediction still had to be produced.

### Slide 35 — Dense prediction: FCNs and encoder–decoder · 1 min 30 · 36 min
**Say.** The decisive step is fully convolutional networks, the FCNs of Long, Shelhamer and Darrell in 2015, whose architecture you see on the right. By removing the fully connected layers in favor of purely convolutional operations, a dense, pixel-level prediction is produced directly, and a segmentation function is learned end-to-end, with no explicit feature extraction stage and no mandatory post-processing. Encoder–decoder architectures very quickly complete this formulation, U-Net, from Ronneberger, Fischer and Brox, the same year, being the most representative example: its skip connections restore in the decoder the localization information lost in downsampling, which improves the delineation of boundaries and the segmentation of small objects. Through their simplicity and their efficiency, these architectures become reference methods for many applications in remote sensing: land-cover mapping, extraction of buildings, roads and hydrographic networks.
**Transition.** Three questions, however, that dense prediction does not settle: context, scales and the diversity of sensors.
**In reserve.** The figure is taken from our review paper with Martina Pastorino, Gabriele Moser and Sebastiano Serpico, published in IEEE Signal Processing Magazine in 2026. The example uses the aerial images of the ISPRS 2D Semantic Labeling Challenge dataset, in Potsdam. On the applications, see Audebert, Le Saux and Lefèvre in 2018, Zhang and colleagues in 2018 for roads, Isikdogan and colleagues in 2017 for water surfaces.

### Slide 36 — Context, scales, modalities · 1 min 20 · 37 min 20
**Say.** The evolution of deep networks then comes with a major effort to better represent spatial context and objects observed at different scales. Residual networks, from He and colleagues in 2016, make it easier to learn deeper models by limiting vanishing gradient problems. The DeepLab architectures introduce dilated convolutions and multiscale aggregation modules, ASPP, which enlarge the receptive field without degrading the spatial resolution of the predictions. And in the same spirit, feature pyramids improve the representation of objects of widely varying sizes — a property that is particularly important for us, since a single scene can contain vehicles, buildings, agricultural fields and forest stands at the same time. Finally, the integration of multimodal data becomes a major direction: deep networks now learn shared representations from optical data, synthetic aperture radar, LiDAR, digital terrain models or ancillary geospatial data.
**Transition.** Under these architecture names, you will have recognized questions we have already met. That is precisely what I would like to make explicit.

### Slide 37 — What deep learning does not eliminate · 1 min 10 · 38 min 30
**Say.** Here is what should be remembered from this section: deep learning does not make the concepts developed over the previous decades disappear, it reformulates them within an end-to-end learning framework. Spatial context, multiscale representation, data fusion, object hierarchy — which used to be described by means of probabilistic, variational or geometric models — are now learned directly by deep architectures. That said, and despite remarkable performance, convolutional networks keep three limitations: their training relies on large amounts of pixel-level annotations, which are particularly costly to produce in remote sensing. Their generalization across sensors, across geographical regions and across acquisition modalities remains limited, and they model very long-range spatial dependencies poorly. It is exactly these three limitations that pave the way for what follows.
**Transition.** What follows is attention mechanisms, and then geospatial foundation models.

### Slide 38 — Transformers and foundation models · 10 s · 38 min 40
**Say.** Tenth section: transformers and foundation models. It is the limitations I have just stated that lead us there, and not a fashion.
**Transition.** Let us start with the mechanism itself: attention.

### Slide 39 — Attention in segmentation · 1 min 30 · 40 min 10
**Say.** The limitations of convolutional architectures, and most of all their difficulty in modeling long-range spatial dependencies, gradually lead to introducing attention mechanisms in semantic segmentation. Transformers were developed for natural language processing — this is the paper by Vaswani and colleagues, in 2017 — and their essential property is to model the relations between distant elements of a sequence directly, without passing through a local neighborhood. Their adaptation to vision, by Dosovitskiy and colleagues in 2021, opens a new phase. Two architectures are particularly representative: Swin Transformer, from Liu and colleagues, and SegFormer, from Xie and colleagues, both in 2021, which combine a hierarchical representation of the image with a more global modeling of the context. This property is of first importance to us, because in remote sensing, identifying a building, a road or an agricultural field does not rely on its local appearance alone, but on its organization within the scene.
**Transition.** A second movement develops in parallel, and it answers a problem that is even more concrete for us: annotations.
**In reserve.** Remember the three levels of context from the contextual section: local, regional, global. It is the third one, the hardest to formalize explicitly, that attention finally makes it possible to address head-on.

### Slide 40 — Learning without annotations · 1 min 10 · 41 min 20
**Say.** In parallel, self-supervised learning becomes a major research direction. Masked autoencoders — I am thinking of the work of He and colleagues, in 2022 — show that rich visual representations can be learned from very large amounts of unlabeled data. This development is a direct response to an imbalance specific to our field: satellite archives are abundant and have been accumulating for decades, whereas pixel-level annotations remain scarce and costly to produce. In other words, this is not only an advance imported from computer vision. It is a response to a constraint we know well.
**Transition.** From these two movements combined, attention and self-supervision, geospatial foundation models are born.
**In reserve.** The cost of annotations already appeared, two slides earlier, among the persistent limitations of convolutional networks. It will come back in the outlook. It is probably the most stubborn problem of the whole talk.

### Slide 41 — Geospatial foundation models · 1 min 10 · 42 min 30
**Say.** This work leads to the emergence of geospatial foundation models, whose general principle you see on the right: pretrained on very large volumes of data, then adapted to very different tasks — classification, segmentation, object detection, change detection. The goal is no longer to optimize an architecture for one particular dataset, but to learn generic representations, transferable across sensors, across geographical regions and across applications. The downside, and I insist on this, is a very high pretraining cost, in compute as well as in hardware and energy resources, which raises real questions of environmental footprint and of accessibility for the community. And above all, this is not a break: the same questions run through the whole history I have just told, except that they are now learned from very large volumes of data rather than built explicitly.
**Transition.** Here we are at the end of the journey. It is time to step back.
**In reserve.** The milestones to cite if I am asked: SatMAE, from Cong and colleagues in 2022; the work of Jakubik and colleagues and of Wang and colleagues in 2023; Segment Anything, from Kirillov and colleagues the same year; and very recently AlphaEarth Foundations, from Brown and colleagues in 2025. In the figure, the principle is always the same: a single pretraining, then light adaptations.

### Slide 42 — Conclusion · 10 s · 42 min 40
**Say.** Eleventh and last section: I would like to end by coming back to the storyline I announced at the beginning.
**Transition.** And the first thing to say is that this history is not linear.

### Slide 43 — A nonlinear history · 1 min 20 · 44 min
**Say.** The history of semantic segmentation in remote sensing does not follow a linear trajectory that would simply go from statistical classifiers to deep networks. It is rather the result of several scientific traditions that gradually came together — statistical classification, kernel methods, ensemble methods, contextual models, Markov random fields, variational methods, stochastic geometry, deep learning and foundation models. Here is the timeline from the beginning again, and you can now read it as a story. The first approaches use local spectral information; contextual and Markov models introduce spatial coherence; variational methods and marked point processes model boundaries, regions and objects; deep networks learn these representations automatically; and transformers and foundation models seek today to build general geospatial representations, multimodal and transferable. And beneath this progression, one recurring principle that you have seen come back slide after slide: a data term plus a regularization, from Markov random fields to the loss functions of deep networks.
**Transition.** Let us end with what is not solved, and there is plenty.
**In reserve.** The mathematical connections between probabilistic graphical models and deep learning are precisely the subject of the survey published with Martina Pastorino, Gabriele Moser and Sebastiano Serpico in IEEE Signal Processing Magazine in 2026.

### Slide 44 — Outlook · 1 min · 45 min
**Say.** The current challenges are still many, and I list them without ranking them: geographic generalization, that is, the ability of a model learned here to work elsewhere; the lack of annotations, which we have just discussed; the fusion of optical, radar and LiDAR data; accounting for the temporal dimension, when our archives are series by nature; model interpretability; and operational robustness, which is the condition for all of this to be really useful. These questions show that semantic segmentation in remote sensing remains an open field, at the intersection of signal and image processing, probabilistic modeling, geometry, computer vision and artificial intelligence, in a geospatial setting. That, I believe, is what still makes it a very fine research topic today.
**Transition.** Thank you for your attention.
**In reserve.** This intersection of disciplines is not a closing formula. It is what explains why the field never moved forward by simply importing computer vision, as I said at the very beginning.

### Slide 45 — Thank you for your attention. · off the clock · 45 min
**Say.** Thank you for your attention — and thank you to Martina Pastorino and Gabriele Moser, from Università di Genova, with whom this work was carried out. I am happy to take your questions.
**In reserve.** The following slides are appendices: the full bibliography and the figure credits. I can come back to them if a particular reference is of interest.

### Slide 46 — References I · appendix · —
**Say.** Here is the full bibliography of the talk: seventy-nine entries, in order of appearance, starting with the source paper itself and the founding books of the 1970s and 1980s.
**In reserve.** This first slide covers references 1 to 21, from the source paper and Duda and Hart to Belgiu and Drăguț.

### Slide 47 — References II · appendix · —
**Say.** Bibliography continued: texture and context, then Markov random fields, their optimization and the first conditional random fields.
**In reserve.** References 22 to 37, from Haralick, Shanmugam and Dinstein to Zheng and colleagues.

### Slide 48 — References III · appendix · —
**Say.** Continued: our own work with Martina Pastorino and Gabriele Moser, then mathematical morphology, the spectral-spatial methods and the first variational models.
**In reserve.** References 38 to 53, from Pastorino and colleagues in 2021 to Kass, Witkin and Terzopoulos.

### Slide 49 — References IV · appendix · —
**Say.** Continued: level sets and region-based models, then the 2012 turning point, dense prediction and the multiscale architectures.
**In reserve.** References 54 to 68, from Osher and Sethian to Lin and colleagues.

### Slide 50 — References V · appendix · —
**Say.** End of the bibliography: multimodal deep learning, transformers, self-supervised learning and geospatial foundation models.
**In reserve.** References 69 to 79, from Ma and colleagues to Kirillov and colleagues.

### Slide 51 — Figure credits · appendix · —
**Say.** Last back-up slide: the credits of the seven figures of the talk, which are all the figures of the paper — in particular the Zeebruges dataset of the IEEE GRSS IADF Technical Committee, with imagery and ground truth provided by the Belgian Royal Military Academy and ONERA, and the SPOT image, copyright CNES.
**In reserve.** The credits already appear under each figure through the talk. This slide only recapitulates them, in case the question comes up.

## Likely questions

**Do foundation models make everything else obsolete?**
No, and that is in fact the heart of my conclusion. They extend questions that run through the whole history of the field — integrating heterogeneous data, representing spatial context, generalizing to new regions, taking advantage of complementary modalities — except that they are learned rather than hand-crafted. And their pretraining cost, in compute as well as in energy, raises real questions of environmental footprint and of accessibility.

**Are Markov random fields still useful for anything?**
Yes, in two ways. CRFs have entered deep networks, first as refinement modules, then as differentiable layers — Zheng and colleagues show in 2015 that a CRF can be read as a recurrent network. And our work with Martina Pastorino and Gabriele Moser goes all the way to CRFNet, in 2024, where a deep convolutional network learns the potentials of the CRF.

**How do you set the parameter beta, or mu and nu in Mumford–Shah?**
They are the trade-off between fidelity to the observations and regularity of the solution: the more you increase them, the smoother the map, and the less it follows the detail of the data. The trade-off depends on the resolution of the image and on the size of the objects you want to keep. For the detail of the Markov framework, I refer you to the survey by Zoltan Kato and myself, in 2012.

**SVMs or random forests?**
The comparison is not really the point, because both improve the decision function and both remain independent of the representation they are given. SVMs generalize remarkably well when training samples are scarce compared with the dimension of the data. Random forests need very little tuning, tolerate noise and provide variable importance measures that are useful for interpretation.

**Why does a model learned on one region not work elsewhere?**
That is geographic generalization, and it is one of the challenges I list in the outlook. Remote sensing scenes have properties that vary with region, season and acquisition conditions, and convolutional networks generalize poorly across sensors, across regions and across modalities. That is precisely one of the motivations for transferable representations.

**Why are annotations such a bottleneck?**
Because supervised learning for segmentation requires pixel-level annotations, which are particularly costly to produce in remote sensing. The imbalance is striking: satellite archives are abundant and have been accumulating for decades, while annotations remain scarce. That is exactly what self-supervision targets, with the masked autoencoders of He and colleagues in 2022.

**What happened to marked point processes and stochastic geometry?**
They are in the unified reading of the conclusion, in the family that models boundaries, regions and objects explicitly, alongside variational methods. For lack of time I do not develop them here, but they are part of the traditions that converged.

**What is left of object-based image analysis?**
A lot, in fact. The regional context identified as early as the 1980s points directly to it, and Thomas Blaschke gives the synthesis in 2010. And the idea of taking segmented regions rather than pixels as analysis units — Tarabalka, Benediktsson and Chanussot, in 2009 — improves the spatial consistency of the maps while reducing noise.

## Facts to get right

**The talk and its authors**
- Source paper: Martina Pastorino, Gabriele Moser, Josiane Zerubia, "Segmentation sémantique en télédétection", Traitement du Signal et des Images (TSI), GRETSI. Also Inria research report RR-9631, HAL hal-05742224, September 2026.
- Josiane Zerubia, Inria Centre at Université Côte d'Azur, Ayana project-team; Martina Pastorino and Gabriele Moser, Università di Genova, DITEN.
- 51 slides, 11 sections, 79 references, 7 figures.

**Sensors, data and figures**
- Landsat, optical, early 1970s; SeaSat, radar, late 1970s.
- Zeebruges dataset: IEEE GRSS IADF Technical Committee; imagery and ground truth from the Belgian Royal Military Academy and ONERA.
- IKONOS image, 4 m, 3 bands, false color (near infrared, red, blue).
- SPOT satellite image, © CNES.
- ISPRS 2D Semantic Labeling Challenge dataset, Potsdam.

**Acronyms**
- MAP: maximum a posteriori; MLC: maximum likelihood classifier. SVM: support vector machines. RF: random forests.
- MRF: Markov random fields; CRF: conditional random fields; ICM: iterated conditional modes.
- EMP: extended morphological profiles. FCN: fully convolutional networks. ASPP: Atrous Spatial Pyramid Pooling, the multiscale aggregation of the DeepLab architectures.
- SAR: synthetic aperture radar. LiDAR. IADF: the Image Analysis and Data Fusion Technical Committee of the IEEE GRSS.

**Dates and names, in the order of the talk**
- Duda and Hart, 1973 · Swain and Davis, 1978 · Richards, 1986 · Hughes, 1968.
- Cortes and Vapnik, 1995 · Vapnik, 1998 · Schölkopf and Smola, 2002 · Camps-Valls and Bruzzone, 2009 · Mountrakis, Im and Ogole, 2011.
- Breiman, 2001 · Gislason, Benediktsson and Sveinsson, 2006 · Belgiu and Drăguț, 2016.
- Haralick and Shapiro, 1985 · Azencott and Graffigne, 1992 · Blaschke, 2010 · Csurka and colleagues, 2023.
- Geman and Geman, 1984 · Besag, 1986 · Solberg, Taxt and Jain, 1996 · Bruzzone and Serpico, 1997 and 1999 · Moser, Serpico and Benediktsson, Proceedings of the IEEE, 2013 · Kato and Zerubia, 2012.
- Kirkpatrick, 1984 · Boykov, Veksler and Zabih, 2001 · Tanaka and colleagues, 2003.
- Lafferty, McCallum and Pereira, 2001 · Krähenbühl and Koltun, 2011 · Zheng and colleagues, 2015 · Pastorino and colleagues, 2021, then CRFNet, 2024 · Voisin, Krylov, Moser, Serpico and Zerubia, 2013.
- Haralick, Shanmugam and Dinstein, 1973 · Dellepiane, Giusto, Serpico and Vernazza, 1991 · Serra, 1982 · Soille, 2003 · Landgrebe, 2003 · Benediktsson, Palmason and Sveinsson, 2005 · Dalla Mura and colleagues, 2010 · Tarabalka, Benediktsson and Chanussot, 2009.
- Kass, Witkin and Terzopoulos, 1988 · Mumford and Shah, 1989 · Osher and Sethian, 1988 · Chan and Vese, 2001 · Samson, Blanc-Féraud, Aubert and Zerubia, 2000.
- Krizhevsky, Sutskever and Hinton, 2012 · Chen and colleagues, 2014 · Castelluccio and colleagues, 2015 · Long, Shelhamer and Darrell, 2015 · Ronneberger, Fischer and Brox, 2015 · He and colleagues, 2016.
- Vaswani and colleagues, 2017 · Dosovitskiy and colleagues, 2021 · Liu and colleagues (Swin), 2021 · Xie and colleagues (SegFormer), 2021 · He and colleagues (masked autoencoders), 2022.
- Cong and colleagues (SatMAE), 2022 · Jakubik and colleagues, 2023 · Wang and colleagues, 2023 · Kirillov and colleagues (Segment Anything), 2023 · Brown and colleagues (AlphaEarth Foundations), 2025.
- Pastorino, Moser, Serpico and Zerubia, IEEE Signal Processing Magazine, 2026.
