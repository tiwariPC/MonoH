
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math
ROOT.gROOT.SetBatch(True)
from MonoHbbQuantities import *
######################################
## set up running mode of the code.
######################################


usage = "usage: %prog [options] arg1 arg2"
parser = optparse.OptionParser(usage)

## data will be true if -d is passed and will be false if -m is passed
parser.add_option("-i", "--inputfile",  dest="inputfile")
parser.add_option("-a", "--analyze", action="store_true",  dest="analyze")
parser.add_option("-m", "--MLow", type=float,  dest="MLow")
parser.add_option("-M", "--MHigh", type=float,  dest="MHigh")
parser.add_option("-o", "--overlap", action="store_true",  dest="overlap")
parser.add_option("-e", "--efficiency", action="store_true",  dest="efficiency")
parser.add_option("-t", "--table", action="store_true",  dest="table")
parser.add_option("-P", "--OtherPlots", action="store_true",  dest="OtherPlots")




(options, args) = parser.parse_args()

print (options.MLow, options.MHigh)
massCutLow = options.MLow 
massCutHigh = options.MHigh
#print 'options = ',[options.inputfile]
inputfilename = options.inputfile

pathlist = inputfilename.split("/")
sizeoflist = len(pathlist)
rootfile='tmp'
if sizeoflist > 6: rootfile = pathlist[7]
textfile = rootfile+".txt"
outputdir='MonoHSamples/'
os.system('mkdir '+outputdir)

outfilename=rootfile+".root"
outfilename =outputdir+'/'+outfilename

#outfilename ='scanningHistograms_Hotline_2fbInv.root'

#inputfilename = 'NCUGlobalTuples_3.root'
debug = False 

def AnalyzeDataSet():
    ## Input rootfile name
    rootfilename = inputfilename
    f = TFile(rootfilename,'READ')
    skimmedTree = f.Get('tree/treeMaker')
    NEntries = skimmedTree.GetEntries()
    npass = 0
    #print [rootfilename, NEntries]
    cutStatus={'total':NEntries}
    
    cutStatus['trigger'] = 0
    cutStatus['filter'] = 0
    cutStatus['pfmet'] =  0
    cutStatus['HiggsID'] = 0
    cutStatus['HMass'] = 0
    cutStatus['btag'] = 0
    cutStatus['dphi'] = 0
    cutStatus['ThinJetVeto'] = 0
    cutStatus['bVeto'] = 0
    cutStatus['eleveto'] = 0
    cutStatus['muveto'] = 0
    cutStatus['tauveto'] = 0
    
    allquantitiesBoosted            = MonoHbbQuantities(outfilename)
    allquantitiesBoosted.defineHisto()

    
    for ievent in range(NEntries):
    #for ievent in range(501):

        skimmedTree.GetEntry(ievent)
        
        ## Get all relevant branches
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Extract branches
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        run                        = skimmedTree.__getattr__('runId')
        lumi                       = skimmedTree.__getattr__('lumiSection')
        event                      = skimmedTree.__getattr__('eventId')

        #if event != 4126: continue                                
        #if lumi  != 42: continue                                
        #print ("run,lumi,event")
        trigName                   = skimmedTree.__getattr__('hlt_trigName')
        trigResult                 = skimmedTree.__getattr__('hlt_trigResult')
        filterName                 = skimmedTree.__getattr__('hlt_filterName')
        filterResult               = skimmedTree.__getattr__('hlt_filterResult')
                                   
        pfMet                      = skimmedTree.__getattr__('pfMetCorrPt')
        pfMetPhi                   = skimmedTree.__getattr__('pfMetCorrPhi')
        
        nFATJets                   = skimmedTree.__getattr__('FATnJet')
        fatjetP4                   = skimmedTree.__getattr__('FATjetP4')
        fatjetPRmassL2L3Corr       = skimmedTree.__getattr__('FATjetPRmassL2L3Corr')
        nSubSoftDropJet            = skimmedTree.__getattr__('FATnSubSDJet')
        subjetSDCSV                = skimmedTree.__getattr__('FATsubjetSDCSV')
        subjetSDPx                 = skimmedTree.__getattr__('FATsubjetSDPx')
        subjetSDPy                 = skimmedTree.__getattr__('FATsubjetSDPy')
        subjetSDPz                 = skimmedTree.__getattr__('FATsubjetSDPz')
        subjetSDE                  = skimmedTree.__getattr__('FATsubjetSDE')
        passFatJetTightID          = skimmedTree.__getattr__('FATjetPassIDTight')
        
        nTHINJets                  = skimmedTree.__getattr__('THINnJet')
        thinjetP4                  = skimmedTree.__getattr__('THINjetP4')
        thinJetCSV                 = skimmedTree.__getattr__('THINjetCISVV2')
        passThinJetLooseID         = skimmedTree.__getattr__('THINjetPassIDLoose')
        passThinJetPUID            = skimmedTree.__getattr__('THINisPUJetID')
        
        nEle                       = skimmedTree.__getattr__('nEle')
        eleP4                      = skimmedTree.__getattr__('eleP4')
        eleIsPassLoose             = skimmedTree.__getattr__('eleIsPassLoose')
        
        nMu                        = skimmedTree.__getattr__('nMu')
        muP4                       = skimmedTree.__getattr__('muP4')
        isLooseMuon                = skimmedTree.__getattr__('isLooseMuon')
        muChHadIso                 = skimmedTree.__getattr__('muChHadIso')
        muNeHadIso                 = skimmedTree.__getattr__('muNeHadIso')
        muGamIso                   = skimmedTree.__getattr__('muGamIso')
        muPUPt                     = skimmedTree.__getattr__('muPUPt')
        
        nTau                       = skimmedTree.__getattr__('HPSTau_n')
        tauP4                      = skimmedTree.__getattr__('HPSTau_4Momentum')
        isDecayModeFinding         = skimmedTree.__getattr__('disc_decayModeFinding')
        passLooseTauIso            = skimmedTree.__getattr__('disc_byLooseIsolationMVA3oldDMwLT')
        HiggsInfo_sorted           = []
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Trigger selection
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        itrig_=0; trig1 = False; trig2 = False;
        trig1 = CheckFilter(trigName, trigResult, 'HLT_PFMET170_NoiseCleaned')
        trig2 = CheckFilter(trigName, trigResult, 'HLT_PFMET90_PFMHT90_')
        #trigstatus =  trig1 | trig2
        trigstatus = True
        if trigstatus == False : continue
        cutStatus['trigger'] += 1
            
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Filter selection
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        filterstatus = False
        filter1 = False; filter2 = False;filter3 = False;filter4 = False
        ifilter_=0
        filter1 = CheckFilter(filterName, filterResult, 'Flag_CSCTightHaloFilter')
        filter2 = CheckFilter(filterName, filterResult, 'Flag_CSCTightHaloFilter')
        filter3 = CheckFilter(filterName, filterResult, 'Flag_CSCTightHaloFilter')
        filter4 = CheckFilter(filterName, filterResult, 'Flag_CSCTightHaloFilter')
        #filterstatus =  filter1 | filter2 & filter3 & filter4
        filterstatus =  True
        #if filterstatus == False : continue 
        cutStatus['filter'] += 1

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## PFMET Selection
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------        
        pfmetstatus = ( pfMet > 170.0 )
        if pfmetstatus == False : continue 
        cutStatus['pfmet'] += 1
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Fat-Jet Selection
        ## Higgs Tagging
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        '''
        if nFATJets>0 :
            print nFATJets, fatjetPRmassL2L3Corr[0], nSubSoftDropJet[0],  bool(passFatJetTightID[0]), fatjetP4[0].Pt(), fatjetP4[0].M()
            if nSubSoftDropJet > 0:
                print subjetSDE[0][0], subjetSDCSV[0][0], subjetSDPx[0][0], subjetSDPy[0][0], subjetSDPz[0][0]
        '''
        ## list comprehensation
        ## y = [s for s in x if len(s) == 2]
        #''' boosted higgs tagging 
        HIndex = -1
        HThinIndex = -1
        nsubjetstatus = False
        higgstag = False
        for ifatjet in range(nFATJets):
            if fatjetP4[ifatjet].Pt() > 200.0  : 
                if abs(fatjetP4[ifatjet].Eta())  < 2.4 : 
                    if (bool(passFatJetTightID[ifatjet]) == True) : 
                        HIndex = ifatjet 
                        break
    
        if HIndex > -1 :
            cutStatus['HiggsID'] += 1
            if (fatjetPRmassL2L3Corr[HIndex] > massCutLow) & ( pfMet > 200.0 ): 
                if fatjetPRmassL2L3Corr[HIndex] < massCutHigh : 
                    fatJetMassStatus = True
                    cutStatus['HMass'] += 1
                    nSubBJet=0;
                    for isj in range(nSubSoftDropJet[HIndex]):
                        if subjetSDCSV[HIndex][isj] > 0.46 : 
                            nSubBJet = nSubBJet + 1
        
                    if nSubBJet>1 : 
                        nsubjetstatus = True
                        cutStatus['btag'] += 1
    
        if nsubjetstatus: 
            print "this is boosted regime"
        else:   
        #if True:
            ''' resolved Higgs boson tagging 
            '''    
            HPtVec=[]
            HMassVec=[]
            pairindex=[]
            HiggsInfo=[]
            for ithinjet in range(nTHINJets):
                j1 = thinjetP4[ithinjet]
                if (j1.Pt() > 30.0)&(abs(j1.Eta())<2.4)&(bool(passThinJetLooseID[ithinjet])==True)&(bool(passThinJetPUID[ithinjet]) == True) & (thinJetCSV[ithinjet] > 0.8):   
                    for jthinjet in range(nTHINJets):
                        if (jthinjet != ithinjet ) & ( jthinjet > ithinjet ) & (jthinjet < nTHINJets) : 
                            j2 = thinjetP4[jthinjet]
                            if (j2.Pt() > 30.0) & (abs(j2.Eta()) <2.4) & (bool(passThinJetLooseID[jthinjet]))&(bool(passThinJetPUID[jthinjet]))&(thinJetCSV[jthinjet] > 0.8) :
                                
                                Hpt = (j1 + j2 ).Pt()
                                HMass = (j1 + j2 ).M()
                                #print (Hpt, HMass)
                                HPtVec.append(Hpt)
                                HMassVec.append(HMass)
                                pair=[]
                                pair.append(ithinjet); pair.append(jthinjet)
                                pairindex.append(pair)
                                p =[ithinjet, jthinjet, HMass, Hpt]
                                HiggsInfo.append(p)

            HiggsInfo_sorted = sorted (HiggsInfo, key=lambda student: student[3], reverse=True)   
            if len(HiggsInfo_sorted) > 0: HThinIndex = len(HiggsInfo_sorted) 
            #print "student=",HiggsInfo_sorted
            

            if HThinIndex > 0:
                mass_ = HiggsInfo_sorted[0][2]
                pt_   = HiggsInfo_sorted[0][3]
                if (mass_ > 100.) & (mass_ < 150.):
                    cutStatus['HMass'] += 1
                    if (pt_>150.): 
                        cutStatus['btag'] += 1
                        higgstag = True
            ''' resolved Higgs boson tagging 
            '''
        ####
        if nsubjetstatus == True : isboosted = True #; print "this is boosted"
        else : isboosted = False
        isresolved = False
        if  (higgstag): isresolved = True;
        else : isresolved = False
        
        if ( isboosted | isresolved ) == False: continue 
        #if ( isresolved ) == False: continue 
        
        #if (nsubjetstatus == False) & (HThinIndex < 1) : continue 
        #if  (HThinIndex < 1) : continue 
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Delta Phi
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        nGoodTHINJets = 0
        nGoodTHINBJets = 0
        jetIndex = -1
        dphiVec=[]
        
        for ijet in range(nTHINJets):
            p4_j = thinjetP4[ijet]
            #print (ijet, DeltaR(p4_j, fatjetP4[HIndex]), p4_j.Pt() , abs(p4_j.Eta()), bool(passThinJetLooseID[ijet]), bool(passThinJetPUID[ijet]), thinJetCSV[ijet])
            if p4_j.Pt() < 30 : continue
            if abs(p4_j.Eta())>4.5 : continue
            if bool(passThinJetLooseID[ijet]) == False : continue
            if bool(passThinJetPUID[ijet]) == False : continue 
            
            if isboosted : 
                #print (isboosted,isresolved)
                if DeltaR(p4_j, fatjetP4[HIndex])  > 0.8:
                    nGoodTHINJets += 1
                    jetIndex=ijet
            if isresolved :
                jet1 = HiggsInfo_sorted[0][0]
                jet2 = HiggsInfo_sorted[0][1]
                if DeltaR(p4_j, thinjetP4[jet1])  > 0.4:
                    if DeltaR(p4_j, thinjetP4[jet2])  > 0.4:
                        nGoodTHINJets += 1
                        jetIndex=ijet
            #print "nGoodTHINJets = ",nGoodTHINJets
            #print ((p4_j.Eta()>2.4), thinJetCSV[ijet]<0.46 )
            
            if abs(p4_j.Eta())>2.4 : continue
            dphi = Phi_mpi_pi(pfMetPhi - p4_j.Phi())
            #print dphi
            dphiVec.append(abs(dphi))
            
            if thinJetCSV[ijet]<0.46 : continue
            if isboosted :
                if DeltaR(p4_j, fatjetP4[HIndex])  > 0.8:
                    nGoodTHINBJets = nGoodTHINBJets + 1
            if isresolved : 
                #print "jet number", ijet
                jet1 = HiggsInfo_sorted[0][0]
                jet2 = HiggsInfo_sorted[0][1]
                if DeltaR(p4_j, thinjetP4[jet1])  > 0.4:
                    if DeltaR(p4_j, thinjetP4[jet2])  > 0.4:
                        nGoodTHINBJets = nGoodTHINBJets + 1
            
            
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## min DPhi
        ## nT<hinJets
        ## b-jet Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        if len(dphiVec) > 0:  
            #print min(dphiVec) 
            if min(dphiVec) < 0.4 : continue 
        cutStatus['dphi'] += 1
        if nGoodTHINJets > 1: continue 
        cutStatus['ThinJetVeto'] += 1
        if nGoodTHINBJets > 0: continue 
        cutStatus['bVeto'] += 1
        
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Electron Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        myEles=[]
        for iele in range(nEle):
            if eleP4[iele].Pt() < 10 : continue
            if abs(eleP4[iele].Eta()) >2.5: continue
            if bool(eleIsPassLoose[iele]) == False : continue
            myEles.append(iele)

        if len(myEles) > 0 : continue
        cutStatus['eleveto'] += 1
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Muon Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        myMuos = []
        for imu in range(nMu):
            if muP4[imu].Pt()<10 : continue
            if abs(muP4[imu].Eta()) > 2.4  : continue
            if  bool(isLooseMuon[imu]) == False  : continue
            relPFIso = (muChHadIso[imu]+ max(0., muNeHadIso[imu] + muGamIso[imu] - 0.5*muPUPt[imu]))/muP4[imu].Pt();
            if relPFIso>0.4 : continue
            myMuos.append(imu)
        if len(myMuos) > 0: continue
        cutStatus['muveto'] += 1
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Tau Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        myTaus=[]
        for itau in range(nTau):
            #print ("tau properties", tauP4[itau].Pt(), abs(tauP4[itau].Eta()), bool(isDecayModeFinding[itau]), bool(passLooseTauIso[itau]))
            if tauP4[itau].Pt()<20 : continue
            if abs(tauP4[itau].Eta())>2.3 : continue
            if bool(isDecayModeFinding[itau]) == False : continue
            if bool(passLooseTauIso[itau]) == False : continue
            myTaus.append(itau);
        
        if len(myTaus)>0 : continue
        cutStatus['tauveto'] += 1
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Photon Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----to be added in future---------------------------------------------------------------------------------------------------------------------------------------
        print (run,lumi,event)
        
        npass = npass +1
        
        ##-------------------------------------------------------------------------------------------------
        ##-------------------------------------------------------------------------------------------------
        ##------------fill all variables needed for further processing-------------------------------------
        ##-------------------------------------------------------------------------------------------------
        ##-------------------------------------------------------------------------------------------------
        regime = False
        if isboosted: regime = True
        if isresolved: regime = False
        #print (isboosted,isresolved, regime)

        
        allquantitiesBoosted.regime     = regime
        allquantitiesBoosted.met        = pfMet
        if regime:      allquantitiesBoosted.mass            = fatjetPRmassL2L3Corr[HIndex]
        if not regime:  allquantitiesBoosted.mass            = HiggsInfo_sorted[0][2]
        
        #print (allquantitiesBoosted.regime, allquantitiesBoosted.met,allquantitiesBoosted.mass )
        allquantitiesBoosted.FillHisto()

    print cutStatus
    #print "npass = ", npass
    
    allquantitiesBoosted.WriteHisto()
    print " efficiency = ", float(npass/float(NEntries))
    f = open('efficiencyfiles/'+textfile, 'w')
    f.write(str(float(npass/float(NEntries))))
    f.close()



        
def CheckFilter(filterName, filterResult,filtercompare):
    ifilter_=0
    filter1 = False
    for ifilter in filterName:
        filter1 = (ifilter.find(filtercompare) != -1)  & (bool(filterResult[ifilter_]) == True)   
        if filter1: break
        ifilter_ = ifilter_ + 1
    return filter1





######################################
######################################
######################################
def MakeTable():
    print "called MakeTable"
    files= [inputfilename]
    legend=legendTemplate
    prefix="V_met_"
    effnamelist = [prefix + ihisto  for ihisto in namelist]
    inputfile={}
    histList=[]
    for ifile_ in range(len(files)):
        print ("opening file  "+files[ifile_])
        inputfile[ifile_] = TFile( files[ifile_] )
        print "fetching histograms"
        for ihisto_ in range(len(effnamelist)):
            histo = inputfile[ifile_].Get(effnamelist[ihisto_])
            histList.append(histo)
    
    for ih in range(len(histList)):
        eff = ("%0.4f" % float(histList[ih].Integral()/histList[0].Integral()))
        toprint =  legendTemplate[ih] + " & " + str(eff) + " \\\\"
        print toprint


def DeltaR(p4_1, p4_2):
    eta1 = p4_1.Eta()
    eta2 = p4_2.Eta()
    eta = eta1 - eta2
    eta_2 = eta * eta
    
    phi1 = p4_1.Phi()
    phi2 = p4_2.Phi()
    phi = Phi_mpi_pi(phi1-phi2)
    phi_2 = phi * phi

    return math.sqrt(eta_2 + phi_2)
    
def Phi_mpi_pi(x):
    kPI = 3.14159265358979323846
    kTWOPI = 2 * kPI
    
    while (x >= kPI): x = x - kTWOPI;
    while (x < -kPI): x = x + kTWOPI;
    return x;
    
if __name__ == "__main__":
    ## analyze the tree and make histograms and all the 2D plots and Efficiency plots. 
    if options.analyze:
        AnalyzeDataSet()
    
    
    
