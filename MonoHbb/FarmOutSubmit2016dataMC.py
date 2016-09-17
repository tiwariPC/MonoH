import os
outputdirname="Raman/AnalysisTuples_2016DataMC_V1/"
inputprefix="--input-dir=root://cmsxrootd.hep.wisc.edu//store/user/khurana/"
cmsswpath="/afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_8_0_11"
exepath="/afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_8_0_11/src/MonoH/MonoHbb/RunUsingFarmOut.py"

fout = open("samplestorun.txt","w")

## 76 samples 

samples='''ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph MonoH2016/V1/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph/crab_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph/160817_150841/
'''

fout.write(samples)
fout.close()

## 
f = open('samplestorun.txt','r')
for line in f:
    a,b = line.split()
    datasetdet=[a,b]
    jobcommand = ("farmoutAnalysisJobs "+outputdirname+"/"+datasetdet[0]+" "+inputprefix+datasetdet[1]+" "+cmsswpath+" "+exepath+" --fwklite --input-files-per-job=1 --extra-inputs=MonoHbbQuantities.py,MonoHBranchReader.py")
    
    print "--------------------------------------------------------------"
    print "submitting jobs for"+datasetdet[0]
    print "--------------------------------------------------------------"
    print jobcommand
    os.system(jobcommand)
    
