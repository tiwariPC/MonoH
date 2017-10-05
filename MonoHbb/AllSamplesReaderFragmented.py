import os 

sourcedir = "/eos/user/s/spmondal/bbDM/data/Filelist_bkg_run2"
samplelist = [f for f in os.listdir(sourcedir) if not os.path.isfile(os.path.join(sourcedir, f))]

outdir = "bbMETSamplesFrag_bkg_run2"

for sample in samplelist:

#    os.system("mkdir -p "+outdir+"/"+sample+"/log")    
    filelist = [f for f in os.listdir(os.path.join(sourcedir, sample)) if os.path.isfile(os.path.join(sourcedir, sample, f)) and f.endswith('.root')]
    
    print "\n=======================\nSubmitting for",sample,"\n=======================\n"
    count = 0
    print "Submitting..."
    
    command=''
    for ifile in filelist: 
        filename =  ifile.rstrip()      
#        command+=  'python MonoHBranchReader.py -a -i '+os.path.join(sourcedir,sample,filename)+' -D '+os.path.join(outdir,sample)+'; '
        command+='python MonoHBranchReader.py -a -i '+os.path.join(sourcedir,sample,filename)+' -D '+os.path.join(outdir,sample)+' &> '+os.path.join(outdir,sample,'log/')+filename.split('.')[0]+'.log; '
#        print "Executing shell command:",command        
        count+=1
#    os.system("nohup sh -c \'"+command+"\' &")
                
    print "Submitted",count,"sequential BranchReader jobs."
        
