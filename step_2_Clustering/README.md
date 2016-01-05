# step 1: Clustering (aGoodMystery)

As a set of initial probes, I was curious how this contested story compared to (i) other 
stories attributed to Poe and (ii) mixed in with stories by other authors. 
Based on previous experiences, I knew a cluster analysis to be a good first test. 

We share four variations using cluster analysis:

1. K-means on only Poe's stories (uses Lexos)
2. Hierarchical on only Poe's stories (uses Python script; converts to ETE and Newick format)
3. K-means when all stories by each author are concatenated together
4. Bootstrap Concensus Tree (uses Stylo in R)
