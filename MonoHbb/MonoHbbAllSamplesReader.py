import os 

f = open('allfiles.txt','r')
outdir = "bbMETSamples"

os.system("mkdir -p "+outdir+"/log")

for ifile in f: 
    filename =  ifile.rstrip()
    print "\n=======================\nSubmitting",filename,"\n=======================\n"
    #os.system('python MonoHBranchReader.py -i '+filename+' -a')
    command='nohup python MonoHBranchReader.py -a -i '+filename+' -D '+outdir+' &> '+outdir+'/log/'+filename.split('/')[-1].split('.')[0]+'.log &'
    print "Executing shell command:",command
    os.system(command)
