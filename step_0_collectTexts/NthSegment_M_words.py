import os
import glob
import shutil
import codecs

"""
Python script to snag the Nth set of words each of size SMALLEST.
The file must have enough words to snag the Nth set of words.
"""

SMALLEST = 4000  # smallest filesize

prompt = "What Nth " + str(SMALLEST) + " words should be used? "

Nth = int(input(prompt))
path = "texts_" + str(Nth) + "_" + str(SMALLEST) + "_ToTry"
#print('\n', path, '\n')

if (os.path.exists(path) ):
    shutil.rmtree(path)
    #os.removedirs(path)
    
os.makedirs( path )

listOfFiles = glob.glob("corpus/*.txt")
#print listOfFiles

enoughWords = (Nth)*SMALLEST

for nextFile in listOfFiles:
    INPUT = codecs.open(nextFile, 'r', encoding='utf-8')
    
    words = ""
    for nextLine in INPUT:

        words += nextLine
        wordList = words.split()
        
        # quit as soon as we can
        if ( len(wordList) > enoughWords):
            break;
        
    #print("n words so far:", len(wordList))
    INPUT.close()
    
    # does this file have enough words to play?
    if ( len(wordList) > SMALLEST ):
        
        # do we have enough words to take the Nth SMALLEST set?
        if ( len(wordList) > enoughWords):
            # snag words of interest in the Nth set
            start = (Nth-1)*SMALLEST
            end   = Nth*SMALLEST
         
            wordList = wordList[start:end]
            words = ' '.join(wordList)    

            outputFileName = os.path.join(path, os.path.basename(nextFile) )
            #print(outputFileName)
    
            setN = "_" + str(Nth) + ".txt"
            outputFileName = outputFileName.replace(".txt", setN)
            #print(outputFileName)
            
            OUTPUT = open(outputFileName, 'w', encoding='utf-8')
 
    
            OUTPUT.write(words)
            OUTPUT.close()
        
            #junk = input("Pause")
            
        else:  # not enough
            print("x"*35)
            print("\tNOT ENOUGH: ", nextFile, " with ", len(wordList), " words <", enoughWords)            

    else:
        print("-"*35)
        print("TOO SMALL: ", nextFile, " with ", len(wordList), " words <", SMALLEST)
        
# end FOR each file


print("\nDone.\n")