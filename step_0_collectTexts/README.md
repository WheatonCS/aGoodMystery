# step 0: Collect Texts (aGoodMystery)

Forming a valid comparison group is critical. Rudman (2012) cautions that a careful selection of texts, the primary data, "is almost universally side-stepped" (p267). The texts provided here are but a first attempt and certainly do not pass Rudman's requirements. 

1. corpus - A wide collection of texts from contemporaries of Poe, both American and British, male and female. As explained below, not all of these texts are used in our analyses. We provide them here for your potential future work.

   In preparation for these analyses, we initially collected 16 Poe short stories, as well as 16 texts from recommended American "contemporaries" of Poe (Cooper, Hawthorne, Irving, and Melville). Knowing we needed more texts from the time period in question (ca. 1820-1840s), we collected 20 stories published at this time by six other American, male authors. In all, our experimental corpus is comprised of 52 texts from eleven authors, plus our contested story "A Dream". Note that not all texts are used in each analysis; at each step, we have tried to be explicit about the texts involved and of course include a local folder containing those texts used at each step.

   *Note: In subsequent work, we acknowledge that we must do a better job at forming and documenting the files used in our working corpus, as pointed out by one reviewer. To be completely honest, this is a product of a computer scientist collecting texts without a domain expert at hand! Although "The Raven" is included in the Excel list of files (see ListOfTexts.xlsx), David Hoover (personal communication) caught the mistake of including that poem in the comparision group and thus it was not used. The takeaway lesson here: this type of work is interdisciplinary and scholars are wise to seek expert counsel when forming any corpus.

2. ListOfTexts.xls - complete list of potential texts to use, including textfile name, author name, national origin, and gender, date of publication, and genre.

3. Henry_W_Poe_corpus - stories purportedly written by Edgar's brother Henry; we include these as stock for related inquiries.

4. Schoberlein_2016_corpus - Stefan Scholberlein's corpus of prose texts used in his 2016 paper (see reference); as of January 2017, we have not used these texts, but we provide it here as an alternate corpus. 

5. NthSegment_M_words.py - A Python script to generate texts all of the same size of M words each. We provide the script as but one example of the type of script we use as we consider how to build a working corpus. We did not use this script in this set of analyses, but of course, word token proportions are used to account for texts of varying size (see step_1 for more on tokenization).


###Notes: 

1. The file "UNKNOWN_ADream_1831.txt" contains the contested story. In some analysis, we change the prefix of this file to "Poe_" to facilitate its potential attribution (or not).

2. As mentioned above, not every one of the texts in the corpus folder are used in each step of our analyses (e.g., in the clustering phase, we use at times only Poe stories; see Step_1_Clustering). For each step in the workflow, we have included the subset from the corpus directory that were used for that particular test. 

3. The texts stored here were all previously scrubbed using Lexos with the following options: make lowercase, remove digits, and remove punctuation (except keep internal-single hyphens and internal word apostrophes). As noted by Hoover (2015), various tools make slight but significant decisions when tokenizing. It is for precisely this reason that we start with a set of texts that have been consistently scrubbed. See step_1_Scrubbing_Tokenization_Culling for more details.

4. The texts by Edgar's brother, Henry W. Poe, are included here but are themselves of contested authorship, thus we typically do *not* include these four stories in our tests.

###Thanks for help in corpus construction from:

Shirrel Rhoades, Editor of Absolutely Amazing Books:
  Many of the Poe stories in text form were obtained from Shirrel Rhodes, publishing consultant, writer, book publisher and the colleague who first brought this question to our attention. 

Sam Coale, Wheaton College:
  Sam tossed out names of "contemporaries" of Poe as a starting set of comparison authors. Most of these texts, e.g., by Hawthorne, Melville, et al. were obtained from Project Gutenberg (http://www.gutenberg.org/).

Ted Underwood, University of Illinois, Urbana-Champaign:
  Ted's blog entry "Open Data" (http://tedunderwood.com/open-data/) led to his sharing stories written in the 1820s and 1830s.

Ryan Cordell, Northeastern University:
  Ryan answered an email plea with multiple suggestions.
1. Charles Brockden Brown is a bit too early, but is certainly a Gothic predecessor to Poe with many stylistic similarities.
2. Robert Montgomery Bird is an even more direct contemporary in both time and style. I'd include Sheppard Lee, but others from Bird as well.
3. You definitely want as much as you can find from George Lippard, a friend and correspondent of Poe's who wrote in the Gothic and city mystery traditions, mostly about Philadelphia. I'd start with The Quaker City.
4. If you could get a sampling of fiction from some of the magazines Poe edited and contributed to (Graham's,Southern Literary Messenger) that would be useful.

Cary Gouldin, Reference librarian, Wheaton College:
  Cary led us to stories published in the magazines where Poe wrote (e.g., *North American Or Weekly Journal of Politics, Science and Literature*), including stories signed with the initials of Edgar’s brother Henry (W.H.P.), many possibly written by Edgar himself (*cf.*, Collins 2013).


 
