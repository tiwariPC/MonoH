import os 

f = open('allfiles.txt','r')

for ifile in f: 
    filename =  ifile.rstrip()
    #os.system('python MonoHBranchReader.py -i '+filename+' -a')
    os.system('python MonoHBranchReader.py -a -i '+filename+' -o ifile.split()[1].root -D bbMETSamples')
