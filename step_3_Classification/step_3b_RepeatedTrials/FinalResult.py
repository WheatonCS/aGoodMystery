import re

# assumes you have run PoeCorpusDec8_2015/classicDelta_manipulation.R

"""
assumes files ready:      
  FinalResultsReport.txt
  Results.txt
  authors.txt
  
produces Stats.csv, confusion matrix for each author
"""


# file of all the texts in the corpus
# authorName_textName.txt
allTexts = open("FinalResultsReport.txt", 'r')

# file of all tests made 
# ADream_1831 	-->	 Poe
Results = open("Results.txt", 'r')

# list of authors used
allAuthors = open("authors.txt", 'r')

# file containing final stats, e.g., confusion matrices
Stats = open("Stats.csv", 'w')

# ----------------------------------------------------------------------------
# make dictionary of (textName: authorName) pairs

nameList={}  # keys are textNames, values are authorNames
# e.g.,  {a_text_name:author, Rookwood1:Ainsworth, SherlockHolmes_1:Doyle, ...}
for line in allTexts:
	# Ainsworth_Rookwood1.txt
	# Cooper_LastMohicans_1.txt
	line = re.split("_", line)
	author = line[0]
	name = line[1:]
	name="_".join(name)	# rejoin textnames that had underscores
	start = 0
	end = name.find('.', start)
	name = name[start:end]	# remove the .txt extension
	
	# name of text is KEY, author of that text is the VALUE
	nameList[name] = author

allTexts.close()

# ----------------------------------------------------------------------------

tab = ','
# e.g.,  Confusion = {"Poe":[0,0,0,0], "Melville":[0,0,0,0], ...}
#        where values are [ True+ | False- | True- |  False+ ]
#                            0        1        2        3 

# e.g., assume CLASS = Poe
TruePOS	 = 0	# you predict Poe (+) and you are right (T)
FalsePOS = 1	# you predict Poe (+) and you are wrong (F)
TrueNEG  = 2	# you don't predict Poe (-) and you are right (T)
FalseNEG = 3	# you don't predict Poe (-) and you are wrong (F)
# ----------------------------------------------------------------------------
# general confusion matrix for each author
authorNamesList = []
Confusion = {}
for line in allAuthors:

	line = re.split("\n", line)
	name = line[0]
	Confusion[name]	= [0]*4		# initialize list of 4 scores to zero
	
	# keep those names in a list
	authorNamesList.append(name)
	
allAuthors.close()
# ----------------------------------------------------------------------------

# initialize dictionary to track authors that are predicted for "A Dream"
ADreamPredictions = {}
for nextAuthor in authorNamesList:
	ADreamPredictions[nextAuthor] = 0



#--------------------------------------------------
Stats.write("Text" + tab + " PREDICTED author " + tab + " WRITTEN by " + '\n')

# for each of the TESTs ...
for line in Results:
	# stylo output format:  textName (no author prefix, no file extension) --> predicted author
	# ADream_1831 	     -->  Poe
	# BracebridgeHall1   -->  Irving
	line = line.rstrip()
	line = re.split(' ', line)

	textName        = line[0]
	predictedAuthor = line[2]
	
	#print (textName, "predicted by", predictedAuthor, "written by", nameList[textName])
	Stats.write(textName + tab + predictedAuthor + tab + nameList[textName] + '\n')
	
	
	# Confusion = {"Poe":[0,0,0,0], "Melville":[0,0,0,0], ...}
	# where values are [ True+ | False- | True- |  False+ ]
	#                      0        1        2        3 	
	
	# for each author: fix confusion matrix CLASS, e.g., first update Poe's matrix, then Melville's, etc.
	for key in Confusion:

		# nameList is dictionary of (textName: authorName) pairs
		actual = nameList[textName]
		
		# if we are working on key's confusion matrix
		if (key == predictedAuthor or key == actual):
			
			if actual == predictedAuthor:	# e.g, MobyDick_2 --> Melville
				Confusion[key][TruePOS]	+= 1		# T+
			elif actual == key and predictedAuthor != key:
				Confusion[key][FalseNEG]	+= 1	# F-
			else: # predicted == key && actual != key
				Confusion[key][FalsePOS] += 1		# F+
		
		else:
			Confusion[key][TrueNEG]	+= 1
			
		
		
#-------------------------------------
	if textName == "ADream_1831":
		ADreamPredictions[predictedAuthor] += 1
		
# end FOR each trial

#-------------------------------------
Stats.write("\n")
Stats.write("Author" + tab + "TruePOS" + tab + "TrueNEG" + tab + "FalsePOS" + tab + "FalseNEG" + '\n')
for key in Confusion:
	Stats.write(key+ tab+ str(Confusion[key][TruePOS])+ tab+ str(Confusion[key][TrueNEG])+ tab+ str(Confusion[key][FalsePOS])+ tab+ str(Confusion[key][FalseNEG])+ '\n')
#---------------------------------------

Stats.write("\n")
# Predicted Authors for A-Dream
Stats.write("Author:" + tab + "Times predicted to write [A Dream]\n")
for author in ADreamPredictions.keys():
    Stats.write(author + tab + str(ADreamPredictions[author]) + "\n")
    
Stats.close()

#---------------------------------------


print("\nDone.\n")

