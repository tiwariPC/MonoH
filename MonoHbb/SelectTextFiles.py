import os
import sys

inputdirname=sys.argv[1]
ControlRegions=['signal','zj','wj','tt','wt']
textFilesList=[]
rootfilesList=[]

for whichCR in ControlRegions:
    for files in  os.listdir(inputdirname) :
        if whichCR in files:
            if ".txt" in files:
                textFilesList.append(files)



for whichCR in ControlRegions:
    for files in  os.listdir(inputdirname) :
        if whichCR in files:
            print files
            if ".root" in files:
                rootfilesList.append(files)


print rootfilesList
datacardsdir='DataCards_'+inputdirname
os.system('rm -rf '+datacardsdir)
os.system(' mkdir -p '+datacardsdir)

for itextfiles in range(len(textFilesList)):
    #os.system ('python MakeDataCards.py '+inputdirname+'/'+textFilesList[itextfiles]+' '+inputdirname+'/'+ControlRegions[itextfiles] +' '+rootfilesList[itextfiles])
    #os.system ('python MakeDataCards.py '+inputdirname+'/'+textFilesList[itextfiles]+' '+inputdirname +' '+rootfilesList[itextfiles])
    #os.system(' mv '+inputdirname+'/'+ControlRegions[itextfiles]+' '+datacardsdir)

    for whichCR in ControlRegions:
        if whichCR in textFilesList[itextfiles]:
            print (whichCR, textFilesList[itextfiles])
            os.system ('python MakeDataCards.py '+inputdirname+'/'+textFilesList[itextfiles]+' '+datacardsdir +' '+rootfilesList[itextfiles] +' '+whichCR)
            os.system('cp '+ inputdirname+'/'+rootfilesList[itextfiles] + ' '+datacardsdir)
    
#print textFilesList
