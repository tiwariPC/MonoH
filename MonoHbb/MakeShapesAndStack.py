### 
###
# Created By : Raman Khurana
# Date       : 03:March:2016
# Time       : 22:20:30 
###
###

## import user defined modules
#from Utils import *
import Utils
import sys
#sys.argv.append( '-b-' )

## this imports basics
from array import array
from ROOT import gROOT, gSystem, gStyle, gRandom
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph, TGaxis
from ROOT import TStyle, TCanvas, TPad, TLegend, TLatex, TText
import ROOT

ROOT.gROOT.SetBatch(True)

import sys, optparse

###################################
## set up running mode of the code. 
###################################
usage = "usage: %prog [options] arg1 arg2"
parser = optparse.OptionParser(usage)
## data will be true if -d is passed and will be false if -m is passed
parser.add_option("-d", "--data", action="store_true",  dest="data")
parser.add_option("-m", "--mc", action="store_false",  dest="data")

(options, args) = parser.parse_args()

print 'options = ',[options.data]



from ROOT import *


#########################################
#
# Set Weights for each sample
#
#########################################

Utils.setweights()
debug_=False




####################################################################################################################
## weighted and summed over all samples histograms for a given physics process. 
####################################################################################################################
def MakeRooDataHist(phys_process, histname, fullrange_=False):
    #filedata = TFile('Histograms_CMSSW76X_BaseLine_METSys_V12/AnalysisHistograms_V0/'+Utils.samples['TT']['files'][0], 'READ')
    filedata = TFile('Histograms_CMSSW76X_2DScanV_V1/AnalysisHistograms_V0/'+Utils.samples['TT']['files'][0], 'READ')
    hist_met_ = filedata.Get('histfacFatJet_ZLight/h_MET0_Nominal')
    hist_met_.Sumw2()
    #print hist_met_.Integral()
    hist_met_.SetDirectory(0)
    TH1.AddDirectory(0)

    hist_met_.Scale(0.0)
    iweight = 0
    for irootfile in Utils.samples[phys_process]['files']:
        file01 = TFile('Histograms_CMSSW76X_2DScanV_V1/AnalysisHistograms_V0/'+irootfile, 'READ')
        hist_ = file01.Get(histname)
        hist_.SetDirectory(0)
        TH1.AddDirectory(0)
        
        if phys_process != 'data_obs': hist_.Scale(Utils.samples[phys_process]['weight'][iweight])
        if phys_process == 'data_obs': hist_.Scale(1)
        
        hist_met_.Add(hist_)
        iweight = iweight + 1
        
        if debug_ :
            print "before ",hist_.Integral()
    h = hist_met_
    return h

############################################################
## background RooDataHist taken from input Rootfiles. 
## to fix the normalisation and pdf of TT and VV and ZH
############################################################

def WriteHistograms(nominalname, postfix, rootfilename, filemode='UPDATE'):
    weights=[]
    if debug_ : print "Top"
    h_tt    = MakeRooDataHist('TT', nominalname, True) 
    h_st    = MakeRooDataHist('ST', nominalname, True) 
    
    
    weight_  = Utils.samples['TT']['weight'][0]         ;  weights.append(weight_)
    weight_  = Utils.samples['VV']['weight'][0]         ;  weights.append(weight_)
    weight_  = Utils.samples['znunujets']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['wjets']['weight'][0]      ;  weights.append(weight_)
    weight_  = Utils.samples['ZH']['weight'][0]         ;  weights.append(weight_)

    h_tt.Add(h_st)
    h_tt.SetNameTitle('TT'+postfix,'TT')
    
    
    if debug_ : print "VV"
    h_VV    = MakeRooDataHist('VV', nominalname, True) 
    h_VV.SetNameTitle('DIBOSON'+postfix,'DIBOSON')
    
    if debug_ : print "ZNN"
    h_znn    = MakeRooDataHist('znunujets', nominalname, True) 
    h_znn.SetNameTitle('DYJets'+postfix,'DYJets')
    
    if debug_ : print "WJ"
    h_wj    = MakeRooDataHist('wjets', nominalname, True) 
    h_wj.SetNameTitle('WJets'+postfix,'WJets')
    
    if debug_ : print "ZH"
    h_zh    = MakeRooDataHist('ZH', nominalname, True) 
    h_zh.SetNameTitle('ZH'+postfix,'ZH')
    
    if debug_ : print "signals start"
    
    ## make a stack of the backgrounds
    if nominalname == 'MonoHFatJetSelection_JetAndLeptonVeto/h_MET0_Nominal':
        c1 = TCanvas()
        bkgStack = THStack ("bkgStack","bkgStack")
        h_zh.SetFillColor(1)
        h_VV.SetFillColor(2)
        h_tt.SetFillColor(3)
        h_znn.SetFillColor(4)
        h_wj.SetFillColor(5)
        
        bkgStack.Add(h_zh,'hist')
        bkgStack.Add(h_VV,'hist')
        bkgStack.Add(h_tt,'hist')
        bkgStack.Add(h_znn,'hist')
        bkgStack.Add(h_wj,'hist')
        
        bkgStack.Draw()
        c1.SaveAs('trystack.png')
    
    
    weight_  = Utils.samples['signal600_300']['weight'][0]   ; weights.append(weight_)
    weight_  = Utils.samples['signal800_300']['weight'][0]   ; weights.append(weight_)
    weight_  = Utils.samples['signal1000_300']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1200_300']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1400_300']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1700_300']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal2000_300']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal2500_300']['weight'][0]  ;  weights.append(weight_)
    
    h_600_300 = MakeRooDataHist('signal600_300', nominalname, True)
    h_600_300.SetNameTitle('monoHbbM600_300'+postfix,'monoHbbM600_300')
    
    h_800_300 = MakeRooDataHist('signal800_300', nominalname, True)
    h_800_300.SetNameTitle('monoHbbM800_300'+postfix,'monoHbbM800_300')
    
    h_1000_300 = MakeRooDataHist('signal1000_300', nominalname, True)
    h_1000_300.SetNameTitle('monoHbbM1000_300'+postfix,'monoHbbM1000_300')

    h_1200_300 = MakeRooDataHist('signal1200_300', nominalname, True)
    h_1200_300.SetNameTitle('monoHbbM1200_300'+postfix,'monoHbbM1200_300')
    
    h_1400_300 = MakeRooDataHist('signal1400_300', nominalname, True)
    h_1400_300.SetNameTitle('monoHbbM1400_300'+postfix,'monoHbbM1400_300')

    h_1700_300 = MakeRooDataHist('signal1700_300', nominalname, True)
    h_1700_300.SetNameTitle('monoHbbM1700_300'+postfix,'monoHbbM1700_300')
    
    h_2000_300 = MakeRooDataHist('signal2000_300', nominalname, True)
    h_2000_300.SetNameTitle('monoHbbM2000_300'+postfix,'monoHbbM2000_300')

    h_2500_300 = MakeRooDataHist('signal2500_300', nominalname, True)
    h_2500_300.SetNameTitle('monoHbbM2500_300'+postfix,'monoHbbM2500_300')

    
    weight_  = Utils.samples['signal600_400']['weight'][0]  ;   weights.append(weight_)
    weight_  = Utils.samples['signal800_400']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1000_400']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal1200_400']['weight'][0];    weights.append(weight_)
    weight_  = Utils.samples['signal1400_400']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal1700_400']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal2000_400']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal2500_400']['weight'][0] ;   weights.append(weight_)
    
    h_600_400 = MakeRooDataHist('signal600_400', nominalname, True)
    h_600_400.SetNameTitle('monoHbbM600_400'+postfix,'monoHbbM600_400')

    h_800_400 = MakeRooDataHist('signal800_400', nominalname, True)
    h_800_400.SetNameTitle('monoHbbM800_400'+postfix,'monoHbbM800_400')

    h_1000_400 = MakeRooDataHist('signal1000_400', nominalname, True)
    h_1000_400.SetNameTitle('monoHbbM1000_400'+postfix,'monoHbbM1000_400')

    h_1200_400 = MakeRooDataHist('signal1200_400', nominalname, True)
    h_1200_400.SetNameTitle('monoHbbM1200_400'+postfix,'monoHbbM1200_400')

    h_1400_400 = MakeRooDataHist('signal1400_400', nominalname, True)
    h_1400_400.SetNameTitle('monoHbbM1400_400'+postfix,'monoHbbM1400_400')

    h_1700_400 = MakeRooDataHist('signal1700_400', nominalname, True)
    h_1700_400.SetNameTitle('monoHbbM1700_400'+postfix,'monoHbbM1700_400')

    h_2000_400 = MakeRooDataHist('signal2000_400', nominalname, True)
    h_2000_400.SetNameTitle('monoHbbM2000_400'+postfix,'monoHbbM2000_400')

    h_2500_400 = MakeRooDataHist('signal2500_400', nominalname, True)
    h_2500_400.SetNameTitle('monoHbbM2500_400'+postfix,'monoHbbM2500_400')
    
    
    weight_  = Utils.samples['signal800_500']['weight'][0]   ; weights.append(weight_)
    weight_  = Utils.samples['signal1000_500']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1200_500']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1400_500']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1700_500']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal2000_500']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal2500_500']['weight'][0]  ;  weights.append(weight_)
    
    h_800_500 = MakeRooDataHist('signal800_500', nominalname, True)
    h_800_500.SetNameTitle('monoHbbM800_500'+postfix,'monoHbbM800_500')

    h_1000_500 = MakeRooDataHist('signal1000_500', nominalname, True)
    h_1000_500.SetNameTitle('monoHbbM1000_500'+postfix,'monoHbbM1000_500')

    h_1200_500 = MakeRooDataHist('signal1200_500', nominalname, True)
    h_1200_500.SetNameTitle('monoHbbM1200_500'+postfix,'monoHbbM1200_500')

    h_1400_500 = MakeRooDataHist('signal1400_500', nominalname, True)
    h_1400_500.SetNameTitle('monoHbbM1400_500'+postfix,'monoHbbM1400_500')

    h_1700_500 = MakeRooDataHist('signal1700_500', nominalname, True)
    h_1700_500.SetNameTitle('monoHbbM1700_500'+postfix,'monoHbbM1700_500')

    h_2000_500 = MakeRooDataHist('signal2000_500', nominalname, True)
    h_2000_500.SetNameTitle('monoHbbM2000_500'+postfix,'monoHbbM2000_500')

    h_2500_500 = MakeRooDataHist('signal2500_500', nominalname, True)
    h_2500_500.SetNameTitle('monoHbbM2500_500'+postfix,'monoHbbM2500_500')

    
    weight_  = Utils.samples['signal800_600']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1000_600']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal1200_600']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal1400_600']['weight'][0];    weights.append(weight_)
    weight_  = Utils.samples['signal1700_600']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal2000_600']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal2500_600']['weight'][0] ;   weights.append(weight_)
    
    
    h_800_600 = MakeRooDataHist('signal800_600', nominalname, True)
    h_800_600.SetNameTitle('monoHbbM800_600'+postfix,'monoHbbM800_600')

    h_1000_600 = MakeRooDataHist('signal1000_600', nominalname, True)
    h_1000_600.SetNameTitle('monoHbbM1000_600'+postfix,'monoHbbM1000_600')

    h_1200_600 = MakeRooDataHist('signal1200_600', nominalname, True)
    h_1200_600.SetNameTitle('monoHbbM1200_600'+postfix,'monoHbbM1200_600')

    h_1400_600 = MakeRooDataHist('signal1400_600', nominalname, True)
    h_1400_600.SetNameTitle('monoHbbM1400_600'+postfix,'monoHbbM1400_600')

    h_1700_600 = MakeRooDataHist('signal1700_600', nominalname, True)
    h_1700_600.SetNameTitle('monoHbbM1700_600'+postfix,'monoHbbM1700_600')

    h_2000_600 = MakeRooDataHist('signal2000_600', nominalname, True)
    h_2000_600.SetNameTitle('monoHbbM2000_600'+postfix,'monoHbbM2000_600')

    h_2500_600 = MakeRooDataHist('signal2500_600', nominalname, True)
    h_2500_600.SetNameTitle('monoHbbM2500_600'+postfix,'monoHbbM2500_600')


    #weight_  = Utils.samples['signal800_700']['weight'][0]  ;  weights.append(weight_)
    #weight_  = Utils.samples['signal1000_700']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal1200_700']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1400_700']['weight'][0] ;   weights.append(weight_)
    weight_  = Utils.samples['signal1700_700']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal2000_700']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal2500_700']['weight'][0]  ;  weights.append(weight_)
    
    #h_600_700 = MakeRooDataHist('signal600_700', nominalname, True)
    #h_600_700.SetNameTitle('monoHbbM600_700'+postfix,'monoHbbM600_700')

    #h_800_700 = MakeRooDataHist('signal800_700', nominalname, True)
    #h_800_700.SetNameTitle('monoHbbM800_700'+postfix,'monoHbbM800_700')

    #h_1000_700 = MakeRooDataHist('signal1000_700', nominalname, True)
    #h_1000_700.SetNameTitle('monoHbbM1000_700'+postfix,'monoHbbM1000_700')

    h_1200_700 = MakeRooDataHist('signal1200_700', nominalname, True)
    h_1200_700.SetNameTitle('monoHbbM1200_700'+postfix,'monoHbbM1200_700')

    h_1400_700 = MakeRooDataHist('signal1400_700', nominalname, True)
    h_1400_700.SetNameTitle('monoHbbM1400_700'+postfix,'monoHbbM1400_700')

    h_1700_700 = MakeRooDataHist('signal1700_700', nominalname, True)
    h_1700_700.SetNameTitle('monoHbbM1700_700'+postfix,'monoHbbM1700_700')

    h_2000_700 = MakeRooDataHist('signal2000_700', nominalname, True)
    h_2000_700.SetNameTitle('monoHbbM2000_700'+postfix,'monoHbbM2000_700')

    h_2500_700 = MakeRooDataHist('signal2500_700', nominalname, True)
    h_2500_700.SetNameTitle('monoHbbM2500_700'+postfix,'monoHbbM2500_700')

    
    weight_  = Utils.samples['signal1000_800']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1200_800']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1400_800']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal1700_800']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal2000_800']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['signal2500_800']['weight'][0]  ;  weights.append(weight_)
    weights.append(1)
    if debug_: print weights
    
    h_1000_800 = MakeRooDataHist('signal1000_800', nominalname, True)
    h_1000_800.SetNameTitle('monoHbbM1000_800'+postfix,'monoHbbM1000_800')

    h_1200_800 = MakeRooDataHist('signal1200_800', nominalname, True)
    h_1200_800.SetNameTitle('monoHbbM1200_800'+postfix,'monoHbbM1200_800')

    h_1400_800 = MakeRooDataHist('signal1400_800', nominalname, True)
    h_1400_800.SetNameTitle('monoHbbM1400_800'+postfix,'monoHbbM1400_800')

    h_1700_800 = MakeRooDataHist('signal1700_800', nominalname, True)
    h_1700_800.SetNameTitle('monoHbbM1700_800'+postfix,'monoHbbM1700_800')

    h_2000_800 = MakeRooDataHist('signal2000_800', nominalname, True)
    h_2000_800.SetNameTitle('monoHbbM2000_800'+postfix,'monoHbbM2000_800')

    h_2500_800 = MakeRooDataHist('signal2500_800', nominalname, True)
    h_2500_800.SetNameTitle('monoHbbM2500_800'+postfix,'monoHbbM2500_800')


    if debug_ : print "signal end"
    h_data = TH1F()
    if filemode == 'RECREATE':
        if debug_ : print "data"
        #newname = nominalname.replace("_Nominal","")
        #if debug_ : print "-- newname = ", newname
        h_data = MakeRooDataHist('data_obs', nominalname, True)
        h_data.SetNameTitle('data_obs', 'data_obs')
        print "data integral = ",h_data.Integral()
        #bins=[200., 350., 500., 3000.]
        #h_data.Rebin(3,"data_obs", bins)
        
        
    fshape = TFile(rootfilename+'.root',filemode)
    fshape.cd()
    
    h_all=[]
    h_all.append(h_tt)
    h_all.append(h_VV)
    h_all.append(h_znn)
    h_all.append(h_wj)
    h_all.append(h_zh)
    h_all.append(h_600_300)
    h_all.append(h_800_300)
    h_all.append(h_1000_300)
    h_all.append(h_1200_300)
    h_all.append(h_1400_300)
    h_all.append(h_1700_300)
    h_all.append(h_2000_300)
    h_all.append(h_2500_300)
    h_all.append(h_600_400)
    h_all.append(h_800_400)
    h_all.append(h_1000_400)
    h_all.append(h_1200_400)
    h_all.append(h_1400_400)
    h_all.append(h_1700_400)
    h_all.append(h_2000_400)
    h_all.append(h_2500_400)
    h_all.append(h_800_500)
    h_all.append(h_1000_500)
    h_all.append(h_1200_500)
    h_all.append(h_1400_500)
    h_all.append(h_1700_500)
    h_all.append(h_2000_500)
    h_all.append(h_2500_500)
    h_all.append(h_800_600)
    h_all.append(h_1000_600)
    h_all.append(h_1200_600)
    h_all.append(h_1400_600)
    h_all.append(h_1700_600)
    h_all.append(h_2000_600)
    h_all.append(h_2500_600)
    h_all.append(h_1200_700)
    h_all.append(h_1400_700)
    h_all.append(h_1700_700)
    h_all.append(h_2000_700)
    h_all.append(h_2500_700)
    h_all.append(h_1000_800)
    h_all.append(h_1200_800)
    h_all.append(h_1400_800)
    h_all.append(h_1700_800)
    h_all.append(h_2000_800)
    h_all.append(h_2500_800)

    
    if postfix =='':
        yieldfile = open(rootfilename+'.txt','w')
    ihist = 0
    for ih in h_all:
        ih.Write()
        error_ = 0.0
        if postfix =='': error_ = weights[ihist] * TMath.Sqrt(ih.Integral())
        if postfix =='': yieldfile.write(ih.GetName()+' '+str(ih.Integral())+' '+str(error_)+'\n')
        ihist = ihist+1

    if postfix =='': 
        if filemode == 'RECREATE': 
            yieldfile.write('DATA'+' '+str(h_data.Integral())+' '+str(0)+'\n')
        yieldfile.close()

    '''
    h_tt.Write()
    h_VV.Write()
    h_znn.Write()
    h_wj.Write()
    h_zh.Write()
    h_600_300.Write()
    h_800_300.Write()
    h_1000_300.Write()
    h_1200_300.Write()
    h_1400_300.Write()
    h_1700_300.Write()
    h_2000_300.Write()
    h_2500_300.Write()
    h_600_400.Write()
    h_800_400.Write()
    h_1000_400.Write()
    #h_1200_400.Write()
    h_1400_400.Write()
    h_1700_400.Write()
    h_2000_400.Write()
    h_2500_400.Write()
    #h_600_500.Write()
    h_800_500.Write()
    h_1000_500.Write()
    h_1200_500.Write()
    h_1400_500.Write()
    h_1700_500.Write()
    h_2000_500.Write()
    h_2500_500.Write()
    #h_600_600.Write()
    h_800_600.Write()
    h_1000_600.Write()
    h_1200_600.Write()
    #h_1400_600.Write()
    h_1700_600.Write()
    h_2000_600.Write()
    h_2500_600.Write()
    #h_600_700.Write()
    #h_800_700.Write()
    #h_1000_700.Write()
    h_1200_700.Write()
    #h_1400_700.Write()
    h_1700_700.Write()
    h_2000_700.Write()
    h_2500_700.Write()
    #h_600_800.Write()
    #h_800_800.Write()
    h_1000_800.Write()
    h_1200_800.Write()
    h_1400_800.Write()
    h_1700_800.Write()
    h_2000_800.Write()
    h_2500_800.Write()
   '''
    if filemode == 'RECREATE':
        h_data.Write()
        #data_obs.Write()
    

def HistogramsOneDir(WhichRegion = 'MonoHFatJetSelection_JetAndLeptonVeto/'):
    print "--------For h_MET0_Nominal--------- "

    WriteHistograms(WhichRegion+'/h_MET0_Nominal','',WhichRegion,'RECREATE')
    '''WriteHistograms(WhichRegion+'/h_MET0_muRUp','_CMS_monoHbb_scaleRUp',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_muRDown','_CMS_monoHbb_scaleRDown',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_muFUp','_CMS_monoHbb_scaleFUp',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_muFDown','_CMS_monoHbb_scaleFDown',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_EWKUp','_CMS_monoHbb_ewkUp',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_EWKDown','_CMS_monoHbb_ewkDown',WhichRegion)
    '''
    for ipdf in range(101):
        hname = 'h_MET0_'+str(ipdf)
        WriteHistograms(WhichRegion+'/'+hname, '_PDF'+str(ipdf),WhichRegion)
    return 0


print "------------For MonoHFatJetSelection_JetAndLeptonVeto--------------"
HistogramsOneDir('MonoHFatJetSelection_JetAndLeptonVeto')
HistogramsOneDir('histfacFatJet_ZLight')
HistogramsOneDir('histfacFatJet_WHeavy')
