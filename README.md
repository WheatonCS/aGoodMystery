# aGoodMystery
This repository (repo) is a collection of computational methods to explore whether an 1831 story
published under the attribution of only 'P' might have been written by Edgar Allan Poe.
If so, it would Poe's first published work (LeBlanc, 2017).

Unlike a published paper that includes but a brief summary of the methods applied and typically no access to the texts used, this repo endorses the call for a more systematic documentation and sharing of computational stylistic methods (*c.f.* Rudman, 2012, *et al.*). Because scholars who are new to computational stylometry are often discouraged too early in the game, we offer what we hope is 
a straightforward series of annotated steps (and mis-steps) for conducting a series of computational probes on a set of digitized texts.

*Note: Based on external reviewer critiques and comments (received December 2016), we have sprinkled new comments throughout the steps to highlight some of our mistakes made and areas where alternate or stronger methods might be employed. As shared here, a tension exists between designing an experiment like an expert and a desire to "just get started". Here we have erred on the side of the latter.*

*Building this repo to facilitate reproducibility involved a significant effort beyond submitting a typical paper, yet this effort, in conjunction with the peer review process, provided the unexpected benefits of (i) a repo in a better state for sharing the work so that others may use it in their early entry to and/or teaching of introductory computational methods, and (ii) an example that serves as a comparison with other models of sharing code such as Jupyter notebooks.*

*Above all, we hope this level of transparency will lead to effective practices and encourage your own play and exploration.*

## Brief Background
![alt text](Poe.jpg "Artist: Scott Cranmer; fabric on canvas with acrylic")
*(Artist: Scott Cranmer; fabric on canvas with acrylic; used with permission)*

I was intrigued when publisher and editor Shirrel Rhoades, formerly at the *Saturday Evening Post*, 
approached me with an 1831 story entitled “A Dream” that he thought was written by Edgar Allan Poe. 
The story was published under only the letter "P".
Poe's first published work was in 1832. The Edgar Allan Poe Society of Baltimore says 
*"This short item has been attributed to Poe as a possible item, but the argument is largely a subjective one based on a sense of tone and style, with no external evidence at all"*
(http://eapoe.org/works/info/st001.htm). Some scholars consider that Poe’s *“first published tale may have been ‘A Dream’ ”* (e.g., Silverman, 1991, p87). Schöberlein's extensive tests on disputed Poe
texts (2016), attribute Poe to "A Dream" on only one of three authorship attribution methods (Delta near 100% as Poe, but not with SVM and NSC methods). 

So, based on the frequencies of some of the most common function words used by Poe and other 
(approximate) contemporaries, 
we seek to gather new evidence in a series of computational probes 
to be performed on "A Dream", a collection
of other known Poe stories, and other texts written by a number of authors, many contemporaries of Poe and/or those who published in similar places (e.g., *The Souther Literary Messenger*).
These probes provide objective views of the material from a new angle and as you will see, often generate more 
questions than when we started. 

## Our Goals
Rather than to attempt to make sweeping claims of authorship, our goals here are three-fold: 
1. To show by example one process of designing and implementing an experiment
2. To facilitate the replication of our results, and 
3. To encourage you to apply your own like-questions to your texts of interest.

## Workflow of Steps
We present a workflow of steps that were taken to probe the question, including the critical early steps of corpus construction and token preparation, as well as unsupervised (cluster analyses) and supervised (classification) methods. The steps available here
in this repo are as follows:

#### step_0_CollectTexts
We share our process for establishing our group of files to use, 
as well as our resulting corpus of "scrubbed" texts used 
in these inquiries. (Note that we comment more fully
on scrubbing in Step 1, although we only cache the scrubbed texts here in this repo).

We include directions for *how* we scrubbed (a non-trivial step in the design of an experiment and a critical one for reproducibility), 
as well as a miscellaneous Python script (not specifically used here in these analyses) to snag the Nth segment of 
M-words from each text as an example of the type of script often needed when preparing your corpus.

*Note: We provide one reviewer's critique of our choice of texts and suggestions for alternatives.*

*Since initial submission, Schöberlein (2016) graciously shared his corpus of 53 prose authors (note: these files have not been scrubbed by Lexos). Hmmm ... repeat workflow with new texts? (I'll show some of these results when using Schöberlein's corpus at DH 2017 in Montreal on August 9, 2017).*

#### step_1_Scrubbing_Tokenization_Culling
A brief description of how we "scrubbed" our text files, counted "words", and which words we chose to discard (cull) during each test.  In particular, we point you to 
[Lexos](http://lexos.wheatoncollege.edu) to first "scrub" the texts so that all subsequent 
texts are tokenized and culled in a consistent fashion no matter what tool or package is used.

*Note: We provide one reviewer's critique of how the Lexos tool handles initial and final apostrophes. While this may seem like a minor issue, it is not, as recently highlighted by Hoover (2015) and others.* 

#### step_2_Clustering
K-means and Hierarchical-agglomerative with [Lexos](http://lexos.wheatoncollege.edu), and Bootstrap Consensus Trees (Eder *et al.*, 2016) were applied.

#### step_3_Classification
We describe our use of Stylo in R (Eder *et al.*, 2016) for Delta, Support-Vector Machine (SVM), and Nearest Shrunken Centroid (NSC) models.

### References [here](References.md)

### Notes:
1. To facilitate replication of individual analyses *for each step*, we have included .zip versions of
the scrubbed texts used in that analysis along with the source code. Cloning this entire repo will thus result
in duplicate copies of text files. We only include copies of the scrubbed texts here, not their original versions.

2. Although we did not include in most of our analyses the stories purportedly written by Edgar's brother Henry (*c.f.*, Collins, 2013), we include a separate directory of these four stories for your other, related, queries.

3. We have tried to document our scripts (really!).  We recognize that more efficient
methods exist. This is especially true in our R script in step_3b that automates a number
of trial runs. 

4. The tools, languages, and packages used (but not included here):
  - Lexos, local version (https://github.com/WheatonCS/Lexos) or available online at http://lexos.wheatoncollege.edu
  - Stylo in R (https://github.com/computationalstylistics/stylo)
  - Python v2.7.x (with Anaconda) and R scripts

Date Last Modified:
  - mdl (July, 2017):    review prior to DH 2017 (Montreal, Canada)
  - mdl (January, 2017): initial responses to DH 2017 reviewer comments
  - mdl (August,  2016): toward an example to encourage others
  - mdl (January, 2016): early play

