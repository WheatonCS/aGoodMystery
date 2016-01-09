# aGoodMystery
This repo is a collection of computational methods to explore whether an 1831 story
published under the attribution of only 'P' might have been written by Edgar Allan Poe.
If so, it would Poe's first published work.


## Brief Background
I was intrigued when publisher and editor Shirrel Rhoades, formerly at the *Saturday Evening Post*, 
approached me an 1831 story entitled “A Dream” that he thought was written by Edgar Allan Poe.
The story was published under only the letter "P".
Poe's first published work was in 1832. The Edgar Allan Poe Society of Baltimore says 
"This short item has been attributed to Poe as a possible item, but the arguement is largely a 
subjective one based on a sense of tone and style, with no external evidence at all"
(http://eapoe.org/works/info/st001.htm), while 
some scholars consider that Poe’s “first published tale may have been ‘A Dream’ ” (Silverman, 1991, p87). 

So, based on the frequencies of some of the most common function words used, 
we seek to gather new evidence in a series of computational probes of "A Dream", a collection
of other Poe stories, and X other texts written by Y authors.
These probes provide objective views of the material from a new angle and as you will see, often generate more 
questions than when we started. 

## Our Goals
Rather than to attempt to make sweeping claims of authorship, our goal here is two-fold: 
(i) to facilitate the replication of our results
and 
(ii) to share our methods so that you can apply your own like-questions to your texts of interest.

## Workflow of Steps
We present a workflow of steps that were taken to probe the question, including:
unsupervised (cluster analyses) and supervised (classification) methods. The steps available here
in this repo are as follows:

###step_0_CollectTexts
We share our corpus and a Python script to snag the Nth segment of M-words from each text.

###step_1_Scrubbing
We point you to Lexos to first "scrub" the texts so that all subsequent texts are tokenized in a consistent fashion.

###step_2_Clustering
K-means, Hierarchical-agglomerative, and Bootstrap Consensus Trees.

###step_3_Classification
Use of Stylo in R (Eder et al., 2016) for Delta, Support-Vector Machine (SVM), and Nearest Shrunken Centroid (NSC) models.

## Notes:
1. To facilitate replication of individual analyses **for each step**, we have included .zip versions of
the texts used in that analysis along with the source code. Cloning this repo will thus result
in duplicate copies of text files.

2. We have tried to document our scripts; however, we recognize that more efficient
methods exist. This is especially true in our R scripts. 

3. The tools, languages, and packages used (but not included here):
- Lexos (https://github.com/WheatonCS/Lexos) or available online at http://lexos.wheatoncollege.edu
- Stylo in R (https://github.com/computationalstylistics/stylo)
- Python (with Anaconda) and R scripts

mdl (January, 2016)
