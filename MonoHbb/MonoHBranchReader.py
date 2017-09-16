#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, TF1
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math

ROOT.gROOT.SetBatch(True)
from MonoHbbQuantities import *
from PileUpWeights import PUWeight

ROOT.gROOT.ProcessLine('.L BTagCalibrationStandalone.cpp+') 

#ROOT.gROOT.ProcessLine('.L TheaCorrection.cpp+') 

######################################
## set up running mode of the code.
######################################

#ROOT.gROOT.ProcessLine('.L PileUpWeights.h')

#print "puweight = ",PUWEIGHT(10)
usage = "usage: %prog [options] arg1 arg2"
parser = optparse.OptionParser(usage)

## data will be true if -d is passed and will be false if -m is passed
parser.add_option("-i", "--inputfile",  dest="inputfile")
parser.add_option("-o", "--outputfile", dest="outputfile")
parser.add_option("-D", "--outputdir", dest="outputdir")

parser.add_option("-a", "--analyze", action="store_true",  dest="analyze")

parser.add_option("-e", "--efficiency", action="store_true",  dest="efficiency")
parser.add_option("-F", "--farmout", action="store_true",  dest="farmout")
parser.add_option("-t", "--table", action="store_true",  dest="table")
parser.add_option("-P", "--OtherPlots", action="store_true",  dest="OtherPlots")

########################################################################################################################
########################## cut values########################################################################
########################################################################################################################

parser.add_option("--dbt", action="store_true",  dest="dbt")
parser.add_option( "--dbtcut", type=float,  dest="dbtcut")

parser.add_option("--theac", action="store_true",  dest="theac")

(options, args) = parser.parse_args()




isfarmout = options.farmout 
print (options.inputfile, options.outputfile )
#print 'options = ',[options.inputfile]
inputfilename = options.inputfile

#print inputfilename
pathlist = inputfilename.split("/")
sizeoflist = len(pathlist)
#print ('sizeoflist = ',sizeoflist)
rootfile='tmphist'
rootfile = pathlist[sizeoflist-1]
textfile = rootfile+".txt"

#outputdir='MonoHSamples/'
#os.system('mkdir '+outputdir)

outfilename=''
if not isfarmout:
    outfilename = options.outputdir + "/" + rootfile

if isfarmout:
    outfilename = options.outputfile


skimmedTree = TChain("outTree")

#print isfarmout



def WhichSample(filename):
    samplename = 'all'
    if filename.find('WJets')>-1:
        samplename = 'WJETS'
    elif filename.find('ZJets')>-1:
        samplename = 'ZJETS'
    elif filename.find('TT')>-1:
        samplename  = 'TT'
    else:
        samplename = 'all'
    return samplename
    


def TheaCorrection(puppipt=200.0,  puppieta=0.0):
    puppisd_corrGEN      = TF1("puppisd_corrGEN","[0]+[1]*pow(x*[2],-[3])");
    puppisd_corrGEN.SetParameters(
        1.00626,
        -1.06161,
        0.07999,
        1.20454
        )
    puppisd_corrRECO_cen =  TF1("puppisd_corrRECO_cen","[0]+[1]*x+[2]*pow(x,2)+[3]*pow(x,3)+[4]*pow(x,4)+[5]*pow(x,5)");
    puppisd_corrRECO_cen.SetParameters(
        1.05807,
        -5.91971e-05,
        2.296e-07,
        -1.98795e-10,
        6.67382e-14,
        -7.80604e-18
        )
    
    puppisd_corrRECO_for = TF1("puppisd_corrRECO_for","[0]+[1]*x+[2]*pow(x,2)+[3]*pow(x,3)+[4]*pow(x,4)+[5]*pow(x,5)");
    puppisd_corrRECO_for.SetParameters(
        1.26638,
        -0.000658496,
        9.73779e-07,
        -5.93843e-10,
        1.61619e-13,
        -1.6272e-17)
    
    genCorr  = 1.
    recoCorr = 1.
    totalWeight = 1.
    
    genCorr =  puppisd_corrGEN.Eval( puppipt )
    if ( abs(puppieta)  <= 1.3 ) :
        recoCorr = puppisd_corrRECO_cen.Eval( puppipt )
    elif( abs(puppieta) > 1.3 ) :
        recoCorr = puppisd_corrRECO_for.Eval( puppipt )
        
    totalWeight = genCorr * recoCorr
    return totalWeight
    



h_t = TH1F('h_t','h_t',2,0,2)
h_t_weight = TH1F('h_t_weight','h_t_weight',2,0,2)

samplename = 'all'
if isfarmout:
    infile = open(inputfilename)
    for ifile in infile: 
        skimmedTree.Add(ifile.rstrip())
        samplename = WhichSample(ifile.rstrip())
        ## for histograms
        f_tmp = TFile.Open(ifile.rstrip(),'READ')
        h_tmp = f_tmp.Get('h_total')
        h_tmp_weight = f_tmp.Get('h_total_mcweight')
        h_t.Add(h_tmp)
        h_t_weight.Add(h_tmp_weight)

if not isfarmout:
    skimmedTree.Add(inputfilename)
    samplename = WhichSample(inputfilename)
    ## for histograms
    f_tmp = TFile(inputfilename,'READ')
    h_tmp = f_tmp.Get('h_total')
    h_tmp_weight = f_tmp.Get('h_total_mcweight')
    h_t.Add(h_tmp)
    h_t_weight.Add(h_tmp_weight)

debug = False 

def AnalyzeDataSet():
    ## Input rootfile name
    
    #rootfilename = inputfilename
    #print (rootfilename,inputfilename)
    #f = TFile(rootfilename,'READ')
    #skimmedTree = f.Get('tree/treeMaker')
    NEntries = skimmedTree.GetEntries()
    print ('NEntries = ',NEntries)
    npass = 0
    #print [rootfilename, NEntries]
    cutStatus={'total':NEntries}
    
    cutStatus['trigger'] = 0
    cutStatus['filter'] = 0
    cutStatus['pfmet'] =  0
#    cutStatus['njetSR1']=  0
#    cutStatus['njet1SR1'] = 0
#    cutStatus['njet2SR1'] = 0
#    cutStatus['njetSR2'] = 0
#    cutStatus['njet1SR2'] = 0
#    cutStatus['njet2SR2'] = 0
#    cutStatus['njet2SR2'] = 0    
    cutStatus['isinSR'] = 0
    cutStatus['hasgoodjets'] = 0
    cutStatus['hasbtaggedjet'] = 0
    cutStatus['btag'] = 0
    cutStatus['dphi'] = 0
    cutStatus['ThinJetVeto'] = 0
    cutStatus['bVeto'] = 0
    cutStatus['eleveto'] = 0
    cutStatus['muveto'] = 0
    cutStatus['tauveto'] = 0
    
    allquantities = MonoHbbQuantities(outfilename)
    allquantities.defineHisto()

    
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # BTag Scale Factor Initialisation--------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    ## FatJets
    calib = ROOT.BTagCalibrationStandalone('csvv1', 'subjet_CSVv2_ichep.csv')
    v_sys = getattr(ROOT, 'vector<string>')()
    v_sys.push_back('up')
    v_sys.push_back('down')
    ### working point, central systematic type, vector of other sys. types 
    ###  0 is for loose op, 1: medium, 2: tight, 3: discr. reshaping
    reader = ROOT.BTagCalibrationStandaloneReader( 0, "central", v_sys )    
    reader.load(calib, 0,  "lt" )  
    reader.load(calib, 1,  "lt" )  
    reader.load(calib, 2,  "incl" )  
    


    ## ThinJets
    calib1 = ROOT.BTagCalibrationStandalone('csvv2', 'CSVv2_ichep.csv')
    reader1 = ROOT.BTagCalibrationStandaloneReader( 0, "central", v_sys )    
    reader1.load(calib1, 0,  "comb" )  
    reader1.load(calib1, 1,  "comb" )  
    reader1.load(calib1, 2,  "incl" )  
    
    #h_total = TH1F('h_total','h_total',2,0,2)
    #h_total_mcweight = TH1F('h_total_mcweight','h_total_mcweight',2,0,2)
    
    
    
    for ievent in range(NEntries):
    #for ievent in range(501):
        
        ##
        sf_resolved1 = []
        sf_resolved2 = []
        sf_boosted1 = []
        sf_boosted2 = []
        #print "event number = ",ievent
        skimmedTree.GetEntry(ievent)
        
        ## Get all relevant branches
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Extract branches
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        run                        = skimmedTree.__getattr__('st_runId')
        lumi                       = skimmedTree.__getattr__('st_lumiSection')
        event                      = skimmedTree.__getattr__('st_eventId')

        #if event != 4126: continue                                
        #if lumi  != 42: continue                                
        if event%100==0: print (event)
        #trigName                   = skimmedTree.__getattr__('st_hlt_trigName')
        #trigResult                 = skimmedTree.__getattr__('st_hlt_trigResult')
        #filterName                 = skimmedTree.__getattr__('st_hlt_filterName')
        #filterResult               = skimmedTree.__getattr__('st_hlt_filterResult')
                                   
        pfMet                      = skimmedTree.__getattr__('st_pfMetCorrPt')
        pfMetPhi                   = skimmedTree.__getattr__('st_pfMetCorrPhi')
        
        #nFatJets                   = skimmedTree.__getattr__('st_nFatJets')
        #fatjetP4                   = skimmedTree.__getattr__('st_FATjetP4')
        #fatjetPRmassL2L3Corr       = skimmedTree.__getattr__('st_FATjetPRmassL2L3Corr')
                
        #nSubSoftDropJet            = skimmedTree.__getattr__('st_FATnSubSDJet')
        #subjetSDCSV                = skimmedTree.__getattr__('st_subjetSDCSV')
        

        
        #subjetSDPx                 = skimmedTree.__getattr__('st_FATsubjetSDPx')
        #subjetSDPy                 = skimmedTree.__getattr__('st_FATsubjetSDPy')
        #subjetSDPz                 = skimmedTree.__getattr__('st_FATsubjetSDPz')
        #subjetSDE                  = skimmedTree.__getattr__('st_FATsubjetSDE')
        #subjetSDPt                  = skimmedTree.__getattr__('st_subjetPt')
        #subjetSDEta                  = skimmedTree.__getattr__('st_subjetEta')
        #passFatJetTightID          = skimmedTree.__getattr__('st_FATjetPassIDTight')
        #subjetHadronFlavor         = skimmedTree.__getattr__('st_subjetFlav')
        
        #doublebtagger              = skimmedTree.__getattr__('st_ADDjet_DoubleSV')
        #tau2                       = skimmedTree.__getattr__('st_FATjetTau2')
        #au1                       = skimmedTree.__getattr__('st_FATjetTau1')
        
        
        nTHINJets                  = skimmedTree.__getattr__('st_THINnJet')
        thinjetP4                  = skimmedTree.__getattr__('st_THINjetP4')
        thinJetCSV                 = skimmedTree.__getattr__('st_THINjetCISVV2')
        #passThinJetLooseID         = skimmedTree.__getattr__('st_THINjetPassIDLoose')
        #passThinJetPUID            = skimmedTree.__getattr__('st_THINisPUJetID')
        THINjetHadronFlavor        = skimmedTree.__getattr__('st_THINjetHadronFlavor')
        thinjetNhadEF              = skimmedTree.__getattr__('st_THINjetNHadEF')
        thinjetChadEF              = skimmedTree.__getattr__('st_THINjetCHadEF')
        
        nEle                       = skimmedTree.__getattr__('st_nEle')
        eleP4                      = skimmedTree.__getattr__('st_eleP4')
        #eleIsPassLoose             = skimmedTree.__getattr__('st_eleIsPassLoose')
        
        nMu                        = skimmedTree.__getattr__('st_nMu')
        muP4                       = skimmedTree.__getattr__('st_muP4')
        #isLooseMuon                = skimmedTree.__getattr__('st_isLooseMuon')
        #muChHadIso                 = skimmedTree.__getattr__('st_muChHadIso')
        #muNeHadIso                 = skimmedTree.__getattr__('st_muNeHadIso')
        #muGamIso                   = skimmedTree.__getattr__('st_muGamIso')
        #muPUPt                     = skimmedTree.__getattr__('st_muPUPt')
        
        nTau                       = skimmedTree.__getattr__('st_HPSTau_n')
        tauP4                      = skimmedTree.__getattr__('st_HPSTau_4Momentum')
        #isDecayModeFinding         = skimmedTree.__getattr__('st_disc_decayModeFinding')
        #passLooseTauIso            = skimmedTree.__getattr__('st_disc_byLooseIsolationMVA3oldDMwLT')
        
        isData                     = skimmedTree.__getattr__('st_isData')
        mcWeight                   = skimmedTree.__getattr__('mcweight')
        pu_nTrueInt                = int(skimmedTree.__getattr__('st_pu_nTrueInt'))
        
        nGenPar                    = skimmedTree.__getattr__('st_nGenPar')
        genParId                   = skimmedTree.__getattr__('st_genParId')
        genMomParId                = skimmedTree.__getattr__('st_genMomParId')
        genParSt                   = skimmedTree.__getattr__('st_genParSt')
        genParP4                   = skimmedTree.__getattr__('st_genParP4')
             
        jetSR1Info           = []
        jetSR2Info           = []
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # MC Weights ----------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        mcweight = 0.0 
        if isData==1:   mcweight =  1.0
        if not isData :
            if mcWeight<0:  mcweight = -1.0
            if mcWeight>0:  mcweight =  1.0
        


        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## PFMET Selection
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------        
        pfmetstatus = ( pfMet > 200.0 )
        if pfmetstatus == False : continue 
        cutStatus['pfmet'] += 1
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        

        ## list comprehensation
        
        inSR1=False
        inSR2=False
        
        if nTHINJets == 2:
            inSR1=True
        elif nTHINJets == 3:
            inSR2=True            
        else:
            continue 
        
        cutStatus['isinSR'] += 1        # The event qualifies to be in either of the SRs based on njet
        
        ## for SR1
         # 2 jets and 1 btagged 
         
        if inSR1:                  
            
            if thinjetP4[0].Pt()>thinjetP4[1].Pt():   # Set lead jet as j1, second jet as j2
                ifirstjet=0
                isecondjet=1
            else:
                ifirstjet=1
                isecondjet=0
                
            j1=thinjetP4[ifirstjet]
            j2=thinjetP4[isecondjet]
            
            if j1.Pt() < 50.0: continue
            if DeltaPhi(j1.Phi(),pfMetPhi) < 0.5: continue            
            if thinjetNhadEF[ifirstjet] > 0.8 : continue
            if thinjetChadEF[ifirstjet]< 0.1: continue
                            
            if j2.Pt() < 30.0: continue
            if DeltaPhi(j1.Phi(),pfMetPhi) < 0.5: continue
            
            cutStatus['hasgoodjets'] += 1           # The jets satisfy the required criteria
            
            if thinJetCSV[ifirstjet] < 0.8: continue            # Lead jet has to be b-tagged
            
            cutStatus['hasbtaggedjet'] += 1         # The b-jet criteria is fulfilled 
            
            jet1pt = j1.Pt()
            jet1phi = j1.Phi()
            jet1eta = j1.Eta()
            jet2pt = j2.Pt()
            jet2phi = j2.Phi()
            jet2eta = j2.Eta()

            jetSR1Info.append([jet1pt,jet1eta,jet1phi])
            jetSR1Info.append([jet2pt,jet2eta,jet2phi])
          
     
     ## for SR2
        # 3 jets and 2 btagged 
        
        if inSR2:
        
            alljetPT=[jet.Pt() for jet in thinjetP4]
            jetindex=[0,1,2]
                        
            sortedjets=[jet for pt,jet in sorted(zip(alljetPT,thinjetP4), reverse=True)]      # This gives a list of jets with their pTs in descending order
            sortedindex=[jetindex for pt,jetindex in sorted(zip(alljetPT,jetindex), reverse=True)]     # Indices of jets in thinjetP4 in decscending order of jetPT
            
            j1=sortedjets[0]
            j2=sortedjets[1]
            j3=sortedjets[2]
            
            ifirstjet=sortedindex[0]
            isecondjet=sortedindex[1]
            ithirdjet=sortedindex[2]
            
            if j1.Pt() < 50.0: continue
            if DeltaPhi(j1.Phi(),pfMetPhi) < 0.5: continue            
            if thinjetNhadEF[ifirstjet] > 0.8 : continue
            if thinjetChadEF[ifirstjet]< 0.1: continue
            
            if j2.Pt() < 50.0: continue
            if DeltaPhi(j2.Phi(),pfMetPhi) < 0.5: continue            
            if thinjetNhadEF[isecondjet] > 0.8 : continue
            if thinjetChadEF[isecondjet]< 0.1: continue
            
            if j3.Pt() < 30.0: continue
            if DeltaPhi(j3.Phi(),pfMetPhi) < 0.5: continue
            
            cutStatus['hasgoodjets'] += 1           # The jets satisfy the required criteria
            
            if thinJetCSV[ifirstjet] < 0.8: continue            # Lead jet has to be b-tagged
            if thinJetCSV[isecondjet] < 0.8: continue           # Second jet has to be b-tagged
            
            cutStatus['hasbtaggedjet'] += 1         # The b-jet criteria is fulfilled 
            
            jet1pt = j1.Pt()
            jet1phi = j1.Phi()
            jet1eta = j1.Eta()
            jet2pt = j2.Pt()
            jet2phi = j2.Phi()
            jet2eta = j2.Eta()
            jet3pt = j3.Pt()
            jet3phi = j3.Phi()
            jet3eta = j3.Eta()

            jetSR2Info.append([jet1pt,jet1eta,jet1phi])
            jetSR2Info.append([jet2pt,jet2eta,jet2phi])
            jetSR2Info.append([jet3pt,jet3eta,jet3phi])

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## min DPhi
        ## nT<hinJets
        ## b-jet Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Leptons Info
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        myEles=[]
        for iele in range(nEle):
            if eleP4[iele].Pt() < 10 : continue
            if abs(eleP4[iele].Eta()) >2.5: continue
            myEles.append(iele)
        
        myMuos = []
        for imu in range(nMu):
            if muP4[imu].Pt()<10 : continue
            if abs(muP4[imu].Eta()) > 2.4  : continue
            myMuos.append(imu)

        myTaus=[]
        for itau in range(nTau):
            if tauP4[itau].Pt()<20 : continue
            if abs(tauP4[itau].Eta())>2.3 : continue
            myTaus.append(itau);
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Lepton Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        nleptons_ = (len(myTaus) + len(myMuos) + len(myEles))
        
        #if not (nleptons_ >= nlepton) : continue 
        #if not (nleptons_ < nLepton) : continue  
        
        #regime = False
        #if isboosted: regime = True
        #if isresolved: regime = False
        
        
        #if regime: 
         #   mt_ = MT(fatjetP4[HIndex].Pt(), pfMet, Phi_mpi_pi(pfMetPhi-fatjetP4[HIndex].Phi()) )
        #if not regime: 
         #   mt_ = MT(HiggsInfo[0][3], pfMet, Phi_mpi_pi(pfMetPhi-HiggsInfo[0][4]) )
        
        #if mt_ < 450.0: continue 
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Photon Veto
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----to be added in future---------------------------------------------------------------------------------------------------------------------------------------
        
        
        npass = npass +1
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # EWK Reweighting And Top pT Reweighting--------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        genpTReweighting = 1.0 
        if isData==1:   genpTReweighting  =  1.0
        if not isData :  genpTReweighting = GenWeightProducer(samplename, nGenPar, genParId, genMomParId, genParSt,genParP4)
        
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## Pileup weight
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        allpuweights = PUWeight()
        len_puweight = len(allpuweights)
        puweight = 0.0
        if isData: puweight = 1.0 
        if not isData:
            if pu_nTrueInt  <= len_puweight: puweight = allpuweights[pu_nTrueInt-1]
            if pu_nTrueInt  > len_puweight : puweight = 0.0 
        #print (len_puweight, pu_nTrueInt, puweight)
        

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        #All Weights ----------------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        #allweights = puweight * mcweight * genpTReweighting
        allweights = mcweight * genpTReweighting 
                
        
        ##-------------------------------------------------------------------------------------------------
        ##-------------------------------------------------------------------------------------------------
        ##------------fill all variables needed for further processing-------------------------------------
        ##-------------------------------------------------------------------------------------------------
        ##-------------------------------------------------------------------------------------------------


        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## BTag Scale Factor ---------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------        
        
        #if regime:
            #print "inside regime"
            #p4_1 = TLorentzVector(subjetSDPx[HIndex][0], subjetSDPy[HIndex][0], subjetSDPz[HIndex][0], subjetSDE[HIndex][0])
            #p4_2 = TLorentzVector(subjetSDPx[HIndex][1], subjetSDPy[HIndex][1], subjetSDPz[HIndex][1], subjetSDE[HIndex][1])
            
         #   pt1 = subjetSDPt[HIndex][0]
         #   eta1 = subjetSDEta[HIndex][0]
         #   pt2 = subjetSDPt[HIndex][1]
         #   eta2 = subjetSDEta[HIndex][1]
            
         #   flav1 = jetflav(subjetHadronFlavor[HIndex][0])
         #   flav2 = jetflav(subjetHadronFlavor[HIndex][1])
            
         #   sf_boosted1 = weightbtag(reader, flav1, pt1, eta1)
         #   sf_boosted2 = weightbtag(reader, flav2, pt2, eta2)
            
         #   if options.dbt:
         #       sf_boosted1 = [1.0,1.0,1.0]
         #       sf_boosted2 = [1.0,1.0,1.0] 
            #print (sf_boosted1, sf_boosted2)
            
        
        #if not regime: 
            
            #print "inside not regime"
           # ij = HiggsInfo_sorted[0][0]
           # jj = HiggsInfo_sorted[0][1]
            
          #  flav1 = jetflav(THINjetHadronFlavor[ij])
          #  flav2 = jetflav(THINjetHadronFlavor[jj])

            #print ("ij, flav, pt, eta, ",ij, flav1, thinjetP4[ij].Pt(), thinjetP4[ij].Eta())
            #reader1.eval_auto_bounds('central', 0, 1.2, 50.)
          #  sf_resolved1 = weightbtag(reader1, flav1, thinjetP4[ij].Pt(), thinjetP4[ij].Eta())
         #   sf_resolved2 = weightbtag(reader1, flav2, thinjetP4[jj].Pt(), thinjetP4[jj].Eta())
            
            #print (sf_resolved1, sf_resolved2)

        
        #########################################
        ## Regime Loop ends here
        #########################################
        #print (sf_resolved1, sf_resolved2,sf_boosted1, sf_boosted2)
       # if regime: 
       #     allweights = allweights * sf_boosted1[0] * sf_boosted2[0]
       # if not regime:
       #     allweights = allweights * sf_resolved1[0] * sf_resolved2[0]
        
        if isData: allweights = 1.0 
        #allquantities.regime     = regime
        allquantities.met        = pfMet
        #allquantities.mt         = mt_
        #if not  ((len(myTaus) + len(myMuos) + len(myEles)) < nLepton) : continue

        #if len(dphiVec)>0: allquantities.dPhi            = min(dphiVec)
        allquantities.N_e             = len(myEles)
        allquantities.N_mu            = len(myMuos)
        allquantities.N_tau           = len(myTaus)
        allquantities.N_Pho           = 0
        #allquantities.N_b             = nGoodTHINBJets
        #allquantities.N_j             = nGoodTHINJets

        allquantities.weight    = allweights
        allquantities.totalevents = 1
        
        #if regime: 
         #allquantities.mass            = fatjetPRmassL2L3Corr[HIndex]
         #allquantities.HiggsPt         = fatjetP4[HIndex].Pt()
         #allquantities.HiggsEta        = fatjetP4[HIndex].Eta()
         #allquantities.HiggsPhi        = fatjetP4[HIndex].Phi()
            
        #if not regime:  
         #allquantities.mass            = HiggsInfo_sorted[0][2]
         
         
        if inSR1:        
            allquantities.jet1_pT_sr1     = jetSR1Info[0][0]
            allquantities.jet1_eta_sr1    = jetSR1Info[0][1]
            allquantities.jet1_phi_sr1    = jetSR1Info[0][2]
            allquantities.jet2_pT_sr1     = jetSR1Info[1][0]
            allquantities.jet2_eta_sr1    = jetSR1Info[1][1]
            allquantities.jet2_phi_sr1    = jetSR1Info[1][2]
        elif inSR2:
            allquantities.jet1_pT_sr2     = jetSR2Info[0][0]
            allquantities.jet1_eta_sr2    = jetSR2Info[0][1]
            allquantities.jet1_phi_sr2    = jetSR2Info[0][2]
            allquantities.jet2_pT_sr1     = jetSR2Info[1][0]
            allquantities.jet2_eta_sr1    = jetSR2Info[1][1]
            allquantities.jet2_phi_sr1    = jetSR2Info[1][2]
            allquantities.jet3_pT_sr1     = jetSR2Info[2][0]
            allquantities.jet3_eta_sr1    = jetSR2Info[2][1]
            allquantities.jet3_phi_sr1    = jetSR2Info[2][2]
        else:
            continue
            
        #print (allquantities.regime, allquantities.met,allquantities.mass )
        allquantities.FillHisto()
    

    #print cutStatus
    #print "npass = ", npass
    NEntries_Weight = h_t.Integral()
    NEntries_total        = h_t_weight.Integral()
    allquantities.WriteHisto((NEntries_total,NEntries_Weight))
    #print " efficiency = ", float(npass/float(NEntries))
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
    
def DeltaPhi(phi1,phi2):
   phi = Phi_mpi_pi(phi1-phi2)
   
   return phi
   
    
def Phi_mpi_pi(x):
    kPI = 3.14159265358979323846
    kTWOPI = 2 * kPI
    
    while (x >= kPI): x = x - kTWOPI;
    while (x < -kPI): x = x + kTWOPI;
    return x;
    
def weightbtag(reader, flav, pt, eta):
    sf_c = reader.eval_auto_bounds('central', flav, eta, pt) 
    sf_low = reader.eval_auto_bounds('down', flav, eta, pt)
    sf_up  = reader.eval_auto_bounds('up', flav, eta, pt)
    btagsf = [sf_c, sf_low, sf_up]
    return btagsf

def jetflav(flav):
    if flav == 5: 
        flavor = 0
    elif flav == 4:
        flavor = 1
    else:
        flavor = 2
    return flavor




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
            if ( (abs(PID) != 11) & (abs(PID) != 12) &  (abs(PID) != 13) & (abs(PID) != 14) &  (abs(PID) != 15) &  (abs(PID) != 16) ): continue
            if ( ( (status != 1) & (abs(PID) != 15)) | ( (status != 2) & (abs(PID) == 15)) ): continue
            if ( (abs(momPID) != 24) & (momPID != PID) ): continue
            goodLepID.append(ig)

        if len(goodLepID) == 2 :
            l4_thisLep = genParP4[goodLepID[0]]
            l4_thatLep = genParP4[goodLepID[1]]
            l4_z = l4_thisLep + l4_thatLep
            
            pt = l4_z.Pt()
            pt__ = pt

            k2 = -0.830041 + 7.93714 *TMath.Power( pt - (-877.978) ,(-0.213831) ) ;
    
    #################        
    #ZJets
    #################
    if sample == "ZJETS":
        goodLepID = []
        for ig in range(nGenPar):
            PID    = genParId[ig]
            momPID = genMomParId[ig]
            status = genParSt[ig]


            if ( (abs(PID) != 12) &  (abs(PID) != 14) &  (abs(PID) != 16) ) : continue
            if ( status != 1 ) : continue 
            if ( (momPID != 23) & (momPID != PID) ) : continue
            goodLepID.append(ig)
        
        if len(goodLepID) == 2 :
            l4_thisLep = genParP4[goodLepID[0]]
            l4_thatLep = genParP4[goodLepID[1]]
            l4_z = l4_thisLep + l4_thatLep
            pt = l4_z.Pt()
            k2 = -0.180805 + 6.04146 *TMath.Power( pt - (-759.098) ,(-0.242556) ) ;

    #################        
    #TTBar
    #################        
    if (sample=="TT"):
        goodLepID = []
        for ig in range(nGenPar):
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
    ## analyze the tree and make histograms and all the 2D plots and Efficiency plots. 
    if options.analyze:
        print "now calling analyzedataset"
        AnalyzeDataSet()
    
    
    

