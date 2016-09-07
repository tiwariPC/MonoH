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
        
    def defineHisto(self):
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
        
        
    def WriteHisto(self):
        f = TFile(self.rootfilename,'RECREATE')
        f.cd()
        for iregime in range(2):
            self.h_met[iregime].Write()
            self.h_mass[iregime].Write()
            self.h_csv1[iregime].Write()
            self.h_csv2[iregime].Write()
        
