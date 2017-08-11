
        ## list comprehensation
        ## for SR1
            ''' 2 jets and 1 btagged 
            '''
            cutsr1[1] += 1
            nJetsr1 = (len(THINnJets) <= 2)
            if nJetsr1 == False  : continue
            cutStatus['njetSR1'] += 1
            for ithinjet in range(THINnJets):
               j1 = thinjetP4[ithinjet]
               if (j1.Pt() > 30.0) & (DeltaPhi(j1.Phi(),pfpuppiMETPhi) > 0.5):
                   njet1SR1index = ithinjet
                   h_jet1_pT_sr1.Fill(j1.Pt())
                   h_jet1_eta_sr1.Fill(j1.Eta())
                   h_jet1_phi_sr1.Fill(j1.Phi())
                   for jthinjet in range(THINnJets):
                        if (jthinjet != ithinjet ) & ( jthinjet > ithinjet ) & (jthinjet < nTHINJets) : 
                            j2 = thinjetP4[jthinjet]
                            if (j2.Pt() < 50.0) : continue
                            if (DeltaPhi(j1.Phi,pfpuppiMETPhi) < 0.5) :continue
                            if (THINjetCISVV2[jthinjet] < 0.8): continue 
                            if thinjetnhadef[jthinjet] > 0.8 : continue
                            if THINjetCHadEF[jthinjet]< 0.1: continue
                            njet1SR1index = jthinjet
                            h_jet2_pT_sr1.Fill(j2.Pt())
                            h_jet2_eta_sr1.Fill(j2.Eta())
                            h_jet2_phi_sr1.Fill(j2.Phi())
            if njet1SR1index > -1 :
               cutStatus['njet1SR1'] += 1
            if njet1SR1index > -1 :
               cutStatus['njet2SR1'] += 1
        
        ## for SR2
            ''' 3 jets and 2 btagged 
            '''
            nJetsr2 = (len(THINnJets) <= 3)
            if nJetsr2 == False : continue
            cutStatus['njetSR2'] += 1
            for ithinjet in range(THINnJets):
                j1 = thinjetP4[ithinjet]
                if (j1.Pt() > 30.0) & (DeltaPhi(j1.Phi(),pfpuppiMETPhi) > 0.5):
                   njet1SR2index = ithinjet
                   h_jet1_pT_sr2.Fill(j1.Pt())
                   h_jet1_eta_sr2.Fill(j1.Eta())
                   h_jet1_phi_sr2.Fill(j1.Phi())
                   for jthinjet in range(THINnJets):
                        if (jthinjet != ithinjet ) & ( jthinjet > ithinjet ) & (jthinjet < nTHINJets) : 
                            j2 = thinjetP4[jthinjet]
                            if (j2.Pt() < 50.0) : continue
                            if (DeltaPhi(j2.Phi,pfpuppiMETPhi) < 0.5) :continue
                            if (THINjetCISVV2[jthinjet] < 0.8): continue 
                            if thinjetnhadef[jthinjet] > 0.8 : continue
                            if THINjetCHadEF[jthinjet]< 0.1: continue
                            njet2SR2index = jthinjet
                            h_jet2_pT_sr2.Fill(j2.Pt())
                            h_jet2_eta_sr2.Fill(j2.Eta())
                            h_jet2_phi_sr2.Fill(j2.Phi())
                           for kthinjet in range(THINnJets):
                              if (kthinjet != ithinjet ) & ( kthinjet > ithinjet ) & (kthinjet < nTHINJets) & kthinjet != jthinjet ) & ( kthinjet > jthinjet ): 
                                  j3 = thinjetP4[kthinjet]
                                  if (j3.Pt() < 50.0) : continue
                                  if (DeltaPhi(j3.Phi,pfpuppiMETPhi) < 0.5) :continue
                                  if (THINjetCISVV2[kthinjet] < 0.8): continue 
                                  if thinjetnhadef[kthinjet] > 0.8 : continue
                                  if THINjetCHadEF[kthinjet]< 0.1: continue
                                  njet3SR2index = jthinjet
                                  h_jet3_pT_sr2.Fill(j3.Pt())
                                  h_jet3_eta_sr2.Fill(j3.Eta())
                                  h_jet3_phi_sr2.Fill(j3.Phi())
            if njet1SR2index > -1 :
               cutStatus['njet1SR2'] += 1
            if njet2SR2index > -1 :
               cutStatus['njet2SR2'] += 1
            if njet3SR2index > -1 :
               cutStatus['njet2SR2'] += 1
               
