#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math
import numpy as numpy_

ROOT.gROOT.LoadMacro("Loader.h+")

## When not running on farmout
inputfilename= 'zj100.txt'
outfilename= 'tmp.root'


## When running on farmout
#inputfilename = os.environ['INPUT']                                                                                                                                                 
#outfilename   = os.environ['OUTPUT']                                                                                                                                                


skimmedTree = TChain("tree/treeMaker")

infile = open(inputfilename)
for ifile in infile: 
    skimmedTree.Add(ifile.rstrip())
    

#if not isfarmout:
#    skimmedTree.Add(inputfilename)
#    samplename = WhichSample(inputfilename)
    
def AnalyzeDataSet():
    
   ## Input rootfile name
    
    #rootfilename = inputfilename
    #print (rootfilename,inputfilename)
    #f = TFile(rootfilename,'READ')
    #skimmedTree = f.Get('tree/treeMaker')
    NEntries = skimmedTree.GetEntries()
    #NEntries = 20000
        
    h_total = TH1F('h_total','h_total',2,0,2)
    h_total_mcweight = TH1F('h_total_mcweight','h_total_mcweight',2,0,2)
    
    outfile = TFile(outfilename,'RECREATE')
    
    outTree = TTree( 'outTree', 'tree branches' )
    #st_runId            = array( 'L', [ 0 ] )
    st_runId            = numpy_.zeros(1, dtype=int)
    st_lumiSection      = array( 'L', [ 0 ] )
    st_eventId          = array( 'L', [ 0 ] )
    st_pfMetCorrPt      = array( 'f', [ 0. ] )
    st_pfMetCorrPhi     = array( 'f', [ 0. ] )
    st_isData           = array( 'b', [ False ] )
    st_nFatJets         = array( 'L', [ 0 ] )
    
        
    
    maxn = 10
    st_FATjetP4 = ROOT.std.vector('TLorentzVector')()
    st_FATjetPRmassL2L3Corr = ROOT.std.vector('float')()
    st_FATnSubSDJet = ROOT.std.vector('int')()
    st_subjetSDCSV  = ROOT.std.vector('std::vector<float>')() 
    st_subjetPt     = ROOT.std.vector('std::vector<float>')()
    st_subjetEta    = ROOT.std.vector('std::vector<float>')()
    st_subjetFlav   = ROOT.std.vector('std::vector<float>')()
    
    
    st_THINnJet = array( 'L', [ 0 ] ) #ROOT.std.vector('int')()
    st_THINjetP4 = ROOT.std.vector('TLorentzVector')()
    st_THINjetCISVV2 = ROOT.std.vector('float')()
    st_THINjetHadronFlavor = ROOT.std.vector('int')()
    
    st_nEle= array( 'L', [ 0 ] ) #ROOT.std.vector('int')()
    st_eleP4= ROOT.std.vector('TLorentzVector')()
    
    st_nMu= array( 'L', [ 0 ] ) #ROOT.std.vector('int')()
    st_muP4= ROOT.std.vector('TLorentzVector')()
    
    st_HPSTau_n= array( 'L', [ 0 ] ) #ROOT.std.vector('int')()
    st_HPSTau_4Momentum= ROOT.std.vector('TLorentzVector')()
    
    mcweight = array( 'f', [ 0 ] )
    st_pu_nTrueInt= array( 'f', [ 0 ] ) #ROOT.std.vector('std::vector<float>')()
    
    st_nGenPar = array( 'L', [ 0 ] ) 
    st_genParId = ROOT.std.vector('int')()
    st_genMomParId = ROOT.std.vector('int')()
    st_genParSt = ROOT.std.vector('int')()
    st_genParP4 = ROOT.std.vector('TLorentzVector')()
    
           
    outTree.Branch( 'st_runId', st_runId , 'st_runId/L')
    outTree.Branch( 'st_lumiSection', st_lumiSection , 'st_lumiSection/L')
    outTree.Branch( 'st_eventId',  st_eventId, 'st_eventId/L')
    outTree.Branch( 'st_pfMetCorrPt', st_pfMetCorrPt , 'st_pfMetCorrPt/F')
    outTree.Branch( 'st_pfMetCorrPhi', st_pfMetCorrPhi , 'st_pfMetCorrPhi/F')
    outTree.Branch( 'st_isData', st_isData , 'st_isData/O')
    
    outTree.Branch( 'st_nFatJets',st_nFatJets, 'st_nFatJets/L')
    outTree.Branch( 'st_FATjetP4', st_FATjetP4)
    outTree.Branch( 'st_FATjetPRmassL2L3Corr', st_FATjetPRmassL2L3Corr) 
    outTree.Branch( 'st_FATnSubSDJet',st_FATnSubSDJet)
    outTree.Branch( 'st_subjetSDCSV', st_subjetSDCSV)
    outTree.Branch( 'st_subjetPt', st_subjetPt)
    outTree.Branch( 'st_subjetEta', st_subjetEta)
    outTree.Branch( 'st_subjetFlav', st_subjetFlav)
    
    outTree.Branch( 'st_THINnJet',st_THINnJet, 'st_THINnJet/L' ) 
    outTree.Branch( 'st_THINjetP4',st_THINjetP4 ) 
    outTree.Branch( 'st_THINjetCISVV2',st_THINjetCISVV2 ) 
    outTree.Branch( 'st_THINjetHadronFlavor',st_THINjetHadronFlavor ) 
    
    outTree.Branch( 'st_nEle',st_nEle , 'st_nEle/L') 
    outTree.Branch( 'st_eleP4',st_eleP4 ) 
    
    outTree.Branch( 'st_nMu',st_nMu , 'st_nMu/L') 
    outTree.Branch( 'st_muP4',st_muP4 ) 
    
    outTree.Branch( 'st_HPSTau_n', st_HPSTau_n, 'st_HPSTau_n/L') 
    outTree.Branch( 'st_HPSTau_4Momentum', st_HPSTau_4Momentum) 
    
    outTree.Branch( 'st_pu_nTrueInt', st_pu_nTrueInt, 'st_pu_nTrueInt/L') 
    outTree.Branch( 'mcweight', mcweight, 'mcweight/F')
    outTree.Branch( 'st_nGenPar',st_nGenPar,'st_nGenPar/L' )  #nGenPar/I
    outTree.Branch( 'st_genParId',st_genParId )  #vector<int>
    outTree.Branch( 'st_genMomParId',st_genMomParId ) 
    outTree.Branch( 'st_genParSt',st_genParSt ) 
    outTree.Branch( 'st_genParP4', st_genParP4) 

    

    '''
    outTree.Branch( '',  , '')
    outTree.Branch( '',  , '')
    '''
    for ievent in range(NEntries):
        
        
#for ievent in range(501):
        skimmedTree.GetEntry(ievent)
        ## Get all relevant branches
        run                        = skimmedTree.__getattr__('runId')
        lumi                       = skimmedTree.__getattr__('lumiSection')
        event                      = skimmedTree.__getattr__('eventId')
        print (run,lumi,event)
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
        subjetHadronFlavor         = skimmedTree.__getattr__('FATsubjetSDHadronFlavor')

        nTHINJets                  = skimmedTree.__getattr__('THINnJet')
        thinjetP4                  = skimmedTree.__getattr__('THINjetP4')
        thinJetCSV                 = skimmedTree.__getattr__('THINjetCISVV2')
        passThinJetLooseID         = skimmedTree.__getattr__('THINjetPassIDLoose')
        passThinJetPUID            = skimmedTree.__getattr__('THINisPUJetID')
        THINjetHadronFlavor        = skimmedTree.__getattr__('THINjetHadronFlavor')
        
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
        isData                     = skimmedTree.__getattr__('isData')
        mcWeight                   = skimmedTree.__getattr__('mcWeight')
        pu_nTrueInt                = int(skimmedTree.__getattr__('pu_nTrueInt'))
        
        nGenPar                    = skimmedTree.__getattr__('nGenPar')
        genParId                   = skimmedTree.__getattr__('genParId')
        genMomParId                = skimmedTree.__getattr__('genMomParId')
        genParSt                   = skimmedTree.__getattr__('genParSt')
        genParP4                   = skimmedTree.__getattr__('genParP4')
        #= skimmedTree.__getattr__('')
        #= skimmedTree.__getattr__('')
             
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # MC Weights ----------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        mcweight[0] = 0.0 
        if isData==1:   mcweight[0] =  1.0
        if not isData :
            if mcWeight<0:  mcweight[0] = -1.0
            if mcWeight>0:  mcweight[0] =  1.0
        

        h_total.Fill(1.);
        h_total_mcweight.Fill(1.,mcweight[0]);
        
        
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Trigger selection
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        itrig_=0; trig1 = False; trig2 = False;
        trig1 = CheckFilter(trigName, trigResult, 'HLT_PFMET170_NoiseCleaned')
        trig2 = CheckFilter(trigName, trigResult, 'HLT_PFMET90_PFMHT90_')
        trig3 = CheckFilter(trigName, trigResult, 'HLT_PFMET120_PFMHT120_') ## dummy
        trig4 = CheckFilter(trigName, trigResult, 'HLT_PFMET110_PFMHT110_') ## dummy
        #trigstatus =  trig1 | trig2
        if not isData:
            trigstatus  = True
        if isData:
            trigstatus =  trig1 | trig2
        
        if trigstatus == False : continue
            
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Filter selection
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        filterstatus = False
        filter1 = False; filter2 = False;filter3 = False;filter4 = False; filter5 = False; filter6 = False
        ifilter_=0
        filter1 = CheckFilter(filterName, filterResult, 'Flag_HBHENoiseFilter')
        filter2 = CheckFilter(filterName, filterResult, 'Flag_globalTightHalo2016Filter')
        filter3 = CheckFilter(filterName, filterResult, 'Flag_eeBadScFilter')
        filter4 = CheckFilter(filterName, filterResult, 'Flag_goodVertices')
        filter5 = CheckFilter(filterName, filterResult, 'Flag_EcalDeadCellTriggerPrimitiveFilter')
        filter6 = True #Flag_HBHENoiseIsoFilter
        
        filterstatus =  filter1 | filter2 & filter3 & filter4 & filter5 & filter6

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## PFMET Selection
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------        
        pfmetstatus = ( pfMet > 170.0 )
        if pfmetstatus == False : continue 
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Fat-Jet Selection
        ## Higgs Tagging
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        jetpassindex=[]
        for ifatjet in range(nFATJets):
            if (fatjetP4[ifatjet].Pt() > 170.0  ) & (abs(fatjetP4[ifatjet].Eta())  < 2.4) & (bool(passFatJetTightID[ifatjet]) == True):
                jetpassindex.append(ifatjet)
                
                
        thinjetpassindex=[]
        for ithinjet in range(nTHINJets):
            j1 = thinjetP4[ithinjet]
            if (j1.Pt() > 30.0)&(abs(j1.Eta())<2.4)&(bool(passThinJetLooseID[ithinjet])==True)&(bool(passThinJetPUID[ithinjet]) == True):
                thinjetpassindex.append(ithinjet)
        if len(thinjetpassindex) < 1 : continue
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Electron Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        myEles=[]
        for iele in range(nEle):
            if (eleP4[iele].Pt() > 10. ) & (abs(eleP4[iele].Eta()) <2.5) & (bool(eleIsPassLoose[iele]) == True) :
                myEles.append(iele)
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Muon Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        myMuos = []
        for imu in range(nMu):
            if (muP4[imu].Pt()>10.) & (abs(muP4[imu].Eta()) < 2.4) & (bool(isLooseMuon[imu]) == True):
                relPFIso = (muChHadIso[imu]+ max(0., muNeHadIso[imu] + muGamIso[imu] - 0.5*muPUPt[imu]))/muP4[imu].Pt();
                if relPFIso<0.4 :
                    myMuos.append(imu)
                    
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Tau Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        myTaus=[]
        for itau in range(nTau):
            if (tauP4[itau].Pt()>20.) & (abs(tauP4[itau].Eta())<2.3) & (bool(isDecayModeFinding[itau]) == True) & (bool(passLooseTauIso[itau]) == True):
                myTaus.append(itau)
        
        
        

        
        st_runId[0]             = long(run)
        st_lumiSection[0]       = lumi
        st_eventId[0]           = event
        print ('-----------',st_runId,st_lumiSection,st_eventId)
        
        st_pfMetCorrPt[0]       = pfMet
        st_pfMetCorrPhi[0]      = pfMetPhi
        st_isData[0]            = isData
        
        st_nFatJets[0]       = len(jetpassindex)
        
        
        st_FATnSubSDJet.clear()
        st_FATjetP4.clear()
        st_subjetSDCSV.clear()
        st_FATjetPRmassL2L3Corr.clear()
        st_subjetPt.clear()
        st_subjetEta.clear()
        st_subjetFlav.clear()
        
        st_THINjetP4.clear()
        st_THINjetCISVV2.clear()
        st_THINjetHadronFlavor.clear()
        
        st_eleP4.clear()
        st_muP4.clear()
        st_HPSTau_4Momentum.clear()
        
        st_genParId.clear()
        st_genMomParId.clear()
        st_genParSt.clear()
        st_genParP4.clear()
        
        for ifatjet in range(len(jetpassindex)):
            #st_fatjetP4[ifatjet] = fatjetP4[ifatjet].Pt()
            st_FATnSubSDJet.push_back(nSubSoftDropJet[ifatjet])
            st_FATjetP4.push_back(fatjetP4[ifatjet])
            st_FATjetPRmassL2L3Corr.push_back(fatjetPRmassL2L3Corr[ifatjet])
            csv= ROOT.std.vector('float')()
            csv.clear()
            pt= ROOT.std.vector('float')()
            pt.clear()
            eta= ROOT.std.vector('float')()
            eta.clear()
            flav= ROOT.std.vector('float')()
            flav.clear()
            
            for isj in range(nSubSoftDropJet[ifatjet]):
                csv.push_back(subjetSDCSV[ifatjet][isj])
                p4 = TLorentzVector(subjetSDPx[ifatjet][isj], subjetSDPy[ifatjet][isj], subjetSDPz[ifatjet][isj], subjetSDE[ifatjet][isj])
                pt.push_back(p4.Pt())
                eta.push_back(p4.Eta())
                flav.push_back(subjetHadronFlavor[ifatjet][isj])
            st_subjetSDCSV.push_back(csv)
            st_subjetPt.push_back(pt)
            st_subjetEta.push_back(eta)
            st_subjetFlav.push_back(flav)
            
        #thinjetpassindex=[]
        st_THINnJet[0] = len(thinjetpassindex)
        for ithinjet in range(len(thinjetpassindex)):
            st_THINjetP4.push_back(thinjetP4[ithinjet])
            st_THINjetCISVV2.push_back(thinJetCSV[ithinjet])
            st_THINjetHadronFlavor.push_back(THINjetHadronFlavor[ithinjet])
            
        st_nEle[0] = len(myEles)
        for iele in range(len(myEles)):
            st_eleP4.push_back(eleP4[iele])
            
        st_nMu[0] = len(myMuos)
        for imu in range(len(myMuos)):
            st_muP4.push_back(muP4[imu])
        
        st_HPSTau_n[0] = len(myTaus)
        for itau in range(len(myTaus)):
            st_HPSTau_4Momentum.push_back(tauP4[itau])
            
        

        st_pu_nTrueInt[0] = pu_nTrueInt
        st_nGenPar[0] =  nGenPar
        for igp in range(nGenPar): 
            st_genParId.push_back(genParId[igp])
            st_genMomParId.push_back(genMomParId[igp])
            st_genParSt.push_back(genParSt[igp])
            st_genParP4.push_back(genParP4[igp])

            #for isj in range(nSubSoftDropJet[ifatjet]):
                
        
        outTree.Fill()
        '''
        for ifatjet in range(len(jetpassindex)):
            skimTree.st_fatjetP4.append(fatjetP4[ifatjet])
            skimTree.st_fatjetPRmassL2L3Corr.append(fatjetPRmassL2L3Corr[ifatjet])
            for isj in range(nSubSoftDropJet[ifatjet]):
                sjSDCSV.append(subjetSDCSV[ifatjet][isj])
                sjSDPx.append(subjetSDPx[ifatjet][isj])
                sjSDPy.append(subjetSDPy[ifatjet][isj])
                sjSDPz.append(subjetSDPz[ifatjet][isj])
                sjSDE.append(subjetSDE[ifatjet][isj])
                sjHadronFlavor.append(subjetHadronFlavor[ifatjet][isj])
            skimTree.st_sjSDCSV.append(sjSDCSV)
            skimTree.st_sjSDPx.append(sjSDPx)
            skimTree.st_sjSDPy.append(sjSDPy)
            skimTree.st_sjSDPz.append(sjSDPz)
            skimTree.st_sjSDE.append(sjSDE)
            skimTree.st_sjHadronFlavor.append(sjHadronFlavor)
        '''
    h_total_mcweight.Write()
    h_total.Write()
    outfile.Write()

        


        
def CheckFilter(filterName, filterResult,filtercompare):
    ifilter_=0
    filter1 = False
    for ifilter in filterName:
        filter1 = (ifilter.find(filtercompare) != -1)  & (bool(filterResult[ifilter_]) == True)   
        if filter1: break
        ifilter_ = ifilter_ + 1
    return filter1




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
    


def GenWeightProducer(sample,nGenPar, genParId, genMomParId, genParSt,genParP4):
    pt__=0;
    #print " inside gen weight "
    k2=1.0
    #################
    # WJets
    #################
    if sample=="WJETS":
        goodLepID = []
        for ig in range(nGenPar): 
            PID    = genParId[ig]
            momPID = genMomParId[ig]
            status = genParSt[ig]
            #print "inside WJ loop pdgid", PID
            #print ("if status =",      (abs(PID) != 11),( abs(PID) != 12),(  abs(PID) != 13 ),(  abs(PID) != 14),(  abs(PID) != 15),(  abs(PID) != 16))
            #print "and of if status ", ( (abs(PID) != 11) & (abs(PID) != 12) &  (abs(PID) != 13) & (abs(PID) != 14) &  (abs(PID) != 15) &  (abs(PID) != 16) )
            
            if ( (abs(PID) != 11) & (abs(PID) != 12) &  (abs(PID) != 13) & (abs(PID) != 14) &  (abs(PID) != 15) &  (abs(PID) != 16) ): continue
            #print "lepton found"
            if ( ( (status != 1) & (abs(PID) != 15)) | ( (status != 2) & (abs(PID) == 15)) ): continue
            #print "tau found"
            if ( (abs(momPID) != 24) & (momPID != PID) ): continue
            #print "W found"
            #print "aftrer WJ if statement"
            goodLepID.append(ig)
        #print "length = ",len(goodLepID)
        if len(goodLepID) == 2 :
            l4_thisLep = genParP4[goodLepID[0]]
            l4_thatLep = genParP4[goodLepID[1]]
            l4_z = l4_thisLep + l4_thatLep
            
            pt = l4_z.Pt()
            pt__ = pt
            print " pt inside "
            k2 = -0.830041 + 7.93714 *TMath.Power( pt - (-877.978) ,(-0.213831) ) ;
    
    #################        
    #ZJets
    #################
    if sample == "ZJETS":
        print " inside zjets "
        goodLepID = []
        for ig in range(nGenPar):
         #   print " inside loop "
            PID    = genParId[ig]
            momPID = genMomParId[ig]
            status = genParSt[ig]
          #  print " after vars "

            if ( (abs(PID) != 12) &  (abs(PID) != 14) &  (abs(PID) != 16) ) : continue
            if ( status != 1 ) : continue 
            if ( (momPID != 23) & (momPID != PID) ) : continue
            goodLepID.append(ig)
        
        if len(goodLepID) == 2 :
            l4_thisLep = genParP4[goodLepID[0]]
            l4_thatLep = genParP4[goodLepID[1]]
            l4_z = l4_thisLep + l4_thatLep
            pt = l4_z.Pt()
            print " pt inside "
            k2 = -0.180805 + 6.04146 *TMath.Power( pt - (-759.098) ,(-0.242556) ) ;

    #################        
    #TTBar
    #################        
    if (sample=="TT"):
        print " inside ttbar "
        goodLepID = []
        for ig in range(nGenPar):
            print "inside TT loop "
            PID    = genParId[ig]
            momPID = genMomParId[ig]
            status = genParSt[ig]
            if ( abs(PID) == 6) :
                goodLepID.append(ig)
        if(len(goodLepID)==2):
            l4_thisLep = genParP4[goodLepID[0]]
            l4_thatLep = genParP4[goodLepID[1]]
            pt1 = TMath.Min(400.0, l4_thisLep.Pt())
            pt2 = TMath.Min(400.0, l4_thatLep.Pt())
            
            w1 = TMath.Exp(0.156 - 0.00137*pt1);
            w2 = TMath.Exp(0.156 - 0.00137*pt2);
            k2 =  1.001*TMath.Sqrt(w1*w2);
            
    if(sample=="all"):
        k2 = 1.0
        
    return k2


def MT(Pt, met, dphi):
    return ROOT.TMath.Sqrt( 2 * Pt * met * (1.0 - ROOT.TMath.Cos(dphi)) )

if __name__ == "__main__":
    AnalyzeDataSet()
    
    
    

