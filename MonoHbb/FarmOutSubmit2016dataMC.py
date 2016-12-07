import os

#outputdirname="Raman/AnalysisHistograms_MergedSkimmedV12_PuppiCA15_V2/"
outputdirname="Raman/AnalysisHistograms_MergedSkimmedV12_Puppi_V7/"
regions=['signal', 'wt', 'zj', 'signalpSB']#, 'wj', 'tt', 'wjalphabet', 'ttalphabet', 'wtalphabet','signalpSB']
#regions=['signalpSB']

#outputdirname="Raman/AnalysisTuples_2016DataMC_V5/TTBar/"
inputprefix="--input-dir=root://cmsxrootd.hep.wisc.edu//store/user/khurana/Raman/Merged_Skimmed/"
cmsswpath="/afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_8_0_11"
exepath="/afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_8_0_11/src/MonoH/MonoHbb/"

fout = open("samplestorun.txt","w")


#samples = '''V12_PuppiCA15_V1 V12_PuppiCA15_V1'''
#samples = '''V12_Puppi_V1 V12_Puppi_V1'''
samples = '''V12_Puppi_V3 V12_Puppi_V3'''

fout.write(samples)
fout.close()

## 

def submitjobs(region_, scriptname):
    exepath_new = exepath + scriptname
    outputdirname_new = outputdirname + '/' + region_
    f = open('samplestorun.txt','r')
    
    for line in f:
        a,b = line.split()
        datasetdet=[a,b]
        jobcommand = ("farmoutAnalysisJobs "+outputdirname_new+"/"+datasetdet[0]+" "+inputprefix+datasetdet[1]+" "+cmsswpath+" "+exepath_new+" --fwklite --input-files-per-job=1 --extra-inputs=MonoHbbQuantities.py,MonoHBranchReader.py,PileUpWeights.py,BTagCalibrationStandalone.cpp,BTagCalibrationStandalone.h,subjet_CSVv2_ichep.csv,CSVv2_ichep.csv")
        
        print "--------------------------------------------------------------"
        print "submitting jobs for"+datasetdet[0]
        print "--------------------------------------------------------------"
        print jobcommand
        os.system(jobcommand)
    



for iregion in regions:
    filein = open('RunAllRegionUsingFarmOut.py','r')
    scriptname = 'RunAllRegionUsingFarmOut_'+iregion+'.py'
    farmoutscript = open(scriptname,'w')
    print ("submitting jobs for ", iregion, "region")
    
    for iline in filein:
        iline = iline.replace('DEMOMODE',iregion)
        farmoutscript.write(iline)
    farmoutscript.close()
    submitjobs(iregion, scriptname)
