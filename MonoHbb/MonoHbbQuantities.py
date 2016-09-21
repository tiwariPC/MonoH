from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D
import ROOT as ROOT
class MonoHbbQuantities:

    def __init__(self, rootfilename):
        self.rootfilename = rootfilename
        #self.allquantities = allquantities
        self.regime   =  True
        
        self.met      =  -999.0
        self.h_met         =  []
        
        self.mass     =  -999.0
        self.h_mass        =  []
        
        self.csv1     =  -999.0
        self.h_csv1        =  []
        
        self.csv2     =  -999.0
        self.h_csv2        =  []
        
        self.h_total   = []
        self.h_total_weight   = []
        
    def defineHisto(self):
        self.h_total.append(TH1F('h_total','h_total',4,0,4))
        self.h_total_weight.append(TH1F('h_total_weight','h_total_weight',4,0,4))
        
        for iregime in range(2):
            postname = str(iregime)
            self.h_met.append(TH1F('h_met_'+postname,  'h_met_'+postname,  100,0.,1000.))
            self.h_mass.append(TH1F('h_mass_'+postname, 'h_mass_'+postname, 100,0.,200.))
            self.h_csv1.append(TH1F('h_csv1_'+postname, 'h_csv1_'+postname, 20,0.,1.))
            self.h_csv2.append(TH1F('h_csv2_'+postname, 'h_csv2_'+postname, 20,0.,1.))

            
            
        print "histo defined"
        
    def FillHisto(self):
        type_ = -1
        if self.regime: type_ = 0
        if not self.regime: type_ = 1
        
        self.h_met [type_].Fill(self.met)
        self.h_mass[type_].Fill(self.mass)
        self.h_csv1[type_].Fill(self.csv1)
        self.h_csv2[type_].Fill(self.csv2)
        
        
    def WriteHisto(self, (nevts,nevts_weight)):
        f = TFile(self.rootfilename,'RECREATE')
        f.cd()
        self.h_total[0].SetBinContent(1,nevts)
        self.h_total[0].Write()
        
        self.h_total_weight[0].SetBinContent(1,nevts_weight)
        self.h_total_weight[0].Write()
        
        for iregime in range(2):
            self.h_met[iregime].Write()
            self.h_mass[iregime].Write()
            self.h_csv1[iregime].Write()
            self.h_csv2[iregime].Write()

