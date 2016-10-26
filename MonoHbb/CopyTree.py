#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector
import ROOT as ROOT
import os 

#inputfilename = os.environ['INPUT']
#outfilename   = os.environ['OUTPUT']
inputfilename = 'zj100.txt'
outfilename = 'tmp.root'

tree_ = TChain("tree/treeMaker")
infile = open(inputfilename)
for ifile in infile:
    tree_.Add(ifile.rstrip())

#file_ = TFile.Open("NCUGlobalTuples_590.root","read")
#tree_ = file_.Get("tree/treeMaker")

file_out = TFile.Open(outfilename,"RECREATE")
metcut = 'pfMetCorrPt>170'
fatjetcut = 'FATjetP4[0].Pt()>200.0 & abs(FATjetP4[0].Eta())<2.4 & FATjetPassIDTight[0] == 1'
thinjetcut = 'THINnJet > 1 & THINjetP4[0].Pt() > 30.0 & THINjetP4[1].Pt() > 30.0 & abs(THINjetP4[0].Eta()) < 4.5 & abs(THINjetP4[1].Eta()) < 4.5 & THINjetPassIDLoose[0] ==1 & THINjetPassIDLoose[1] ==1 '

allcut = metcut + ' & (  (' + fatjetcut + ' ) | ( ' + thinjetcut + ') )'
print allcut
tree_.CopyTree(allcut).Write("treeMaker")#skimmedTree")

h_total = TH1F('h_total','h_total',2,0,2)
totalevents= tree_.GetEntries()

h_total_w = TH1F('h_total_w','h_total_w',2,0,2)
totalevents_w = tree_.GetEntries()

h_total.SetBinContent(1,totalevents)
h_total.Write()
file_out.Close()
