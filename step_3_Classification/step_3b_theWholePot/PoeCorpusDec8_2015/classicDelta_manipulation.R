library(stylo) 
# R script to apply Eder's 'Stylo in R' attribution methods
# texts are randomly separated into /PRIMARY(train) and /SECONDARY(test) sets
# where NUMOFTESTS (see below) decides on the number of k-fold iterations
#     [ Jingxian Liu and Mark LeBlanc (December 2015) ]

# Note: this script is run in the same directory as the texts
#       output is written to parent (../) directory

# The file "../Results.txt" will contain stylo's attribution for all trials
# A subsequent Python script (see Final_Result.py) will provide summary stats 
#   and confusion matrices for each author

set.seed(as.integer(Sys.time()))	# set the seed for a random generator using the current time

# prepare OUTPUT files:
#    1) ../FinalResultsReport.txt -- list of all texts used in this trial
#    2) ../result directory where results of each test is cached
#    3) ../authors.txt
#    4) ../Results.txt (concatenation of attribution results from all the trials)

if (file.exists("../result")){
	unlink("../result",recursive = TRUE)
} 


if (!file.exists("../Rankings"))
{
	dir.create(file.path("..", "Rankings"))
} else
{
	unlink("../Rankings",recursive = TRUE)
	dir.create(file.path("..", "Rankings"))
}


# glob a list of ALL the files with extension ".txt" used in this trial 
Files = list.files(path=".", pattern = ".txt") 

# write those files to FinalResultsReport.txt
write(Files,file = "../FinalResultsReport.txt", append = FALSE, ncolumns = 1, sep = "\t")

# make a vector of author names; author names must be prefixes to text names
# e.g.,    Cooper_LastMohicans_1.txt,  Poe_MaskOfTheRedDeath.txt
authors <- c()
for (i in Files)
{
	names = unlist(strsplit(i, "[_]"))
	authorName<-names[[1]]
	if (authorName %in% authors) {
	}
	else {
		authors <- c(authors,authorName)
	}
}
# print (authors)

result = c()
NUMOFTESTS = 10		#  set k-fold iterations, where k is NUMOFTESTS
for (j in 1:NUMOFTESTS)
{
	# make sure directories and file of author names are ready
	if (!file.exists("../secondary_set")){
		dir.create(file.path("..", "secondary_set"))
	} 
	else{
		unlink("../secondary_set",recursive = TRUE)
		dir.create(file.path("..", "secondary_set"))
	}
	if (!file.exists("../primary_set")){
		dir.create(file.path("..", "primary_set"))
	} 
	else{
		unlink("../primary_set",recursive = TRUE)
		dir.create(file.path("..", "primary_set"))
	}
	if (!file.exists("../result")){
		dir.create(file.path("..", "result"))
	} 
 	if (file.exists("../authors.txt")){
		unlink("../authors.txt",recursive = TRUE)
	}


	# for each of the authors in this trial
	for (i in authors)
	{
		#prefix
		authorName = paste(i, "_" ,sep = "")
		
		#print(authorName)

		# generate a list of texts (filenames) by this author
		temp<-list.files(path = ".", pattern = i)
		
		# must have more than one(1) file in order to be selected to be in the TEST set (secondary_set)
		if(length(temp) >1) {
			# randomly shuffle up the texts by that author 
			temp <- sample(temp)
			
			# NOTE: in this case, we are particularly interested in the contested story "A Dream"
			#       so we take special care that this text *always* ends up in the TEST (secondary_set)
			# path for the first file in temp
			if (authorName == "Poe_") {
				
				# copy the story "A Dream" into the secondary set 
				filename = "Poe_ADream_1831.txt"
				newName = "../secondary_set/ADream_1831.txt"
				file.copy(filename, newName)
				
				# when shuffling Poe's texts, check if the first text was "A Dream"; if so,
				# make sure at least one other Poe text (here, the 2nd text) is tested in this iteration
				if (temp[1] == "Poe_ADream_1831.txt"){
					filename = paste("./",temp[2], sep="")
					newName = sub("Poe_", "", temp[2])
					newName = paste("../secondary_set/", newName,sep="")
					file.copy(filename, newName)
				}
			}
			
			filename= paste("./",temp[1], sep="")
			#print (filename)
			# cut out the prefix
			newName = sub(authorName, "",temp[1])
			# generate the path name for that file
			newName = paste("../secondary_set/", newName,sep="")
			
			# copy the file to secondary set
			file.copy(filename, newName)	
					
			# move M texts by this author to TRAINing (primary_set)
			M = 1
			if (length(temp) > M) {
				maxToTest = M+1
			}
			else {
				maxToTest = length(temp)
			}
			
			# or just put all the other files in PRIMARY set if next line uncommented
			maxToTest = length(temp)
			
			for (k in 2: maxToTest){
				if (temp[k] != "Poe_ADream_1831.txt"){
					filename= paste("./",temp[k], sep="")
					file.copy(filename, "../primary_set/")
				}
			}
			write(i, file = "../authors.txt", append = TRUE, sep = "")
		
		}
		
		# if an author only has one text, into the PRIMARY (train) set you go
		else{
			filename= paste("./",temp[1], sep="")
			file.copy(filename, "../primary_set/")

		}
	}
	
	# --------- all the work above was to prepare the TRAINing and TESTing sets
	#
	# time to apply stylo's method
	results <- classify(gui = FALSE, path="../", 
		training.corpus.dir = "./primary_set", 
		test.corpus.dir = "./secondary_set", #number.of.candidates=15,
		analyzed.features="w", ngram.size=1, 
		mfw.min=100, mfw.max=100, mfw.incr=100, start.at=1,
		method="delta",
		culling.min=100, culling.max=100, culling.incr=1, 
		save.analyzed.freqs=TRUE,
		how.many.correct.attributions=TRUE,
		final.ranking.of.candidates=TRUE,
		save.distance.tables=TRUE)
		
	# save stylo's output (in 'final_result') of this j(th) trial in the /result directory
	resultName = paste("../result/final_result", j, sep="_")	
	file.copy("../final_results.txt", resultName)
	
	# also dump Delta's 1st,2nd, 3rd RANKINGS
	# now, we retrieve both frequency tables from 'results' (thx to Eder et al. 2015 :)
	train = results$frequencies.training.set[,results$features.actually.used]
	test = results$frequencies.test.set[,results$features.actually.used]

	# now, we apply just a function for Delta classification
	delta.results = perform.delta(train, test)

	# from the results, we retrieve one of the attributes, i.e. the rankings
	delta.rankings = attr(delta.results, "rankings")

	resultName = paste("../Rankings/ClassicDELTA_rankings", j, sep="_")

	write.csv(delta.rankings, file = resultName)
	
}  # end NUMOFTEST trials


if (file.exists("../Results.txt")){
	unlink("../Results.txt",recursive = TRUE)
} 

# z<- file("../Results.txt", "w")

for (i in 1:NUMOFTESTS){

	fileName=paste("../result/final_result", i, sep="_")
	conn<-file(fileName, open="r")
	linn=readLines(conn)
	
	# the lines involved in the stylo TEST include the substring "-->", for example:
	# ADream_1831 	-->	 Poe        
	# MobyDick_2 	-->	 Melville
	testedLines = grep("-->", linn)
	
	# testedLines will now contain the INDICES of those lines that matched
	firstIndex = testedLines[1]
	lastIndex = testedLines[length(testedLines)]
	result = linn[firstIndex:lastIndex]
	
	write(result, file = "../Results.txt", append = TRUE, sep = "")
}

# After this R script, 
# a subsequent Python script (see ../Final_Result.py) will provide summary stats 
#   and confusion matrices for each author

