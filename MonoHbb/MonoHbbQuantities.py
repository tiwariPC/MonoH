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
        #self.N_j             = -10
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
        


        self.h_mt              = []
        #self.h_dPhi            = []
        self.h_N_e             = []
        self.h_N_mu            = []
        self.h_N_tau           = []
        self.h_N_Pho           = []
        #self.h_N_b             = []
        #self.h_N_j             = []
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
        

        self.h_met.append(TH1F('h_met_',  'h_met_',  1000,0.,1000.))
        

        #metbins_ = [200,350,500,1000]
        #self.h_met_rebin.append(TH1F('h_met_rebin_'+postname,  'h_met_rebin'+postname,  3, array(('d'),metbins_)))

        #self.h_mass.append(TH1F('h_mass_'+postname, 'h_mass_'+postname, 400,0.,400.))

        self.h_met_vs_mass.append(TH2F('h_met_vs_mass_', 'h_met_vs_mass_', 1000, 0., 1000., 250, 0, 250.))

        self.h_csv1.append(TH1F('h_csv1_', 'h_csv1_', 20,0.,1.))
        self.h_csv2.append(TH1F('h_csv2_', 'h_csv2_', 20,0.,1.))
        #self.h_mt.append(TH1F('h_mt_'+postname,'h_mt_'+postname,100,400.,1400.))
        #self.h_dPhi.append(TH1F('h_dPhi_'+postname,'h_dPhi_'+postname,70, -3.5, 3.5 ))
        self.h_N_e.append(TH1F('h_N_e_','h_N_e_',3,0,3))
        self.h_N_mu.append(TH1F('h_N_mu_','h_N_mu_',3,0,3))
        self.h_N_tau.append(TH1F('h_N_tau_','h_N_tau_',3,0,3))
        self.h_N_Pho.append(TH1F('h_N_Pho_','h_N_Pho_',3,0,3))
        #self.h_N_b.append(TH1F('h_N_b_'+postname,'h_N_b_'+postname,3,0,3))
        #self.h_N_j.append(TH1F('h_N_j_'+postname,'h_N_j_'+postname,5,0,5))
        #self.h_jet1_pT_sr1.append(TH1F('h_jet1_pT_sr1_'+postname,'h_jet1_pT_sr1_'+postname,1000,0.,1000.))
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

        print "histo defined"
        
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
        

        self.h_met_vs_mass .Fill(self.met, self.mass, WF)

        #self.h_mass           Fill(self.mass,      WF)
        self.h_csv1           .Fill(self.csv1,      WF)
        self.h_csv2           .Fill(self.csv2,      WF)
        self.h_mt             .Fill(self.mt,        WF)
        #self.h_dPhi           Fill(self.dPhi,      WF)
        self.h_N_e            .Fill(self.N_e,       WF)
        self.h_N_mu           .Fill(self.N_mu,      WF)
        self.h_N_tau          .Fill(self.N_tau,     WF)
        self.h_N_Pho          .Fill(self.N_Pho,     WF)
        #self.h_N_b            Fill(self.N_b,       WF)
        #self.h_N_j            Fill(self.N_j,       WF)
        self.h_jet1_pT_sr1    .Fill(self.jet1_pT_sr1,    WF)
        self.h_jet1_eta_sr1   .Fill(self.jet1_eta_sr1,  WF)
        self.h_jet1_phi_sr1   .Fill(self.jet1_phi_sr1,  WF)
        self.h_jet2_pT_sr1    .Fill(self.jet2_pT_sr1,  WF)
        self.h_jet2_eta_sr1   .Fill(self.jet2_eta_sr1,  WF)
        self.h_jet2_phi_sr1   .Fill(self.jet2_phi_sr1,  WF)
        self.h_jet1_pT_sr2    .Fill(self.jet1_pT_sr2,  WF)
        self.h_jet1_eta_sr2   .Fill(self.jet1_eta_sr2,  WF)
        self.h_jet1_phi_sr2   .Fill(self.jet1_phi_sr2,  WF)
        self.h_jet2_pT_sr2    .Fill(self.jet2_pT_sr2,  WF)
        self.h_jet2_eta_sr2   .Fill(self.jet2_eta_sr2,  WF)
        self.h_jet2_phi_sr2   .Fill(self.jet2_phi_sr2,  WF)
        self.h_jet3_pT_sr2    .Fill(self.jet3_pT_sr2,  WF)
        self.h_jet3_eta_sr2   .Fill(self.jet3_eta_sr2,  WF)
        self.h_jet3_phi_sr2   .Fill(self.jet3_phi_sr2,  WF)
        
        
    def WriteHisto(self, (nevts,nevts_weight)):
        f = TFile(self.rootfilename,'RECREATE')
        f.cd()
        self.h_total[0].SetBinContent(1,nevts)
        self.h_total[0].Write()
        
        self.h_total_weight[0].SetBinContent(1,nevts_weight)
        self.h_total_weight[0].Write()
        
        self.h_met[0].Write()
        #self.h_met_rebin[iregime].Write()
        for ipdf in range(101):
            self.h_met_pdf[0][ipdf].Write()
        for imuR in range(2):
            self.h_met_muR[0][imuR].Write()
        for imuF in range(2):
            self.h_met_muF[0][imuF].Write()

        self.h_met_vs_mass.Write()

        #self.h_mass.Write()
        self.h_csv1.Write()
        self.h_csv2.Write()
        self.h_mt.Write()
        #self.h_dPhi.Write()
        self.h_N_e.Write()
        self.h_N_mu.Write()
        self.h_N_tau.Write()
        self.h_N_Pho.Write()
        #self.h_N_b.Write()
        #self.h_N_j.Write()
        #self.h_mass.Write()
        self.h_jet1_pT_sr1.Write()
        self.h_jet1_eta_sr1.Write()
        self.h_jet1_phi_sr1.Write()
        self.h_jet2_pT_sr1.Write()
        self.h_jet2_eta_sr1.Write()
        self.h_jet2_phi_sr1.Write()
        self.h_jet1_pT_sr2.Write()
        self.h_jet1_eta_sr2.Write()
        self.h_jet1_phi_sr2.Write()
        self.h_jet2_pT_sr2.Write()
        self.h_jet2_eta_sr2.Write()
        self.h_jet2_phi_sr2.Write()
        self.h_jet3_pT_sr2.Write()
        self.h_jet3_eta_sr2.Write()
        self.h_jet3_phi_sr2.Write()
