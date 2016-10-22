# step 1: Scrubbing (aGoodMystery)

As noted by Hoover (2015), "the process of tokenizing texts is typically out of sight and almost out of mind" since various tools make slight but significant decisions when tokenizing. It is for precisely this reason that we start with a set of texts that have been consistently scrubbed to avoid subsequent and varying interpretations of a "token", in our case "a word". 

To prepare the texts for subsequent analyses, I used a local install of Lexos, our group’s web-based, open-source workflow of tools for such work (Kleinman, LeBlanc, Drout and Zhang, 2016). I uploaded the group of texts to Lexos and “scrubbed” them by applying the following options: (i) all words were converted to lowercase, thus ensuring for example that “The” and “the” are counted as the same word), (ii) all punctuation was removed, so for example “night.” appearing at the end of a sentence with a period (.) and “night” are counted as the same, (iii) however, a single word-internal hyphen and word-internal apostrophes were kept, thus retaining hyphenated words, apostrophes in contractions and singular possessives. 


The texts stored here were all previously scrubbed using Lexos with the following options: make lowercase, remove digits, and remove punctuation (except keep internal-single hyphens and internal word apostrophes). 


Scrub Texts (using [Lexos](http://lexos.wheatoncollege.edu))
0. Texts were uploaded (in batches)
1. From the Prepare menu: Scrub
    (a) Remove All Punctuation (keep internal-single hyphens and internal word apostrophes)
    (b) Make Lowercase
    (c) Remove Digits
    (d) Scrub Tags (remove tags)

2. Apply Scrubbing

Tokenization and Culling
In this and all subsequent analyses unless otherwise noted, we chose to treat each individual word as its own token (in the lingo, a 1-gram word-token). Culling varies in each analysis. We often tried multiple versions of culling, for example, at times we used all the words vs. only the most frequent 100 words vs. the most frequent words that appear in each text at least once.

Note:
Lexos and 'Stylo in R' perform similar operations for keeping the Most Frequent Words (MFW) and culling.

Lexos_Tokenization_Culling.png - A screen shot image of the Lexos options set to keep the most frequent words that appear in each text at least once

Lexos_DTM.csv - A sample downloaded Document-Term Matrix (DTM) from Lexos after tokenization and culling. 

