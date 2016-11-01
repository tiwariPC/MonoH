import os

outputdirname="Raman/AnalysisHistograms_MergedSkimmedV11_V10/"
regions=['signal', 'wj', 'tt','zj']

#outputdirname="Raman/AnalysisTuples_2016DataMC_V5/TTBar/"
inputprefix="--input-dir=root://cmsxrootd.hep.wisc.edu//store/user/khurana/Raman/Merged_Skimmed/"
cmsswpath="/afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_8_0_11"
exepath="/afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_8_0_11/src/MonoH/MonoHbb/"

fout = open("samplestorun.txt","w")

## 76 samples 

samples = '''V9 V9'''

samplesold='''ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-700_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-400_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph  
ZJetsToNuNu_HT-400To600_13TeV-madgraph ZJetsToNuNu_HT-400To600_13TeV-madgraph
ZJetsToNuNu_HT-200To400_13TeV-madgraph ZJetsToNuNu_HT-200To400_13TeV-madgraph
ZJetsToNuNu_HT-600To800_13TeV-madgraph ZJetsToNuNu_HT-600To800_13TeV-madgraph
ZJetsToNuNu_HT-1200To2500_13TeV-madgraph ZJetsToNuNu_HT-1200To2500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph
WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8 WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8
WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ZJetsToNuNu_HT-100To200_13TeV-madgraph ZJetsToNuNu_HT-100To200_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph
ZJetsToNuNu_HT-800To1200_13TeV-madgraph ZJetsToNuNu_HT-800To1200_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph
WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1 ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1
TT_TuneCUETP8M1_13TeV-powheg-pythia8 TT_TuneCUETP8M1_13TeV-powheg-pythia8
WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph
WW_TuneCUETP8M1_13TeV-pythia8 WW_TuneCUETP8M1_13TeV-pythia8
ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1 ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1
WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph
ZZ_TuneCUETP8M1_13TeV-pythia8 ZZ_TuneCUETP8M1_13TeV-pythia8
ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1 ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1
ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1 ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1
ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8 ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8
ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1 ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1
WZ_TuneCUETP8M1_13TeV-pythia8 WZ_TuneCUETP8M1_13TeV-pythia8
ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph
WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph
WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
MET MET
'''

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
