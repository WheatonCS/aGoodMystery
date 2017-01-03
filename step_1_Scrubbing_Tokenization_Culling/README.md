# step 1: Scrubbing (aGoodMystery)

As noted by Hoover (2015), "the process of tokenizing texts is typically out of sight and almost out of mind" since various tools make slight but significant decisions when tokenizing. It is for precisely this reason that we start with a set of texts that have been consistently scrubbed to avoid subsequent and varying interpretations of a "token", in our case "a word". 

To prepare the texts for subsequent analyses, we used a local install of [Lexos](http://lexos.wheatoncollege.edu), our group’s web-based, open-source workflow of tools for such work (Kleinman, LeBlanc, Drout and Zhang, 2016). We uploaded the group of texts to Lexos and “scrubbed” them by applying the following options: (i) all words were converted to lowercase, thus ensuring for example that “The” and “the” are counted as the same word), (ii) all punctuation was removed, so for example “night.” appearing at the end of a sentence with a period (.) and “night” are counted as the same, (iii) however, a single word-internal hyphen and word-internal apostrophes were kept, thus retaining hyphenated words, apostrophes in contractions and singular possessives. 

*Note: The process of "scrubbing" and tokenizing texts is a real challenge and despite years of adding functionality to this part of the workflow (e.g., we now handle punctuation in all languages), our Lexos software still requires more work. As pointed out by one reviewer, Lexos converts possessive plurals ending in 's' into regular plurals. Also, as Hoover (2015) points out, handling multiple hyphens is complicated and Lexos does not distinguish between hyphenated words and double hyphens used to end a sentence such as found in many of Poe's stories. Both of these items are on our action-item list for upcoming work.*

The texts stored in the step_0 corpus folder were all previously scrubbed using Lexos with the following options: make lowercase, remove digits, and remove punctuation (except keep internal-single hyphens and internal word apostrophes). 


###Scrub Texts (using [Lexos](http://lexos.wheatoncollege.edu))
1. Texts were uploaded (in batches)
2. From the Prepare menu: Scrub
  * Remove All Punctuation (keep internal-single hyphens and internal word apostrophes)
  * Make Lowercase
  * Remove Digits
  * Scrub Tags (remove tags)
3. Apply Scrubbing

###Tokenization and Culling
In this and all subsequent analyses unless otherwise noted, we chose to treat each individual word as its own token (in the lingo, a 1-gram word-token). Culling, the decision as to which of the words to use in an analysis, varies in each test. We often tried multiple versions of culling, for example, at times we used all the words that appear in any of the texts *vs.* only the most frequent 100 words *vs.* the most frequent words that appear in each text at least once. To reproduce the results, the reader is cautioned to note the decisions made at each step.

Note:
Lexos and 'Stylo in R' perform similar operations for keeping the Most Frequent Words (MFW) and culling.

Other files:
  - Lexos_Tokenization_Culling.png - A screen shot image of the Lexos options set to keep the most frequent words that appear in each of the 19 texts at least once
![alt text](https://github.com/WheatonCS/aGoodMystery/blob/master/step_1_Scrubbing_Tokenization_Culling/Lexos_Tokenization_Culling.png "Culling options")

  - Figure_1_VectorsOfProportions.png - A screen shot image of some of the token (word) proportions in a few texts
![alt text](https://github.com/WheatonCS/aGoodMystery/blob/master/step_1_Scrubbing_Tokenization_Culling/Figure_1_VectorsOfProportions.png
"Proportions of some words in a few texts")

  - Lexos_DTM.csv - A sample downloaded Document-Term Matrix (DTM) from Lexos after tokenization and culling. 

