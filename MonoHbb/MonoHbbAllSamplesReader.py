import os 

parallel=False

f = open('allfiles4.txt','r')
outdir = "bbMETSamples_large"

if parallel:
    os.system("mkdir -p "+outdir+"/log")

for ifile in f: 
    filename =  ifile.rstrip()
    print "\n=======================\nSubmitting",filename,"\n=======================\n"
    
    if parallel:
        command='nohup python MonoHBranchReader.py -a -i '+filename+' -D '+outdir+' &> '+outdir+'/log/'+filename.split('/')[-1].split('.')[0]+'.log &'
    else:
        command='python MonoHBranchReader.py -a -i '+filename+' -D '+outdir
    print "Executing shell command:",command
    os.system(command)

f.close()
