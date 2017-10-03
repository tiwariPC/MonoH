from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TH2F
import ROOT as ROOT
class MonoHbbQuantities:

    def __init__(self, rootfilename):
        self.rootfilename = rootfilename
        #self.allquantities = allquantities
        #self.regime   =  True
        
        self.met      =  -999.0
        self.h_met         =  []
        #self.h_met_rebin         =  []
        
        #self.mass     =  -999.0
        #self.h_mass        =  []
        
        self.csv1     =  -999.0
        self.h_csv1        =  []
        
        self.csv2     =  -999.0
        self.h_csv2        =  []
        
        self.mt              = -999.
        #self.dPhi            = -999.
        self.N_e             = -10
        self.N_mu            = -10
        self.N_tau           = -10
        self.N_Pho           = -10
        #self.N_b             = -10
        self.N_j             = -10
        #self.mass            = -999.
        self.jet1_pT_sr1     = -999.
        self.jet1_eta_sr1    = -999.
        self.jet1_phi_sr1    = -999.
        self.jet2_pT_sr1     = -999.
        self.jet2_eta_sr1    = -999.
        self.jet2_phi_sr1    = -999.
        self.jet1_pT_sr2     = -999.
        self.jet1_eta_sr2    = -999.
        self.jet1_phi_sr2    = -999.
        self.jet2_pT_sr2     = -999.
        self.jet2_eta_sr2    = -999.
        self.jet2_phi_sr2    = -999.
        self.jet3_pT_sr2     = -999.
        self.jet3_eta_sr2    = -999.
        self.jet3_phi_sr2    = -999.
        
        self.jet1_csv_sr1    = -999.
        self.jet2_csv_sr1    = -999.
        self.jet1_csv_sr2    = -999.
        self.jet2_csv_sr2    = -999.
        self.jet3_csv_sr2    = -999.
        
        
        #for ZCR
        self.jet1_pT_Zcr1     = -999.
        self.jet1_eta_Zcr1    = -999.
        self.jet1_phi_Zcr1    = -999.
        self.jet2_pT_Zcr1     = -999.
        self.jet2_eta_Zcr1    = -999.
        self.jet2_phi_Zcr1    = -999.
        self.jet1_pT_Zcr2     = -999.
        self.jet1_eta_Zcr2    = -999.
        self.jet1_phi_Zcr2    = -999.
        self.jet2_pT_Zcr2     = -999.
        self.jet2_eta_Zcr2    = -999.
        self.jet2_phi_Zcr2    = -999.
        self.jet3_pT_Zcr2     = -999.
        self.jet3_eta_Zcr2    = -999.
        self.jet3_phi_Zcr2    = -999.
        self.ZhadronRecoil1    = -999.
        self.Zmass1            = -999.
        self.ZpT1              = -999.
        self.ZhadronRecoil2    = -999.
        self.Zmass2            = -999.
        self.ZpT2              = -999.
        self.mu1_pT_Zcr1       = -999.
        self.mu2_pT_Zcr1       = -999.
        self.el1_pT_Zcr1       = -999.
        self.el2_pT_Zcr1       = -999.
        self.mu1_eta_Zcr1      = -999.
        self.mu2_eta_Zcr1      = -999.
        self.el1_eta_Zcr1      = -999.
        self.el2_eta_Zcr1      = -999.
        self.mu1_phi_Zcr1      = -999.
        self.mu2_phi_Zcr1      = -999.
        self.el1_phi_Zcr1      = -999.
        self.el2_phi_Zcr1      = -999.
        self.mu1_iso_Zcr1      = -999.
        self.mu2_iso_Zcr1      = -999.
        self.mu1_pT_Zcr2       = -999.
        self.mu2_pT_Zcr2       = -999.
        self.el1_pT_Zcr2       = -999.
        self.el2_pT_Zcr2       = -999.
        self.mu1_eta_Zcr2      = -999.
        self.mu2_eta_Zcr2      = -999.
        self.el1_eta_Zcr2      = -999.
        self.el2_eta_Zcr2      = -999.
        self.mu1_phi_Zcr2      = -999.
        self.mu2_phi_Zcr2      = -999.
        self.el1_phi_Zcr2      = -999.
        self.el2_phi_Zcr2      = -999.
        self.mu1_iso_Zcr2      = -999.
        self.mu2_iso_Zcr2      = -999.
        
        self.jet1_csv_Zcr1    = -999.
        self.jet2_csv_Zcr1    = -999.
        self.jet1_csv_Zcr2    = -999.
        self.jet2_csv_Zcr2    = -999.
        self.jet3_csv_Zcr2    = -999.
        
        #for WCR
        self.jet1_pT_Wcr1     = -999.
        self.jet1_eta_Wcr1    = -999.
        self.jet1_phi_Wcr1    = -999.
        self.jet2_pT_Wcr1     = -999.
        self.jet2_eta_Wcr1    = -999.
        self.jet2_phi_Wcr1    = -999.
        self.jet1_pT_Wcr2     = -999.
        self.jet1_eta_Wcr2    = -999.
        self.jet1_phi_Wcr2    = -999.
        self.jet2_pT_Wcr2     = -999.
        self.jet2_eta_Wcr2    = -999.
        self.jet2_phi_Wcr2    = -999.
        self.jet3_pT_Wcr2     = -999.
        self.jet3_eta_Wcr2    = -999.
        self.jet3_phi_Wcr2    = -999.
        self.WhadronRecoil1    = -999.
        self.Wmass1            = -999.
        self.WpT1              = -999.
        self.WhadronRecoil2    = -999.
        self.Wmass2            = -999.
        self.WpT2              = -999.
        self.mu1_pT_Wcr1       = -999.
        self.el1_pT_Wcr1       = -999.
        self.mu1_eta_Wcr1      = -999.
        self.el1_eta_Wcr1      = -999.
        self.mu1_phi_Wcr1      = -999.
        self.el1_phi_Wcr1      = -999.
        self.mu1_iso_Wcr1      = -999.
        self.mu1_pT_Wcr2       = -999.
        self.el1_pT_Wcr2       = -999.
        self.mu1_eta_Wcr2      = -999.
        self.el1_eta_Wcr2      = -999.
        self.mu1_phi_Wcr2      = -999.
        self.el1_phi_Wcr2      = -999.
        self.mu1_iso_Wcr2      = -999.
        
        self.jet1_csv_Wcr1    = -999.
        self.jet2_csv_Wcr1    = -999.
        self.jet1_csv_Wcr2    = -999.
        self.jet2_csv_Wcr2    = -999.
        self.jet3_csv_Wcr2    = -999.
        
        #for TOPcr
        self.jet1_pT_TOPcr1     = -999.
        self.jet1_eta_TOPcr1    = -999.
        self.jet1_phi_TOPcr1    = -999.
        self.jet2_pT_TOPcr1     = -999.
        self.jet2_eta_TOPcr1    = -999.
        self.jet2_phi_TOPcr1    = -999.
        self.jet1_pT_TOPcr2     = -999.
        self.jet1_eta_TOPcr2    = -999.
        self.jet1_phi_TOPcr2    = -999.
        self.jet2_pT_TOPcr2     = -999.
        self.jet2_eta_TOPcr2    = -999.
        self.jet2_phi_TOPcr2    = -999.
        self.jet3_pT_TOPcr2     = -999.
        self.jet3_eta_TOPcr2    = -999.
        self.jet3_phi_TOPcr2    = -999.
        self.TOPRecoil1          = -999.
        self.TOPRecoil2          = -999.
        self.mu1_pT_TOPcr1       = -999.
        self.el1_pT_TOPcr1       = -999.
        self.mu1_eta_TOPcr1      = -999.
        self.el1_eta_TOPcr1      = -999.
        self.mu1_phi_TOPcr1      = -999.
        self.el1_phi_TOPcr1      = -999. 
        self.mu1_iso_TOPcr1      = -999.
        self.mu1_pT_TOPcr2       = -999.
        self.el1_pT_TOPcr2       = -999.
        self.mu1_eta_TOPcr2      = -999.
        self.el1_eta_TOPcr2      = -999.
        self.mu1_phi_TOPcr2      = -999.
        self.el1_phi_TOPcr2      = -999. 
        self.mu1_iso_TOPcr2      = -999.
        
        self.jet1_csv_TOPcr1    = -999.
        self.jet2_csv_TOPcr1    = -999.
        self.jet1_csv_TOPcr2    = -999.
        self.jet2_csv_TOPcr2    = -999.
        self.jet3_csv_TOPcr2    = -999.


        self.h_mt              = []
        #self.h_dPhi            = []
        self.h_N_e             = []
        self.h_N_mu            = []
        self.h_N_tau           = []
        self.h_N_Pho           = []
        #self.h_N_b             = []
        self.h_N_j             = []
        #self.h_mass            = []
        self.h_met_pdf         = []
        self.h_met_muR         = []
        self.h_met_muF         = []
        self.h_jet1_pT_sr1     = []
        self.h_jet1_eta_sr1    = []
        self.h_jet1_phi_sr1    = []
        self.h_jet2_pT_sr1     = []
        self.h_jet2_eta_sr1    = []
        self.h_jet2_phi_sr1    = []
        self.h_jet1_pT_sr2     = []
        self.h_jet1_eta_sr2    = []
        self.h_jet1_phi_sr2    = []
        self.h_jet2_pT_sr2     = []
        self.h_jet2_eta_sr2    = []
        self.h_jet2_phi_sr2    = []
        self.h_jet3_pT_sr2     = []
        self.h_jet3_eta_sr2    = []
        self.h_jet3_phi_sr2    = []
        
        #for ZCR
        self.h_jet1_pT_Zcr1     = []
        self.h_jet1_eta_Zcr1    = []
        self.h_jet1_phi_Zcr1    = []
        self.h_jet2_pT_Zcr1     = []
        self.h_jet2_eta_Zcr1    = []
        self.h_jet2_phi_Zcr1    = []
        self.h_jet1_pT_Zcr2     = []
        self.h_jet1_eta_Zcr2    = []
        self.h_jet1_phi_Zcr2    = []
        self.h_jet2_pT_Zcr2     = []
        self.h_jet2_eta_Zcr2    = []
        self.h_jet2_phi_Zcr2    = []
        self.h_jet3_pT_Zcr2     = []
        self.h_jet3_eta_Zcr2    = []
        self.h_jet3_phi_Zcr2    = []
        self.h_ZhadronRecoil1    = []
        self.h_Zmass1            = []
        self.h_ZpT1              = []
        self.h_ZhadronRecoil2    = []
        self.h_Zmass2            = []
        self.h_ZpT2              = []
        self.h_mu1_pT_Zcr1       = []
        self.h_mu2_pT_Zcr1       = []
        self.h_el1_pT_Zcr1       = []
        self.h_el2_pT_Zcr1       = []
        self.h_mu1_eta_Zcr1      = []
        self.h_mu2_eta_Zcr1      = []
        self.h_el1_eta_Zcr1      = []
        self.h_el2_eta_Zcr1      = []
        self.h_mu1_phi_Zcr1      = []
        self.h_mu2_phi_Zcr1      = []
        self.h_el1_phi_Zcr1      = []
        self.h_el2_phi_Zcr1      = []
        self.h_mu1_iso_Zcr1      = []
        self.h_mu2_iso_Zcr1      = []
        self.h_mu1_pT_Zcr2       = []
        self.h_mu2_pT_Zcr2       = []
        self.h_el1_pT_Zcr2       = []
        self.h_el2_pT_Zcr2       = []
        self.h_mu1_eta_Zcr2      = []
        self.h_mu2_eta_Zcr2      = []
        self.h_el1_eta_Zcr2      = []
        self.h_el2_eta_Zcr2      = []
        self.h_mu1_phi_Zcr2      = []
        self.h_mu2_phi_Zcr2      = []
        self.h_el1_phi_Zcr2      = []
        self.h_el2_phi_Zcr2      = []
        self.h_mu1_iso_Zcr2      = []
        self.h_mu2_iso_Zcr2      = []
        
        self.h_jet1_csv_Zcr1    = []
        self.h_jet2_csv_Zcr1    = []
        self.h_jet1_csv_Zcr2    = []
        self.h_jet2_csv_Zcr2    = []
        self.h_jet3_csv_Zcr2    = []
        
        #for WCR
        self.h_jet1_pT_Wcr1     = []
        self.h_jet1_eta_Wcr1    = []
        self.h_jet1_phi_Wcr1    = []
        self.h_jet2_pT_Wcr1     = []
        self.h_jet2_eta_Wcr1    = []
        self.h_jet2_phi_Wcr1    = []
        self.h_jet1_pT_Wcr2     = []
        self.h_jet1_eta_Wcr2    = []
        self.h_jet1_phi_Wcr2    = []
        self.h_jet2_pT_Wcr2     = []
        self.h_jet2_eta_Wcr2    = []
        self.h_jet2_phi_Wcr2    = []
        self.h_jet3_pT_Wcr2     = []
        self.h_jet3_eta_Wcr2    = []
        self.h_jet3_phi_Wcr2    = []
        self.h_WhadronRecoil1    = []
        self.h_Wmass1            = []
        self.h_WpT1              = []
        self.h_WhadronRecoil2    = []
        self.h_Wmass2            = []
        self.h_WpT2              = []
        self.h_mu1_pT_Wcr1       = []
        self.h_el1_pT_Wcr1       = []
        self.h_mu1_eta_Wcr1      = []
        self.h_el1_eta_Wcr1      = []
        self.h_mu1_phi_Wcr1      = []
        self.h_el1_phi_Wcr1      = []
        self.h_mu1_iso_Wcr1      = []
        self.h_mu1_pT_Wcr2       = []
        self.h_el1_pT_Wcr2       = []
        self.h_mu1_eta_Wcr2      = []
        self.h_el1_eta_Wcr2      = []
        self.h_mu1_phi_Wcr2      = []
        self.h_el1_phi_Wcr2      = []
        self.h_mu1_iso_Wcr2      = []
        
        self.h_jet1_csv_Wcr1    = []
        self.h_jet2_csv_Wcr1    = []
        self.h_jet1_csv_Wcr2    = []
        self.h_jet2_csv_Wcr2    = []
        self.h_jet3_csv_Wcr2    = []
        
        #for TOPcr
        self.h_jet1_pT_TOPcr1     = []
        self.h_jet1_eta_TOPcr1    = []
        self.h_jet1_phi_TOPcr1    = []
        self.h_jet2_pT_TOPcr1     = []
        self.h_jet2_eta_TOPcr1    = []
        self.h_jet2_phi_TOPcr1    = []
        self.h_jet1_pT_TOPcr2     = []
        self.h_jet1_eta_TOPcr2    = []
        self.h_jet1_phi_TOPcr2    = []
        self.h_jet2_pT_TOPcr2     = []
        self.h_jet2_eta_TOPcr2    = []
        self.h_jet2_phi_TOPcr2    = []
        self.h_jet3_pT_TOPcr2     = []
        self.h_jet3_eta_TOPcr2    = []
        self.h_jet3_phi_TOPcr2    = []
        self.h_TOPRecoil1          = []
        self.h_TOPRecoil2          = []
        self.h_mu1_pT_TOPcr1       = []
        self.h_el1_pT_TOPcr1       = []
        self.h_mu1_eta_TOPcr1      = []
        self.h_el1_eta_TOPcr1      = []
        self.h_mu1_phi_TOPcr1      = []
        self.h_el1_phi_TOPcr1      = []
        self.h_mu1_iso_TOPcr1      = []
        self.h_mu1_pT_TOPcr2       = []
        self.h_el1_pT_TOPcr2       = []
        self.h_mu1_eta_TOPcr2      = []
        self.h_el1_eta_TOPcr2      = []
        self.h_mu1_phi_TOPcr2      = []
        self.h_el1_phi_TOPcr2      = []
        self.h_mu1_iso_TOPcr2      = []
        
        self.h_jet1_csv_TOPcr1    = []
        self.h_jet2_csv_TOPcr1    = []
        self.h_jet1_csv_TOPcr2    = []
        self.h_jet2_csv_TOPcr2    = []
        self.h_jet3_csv_TOPcr2    = []
        
        ## 2d histograms 
        self.h_met_vs_mass     = []
        
        self.weight   = 1.0 

        self.weight_pdf   = []
        self.weight_muR   = []
        self.weight_muF   = []

        self.h_total   = []
        self.h_total_weight   = []
        
    def defineHisto(self):
        self.h_total.append(TH1F('h_total','h_total',2,0,2))
        self.h_total_weight.append(TH1F('h_total_weight','h_total_weight',2,0,2))
        
#        self.h_cutflow=TH1F('h_cutflow_','h_cutflow_',7, 0, 7)                          # Cutflow     

        self.h_met.append(TH1F('h_met_',  'h_met_',  1000,0.,1000.))
        

        #metbins_ = [200,350,500,1000]
        #self.h_met_rebin.append(TH1F('h_met_rebin_'+postname,  'h_met_rebin'+postname,  3, array(('d'),metbins_)))

        #self.h_mass.append(TH1F('h_mass_'+postname, 'h_mass_'+postname, 400,0.,400.))

        self.h_met_vs_mass.append(TH2F('h_met_vs_mass_', 'h_met_vs_mass_', 1000, 0., 1000., 250, 0, 250.))

        self.h_csv1.append(TH1F('h_csv1_', 'h_csv1_', 20,0.,1.))
        self.h_csv2.append(TH1F('h_csv2_', 'h_csv2_', 20,0.,1.))
        #self.h_mt.append(TH1F('h_mt_'+postname,'h_mt_'+postname,100,400.,1400.))
        #self.h_dPhi.append(TH1F('h_dPhi_'+postname,'h_dPhi_'+postname,70, -3.5, 3.5 ))
        self.h_N_e.append(TH1F('h_N_e_','h_N_e_',5,0,5))
        self.h_N_mu.append(TH1F('h_N_mu_','h_N_mu_',5,0,5))
        self.h_N_tau.append(TH1F('h_N_tau_','h_N_tau_',5,0,5))
        self.h_N_Pho.append(TH1F('h_N_Pho_','h_N_Pho_',5,0,5))
        #self.h_N_b.append(TH1F('h_N_b_'+postname,'h_N_b_'+postname,3,0,3))
        self.h_N_j.append(TH1F('h_N_j_','h_N_j_',10,0,10))
        self.h_jet1_pT_sr1.append(TH1F('h_jet1_pT_sr1_','h_jet1_pT_sr1_',1000,0.,1000.))
        self.h_jet1_eta_sr1.append(TH1F('h_jet1_eta_sr1_','h_jet1_eta_sr1_',70, -3.5, 3.5))
        self.h_jet1_phi_sr1.append(TH1F('h_jet1_phi_sr1_','h_jet1_phi_sr1_',70, -3.5, 3.5))
        self.h_jet2_pT_sr1.append(TH1F('h_jet2_pT_sr1_','h_jet2_pT_sr1_',1000,0.,1000.))
        self.h_jet2_eta_sr1.append(TH1F('h_jet2_eta_sr1_','h_jet2_eta_sr1_',70, -3.5, 3.5))
        self.h_jet2_phi_sr1.append(TH1F('h_jet2_phi_sr1_','h_jet2_phi_sr1_',70, -3.5, 3.5))
        self.h_jet1_pT_sr2.append(TH1F('h_jet1_pT_sr2_','h_jet1_pT_sr2_',1000,0.,1000.))
        self.h_jet1_eta_sr2.append(TH1F('h_jet1_eta_sr2_','h_jet1_eta_sr2_',70, -3.5, 3.5))
        self.h_jet1_phi_sr2.append(TH1F('h_jet1_phi_sr2_','h_jet1_phi_sr2_',70, -3.5, 3.5))
        self.h_jet2_pT_sr2.append(TH1F('h_jet2_pT_sr2_','h_jet2_pT_sr2_',1000,0.,1000.))
        self.h_jet2_eta_sr2.append(TH1F('h_jet2_eta_sr2_','h_jet2_eta_sr2_',70, -3.5, 3.5))
        self.h_jet2_phi_sr2.append(TH1F('h_jet2_phi_sr2_','h_jet2_phi_sr2_',70, -3.5, 3.5))
        self.h_jet3_pT_sr2.append(TH1F('h_jet3_pT_sr2_','h_jet3_pT_sr2_',1000,0.,1000.))
        self.h_jet3_eta_sr2.append(TH1F('h_jet3_eta_sr2_','h_jet3_eta_sr2_',70, -3.5, 3.5))
        self.h_jet3_phi_sr2.append(TH1F('h_jet3_phi_sr2_','h_jet3_phi_sr2_',70, -3.5, 3.5))
        
        #for ZCR
        self.h_jet1_pT_Zcr1.append(TH1F('h_jet1_pT_Zcr1_','h_jet1_pT_Zcr1_',1000,0.,1000.))
        self.h_jet1_eta_Zcr1.append(TH1F('h_jet1_eta_Zcr1_','h_jet1_eta_Zcr1_',70, -3.5, 3.5))
        self.h_jet1_phi_Zcr1.append(TH1F('h_jet1_phi_Zcr1_','h_jet1_phi_Zcr1_',70, -3.5, 3.5))
        self.h_jet2_pT_Zcr1.append(TH1F('h_jet2_pT_Zcr1_','h_jet2_pT_Zcr1_',1000,0.,1000.))
        self.h_jet2_eta_Zcr1.append(TH1F('h_jet2_eta_Zcr1_','h_jet2_eta_Zcr1_',70, -3.5, 3.5))
        self.h_jet2_phi_Zcr1.append(TH1F('h_jet2_phi_Zcr1_','h_jet2_phi_Zcr1_',70, -3.5, 3.5))
        self.h_jet1_pT_Zcr2.append(TH1F('h_jet1_pT_Zcr2_','h_jet1_pT_Zcr2_',1000,0.,1000.))
        self.h_jet1_eta_Zcr2.append(TH1F('h_jet1_eta_Zcr2_','h_jet1_eta_Zcr2_',70, -3.5, 3.5))
        self.h_jet1_phi_Zcr2.append(TH1F('h_jet1_phi_Zcr2_','h_jet1_phi_Zcr2_',70, -3.5, 3.5))
        self.h_jet2_pT_Zcr2.append(TH1F('h_jet2_pT_Zcr2_','h_jet2_pT_Zcr2_',1000,0.,1000.))
        self.h_jet2_eta_Zcr2.append(TH1F('h_jet2_eta_Zcr2_','h_jet2_eta_Zcr2_',70, -3.5, 3.5))
        self.h_jet2_phi_Zcr2.append(TH1F('h_jet2_phi_Zcr2_','h_jet2_phi_Zcr2_',70, -3.5, 3.5))
        self.h_jet3_pT_Zcr2.append(TH1F('h_jet3_pT_Zcr2_','h_jet3_pT_Zcr2_',1000,0.,1000.))
        self.h_jet3_eta_Zcr2.append(TH1F('h_jet3_eta_Zcr2_','h_jet3_eta_Zcr2_',70, -3.5, 3.5))
        self.h_jet3_phi_Zcr2.append(TH1F('h_jet3_phi_Zcr2_','h_jet3_phi_Zcr2_',70, -3.5, 3.5))
        self.h_ZhadronRecoil1.append(TH1F('h_ZhadronRecoil1_','h_ZhadronRecoil1_',1000,0.,1000.))
        self.h_Zmass1.append(TH1F('h_Zmass1_','h_Zmass1_',1000,0.,500.))
        self.h_ZpT1.append(TH1F('h_ZpT1_','h_ZpT1_',1000,0.,1000.))
        self.h_ZhadronRecoil2.append(TH1F('h_ZhadronRecoil2_','h_ZhadronRecoil2_',1000,0.,1000.))
        self.h_Zmass2.append(TH1F('h_Zmass2_','h_Zmass2_',1000,0.,500.))
        self.h_ZpT2.append(TH1F('h_ZpT2_','h_ZpT2_',1000,0.,1000.))
        self.h_mu1_pT_Zcr1.append(TH1F('h_mu1_pT_Zcr1_','h_mu1_pT_Zcr1_',1000,0.,1000.))
        self.h_mu2_pT_Zcr1.append(TH1F('h_mu2_pT_Zcr1_','h_mu2_pT_Zcr1_',1000,0.,1000.))
        self.h_el1_pT_Zcr1.append(TH1F('h_el1_pT_Zcr1_','h_el1_pT_Zcr1_',1000,0.,1000.))
        self.h_el2_pT_Zcr1.append(TH1F('h_el2_pT_Zcr1_','h_el2_pT_Zcr1_',1000,0.,1000.))
        self.h_mu1_eta_Zcr1.append(TH1F('h_mu1_eta_Zcr1_','h_mu1_eta_Zcr1_',70, -3.5, 3.5))
        self.h_mu2_eta_Zcr1.append(TH1F('h_mu2_eta_Zcr1_','h_mu2_eta_Zcr1_',70, -3.5, 3.5))
        self.h_el1_eta_Zcr1.append(TH1F('h_el1_eta_Zcr1_','h_el1_eta_Zcr1_',70, -3.5, 3.5))
        self.h_el2_eta_Zcr1.append(TH1F('h_el2_eta_Zcr1_','h_el2_eta_Zcr1_',70, -3.5, 3.5))
        self.h_mu1_phi_Zcr1.append(TH1F('h_mu1_phi_Zcr1_','h_mu1_phi_Zcr1_',70, -3.5, 3.5))
        self.h_mu2_phi_Zcr1.append(TH1F('h_mu2_phi_Zcr1_','h_mu2_phi_Zcr1_',70, -3.5, 3.5))
        self.h_el1_phi_Zcr1.append(TH1F('h_el1_phi_Zcr1_','h_el1_phi_Zcr1_',70, -3.5, 3.5))
        self.h_el2_phi_Zcr1.append(TH1F('h_el2_phi_Zcr1_','h_el2_phi_Zcr1_',70, -3.5, 3.5))
        self.h_mu1_iso_Zcr1.append(TH1F('h_mu1_iso_Zcr1_','h_mu1_iso_Zcr1_',70, 0,.25))
        self.h_mu2_iso_Zcr1.append(TH1F('h_mu2_iso_Zcr1_','h_mu2_iso_Zcr1_',70, 0,.25))
        self.h_mu1_pT_Zcr2.append(TH1F('h_mu1_pT_Zcr2_','h_mu1_pT_Zcr2_',1000,0.,1000.))
        self.h_mu2_pT_Zcr2.append(TH1F('h_mu2_pT_Zcr2_','h_mu2_pT_Zcr2_',1000,0.,1000.))
        self.h_el1_pT_Zcr2.append(TH1F('h_el1_pT_Zcr2_','h_el1_pT_Zcr2_',1000,0.,1000.))
        self.h_el2_pT_Zcr2.append(TH1F('h_el2_pT_Zcr2_','h_el2_pT_Zcr2_',1000,0.,1000.))
        self.h_mu1_eta_Zcr2.append(TH1F('h_mu1_eta_Zcr2_','h_mu1_eta_Zcr2_',70, -3.5, 3.5))
        self.h_mu2_eta_Zcr2.append(TH1F('h_mu2_eta_Zcr2_','h_mu2_eta_Zcr2_',70, -3.5, 3.5))
        self.h_el1_eta_Zcr2.append(TH1F('h_el1_eta_Zcr2_','h_el1_eta_Zcr2_',70, -3.5, 3.5))
        self.h_el2_eta_Zcr2.append(TH1F('h_el2_eta_Zcr2_','h_el2_eta_Zcr2_',70, -3.5, 3.5))
        self.h_mu1_phi_Zcr2.append(TH1F('h_mu1_phi_Zcr2_','h_mu1_phi_Zcr2_',70, -3.5, 3.5))
        self.h_mu2_phi_Zcr2.append(TH1F('h_mu2_phi_Zcr2_','h_mu2_phi_Zcr2_',70, -3.5, 3.5))
        self.h_el1_phi_Zcr2.append(TH1F('h_el1_phi_Zcr2_','h_el1_phi_Zcr2_',70, -3.5, 3.5))
        self.h_el2_phi_Zcr2.append(TH1F('h_el2_phi_Zcr2_','h_el2_phi_Zcr2_',70, -3.5, 3.5))
        self.h_mu1_iso_Zcr2.append(TH1F('h_mu1_iso_Zcr2_','h_mu1_iso_Zcr2_',70, 0,.25))
        self.h_mu2_iso_Zcr2.append(TH1F('h_mu2_iso_Zcr2_','h_mu2_iso_Zcr2_',70, 0,.25))
        
        self.h_jet1_csv_Zcr1.append(TH1F('h_jet1_csv_Zcr1_','h_jet1_csv_Zcr1_',100, 0,1.05))
        self.h_jet2_csv_Zcr1.append(TH1F('h_jet2_csv_Zcr1_','h_jet2_csv_Zcr1_',100, 0,1.05))
        self.h_jet1_csv_Zcr2.append(TH1F('h_jet1_csv_Zcr2_','h_jet1_csv_Zcr2_',100, 0,1.05))
        self.h_jet2_csv_Zcr2.append(TH1F('h_jet2_csv_Zcr2_','h_jet2_csv_Zcr2_',100, 0,1.05))
        self.h_jet3_csv_Zcr2.append(TH1F('h_jet3_csv_Zcr2_','h_jet3_csv_Zcr2_',100, 0,1.05))
        
        #for WCR
        self.h_jet1_pT_Wcr1.append(TH1F('h_jet1_pT_Wcr1_','h_jet1_pT_Wcr1_',1000,0.,1000.))
        self.h_jet1_eta_Wcr1.append(TH1F('h_jet1_eta_Wcr1_','h_jet1_eta_Wcr1_',70, -3.5, 3.5))
        self.h_jet1_phi_Wcr1.append(TH1F('h_jet1_phi_Wcr1_','h_jet1_phi_Wcr1_',70, -3.5, 3.5))
        self.h_jet2_pT_Wcr1.append(TH1F('h_jet2_pT_Wcr1_','h_jet2_pT_Wcr1_',1000,0.,1000.))
        self.h_jet2_eta_Wcr1.append(TH1F('h_jet2_eta_Wcr1_','h_jet2_eta_Wcr1_',70, -3.5, 3.5))
        self.h_jet2_phi_Wcr1.append(TH1F('h_jet2_phi_Wcr1_','h_jet2_phi_Wcr1_',70, -3.5, 3.5))
        self.h_jet1_pT_Wcr2.append(TH1F('h_jet1_pT_Wcr2_','h_jet1_pT_Wcr2_',1000,0.,1000.)) 
        self.h_jet1_eta_Wcr2.append(TH1F('h_jet1_eta_Wcr2_','h_jet1_eta_Wcr2_',70, -3.5, 3.5))
        self.h_jet1_phi_Wcr2.append(TH1F('h_jet1_phi_Wcr2_','h_jet1_phi_Wcr2_',70, -3.5, 3.5))
        self.h_jet2_pT_Wcr2.append(TH1F('h_jet2_pT_Wcr2_','h_jet2_pT_Wcr2_',1000,0.,1000.)) 
        self.h_jet2_eta_Wcr2.append(TH1F('h_jet2_eta_Wcr2_','h_jet2_eta_Wcr2_',70, -3.5, 3.5))
        self.h_jet2_phi_Wcr2.append(TH1F('h_jet2_phi_Wcr2_','h_jet2_phi_Wcr2_',70, -3.5, 3.5))
        self.h_jet3_pT_Wcr2.append(TH1F('h_jet3_pT_Wcr2_','h_jet3_pT_Wcr2_',1000,0.,1000.))
        self.h_jet3_eta_Wcr2.append(TH1F('h_jet3_eta_Wcr2_','h_jet3_eta_Wcr2_',70, -3.5, 3.5))
        self.h_jet3_phi_Wcr2.append(TH1F('h_jet3_phi_Wcr2_','h_jet3_phi_Wcr2_',70, -3.5, 3.5))
        self.h_WhadronRecoil1.append(TH1F('h_WhadronRecoil1_','h_WhadronRecoil1_',1000,0.,1000.))
        self.h_Wmass1.append(TH1F('h_Wmass1_','h_Wmass1_',1000,0.,500.))
        self.h_WpT1.append(TH1F('h_WpT1_','h_WpT1_',1000,0.,1000.))
        self.h_WhadronRecoil2.append(TH1F('h_WhadronRecoil2_','h_WhadronRecoil2_',1000,0.,1000.))
        self.h_Wmass2.append(TH1F('h_Wmass2_','h_Wmass2_',1000,0.,500.))
        self.h_WpT2.append(TH1F('h_WpT2_','h_WpT2_',1000,0.,1000.))
        self.h_mu1_pT_Wcr1.append(TH1F('h_mu1_pT_Wcr1_','h_mu1_pT_Wcr1_',1000,0.,1000.))
        self.h_el1_pT_Wcr1.append(TH1F('h_el1_pT_Wcr1_','h_el1_pT_Wcr1_',1000,0.,1000.))
        self.h_mu1_eta_Wcr1.append(TH1F('h_mu1_eta_Wcr1_','h_mu1_eta_Wcr1_',70, -3.5, 3.5))
        self.h_el1_eta_Wcr1.append(TH1F('h_el1_eta_Wcr1_','h_el1_eta_Wcr1_',70, -3.5, 3.5))
        self.h_mu1_phi_Wcr1.append(TH1F('h_mu1_phi_Wcr1_','h_mu1_phi_Wcr1_',70, -3.5, 3.5))
        self.h_el1_phi_Wcr1.append(TH1F('h_el1_phi_Wcr1_','h_el1_phi_Wcr1_',70, -3.5, 3.5))
        self.h_mu1_iso_Wcr1.append(TH1F('h_mu1_iso_Wcr1_','h_mu1_iso_Wcr1_',70, 0,.25))
        self.h_mu1_pT_Wcr2.append(TH1F('h_mu1_pT_Wcr2_','h_mu1_pT_Wcr2_',1000,0.,1000.))
        self.h_el1_pT_Wcr2.append(TH1F('h_el1_pT_Wcr2_','h_el1_pT_Wcr2_',1000,0.,1000.))
        self.h_mu1_eta_Wcr2.append(TH1F('h_mu1_eta_Wcr2_','h_mu1_eta_Wcr2_',70, -3.5, 3.5))
        self.h_el1_eta_Wcr2.append(TH1F('h_el1_eta_Wcr2_','h_el1_eta_Wcr2_',70, -3.5, 3.5))
        self.h_mu1_phi_Wcr2.append(TH1F('h_mu1_phi_Wcr2_','h_mu1_phi_Wcr2_',70, -3.5, 3.5))
        self.h_el1_phi_Wcr2.append(TH1F('h_el1_phi_Wcr2_','h_el1_phi_Wcr2_',70, -3.5, 3.5))
        self.h_mu1_iso_Wcr2.append(TH1F('h_mu1_iso_Wcr2_','h_mu1_iso_Wcr2_',70, 0,.25))
        
        self.h_jet1_csv_Wcr1.append(TH1F('h_jet1_csv_Wcr1_','h_jet1_csv_Wcr1_',100, 0,1.05))
        self.h_jet2_csv_Wcr1.append(TH1F('h_jet2_csv_Wcr1_','h_jet2_csv_Wcr1_',100, 0,1.05))
        self.h_jet1_csv_Wcr2.append(TH1F('h_jet1_csv_Wcr2_','h_jet1_csv_Wcr2_',100, 0,1.05))
        self.h_jet2_csv_Wcr2.append(TH1F('h_jet2_csv_Wcr2_','h_jet2_csv_Wcr2_',100, 0,1.05))
        self.h_jet3_csv_Wcr2.append(TH1F('h_jet3_csv_Wcr2_','h_jet3_csv_Wcr2_',100, 0,1.05))
        
        #for TOPcr
        self.h_jet1_pT_TOPcr1.append(TH1F('h_jet1_pT_TOPcr1_','h_jet1_pT_TOPcr1_',1000,0.,1000.))
        self.h_jet1_eta_TOPcr1.append(TH1F('h_jet1_eta_TOPcr1_','h_jet1_eta_TOPcr1_',70, -3.5, 3.5))
        self.h_jet1_phi_TOPcr1.append(TH1F('h_jet1_phi_TOPcr1_','h_jet1_phi_TOPcr1_',70, -3.5, 3.5))
        self.h_jet2_pT_TOPcr1.append(TH1F('h_jet2_pT_TOPcr1_','h_jet2_pT_TOPcr1_',1000,0.,1000.))
        self.h_jet2_eta_TOPcr1.append(TH1F('h_jet2_eta_TOPcr1_','h_jet2_eta_TOPcr1_',70, -3.5, 3.5))
        self.h_jet2_phi_TOPcr1.append(TH1F('h_jet2_phi_TOPcr1_','h_jet2_phi_TOPcr1_',70, -3.5, 3.5))
        self.h_jet1_pT_TOPcr2.append(TH1F('h_jet1_pT_TOPcr2_','h_jet1_pT_TOPcr2_',1000,0.,1000.))
        self.h_jet1_eta_TOPcr2.append(TH1F('h_jet1_eta_TOPcr2_','h_jet1_eta_TOPcr2_',70, -3.5, 3.5))
        self.h_jet1_phi_TOPcr2.append(TH1F('h_jet1_phi_TOPcr2_','h_jet1_phi_TOPcr2_',70, -3.5, 3.5))
        self.h_jet2_pT_TOPcr2.append(TH1F('h_jet2_pT_TOPcr2_','h_jet2_pT_TOPcr2_',1000,0.,1000.))
        self.h_jet2_eta_TOPcr2.append(TH1F('h_jet2_eta_TOPcr2_','h_jet2_eta_TOPcr2_',70, -3.5, 3.5))
        self.h_jet2_phi_TOPcr2.append(TH1F('h_jet2_phi_TOPcr2_','h_jet2_phi_TOPcr2_',70, -3.5, 3.5))
        self.h_jet3_pT_TOPcr2.append(TH1F('h_jet3_pT_TOPcr2_','h_jet3_pT_TOPcr2_',1000,0.,1000.))
        self.h_jet3_eta_TOPcr2.append(TH1F('h_jet3_eta_TOPcr2_','h_jet3_eta_TOPcr2_',70, -3.5, 3.5))
        self.h_jet3_phi_TOPcr2.append(TH1F('h_jet3_phi_TOPcr2_','h_jet3_phi_TOPcr2_',70, -3.5, 3.5))
        self.h_TOPRecoil1.append(TH1F('h_TOPRecoil1_','h_TOPRecoil1_',1000,0.,1000.))
        self.h_TOPRecoil2.append(TH1F('h_TOPRecoil2_','h_TOPRecoil2_',1000,0.,1000.))
        self.h_mu1_pT_TOPcr1.append(TH1F('h_mu1_pT_TOPcr1_','h_mu1_pT_TOPcr1_',1000,0.,1000.))
        self.h_el1_pT_TOPcr1.append(TH1F('h_el1_pT_TOPcr1_','h_el1_pT_TOPcr1_',1000,0.,1000.))
        self.h_mu1_eta_TOPcr1.append(TH1F('h_mu1_eta_TOPcr1_','h_mu1_eta_TOPcr1_',70, -3.5, 3.5))
        self.h_el1_eta_TOPcr1.append(TH1F('h_el1_eta_TOPcr1_','h_el1_eta_TOPcr1_',70, -3.5, 3.5))
        self.h_mu1_phi_TOPcr1.append(TH1F('h_mu1_phi_TOPcr1_','h_mu1_phi_TOPcr1_',70, -3.5, 3.5))
        self.h_el1_phi_TOPcr1.append(TH1F('h_el1_phi_TOPcr1_','h_el1_phi_TOPcr1_',70, -3.5, 3.5))
        self.h_mu1_iso_TOPcr1.append(TH1F('h_mu1_iso_TOPcr1_','h_mu1_iso_TOPcr1_',70, 0,.25))
        self.h_mu1_pT_TOPcr2.append(TH1F('h_mu1_pT_TOPcr2_','h_mu1_pT_TOPcr2_',1000,0.,1000.))
        self.h_el1_pT_TOPcr2.append(TH1F('h_el1_pT_TOPcr2_','h_el1_pT_TOPcr2_',1000,0.,1000.))
        self.h_mu1_eta_TOPcr2.append(TH1F('h_mu1_eta_TOPcr2_','h_mu1_eta_TOPcr2_',70, -3.5, 3.5))
        self.h_el1_eta_TOPcr2.append(TH1F('h_el1_eta_TOPcr2_','h_el1_eta_TOPcr2_',70, -3.5, 3.5))
        self.h_mu1_phi_TOPcr2.append(TH1F('h_mu1_phi_TOPcr2_','h_mu1_phi_TOPcr2_',70, -3.5, 3.5))
        self.h_el1_phi_TOPcr2.append(TH1F('h_el1_phi_TOPcr2_','h_el1_phi_TOPcr2_',70, -3.5, 3.5))
        self.h_mu1_iso_TOPcr2.append(TH1F('h_mu1_iso_TOPcr2_','h_mu1_iso_TOPcr2_',70, 0,.25))
        
        self.h_jet1_csv_TOPcr1.append(TH1F('h_jet1_csv_TOPcr1_','h_jet1_csv_Zcr1_',100, 0,1.05))
        self.h_jet2_csv_TOPcr1.append(TH1F('h_jet2_csv_TOPcr1_','h_jet2_csv_Zcr1_',100, 0,1.05))
        self.h_jet1_csv_TOPcr2.append(TH1F('h_jet1_csv_TOPcr2_','h_jet1_csv_ZCr2_',100, 0,1.05))
        self.h_jet2_csv_TOPcr2.append(TH1F('h_jet2_csv_TOPcr2_','h_jet2_csv_Zcr2_',100, 0,1.05))
        self.h_jet3_csv_TOPcr2.append(TH1F('h_jet3_csv_TOPcr2_','h_jet3_csv_Zcr2_',100, 0,1.05))
        
        
        h_met_pdf_tmp = []
        for ipdf in range(101):
            midname = str(ipdf)
            h_met_pdf_tmp.append(TH1F('h_met_pdf'+'_'+midname+'_',  'h_met_pdf',  1000,0.,1000.))
        self.h_met_pdf.append(h_met_pdf_tmp)
        h_met_muR_tmp = []
        for imuR in range(2):
            midname = str(imuR)
            h_met_muR_tmp.append(TH1F('h_met_muR'+'_'+midname+'_',  'h_met_muR',  1000,0.,1000.))
        self.h_met_muR.append(h_met_muR_tmp)
        h_met_muF_tmp = []
        for imuF in range(2):
            midname = str(imuF)
            h_met_muF_tmp.append(TH1F('h_met_muF'+'_'+midname+'_',  'h_met_muF',  1000,0.,1000.))
        self.h_met_muF.append(h_met_muF_tmp)

        print "Histograms defined"
        
    def FillHisto(self):
        WF = self.weight
        #print "WF = ", WF
        self.h_met[0]        .Fill(self.met,       WF)
        
        
        for ipdf in range(101):
            self.h_met_pdf[0]        [ipdf].Fill(self.met,       1.0)

        for imuR in range(2):
            self.h_met_muR[0]        [imuR].Fill(self.met,       1.0)
            
        for imuF in range(2):
            self.h_met_muF[0]        [imuF].Fill(self.met,       1.0)
        

        #self.h_met_vs_mass[0] .Fill(self.met, self.mass, WF)

        #self.h_mass           Fill(self.mass,      WF)
        #self.h_csv1           .Fill(self.csv1,      WF)
        #self.h_csv2           .Fill(self.csv2,      WF)
        #self.h_mt             .Fill(self.mt,        WF)
        #self.h_dPhi           Fill(self.dPhi,      WF)
        self.h_N_e[0]            .Fill(self.N_e,       WF)
        self.h_N_mu[0]           .Fill(self.N_mu,      WF)
        self.h_N_tau[0]          .Fill(self.N_tau,     WF)
        self.h_N_Pho[0]          .Fill(self.N_Pho,     WF)
        #self.h_N_b            Fill(self.N_b,       WF)
        self.h_N_j            Fill(self.N_j,       WF)
#        print len(self.h_jet1_pT_sr1)
#        print "HbbQuants: "+str(self.jet1_pT_sr2)
        
        if self.jet1_pT_sr1 is not None:    self.h_jet1_pT_sr1[0]    .Fill(self.jet1_pT_sr1,   WF)
        if self.jet1_eta_sr1 is not None:   self.h_jet1_eta_sr1[0]   .Fill(self.jet1_eta_sr1,  WF)
        if self.jet1_phi_sr1 is not None:   self.h_jet1_phi_sr1[0]   .Fill(self.jet1_phi_sr1,  WF)
        if self.jet2_pT_sr1 is not None:    self.h_jet2_pT_sr1[0]    .Fill(self.jet2_pT_sr1,   WF)
        if self.jet2_eta_sr1 is not None:   self.h_jet2_eta_sr1[0]   .Fill(self.jet2_eta_sr1,  WF)
        if self.jet2_phi_sr1 is not None:   self.h_jet2_phi_sr1[0]   .Fill(self.jet2_phi_sr1,  WF)
        
        if self.jet1_pT_sr2 is not None:    self.h_jet1_pT_sr2[0]    .Fill(self.jet1_pT_sr2,   WF)
        if self.jet1_eta_sr2 is not None:   self.h_jet1_eta_sr2[0]   .Fill(self.jet1_eta_sr2,  WF)
        if self.jet1_phi_sr2 is not None:   self.h_jet1_phi_sr2[0]   .Fill(self.jet1_phi_sr2,  WF)
        if self.jet2_pT_sr2 is not None:    self.h_jet2_pT_sr2[0]    .Fill(self.jet2_pT_sr2,   WF)
        if self.jet2_eta_sr2 is not None:   self.h_jet2_eta_sr2[0]   .Fill(self.jet2_eta_sr2,  WF)
        if self.jet2_phi_sr2 is not None:   self.h_jet2_phi_sr2[0]   .Fill(self.jet2_phi_sr2,  WF)
        if self.jet3_pT_sr2 is not None:    self.h_jet3_pT_sr2[0]    .Fill(self.jet3_pT_sr2,   WF)
        if self.jet3_eta_sr2 is not None:   self.h_jet3_eta_sr2[0]   .Fill(self.jet3_eta_sr2,  WF)
        if self.jet3_phi_sr2 is not None:   self.h_jet3_phi_sr2[0]   .Fill(self.jet3_phi_sr2,  WF)
        
        ##For ZCRs##
        if self.jet1_pT_Zcr1 is not None:    self.h_jet1_pT_Zcr1[0]    .Fill(self.jet1_pT_Zcr1,   WF)
        if self.jet1_eta_Zcr1 is not None:   self.h_jet1_eta_Zcr1[0]   .Fill(self.jet1_eta_Zcr1,  WF)
        if self.jet1_phi_Zcr1 is not None:   self.h_jet1_phi_Zcr1[0]   .Fill(self.jet1_phi_Zcr1,  WF)
        if self.jet2_pT_Zcr1 is not None:    self.h_jet2_pT_Zcr1[0]    .Fill(self.jet2_pT_Zcr1,   WF)
        if self.jet2_eta_Zcr1 is not None:   self.h_jet2_eta_Zcr1[0]   .Fill(self.jet2_eta_Zcr1,  WF)
        if self.jet2_phi_Zcr1 is not None:   self.h_jet2_phi_Zcr1[0]   .Fill(self.jet2_phi_Zcr1,  WF)
        
        if self.jet1_pT_Zcr2 is not None:    self.h_jet1_pT_Zcr2[0]    .Fill(self.jet1_pT_Zcr2,   WF)
        if self.jet1_eta_Zcr2 is not None:   self.h_jet1_eta_Zcr2[0]   .Fill(self.jet1_eta_Zcr2,  WF)
        if self.jet1_phi_Zcr2 is not None:   self.h_jet1_phi_Zcr2[0]   .Fill(self.jet1_phi_Zcr2,  WF)
        if self.jet2_pT_Zcr2 is not None:    self.h_jet2_pT_Zcr2[0]    .Fill(self.jet2_pT_Zcr2,   WF)
        if self.jet2_eta_Zcr2 is not None:   self.h_jet2_eta_Zcr2[0]   .Fill(self.jet2_eta_Zcr2,  WF)
        if self.jet2_phi_Zcr2 is not None:   self.h_jet2_phi_Zcr2[0]   .Fill(self.jet2_phi_Zcr2,  WF)
        if self.jet3_pT_Zcr2 is not None:    self.h_jet3_pT_Zcr2[0]    .Fill(self.jet3_pT_Zcr2,   WF)
        if self.jet3_eta_Zcr2 is not None:   self.h_jet3_eta_Zcr2[0]   .Fill(self.jet3_eta_Zcr2,  WF)
        if self.jet3_phi_Zcr2 is not None:   self.h_jet3_phi_Zcr2[0]   .Fill(self.jet3_phi_Zcr2,  WF)
        
        if self.ZhadronRecoil1 is not None:  self.h_ZhadronRecoil1[0]  .Fill(self.ZhadronRecoil1,  WF)
        if self.Zmass1 is not None:          self.h_Zmass1[0]          .Fill(self.Zmass1,          WF)
        if self.ZpT1 is not None:            self.h_ZpT1[0]            .Fill(self.ZpT1,            WF)
        if self.ZhadronRecoil2 is not None:  self.h_ZhadronRecoil2[0]  .Fill(self.ZhadronRecoil2,  WF)
        if self.Zmass2 is not None:          self.h_Zmass2[0]          .Fill(self.Zmass2,          WF)
        if self.ZpT2 is not None:            self.h_ZpT2[0]            .Fill(self.ZpT2,            WF)
        if self.mu1_pT_Zcr1 is not  None:   self.h_mu1_pT_Zcr1[0]      .Fill(self.mu1_pT_Zcr1,     WF)
        if self.mu2_pT_Zcr1 is not  None:   self.h_mu2_pT_Zcr1[0]      .Fill(self.mu2_pT_Zcr1,     WF)
        if self.el1_pT_Zcr1 is not  None:   self.h_el1_pT_Zcr1[0]      .Fill(self.el1_pT_Zcr1,     WF)
        if self.el2_pT_Zcr1 is not  None:   self.h_el2_pT_Zcr1[0]      .Fill(self.el2_pT_Zcr1,     WF)
        if self.mu1_eta_Zcr1 is not None:   self.h_mu1_eta_Zcr1[0]     .Fill(self.mu1_eta_Zcr1,    WF)
        if self.mu2_eta_Zcr1 is not None:   self.h_mu2_eta_Zcr1[0]     .Fill(self.mu2_eta_Zcr1,    WF)
        if self.el1_eta_Zcr1 is not None:   self.h_el1_eta_Zcr1[0]     .Fill(self.el1_eta_Zcr1,    WF)
        if self.el2_eta_Zcr1 is not None:   self.h_el2_eta_Zcr1[0]     .Fill(self.el2_eta_Zcr1,    WF)
        if self.mu1_phi_Zcr1 is not None:   self.h_mu1_phi_Zcr1[0]     .Fill(self.mu1_phi_Zcr1,    WF)
        if self.mu2_phi_Zcr1 is not None:   self.h_mu1_phi_Zcr1[0]     .Fill(self.mu1_phi_Zcr1,    WF)
        if self.el1_phi_Zcr1 is not None:   self.h_el1_phi_Zcr1[0]     .Fill(self.el1_phi_Zcr1,    WF)
        if self.el2_phi_Zcr1 is not None:   self.h_el2_phi_Zcr1[0]     .Fill(self.el2_phi_Zcr1,    WF)
        if self.mu1_iso_Zcr1 is not None:   self.h_mu1_iso_Zcr1[0]     .Fill(self.mu1_iso_Zcr1,    WF)
        if self.mu2_iso_Zcr1 is not None:   self.h_mu2_iso_Zcr1[0]     .Fill(self.mu2_iso_Zcr1,    WF)
        
        if self.mu1_pT_Zcr2 is not  None:   self.h_mu1_pT_Zcr2[0]      .Fill(self.mu1_pT_Zcr2,     WF)
        if self.mu2_pT_Zcr2 is not  None:   self.h_mu2_pT_Zcr2[0]      .Fill(self.mu2_pT_Zcr2,     WF)
        if self.el1_pT_Zcr2 is not  None:   self.h_el1_pT_Zcr2[0]      .Fill(self.el1_pT_Zcr2,     WF)
        if self.el2_pT_Zcr2 is not  None:   self.h_el2_pT_Zcr2[0]      .Fill(self.el2_pT_Zcr2,     WF)
        if self.mu1_eta_Zcr2 is not None:   self.h_mu1_eta_Zcr2[0]     .Fill(self.mu1_eta_Zcr2,    WF)
        if self.mu2_eta_Zcr2 is not None:   self.h_mu2_eta_Zcr2[0]     .Fill(self.mu2_eta_Zcr2,    WF)
        if self.el1_eta_Zcr2 is not None:   self.h_el1_eta_Zcr2[0]     .Fill(self.el1_eta_Zcr2,    WF)
        if self.el2_eta_Zcr2 is not None:   self.h_el2_eta_Zcr2[0]     .Fill(self.el2_eta_Zcr2,    WF)
        if self.mu1_phi_Zcr2 is not None:   self.h_mu1_phi_Zcr2[0]     .Fill(self.mu1_phi_Zcr2,    WF)
        if self.mu2_phi_Zcr2 is not None:   self.h_mu1_phi_Zcr2[0]     .Fill(self.mu1_phi_Zcr2,    WF)
        if self.el1_phi_Zcr2 is not None:   self.h_el1_phi_Zcr2[0]     .Fill(self.el1_phi_Zcr2,    WF)
        if self.el2_phi_Zcr2 is not None:   self.h_el2_phi_Zcr2[0]     .Fill(self.el2_phi_Zcr2,    WF)
        if self.mu1_iso_Zcr2 is not None:   self.h_mu1_iso_Zcr2[0]     .Fill(self.mu1_iso_Zcr2,    WF)
        if self.mu2_iso_Zcr2 is not None:   self.h_mu2_iso_Zcr2[0]     .Fill(self.mu2_iso_Zcr2,    WF)
        
        if self.jet1_csv_Zcr1 is not None:    self.h_jet1_csv_Zcr1[0]    .Fill(self.jet1_csv_Zcr1,   WF)
        if self.jet2_csv_Zcr1 is not None:    self.h_jet2_csv_Zcr1[0]    .Fill(self.jet2_csv_Zcr1,   WF)
        if self.jet1_csv_Zcr2 is not None:    self.h_jet1_csv_Zcr2[0]    .Fill(self.jet1_csv_Zcr2,   WF)
        if self.jet2_csv_Zcr2 is not None:    self.h_jet2_csv_Zcr2[0]    .Fill(self.jet2_csv_Zcr2,   WF)
        if self.jet3_csv_Zcr2 is not None:    self.h_jet3_csv_Zcr2[0]    .Fill(self.jet3_csv_Zcr2,   WF)
        
        ##For WCRs##
        if self.jet1_pT_Wcr1 is not None:    self.h_jet1_pT_Wcr1[0]    .Fill(self.jet1_pT_Wcr1,   WF)
        if self.jet1_eta_Wcr1 is not None:   self.h_jet1_eta_Wcr1[0]   .Fill(self.jet1_eta_Wcr1,  WF)
        if self.jet1_phi_Wcr1 is not None:   self.h_jet1_phi_Wcr1[0]   .Fill(self.jet1_phi_Wcr1,  WF)
        if self.jet2_pT_Wcr1 is not None:    self.h_jet2_pT_Wcr1[0]    .Fill(self.jet2_pT_Wcr1,   WF)
        if self.jet2_eta_Wcr1 is not None:   self.h_jet2_eta_Wcr1[0]   .Fill(self.jet2_eta_Wcr1,  WF)
        if self.jet2_phi_Wcr1 is not None:   self.h_jet2_phi_Wcr1[0]   .Fill(self.jet2_phi_Wcr1,  WF)
        
        if self.jet1_pT_Wcr2 is not None:    self.h_jet1_pT_Wcr2[0]    .Fill(self.jet1_pT_Wcr2,   WF)
        if self.jet1_eta_Wcr2 is not None:   self.h_jet1_eta_Wcr2[0]   .Fill(self.jet1_eta_Wcr2,  WF)
        if self.jet1_phi_Wcr2 is not None:   self.h_jet1_phi_Wcr2[0]   .Fill(self.jet1_phi_Wcr2,  WF)
        if self.jet2_pT_Wcr2 is not None:    self.h_jet2_pT_Wcr2[0]    .Fill(self.jet2_pT_Wcr2,   WF)
        if self.jet2_eta_Wcr2 is not None:   self.h_jet2_eta_Wcr2[0]   .Fill(self.jet2_eta_Wcr2,  WF)
        if self.jet2_phi_Wcr2 is not None:   self.h_jet2_phi_Wcr2[0]   .Fill(self.jet2_phi_Wcr2,  WF)
        if self.jet3_pT_Wcr2 is not None:    self.h_jet3_pT_Wcr2[0]    .Fill(self.jet3_pT_Wcr2,   WF)
        if self.jet3_eta_Wcr2 is not None:   self.h_jet3_eta_Wcr2[0]   .Fill(self.jet3_eta_Wcr2,  WF)
        if self.jet3_phi_Wcr2 is not None:   self.h_jet3_phi_Wcr2[0]   .Fill(self.jet3_phi_Wcr2,  WF)
        
        if self.WhadronRecoil1 is not None:   self.h_WhadronRecoil1[0]   .Fill(self.WhadronRecoil1,  WF)
        if self.Wmass1 is not None:           self.h_Wmass1[0]           .Fill(self.Wmass1,          WF)
        if self.WpT1 is not None:             self.h_WpT1[0]             .Fill(self.WpT1,            WF)
        if self.WhadronRecoil2 is not None:   self.h_WhadronRecoil2[0]   .Fill(self.WhadronRecoil2,  WF)
        if self.Wmass2 is not None:           self.h_Wmass2[0]           .Fill(self.Wmass2,          WF)
        if self.WpT2 is not None:             self.h_WpT2[0]             .Fill(self.WpT2,            WF)
        if self.mu1_pT_Wcr1 is not None:      self.h_mu1_pT_Wcr1[0]      .Fill(self.mu1_pT_Wcr1,     WF)
        if self.el1_pT_Wcr1 is not None:      self.h_el1_pT_Wcr1[0]      .Fill(self.el1_pT_Wcr1,     WF)
        if self.mu1_eta_Wcr1 is not None:     self.h_mu1_eta_Wcr1[0]     .Fill(self.mu1_eta_Wcr1,    WF) 
        if self.el1_eta_Wcr1 is not None:     self.h_el1_eta_Wcr1[0]     .Fill(self.el1_eta_Wcr1,    WF)
        if self.mu1_phi_Wcr1 is not None:     self.h_mu1_phi_Wcr1[0]     .Fill(self.mu1_phi_Wcr1,    WF)
        if self.el1_phi_Wcr1 is not None:     self.h_el1_phi_Wcr1[0]     .Fill(self.el1_phi_Wcr1,    WF)
        if self.mu1_iso_Wcr1 is not None:     self.h_mu1_iso_Wcr1[0]     .Fill(self.mu1_iso_Wcr1,    WF)
        
        if self.mu1_pT_Wcr2 is not None:      self.h_mu1_pT_Wcr2[0]      .Fill(self.mu1_pT_Wcr2,     WF)
        if self.el1_pT_Wcr2 is not None:      self.h_el1_pT_Wcr2[0]      .Fill(self.el1_pT_Wcr2,     WF)
        if self.mu1_eta_Wcr2 is not None:     self.h_mu1_eta_Wcr2[0]     .Fill(self.mu1_eta_Wcr2,    WF) 
        if self.el1_eta_Wcr2 is not None:     self.h_el1_eta_Wcr2[0]     .Fill(self.el1_eta_Wcr2,    WF)
        if self.mu1_phi_Wcr2 is not None:     self.h_mu1_phi_Wcr2[0]     .Fill(self.mu1_phi_Wcr2,    WF)
        if self.el1_phi_Wcr2 is not None:     self.h_el1_phi_Wcr2[0]     .Fill(self.el1_phi_Wcr2,    WF)
        if self.mu1_iso_Wcr2 is not None:     self.h_mu1_iso_Wcr2[0]     .Fill(self.mu1_iso_Wcr2,    WF)
        
        if self.jet1_csv_Wcr1 is not None:    self.h_jet1_csv_Wcr1[0]    .Fill(self.jet1_csv_Wcr1,   WF)
        if self.jet2_csv_Wcr1 is not None:    self.h_jet2_csv_Wcr1[0]    .Fill(self.jet2_csv_Wcr1,   WF)
        if self.jet1_csv_Wcr2 is not None:    self.h_jet1_csv_Wcr2[0]    .Fill(self.jet1_csv_Wcr2,   WF)
        if self.jet2_csv_Wcr2 is not None:    self.h_jet2_csv_Wcr2[0]    .Fill(self.jet2_csv_Wcr2,   WF)
        if self.jet3_csv_Wcr2 is not None:    self.h_jet3_csv_Wcr2[0]    .Fill(self.jet3_csv_Wcr2,   WF)
        
        ##For TopCRs##
        if self.jet1_pT_TOPcr1 is not None:    self.h_jet1_pT_TOPcr1[0]    .Fill(self.jet1_pT_TOPcr1,   WF)
        if self.jet1_eta_TOPcr1 is not None:   self.h_jet1_eta_TOPcr1[0]   .Fill(self.jet1_eta_TOPcr1,  WF)
        if self.jet1_phi_TOPcr1 is not None:   self.h_jet1_phi_TOPcr1[0]   .Fill(self.jet1_phi_TOPcr1,  WF)
        if self.jet2_pT_TOPcr1 is not None:    self.h_jet2_pT_TOPcr1[0]    .Fill(self.jet2_pT_TOPcr1,   WF)
        if self.jet2_eta_TOPcr1 is not None:   self.h_jet2_eta_TOPcr1[0]   .Fill(self.jet2_eta_TOPcr1,  WF)
        if self.jet2_phi_TOPcr1 is not None:   self.h_jet2_phi_TOPcr1[0]   .Fill(self.jet2_phi_TOPcr1,  WF)
        
        if self.jet1_pT_TOPcr2 is not None:    self.h_jet1_pT_TOPcr2[0]    .Fill(self.jet1_pT_TOPcr2,   WF)
        if self.jet1_eta_TOPcr2 is not None:   self.h_jet1_eta_TOPcr2[0]   .Fill(self.jet1_eta_TOPcr2,  WF)
        if self.jet1_phi_TOPcr2 is not None:   self.h_jet1_phi_TOPcr2[0]   .Fill(self.jet1_phi_TOPcr2,  WF)
        if self.jet2_pT_TOPcr2 is not None:    self.h_jet2_pT_TOPcr2[0]    .Fill(self.jet2_pT_TOPcr2,   WF)
        if self.jet2_eta_TOPcr2 is not None:   self.h_jet2_eta_TOPcr2[0]   .Fill(self.jet2_eta_TOPcr2,  WF)
        if self.jet2_phi_TOPcr2 is not None:   self.h_jet2_phi_TOPcr2[0]   .Fill(self.jet2_phi_TOPcr2,  WF)
        if self.jet3_pT_TOPcr2 is not None:    self.h_jet3_pT_TOPcr2[0]    .Fill(self.jet3_pT_TOPcr2,   WF)
        if self.jet3_eta_TOPcr2 is not None:   self.h_jet3_eta_TOPcr2[0]   .Fill(self.jet3_eta_TOPcr2,  WF)
        if self.jet3_phi_TOPcr2 is not None:   self.h_jet3_phi_TOPcr2[0]   .Fill(self.jet3_phi_TOPcr2,  WF)
        
        if self.mu1_pT_TOPcr1 is not None:      self.h_mu1_pT_TOPcr1[0]      .Fill(self.mu1_pT_TOPcr1,     WF)
        if self.el1_pT_TOPcr1 is not None:      self.h_el1_pT_TOPcr1[0]      .Fill(self.el1_pT_TOPcr1,     WF)
        if self.mu1_eta_TOPcr1 is not None:     self.h_mu1_eta_TOPcr1[0]     .Fill(self.mu1_eta_TOPcr1,    WF) 
        if self.el1_eta_TOPcr1 is not None:     self.h_el1_eta_TOPcr1[0]     .Fill(self.el1_eta_TOPcr1,    WF)
        if self.mu1_phi_TOPcr1 is not None:     self.h_mu1_phi_TOPcr1[0]     .Fill(self.mu1_phi_TOPcr1,    WF)
        if self.el1_phi_TOPcr1 is not None:     self.h_el1_phi_TOPcr1[0]     .Fill(self.el1_phi_TOPcr1,    WF)
        if self.mu1_iso_TOPcr1 is not None:     self.h_mu1_iso_TOPcr1[0]     .Fill(self.mu1_iso_TOPcr1,    WF)
        
        if self.mu1_pT_TOPcr2 is not None:      self.h_mu1_pT_TOPcr2[0]      .Fill(self.mu1_pT_TOPcr2,     WF)
        if self.el1_pT_TOPcr2 is not None:      self.h_el1_pT_TOPcr2[0]      .Fill(self.el1_pT_TOPcr2,     WF)
        if self.mu1_eta_TOPcr2 is not None:     self.h_mu1_eta_TOPcr2[0]     .Fill(self.mu1_eta_TOPcr2,    WF) 
        if self.el1_eta_TOPcr2 is not None:     self.h_el1_eta_TOPcr2[0]     .Fill(self.el1_eta_TOPcr2,    WF)
        if self.mu1_phi_TOPcr2 is not None:     self.h_mu1_phi_TOPcr2[0]     .Fill(self.mu1_phi_TOPcr2,    WF)
        if self.el1_phi_TOPcr2 is not None:     self.h_el1_phi_TOPcr2[0]     .Fill(self.el1_phi_TOPcr2,    WF)
        if self.mu1_iso_TOPcr2 is not None:     self.h_mu1_iso_TOPcr2[0]     .Fill(self.mu1_iso_TOPcr2,    WF)
        
        if self.TOPRecoil1 is not None:         self.h_TOPRecoil1[0]         .Fill(self.TOPRecoil1,  WF)
        if self.TOPRecoil2 is not None:         self.h_TOPRecoil2[0]         .Fill(self.TOPRecoil2,  WF)
       
        if self.jet1_csv_TOPcr1 is not None:    self.h_jet1_csv_TOPcr1[0]    .Fill(self.jet1_csv_TOPcr1,   WF)
        if self.jet2_csv_TOPcr1 is not None:    self.h_jet2_csv_TOPcr1[0]    .Fill(self.jet2_csv_TOPcr1,   WF)
        if self.jet1_csv_TOPcr2 is not None:    self.h_jet1_csv_TOPcr2[0]    .Fill(self.jet1_csv_TOPcr2,   WF)
        if self.jet2_csv_TOPcr2 is not None:    self.h_jet2_csv_TOPcr2[0]    .Fill(self.jet2_csv_TOPcr2,   WF)
        if self.jet3_csv_TOPcr2 is not None:    self.h_jet3_csv_TOPcr2[0]    .Fill(self.jet3_csv_TOPcr2,   WF)
        
    def WriteHisto(self, (nevts,nevts_weight,cutflowvalues,cutflownames,CRvalues,CRnames)):
        f = TFile(self.rootfilename,'RECREATE')
        print 
        f.cd()
        self.h_total[0].SetBinContent(1,nevts)
        self.h_total[0].Write()
        
        self.h_total_weight[0].SetBinContent(1,nevts_weight)
        self.h_total_weight[0].Write()
        
        ncutflow=len(cutflowvalues)
        self.h_cutflow=TH1F('h_cutflow_','h_cutflow_',ncutflow, 0, ncutflow)                          # Cutflow         
        for icutflow in range(len(cutflowvalues)):
            self.h_cutflow.GetXaxis().SetBinLabel(icutflow+1,cutflownames[icutflow])
            self.h_cutflow.SetBinContent(icutflow+1,cutflowvalues[icutflow])
        self.h_cutflow.Write()
        
        nCR=len(CRvalues)
        self.h_CRs=TH1F('h_CRs_','h_CRs_',nCR, 0, nCR)                          # Cutflow         
        for iCR in range(nCR):
            self.h_CRs.GetXaxis().SetBinLabel(iCR+1,CRnames[icutflow])
            self.h_CRs.SetBinContent(iCR+1,CRvalues[iCR])
        self.h_CRs.Write()
        
        self.h_met[0].Write()
        #self.h_met_rebin[iregime].Write()
        for ipdf in range(2):
            self.h_met_pdf[0][ipdf].Write()
        for imuR in range(2):
            self.h_met_muR[0][imuR].Write()
        for imuF in range(2):
            self.h_met_muF[0][imuF].Write()

        #self.h_met_vs_mass.Write()

        #self.h_mass.Write()
        #self.h_csv1.Write()
        #self.h_csv2.Write()
        #self.h_mt.Write()
        #self.h_dPhi.Write()
        self.h_N_e[0].Write()
        self.h_N_mu[0].Write()
        self.h_N_tau[0].Write()
        self.h_N_Pho[0].Write()
        #self.h_N_b.Write()
        self.h_N_j.Write()
        #self.h_mass.Write()
        self.h_jet1_pT_sr1[0].Write()
        self.h_jet1_eta_sr1[0].Write()
        self.h_jet1_phi_sr1[0].Write()
        self.h_jet2_pT_sr1[0].Write()
        self.h_jet2_eta_sr1[0].Write()
        self.h_jet2_phi_sr1[0].Write()
        self.h_jet1_pT_sr2[0].Write()
        self.h_jet1_eta_sr2[0].Write()
        self.h_jet1_phi_sr2[0].Write()
        self.h_jet2_pT_sr2[0].Write()
        self.h_jet2_eta_sr2[0].Write()
        self.h_jet2_phi_sr2[0].Write()
        self.h_jet3_pT_sr2[0].Write()
        self.h_jet3_eta_sr2[0].Write()
        self.h_jet3_phi_sr2[0].Write()
         #for ZCR
        self.h_jet1_pT_Zcr1[0].Write()
        self.h_jet1_eta_Zcr1[0].Write()
        self.h_jet1_phi_Zcr1[0].Write()
        self.h_jet2_pT_Zcr1[0].Write()
        self.h_jet2_eta_Zcr1[0].Write()
        self.h_jet2_phi_Zcr1[0].Write()
        self.h_jet1_pT_Zcr2[0].Write()
        self.h_jet1_eta_Zcr2[0].Write()
        self.h_jet1_phi_Zcr2[0].Write()
        self.h_jet2_pT_Zcr2[0].Write()
        self.h_jet2_eta_Zcr2[0].Write()
        self.h_jet2_phi_Zcr2[0].Write()
        self.h_jet3_pT_Zcr2[0].Write()
        self.h_jet3_eta_Zcr2[0].Write()
        self.h_jet3_phi_Zcr2[0].Write()
        self.h_ZhadronRecoil1[0].Write()
        self.h_Zmass1[0].Write()
        self.h_ZpT1[0].Write()
        self.h_ZhadronRecoil2[0].Write()
        self.h_Zmass2[0].Write()
        self.h_ZpT2[0].Write()
        self.h_mu1_pT_Zcr1[0].Write()
        self.h_mu2_pT_Zcr1[0].Write()
        self.h_el1_pT_Zcr1[0].Write()
        self.h_el2_pT_Zcr1[0].Write()
        self.h_mu1_eta_Zcr1[0].Write()
        self.h_mu2_eta_Zcr1[0].Write()
        self.h_el1_eta_Zcr1[0].Write()
        self.h_el2_eta_Zcr1[0].Write()
        self.h_mu1_phi_Zcr1[0].Write()
        self.h_mu2_phi_Zcr1[0].Write()
        self.h_el1_phi_Zcr1[0].Write()
        self.h_el2_phi_Zcr1[0].Write()
        self.h_mu1_iso_Zcr1[0].Write()
        self.h_mu2_iso_Zcr1[0].Write()
        
        self.h_jet1_csv_Zcr1[0].Write()
        self.h_jet2_csv_Zcr1[0].Write()
        self.h_jet1_csv_Zcr2[0].Write()
        self.h_jet2_csv_Zcr2[0].Write()
        self.h_jet3_csv_Zcr2[0].Write()
        
        self.h_mu1_pT_Zcr2[0].Write()
        self.h_mu2_pT_Zcr2[0].Write()
        self.h_el1_pT_Zcr2[0].Write()
        self.h_el2_pT_Zcr2[0].Write()
        self.h_mu1_eta_Zcr2[0].Write()
        self.h_mu2_eta_Zcr2[0].Write()
        self.h_el1_eta_Zcr2[0].Write()
        self.h_el2_eta_Zcr2[0].Write()
        self.h_mu1_phi_Zcr2[0].Write()
        self.h_mu2_phi_Zcr2[0].Write()
        self.h_el1_phi_Zcr2[0].Write()
        self.h_el2_phi_Zcr2[0].Write()
        self.h_mu1_iso_Zcr2[0].Write()
        self.h_mu2_iso_Zcr2[0].Write()
        
        #for WCR
        self.h_jet1_pT_Wcr1[0].Write()
        self.h_jet1_eta_Wcr1[0].Write()
        self.h_jet1_phi_Wcr1[0].Write()
        self.h_jet2_pT_Wcr1[0].Write()
        self.h_jet2_eta_Wcr1[0].Write()
        self.h_jet2_phi_Wcr1[0].Write()
        self.h_jet1_pT_Wcr2[0].Write()
        self.h_jet1_eta_Wcr2[0].Write()
        self.h_jet1_phi_Wcr2[0].Write()
        self.h_jet2_pT_Wcr2[0].Write()
        self.h_jet2_eta_Wcr2[0].Write()
        self.h_jet2_phi_Wcr2[0].Write()
        self.h_jet3_pT_Wcr2[0].Write()
        self.h_jet3_eta_Wcr2[0].Write()
        self.h_jet3_phi_Wcr2[0].Write()
        self.h_WhadronRecoil1[0].Write()
        self.h_Wmass1[0].Write()
        self.h_WpT1[0].Write()
        self.h_WhadronRecoil2[0].Write()
        self.h_Wmass2[0].Write()
        self.h_WpT2[0].Write()
        self.h_mu1_pT_Wcr1[0].Write()
        self.h_el1_pT_Wcr1[0].Write()
        self.h_mu1_eta_Wcr1[0].Write()
        self.h_el1_eta_Wcr1[0].Write()
        self.h_mu1_phi_Wcr1[0].Write()
        self.h_el1_phi_Wcr1[0].Write()
        self.h_mu1_iso_Wcr1[0].Write()
        self.h_mu1_pT_Wcr2[0].Write()
        self.h_el1_pT_Wcr2[0].Write()
        self.h_mu1_eta_Wcr2[0].Write()
        self.h_el1_eta_Wcr2[0].Write()
        self.h_mu1_phi_Wcr2[0].Write()
        self.h_el1_phi_Wcr2[0].Write()
        self.h_mu1_iso_Wcr2[0].Write()
        
        self.h_jet1_csv_Wcr1[0].Write()
        self.h_jet2_csv_Wcr1[0].Write()
        self.h_jet1_csv_Wcr2[0].Write()
        self.h_jet2_csv_Wcr2[0].Write()
        self.h_jet3_csv_Wcr2[0].Write()
        
        #for TOPcr
        self.h_jet1_pT_TOPcr1[0].Write()
        self.h_jet1_eta_TOPcr1[0].Write()
        self.h_jet1_phi_TOPcr1[0].Write()
        self.h_jet2_pT_TOPcr1[0].Write()
        self.h_jet2_eta_TOPcr1[0].Write()
        self.h_jet2_phi_TOPcr1[0].Write()
        self.h_jet1_pT_TOPcr2[0].Write()
        self.h_jet1_eta_TOPcr2[0].Write()
        self.h_jet1_phi_TOPcr2[0].Write()
        self.h_jet2_pT_TOPcr2[0].Write()
        self.h_jet2_eta_TOPcr2[0].Write()
        self.h_jet2_phi_TOPcr2[0].Write()
        self.h_jet3_pT_TOPcr2[0].Write()
        self.h_jet3_eta_TOPcr2[0].Write()
        self.h_jet3_phi_TOPcr2[0].Write()
        self.h_TOPRecoil1[0].Write()
        self.h_TOPRecoil2[0].Write()
        self.h_mu1_pT_TOPcr1[0].Write()
        self.h_el1_pT_TOPcr1[0].Write()
        self.h_mu1_eta_TOPcr1[0].Write()
        self.h_el1_eta_TOPcr1[0].Write()
        self.h_mu1_phi_TOPcr1[0].Write()
        self.h_el1_phi_TOPcr1[0].Write()
        self.h_mu1_iso_TOPcr1[0].Write()
        self.h_mu1_pT_TOPcr2[0].Write()
        self.h_el1_pT_TOPcr2[0].Write()
        self.h_mu1_eta_TOPcr2[0].Write()
        self.h_el1_eta_TOPcr2[0].Write()
        self.h_mu1_phi_TOPcr2[0].Write()
        self.h_el1_phi_TOPcr2[0].Write()
        self.h_mu1_iso_TOPcr2[0].Write()
        
        self.h_jet1_csv_TOPcr1[0].Write()
        self.h_jet2_csv_TOPcr1[0].Write()
        self.h_jet1_csv_TOPcr2[0].Write()
        self.h_jet2_csv_TOPcr2[0].Write()
        self.h_jet3_csv_TOPcr2[0].Write()
