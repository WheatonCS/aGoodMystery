# step 2b: Python version of hierarchical clustering 

As an alternative to using Lexos, I clustered the eighteen(18) stories attributed to Poe with "A Dream" (UNKNOWN_ADream.txt)
using Python's sklearn, scipy, and matplotlib modules. The script continues (so we could play with ETE and Newick formats),
converting the linkage matrix to scipy tree to an ETE tree (Environment for (phylogenetic) Tree Exploration, http://etetoolkit.org/)
to a Newick string (which could be written to a file if desired, but presently commented out).

Notes:
- No culling was done on the word list here; all words were used.
