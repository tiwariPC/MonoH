import os
import sys

inputdirname=sys.argv[1]
nargv = len(sys.argv) -2
print nargv
print sys.argv[2]
ControlRegions=[]

for iargv in range(0,nargv):
    ControlRegions.append(sys.argv[iargv+2])

print ControlRegions
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
datacardsdir = inputdirname.replace('AllRegions', 'DataCards_AllRegions')

os.system('rm -rf '+datacardsdir)
os.system(' mkdir -p '+datacardsdir)

for itextfiles in range(len(textFilesList)):
    for whichCR in ControlRegions:
        if whichCR in textFilesList[itextfiles]:
            print (whichCR, textFilesList[itextfiles])
            os.system ('python MakeDataCards.py '+inputdirname+'/'+textFilesList[itextfiles]+' '+datacardsdir +' '+rootfilesList[itextfiles] +' '+whichCR)
            os.system('cp '+ inputdirname+'/'+rootfilesList[itextfiles] + ' '+datacardsdir)
    
#print textFilesList
