# step 2c: K-means clustering "A Dream" against the collected (concatenated) works of other authors.

We were bothered by the relatively small sizes of the Poe stories and the way the clusters formed relative to file size. 
I performed an additional cluster analysis with Lexos, but this time combining (concatenating) each of the stories 
by eleven authors into one file per author.
For example, I concatenated Doyle’s “Adventures of the Cardboard Box”, 
“Sherlock Holmes”, and “Sign of the Four” into one file and all of Poe’s stories (but not the contested “A Dream”) 
into another file. Using these concatenations of complete stories from Poe and ten other authors (Cooper, Doyle, Hawthorne, Irving, 
Lippard, Quincey), I performed new trials of K-means clustering. 
When forced into two to five clusters (2<=K<=5), “A Dream” clusters with the collection of other Poe stories (see attached Figure).

