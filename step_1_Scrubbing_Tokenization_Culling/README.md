# step 1: Scrubbing (aGoodMystery)

Because different tools and packages are used throughout these tests, we
chose to "scrub" once to avoid subsequent and varying interpretations of a "token",
in our case "a word".

Steps:
=====================================================================
(0) UPLOAD A1.3_Dan_T00030.txt and A3.3_Az_T00130.txt
=====================================================================
(1) SCRUB both:
    (a) Remove punctuation
    (b) Make Lowercase
    (c) Remove Digits
    (d) Keep Words Between corr/foreign Tags

    (e) Load the DAZ_lemma.txt file for Lemmas
    (f) Load the DAZ_consolidation.txt file for Consolidations
    (g) Set Special Characters to Dictionary of Old English (sgml)

    Apply Scrubbing




In this and all subsequent analyses unless otherwise noted, we chose to treat each individual word as its own token (in the lingo, a 1-gram word-token). Culling varies in each analysis. We often tried multiple versions of culling, for example, at times we used all the words vs. only the most frequent 100 words vs. the most frequent words that appear in each text at least once.

Note:
All texts have been previously and consistently scrubbed (in Lexos; see Step 0).

Lexos and 'Stylo in R' perform similar operations for keeping the Most Frequent Words (MFW) and culling.

Lexos_Tokenization_Culling.png - A screen shot image of the Lexos options set to keep the most frequent words that appear in each text at least once

Lexos_DTM.csv - A downloaded Document-Term Matrix (DTM) from Lexos after tokenization and culling. 

