# step 3a: Classification (aGoodMystery)

First a couple of small tests to apply Stylo in R's DELTA (or use another method of your choosing).

**oneShuffle**:
Shuffle our "whole pot" of individual texts and apply Delta. More specifically, one sample text segment from each author was tested against a Delta model built from the remaining texts. The contested "A Dream" is also placed in the test (secondary_set).

**MergedTextsForEachAuthor**:  (not yet shown)
Apply Eder’s classic Delta using “A Dream” as the sole test against a model built using concatenated stories from a small set of recommended authors, including a Poe Gothic predecessor (Charles Brockden Brown), a direct contemporary in time and style (Robert Montgomery Bird), and a friend later in life and correspondent of Poe (George Lippard) (Cordell, personal communication). Additional concatenated texts for other authors are included in a directory of "otherTexts" for building various training (primary_set) and test (secondary_set) configuations.  

In the next step (3b), we show a script that automates the construction of the primary_set (training set) and second_set (test set). Here, we slow it down a bit and just perform one trial.
