# aGoodMystery
This repo is a collection of computational methods to explore whether an 1831 story
published under the attribution of only 'P' might have been written by Edgar Allan Poe.
If so, it would Poe's first published work.


## Brief Background
I was intrigued when publisher and editor Shirrel Rhoades, formerly at the *Saturday Evening Post*, 
approached me with an 1831 story entitled “A Dream” that he thought was written by Edgar Allan Poe.
The story was published under only the letter "P".
Poe's first published work was in 1832. The Edgar Allan Poe Society of Baltimore says 
*"This short item has been attributed to Poe as a possible item, but the arguement is largely a 
subjective one based on a sense of tone and style, with no external evidence at all"*
(http://eapoe.org/works/info/st001.htm), while 
some scholars consider that Poe’s *“first published tale may have been ‘A Dream’ ”* (Silverman, 1991, p87). 

So, based on the frequencies of some of the most common function words used by Poe and other 
(approximate) contemporaries, 
we seek to gather new evidence in a series of computational probes 
to be performed on "A Dream", a collection
of other known Poe stories, and X other texts written by Y authors.
These probes provide objective views of the material from a new angle and as you will see, often generate more 
questions than when we started. 

## Our Goals
Rather than to attempt to make sweeping claims of authorship, our goal here is two-fold: 
1. To facilitate the replication of our results and 
2. To share our methods so that you can apply your own like-questions to your texts of interest.

## Workflow of Steps
We present a workflow of steps that were taken to probe the question, including:
unsupervised (cluster analyses) and supervised (classification) methods. The steps available here
in this repo are as follows:

####step_0_CollectTexts
We share our process for establishing our group of files to use, 
as well as our resulting corpus of "scrubbed" texts used 
in these inquiries. (Note that we comment more fully
on scrubbing in Step 1, although we only cache the scrubbed texts here in this repo).

directions for how we scrubbed, 
and a miscellaneous Python script (not used here) to snag the Nth segment of 
M-words from each text as an example of the type of script often needed when preparing your corpus.


####step_1_Scrubbing_Tokenization_Culling
A brief description of how we "scrubbed" our text files, counted "words", and which words we chose to discard (cull) during each test.  In particular, we point you to 
Lexos (http://lexos.wheatoncollege.edu) to first "scrub" the texts so that all subsequent 
texts are tokenized and culled in a consistent fashion no matter what tool or package is used.

####step_2_Clustering
K-means, Hierarchical-agglomerative, and Bootstrap Consensus Trees were applied.

####step_3_Classification
We describe our use of Stylo in R (Eder et al., 2016) for Delta, Support-Vector Machine (SVM), and nearest shrunken centroid (NSC) models.

### Notes:
1. To facilitate replication of individual analyses *for each step*, we have included .zip versions of
the scrubbed texts used in that analysis along with the source code. Cloning this entire repo will thus result
in duplicate copies of text files. We only include copies of the scrubbed texts here, not their original versions.

2. Although we did not include in most of our analyses the stories proportedly written by Edgar's brother Henry (*cf.*, Collins, 2013), we include a separate directory of these four stories for your other, related, queries.

2. We have tried to document our scripts (really!).  We recognize that more efficient
methods exist. This is especially true in our R script in step_3b that automates a number
of trial runs. 

3. The tools, languages, and packages used (but not included here):
  - Lexos, local version (https://github.com/WheatonCS/Lexos) or available online at http://lexos.wheatoncollege.edu
  - Stylo in R (https://github.com/computationalstylistics/stylo)
  - Python (with Anaconda) and R scripts

mdl (January, 2016)
