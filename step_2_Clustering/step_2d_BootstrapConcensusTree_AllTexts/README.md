# step 2d: Bootstrap Concensus Tree (BCT) using Stylo in R

As a final unsupervised probe, we turned to Stylo’s (Stylometry with R) Bootstrap Consensus Tree. 
The BCT aggregates results over multiple cluster analyses and shows those texts that 
satisfy a consensus number of the individual trials (here 50%). 
Using 12 different authors and at least two texts by each author for a total of 46 stories, 
stylo formed a concensus cluster of the texts using the following frequency bands of the most-frequent words: 
100 MFW, 200 MFW, …, 1000 MFW. No culling was performed.

Of interest are that each authors’ stories cluster consistently together (with the exception that 
Bird’s initial section of “Sheppard Lee” and his “Calavar” are found in different clades, in red) . 
“A Dream” clusters (again) with the smaller Poe texts. 
As you’ll see, I also couldn’t resist tossing in the four stories sometimes attributed to 
Edgar’s brother Henry (“Monte Video”, “A Fragment”, “The Pirate”, and “Recollections”).  
These four stories are found within the cluster of Poe’s known works. Hmmm ... (note to self to return
here to explore this more fully). 
