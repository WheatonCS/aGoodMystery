library(stylo) 
# R script to apply Eder et al.'s 'Stylo in R' attribution methods 
# classication.method is (currently) "delta" (could be "svm", "nsc", etc)
#
# Thanks to Eder (personal communication and help) and Eder, Rybicki, and Kestemont (2016).

# this example runs only ONE trial (using present state of PRI/ and SEC/), but of course
# you'll want to vary the text distribution between PRI/ and SEC/ (see step_3b_RepeatedTrials)

	# --------- assumes you already prepared TRAINing (primary_set) and TESTing (secondary_set) directories
	
	# class names are authorName_prefixToFileName.txt
	# e.g., Poe_Berenice_1835.txt
	
	# time to apply stylo's method
	
	# we'll use strong culling
	# on Delta with 100 MFW, 100% culling: only top-40 words meet criteria
	
	results <- classify(gui = FALSE, path="./", 
		training.corpus.dir = "./primary_set", 
		test.corpus.dir = "./secondary_set", 
		analyzed.features="w", ngram.size=1, 
		mfw.min=100, mfw.max=100, mfw.incr=100, start.at=1,
		classification.method="delta",
		culling.min=100, culling.max=100, culling.incr=1, 
		save.analyzed.freqs=TRUE,
		how.many.correct.attributions=TRUE,
		final.ranking.of.candidates=TRUE,
		save.distance.tables=TRUE)

			
	# optional, if using DELTA (or NSC or SVM)
	# also dump Delta's 1st,2nd, 3rd RANKINGS
	
	# now, we retrieve both frequency tables from 'results' (thx to Eder et al. 2015 :)
	train = results$frequencies.training.set[,results$features.actually.used]
	test = results$frequencies.test.set[,results$features.actually.used]

	# now, we apply just a function for Delta classification
	delta.results = perform.delta(train, test)

	# from the results, we retrieve one of the attributes, i.e. the rankings
	delta.rankings = attr(delta.results, "rankings")
	
	# 
	resultName = paste("DELTA_rankings", "test.txt", sep="_")

	write.csv(delta.rankings, file = resultName)
