# step 1: K-means Clustering (aGoodMystery)

Eighteen(18) stories attributed to Poe clustered with "A Dream" (UNKNOWN_ADream.txt)

Here, we assume the texts have been previously scrubbed (see notes in step 0).
We used a local installation of the Lexos tools for tokenization and K-means clustering, although
with these relatively small in number and size files, the web-based version of Lexos would also work
(http://lexos.wheatoncollege.edu - see K-means clustering under the Analyze pull-down menu).

The following Lexos workflow was followed:
1. UPLOAD: The 19 texts were uploaded to Lexos (18 by Poe and "A Dream").
2. SCRUB:  Since the texts were all subsequently scrubbed, we can proceed to tokenization.

[steps 3-5 can all be performed on the K-means page]

3. TOKENIZE: In this and all subsequent analyses unless otherwise noted, we chose to treat each individual word as its own token (in the lingo, a 1-gram word-token).
4. CULL: Only the most frequent words that appear in all stories were included. In this case, 38 words met the criteria.
5. ANALYZE: K-means options:  K=4, distance metric=Euclidean, and all other defaults
