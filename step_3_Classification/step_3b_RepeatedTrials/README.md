# step 3b: Classification with Delta (aGoodMystery)

The folder /noParts... contains an R script to apply Eder's 'Stylo in R' attribution methods. The texts are randomly separated into /PRIMARY(train) and /SECONDARY(test) sets where NUMOFTESTS (see script) decides on the number of k-fold iterations.  [Jingxian Liu and Mark LeBlanc (December 2015)]

Note: This script is run in the same directory as the texts and the output is written to (this) parent (../) directory.

After execution of the R script (classicDelta_manipulation.R) in the folder noPart..., the file "../Results.txt" will contain stylo's attribution for all trials. A subsequent Python script (Final_Result.py) will provide summary stats and will build confusion matrices for each author.

OUTPUT files (once the R script is run):

1. FinalResultsReport.txt -- list of all texts used in this trial
2. result/ --  directory where results of each test are cached
3. authors.txt -- list of authors involved
4. Results.txt -- concatenation of attribution results from all the trials

