import sys
import os
import ROOT
ROOT.gROOT.SetBatch(True)  



if len(sys.argv) < 4 :
    print "insufficient options provided see help function "
    exit (1)

if len(sys.argv) == 4 :
    print ('You are makeing datacards for '+sys.argv[1]+' and datacards will be saved in '+sys.argv[2])


#inputtextfilename='TwoSubJets.txt'
#dirtosave='twosubjets'
inputtextfilename=sys.argv[1]
dirtosave=sys.argv[2]
rootfilename=sys.argv[3]
datacrdPrefix=sys.argv[4]
os.system('mkdir -p '+dirtosave)

## prepare template datacard and store in this variable. 
## do whatever change you want to do 
## and keep variables in capital letters with prefix "T" e.g. signal strength can be written as TSIGNAL and DYJets can be TDYJETS
## these can be replaced by either a python or shell script to make datacards for a specific mass point and analysis. 
templatecard='''
imax    1       number of channels
jmax    *       number of backgrounds
kmax    *       number of nuisance parameters (sources of systematical uncertainties)

-------------------------------------------------------------------------------------------------

shapes *     MONOHBB  ROOTFILENAME $PROCESS $PROCESS_$SYSTEMATIC

-------------------------------------------------------------------------------------------------
bin                      MONOHBB
observation              DATARATE

-------------------------------------------------------------------------------------------------

bin                      MONOHBB   MONOHBB    MONOHBB    MONOHBB    MONOHBB    MONOHBB
process                  SIGNALNAME       DYJETS      WJETS      ZH          TT        DIBOSON 

-------------------------------------------------------------------------------------------------

process                  0                1          2             3          4         5  

rate                SIGNALRATE       DYJETSRATE    WJETSRATE    ZHRATE      TTRATE    DIBOSONRATE 

-------------------------------------------------------------------------------------------------

######################   #### #########  Sig   DYJet  WJets  ZH       TT     DIBOSON  
lumi_13TeV                lnN            1.026    -      -     1.026     -      1.026  
pdf_qqbar                 lnN            1.01    -      -     1.01     -      1.01
pdf_gg                    lnN             -      -     -      1.50       -        - 

#CMS_monoHbb_ewk           shape          -      1.0  1.0   -    -    -
#CMS_monoHbb_scaleF        shape          -      1.0  1.0   -    -    -
#CMS_monoHbb_scaleR        shape          -      1.0  1.0   -    -    -

#CMS_monoHbb_scaleF        shape          1.0     -    -    -    -    -
#CMS_monoHbb_scaleR        shape          1.0     -    -    -    -    -

CMS_monoHbb_ewk           lnN          -      1.05  1.05   -    -    -
CMS_monoHbb_scaleF        lnN          -      1.02  1.02   -    -    -
CMS_monoHbb_scaleR        lnN          -      1.02  1.02   -    -    -
CMS_monoHbb_scaleF        lnN          1.02     -    -    -    -    -
CMS_monoHbb_scaleR        lnN          1.02     -    -    -    -    -


CMS_monoHbb_pdf              lnN         -     1.05   1.05   1.05   1.05   1.05
CMS_monoHbb_pdf_sig          lnN         1.05   -     -       -      -      - 
CMS_monoHbb_ToppT            lnN         -      -      -       -     1.20   - 
CMS_monoHbb_metUnclusteredEn lnN         1.05   1.05   1.05   1.05   1.05   1.05


QCDscale_VH               lnN            1.04    -      -     1.04     -        - 
QCDscale_VV               lnN             -      -      -     -        -      1.04

CMS_monoHbb_ST               lnN             -      -      -      -       1.25     - 
CMS_monoHbb_VV               lnN             -      -      -      -       -      1.25
CMS_monoHbb_eff_b            lnN            1.07    -      -    1.07      -      1.07
CMS_monoHbb_fake_b_13TeV     lnN            1.03    -      -    1.03      -        - 
CMS_monoHbb_res_j            lnN            1.05    1.05   1.05   1.05      1.05      1.05
CMS_monoHbb_scale_j          lnN            1.05    1.05   1.05   1.05      1.05      1.05

CMS_monoHbb_HMassShower      lnN            1.07    1.07    -      -         -         -
CMS_monoHbb_HMass            lnN            1.10/0.90  0.90/1.10  -    -     -         -



CMS_monoHbb_WHFunc         lnN             -      -     1.10   -        -        - 
#CMS_monoHbb_Wjets_SF         lnN             -      -     1.10   -        -        - 
#CMS_monoHbb_DYjets_SF        lnN             -     1.10    -     -        -        -    
#CMS_monoHbb_TT_SF            lnN             -      -      -     -       1.10      - 




CMS_monoHbb_monoH_stat       lnN            SIGNALERRRATE    -      -     -        -        -
CMS_monoHbb_ggZH_stat        lnN             -      -      -    ZHERRRATE      -        - 
CMS_monoHbb_Wjets_stat       lnN            -      -     WJETSERRRATE   -        -        - 
CMS_monoHbb_DYjets_stat      lnN            -      DYJETSERRRATE   -     -        -        - 
CMS_monoHbb_TT_stat          lnN            -      -      -     -       TTERRRATE      -
CMS_monoHbb_VV_stat          lnN            -      -      -     -        -      DIBOSONERRRATE


#SIGNALNAME_stat_bin1       shape           1.0    -      -     -       -       -
#SIGNALNAME_stat_bin2       shape           1.0    -      -     -       -       -
#SIGNALNAME_stat_bin3       shape           1.0    -      -     -       -       -
#
#DYJETS_stat_bin1           shape           -      1.0    -     -       -       -
#DYJETS_stat_bin2           shape           -      1.0    -     -       -       -
#DYJETS_stat_bin3           shape           -      1.0    -     -       -       -
#
#WJETS_stat_bin1           shape           -       -     1.0    -        -      -
#WJETS_stat_bin2           shape           -       -     1.0    -        -      -
#WJETS_stat_bin3           shape           -       -     1.0    -        -      -
#
#ZH_stat_bin1             shape           -       -     -      1.0      -      - 
#ZH_stat_bin2             shape           -       -     -      1.0      -      - 
#ZH_stat_bin3             shape           -       -     -      1.0      -      - 
#
#TT_stat_bin1             shape           -       -     -       -       1.0   -     
#TT_stat_bin2             shape           -       -     -       -       1.0   -     
#TT_stat_bin3             shape           -       -     -       -       1.0   -     
#
#DIBOSON_stat_bin1        shape           -       -     -       -       -     1.0
#DIBOSON_stat_bin2        shape           -       -     -       -       -     1.0
#DIBOSON_stat_bin3        shape           -       -     -       -       -     1.0


CMS_monoHbb_trigger_MET      lnN          1.03     -      -    1.03      -      1.03


######################   #### #########  Sig   DYJet  WJets  ZH       TT     DIBOSON  
'''

## template datacard ends here 

## Write templat datacard to the text file with placeholders.
##
datacard = open('DataCard_MXXXGeV.txt','w')
datacard.write(templatecard)
datacard.close()

## Function to provide the normalization weight factors
def Normalize(n,xs,tot):
    yield_ = n*xs*1./tot
    return yield_



## map of placeholder used in the Template datacard.
## This is analysis specific.
nameinnumber=['TT',
              'DIBOSON',
              'ZH',
              'DYJETS',
              'WJETS',
              'DATA']

## List of signal samples for which limit is needed. 
## This is analysis specific.
a0masspoints=['300',
              '400',
              '500',
              '600',
              '700',
              '800']
              

signalnameinnumber=[ 'monoHbbM600_300',
                     'monoHbbM800_300',
                     'monoHbbM1000_300',
                     'monoHbbM1200_300',
                     'monoHbbM1400_300',
                     'monoHbbM1700_300',
                     'monoHbbM2000_300',
                     'monoHbbM2500_300',
                     
                     'monoHbbM600_400',
                     'monoHbbM800_400',
                     'monoHbbM1000_400',
                     'monoHbbM1200_400',
                     'monoHbbM1400_400',
                     'monoHbbM1700_400',
                     'monoHbbM2000_400',
                     'monoHbbM2500_400',
                     
                     #'monoHbbM600_500',
                     'monoHbbM800_500',
                     'monoHbbM1000_500',
                     'monoHbbM1200_500',
                     'monoHbbM1400_500',
                     'monoHbbM1700_500',
                     'monoHbbM2000_500',
                     'monoHbbM2500_500',
                     
                     #'monoHbbM600_600',
                     'monoHbbM800_600',
                     'monoHbbM1000_600',
                     'monoHbbM1200_600',
                     'monoHbbM1400_600',
                     'monoHbbM1700_600',
                     'monoHbbM2000_600',
                     'monoHbbM2500_600',
                     
                     #'monoHbbM600_700',
                     #'monoHbbM800_700',
                     #'monoHbbM1000_700',
                     'monoHbbM1200_700',
                     'monoHbbM1400_700',
                     'monoHbbM1700_700',
                     'monoHbbM2000_700',
                     'monoHbbM2500_700',
                     
                     #'monoHbbM600_800',
                     #'monoHbbM800_800',
                     'monoHbbM1000_800',
                     'monoHbbM1200_800',
                     'monoHbbM1400_800',
                     'monoHbbM1700_800',
                     'monoHbbM2000_800',
                     'monoHbbM2500_800'
                     
                     
                     ]


## create the names of place RATE holders
placeholder = [x + "RATE" for x in nameinnumber]
placeholdererr = [x + "ERRRATE" for x in nameinnumber]
## print placeholder
print placeholder
print placeholdererr


## valuemap for background and signal with a default value
valuemap = {
    "default" : 0.0
    }

valuemaperr = {
    "default" : 0.0
    }

signalvaluemap = {
    "default" : 0.0
    }

signalvaluemaperr = {
    "default" : 0.0
    }

## Read the signal background numbers from plain TEXTFile
## this value map is used later to get the datacard by replacing the
## place holders with values stored in this map.
numbers = open(inputtextfilename,'r')
for iline in numbers:
    a,b,c = iline.split()
    for iname in range(len(nameinnumber)):
        if a==nameinnumber[iname]:
            stringtoprint = nameinnumber[iname]+" value is "+b
            #print "stringtoprint=",stringtoprint
            ratename = nameinnumber[iname]+"RATE"
            valuemap[ratename]=b
            if float(b) > 0. : valuemaperr[ratename]=str(1.0 + round( float(c)/float(b), 2) )
            if float(b) == 0 : valuemaperr[ratename]=str(1.0)
    ### Following lines fill the 
    ### value map for signal points
    for isigname in range(len(signalnameinnumber)):
        if a==signalnameinnumber[isigname]:
            stringtoprint = signalnameinnumber[isigname]+" value is "+b
            #print "stringtoprint = ",stringtoprint
            ratename = signalnameinnumber[isigname]+"RATE"
            signalvaluemap[ratename]=b
            if float(b) > 0. : signalvaluemaperr[ratename]= str(1.0 + round(float(c)/float(b), 2) )
            if float(b) == 0 : signalvaluemaperr[ratename]= str(1.0 )
        

#print valuemap
#print valuemaperr
#print signalvaluemap
#print signalvaluemaperr

## Method to access the rootfiles
## Use it to clone and then 
#sigTFile = ROOT.TFile('Merged_DMHistosSpring15_1/main-NCUGlobalTuples_M1500.root','READ')
#sigEvent  = sigTFile.Get('CutFlowAndEachCut/h_cutflow_0')
#sigTEvent = sigTFile.Get('nEvents')
#print sigEvent.GetBinContent(7)
#scaledsig = Normalize(sigEvent.GetBinContent(7), SignalXS['M1500'],sigTEvent.GetEntries())
#print scaledsig


def MakeDataCard(masspoint, a0massvalue):
    datacard = open('DataCard_MXXXGeV.txt','r')
    newdatacardname = dirtosave+'/'+datacrdPrefix+'_DataCard_'+masspoint+'GeV_MonoHbb_13TeV.txt'
    os.system('rm '+newdatacardname)
    datacard600 = open(newdatacardname,'w')
    
    for line in datacard:
        ## replace the background values.
        for ival in range(len(placeholder)):
            line = line.replace(placeholder[ival],valuemap[placeholder[ival]])
            line = line.replace(placeholdererr[ival],valuemaperr[placeholder[ival]])
        
        ## replace the signal values
        masspointrate = masspoint + "RATE"
        line = line.replace('SIGNALRATE', signalvaluemap[masspointrate])
        name = str(masspoint)
        line = line.replace('SIGNALNAME',name)
        line = line.replace('SIGNALERRRATE', signalvaluemaperr[masspointrate])
        line = line.replace('ROOTFILENAME',rootfilename)
        line = line.replace('kmax 25','kmax 26')
        datacard600.write(line)
    datacard600.close()



## for A0 = 300 GeV
for imasspoint in range(len(signalnameinnumber)):
    MakeDataCard(signalnameinnumber[imasspoint], "_300")


print "datacards produced"





