# step 1: Tokenization and Culling (aGoodMystery)

In this and all subsequent analyses unless otherwise noted, we chose to treat each individual word as its own token (in the lingo, a 1-gram word-token). Culling varies in each analysis. We often tried multiple versions of culling, for example, at times we used all the words vs. only the most frequent 100 words vs. the most frequent words that appear in each text at least once.

Note:
All texts have been previously and consistently scrubbed (in Lexos; see Step 0).

Lexos and 'Stylo in R' perform similar operations for keeping the Most Frequent Words (MFW) and culling.

Lexos_Tokenization_Culling.png - A screen shot image of the Lexos options set to keep the most frequent words that appear in each text at least once

Lexos_DTM.csv - A downloaded Document-Term Matrix (DTM) from Lexos after tokenization and culling. 

