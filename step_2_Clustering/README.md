# step 2: Clustering (aGoodMystery)

As a set of initial probes, I was curious how this contested story compared to (i) other 
stories attributed to Poe and (ii) mixed in with stories by other authors. 
Based on previous experiences, I knew a cluster analysis to be a good first test. 

We share four variations using cluster analysis:

1. K-means on only Poe's stories (uses Lexos)
2. Hierarchical on only Poe's stories (uses Python script; converts to ETE and Newick format)
3. K-means when all stories by each author are concatenated together
4. Bootstrap Concensus Tree (uses Stylo in R)

### Tokenization
Having scrubbed the texts, when I proceeded in the Lexos workflow to apply a cluster analysis, I had to make 
decisions on what tokens to count. 
In these cluster analyses, I chose to treat each individual word as its own token (in the lingo, a 1-gram word-token ). Since the texts are of different lengths (for example, “A Dream” being 1,207 words and “Cask of Amontillado” 2,341 words, 
 the counts of each word in each text are normalized to proportions by dividing each word count in a text by the total number of words in that text . Finally, the list of words (terms) used was culled to include only those words that appear at least once in each of the stories in question.


Lexos provides a number of tokenize and normalization options. In short, users can decide to count groups of words (word n-grams) or groups of contiguous characters (character n-grams), where n refers to the number of units in a single token, for example, “the dog”, “dog ran”, and “ran away” are word 2-grams whereas “the d”, “he do”,  and   “e dog” are character 5-grams. Various studies have shown success with both n-gram options.

At this point, the workflow has led us to a stage where 19 stories are each represented by a vector of normalized word frequencies for the 38 words that appear at least one time in each story. Together, this is referred to as the Document Term Matrix (DTM). Each vector of word frequencies represents a stylistic signature for that text. 
