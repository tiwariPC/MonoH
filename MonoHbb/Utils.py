from ROOT import TFile, TH1F


prefix = 'AnalysisHistograms_MergedSkimmedV11_V10/signal/'
whichregion='sigmal'

histdirname = ''
lumi = 12900 

## We can set the efficiency for each sample here which can be used later on for the plotting which would be very easy, quick and useful. 
samples={
    ## data 
    'data_obs' : {
        'order' : 0,
        'files' : ['Merged_MET-SkimTree.root'],
        'xsec'      : [1.],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Data",
        'weight': [1.],
        'plot': True,
        },
    
    ## TT-Bar
    'TT' : {
        'order' : 0,
        'files' : ['Merged_TT_TuneCUETP8M1_13TeV-powheg-pythia8-SkimTree.root'],
        'xsec'      : [831.76],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t}",
        'weight': [1.],
        'plot': True,
        },
    
    ## Z ->nunu + Jets
    ## Fixme: last 4 cross-sections are wrong at this moment. 
    'znunujets' : {
        'order' : 0,
        'files' : ['Merged_ZJetsToNuNu_HT-100To200_13TeV-madgraph-SkimTree.root','Merged_ZJetsToNuNu_HT-200To400_13TeV-madgraph-SkimTree.root','Merged_ZJetsToNuNu_HT-400To600_13TeV-madgraph-SkimTree.root','Merged_ZJetsToNuNu_HT-600To800_13TeV-madgraph-SkimTree.root','Merged_ZJetsToNuNu_HT-800To1200_13TeV-madgraph-SkimTree.root','Merged_ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-SkimTree.root','Merged_ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [1.626*280.47, 1.617*78.36, 1.459*10.94, 1.391*4.203, 1.391*4.203, 1.391*4.203, 1.391*4.203],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t}",
        'weight': [1.,1.,1.,1.,1.0,1.0,1.0],
        'plot': True,
        },

    ## W + Jets
    'wjets' : {
        'order' : 0,
        'files' : ['Merged_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root','Merged_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root','Merged_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root','Merged_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root','Merged_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root','Merged_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root','Merged_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root'],
        'xsec'      : [1.459*1347., 1.434*360., 1.532*48.9, 1.004*12.8, 1.004*5.26, 1.004*1.33, 1.004*0.03089],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t}",
        'weight': [1.,1.,1., 1.,1.,1., 1.],
        'plot': True,
        },


    ## Diboson
    'VV' : {
        'order' : 0,
        'files' : ['Merged_WW_TuneCUETP8M1_13TeV-pythia8-SkimTree.root','Merged_WZ_TuneCUETP8M1_13TeV-pythia8-SkimTree.root','Merged_ZZ_TuneCUETP8M1_13TeV-pythia8-SkimTree.root'],
        'xsec'      : [118.7, 66.1, 15.4],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t}",
        'weight': [1.,1.,1.],
        'plot': True,
        },


    ## ZH
    'ZH' : {
        'order' : 0,
        'files' : ['Merged_ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8-SkimTree.root'],
        'xsec'      : [0.8696*0.577*0.2],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "ZH",
        'weight': [1.],
        'plot': True,
        },

    ## Single Top
    'ST' : {
        'order' : 0,
        'files' : ['Merged_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-SkimTree.root','Merged_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1-SkimTree.root','Merged_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-SkimTree.root','Merged_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-SkimTree.root'],
        'xsec'      : [3.36, 26.38, 35.6, 35.6],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Single Top",
        'weight': [1.,1.,1.,1.,1.],
        'plot': True,
        },


    ## ATLAS cross-section times BR
    ## Sigmal
    'signal600_300' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph-SkimTree.root'],
        #'xsec'      : [0.2147594],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal800_300' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph-SkimTree.root'],
        #'xsec'      : [0.13309659],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1000_300' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph-SkimTree.root'],
        #'xsec'      : [0.06885918],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1200_300' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph-SkimTree.root'],
        #'xsec'      : [0.036382158],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1400_300' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph-SkimTree.root'],
        #'xsec'      : [0.019927272],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1700_300' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph-SkimTree.root'],
        #'xsec'      : [0.008659039],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2000_300' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph-SkimTree.root'],
        #'xsec'      : [0.0040214592],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2500_300' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph-SkimTree.root'],
        #'xsec'      : [0.0012504744],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },



    ## 1 pb as cross and 0.577 as BR
    ## Sigmal for 2D Scan
    'signal600_400' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal800_400' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1000_400' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    #### Sigmal
    'signal1200_400' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1400_400' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1700_400' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-400_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2000_400' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2500_400' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## 1 pb as cross and 0.577 as BR
    ## Sigmal for 2D Scan

    ## Sigmal
    'signal800_500' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1000_500' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1200_500' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1400_500' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1700_500' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2000_500' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2500_500' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },


## 1 pb as cross and 0.577 as BR
    ## Sigmal for 2D Scan

    ## Sigmal
    'signal800_600' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1000_600' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1200_600' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1400_600' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1700_600' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    ## Fixme
    'signal2000_600' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2500_600' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },


    ## 1 pb as cross and 0.577 as BR
    ## Sigmal for 2D Scan

    ## Sigmal
    #'signal1000_700' : {
    #    'order' : 0,
    #    'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph-SkimTree.root'],
    #    'xsec'      : [0.577],
    #    'fillcolor' : 2,
    #    'fillstyle' : 1,
    #    'linecolor' : 1,
    #    'linewidth' : 2,
    #    'linestyle' : 1,
    #    'label' : "",
    #    'weight': [1.],
    #    'plot': True,
    #    },

    ## Sigmal
    'signal1200_700' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1400_700' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1700_700' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2000_700' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2500_700' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },


    ## 1 pb as cross and 0.577 as BR
    ## Sigmal for 2D Scan

    ## Sigmal
    'signal1000_800' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1200_800' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1400_800' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal1700_800' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2000_800' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    ## Sigmal
    'signal2500_800' : {
        'order' : 0,
        'files' : ['Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph-SkimTree.root'],
        'xsec'      : [0.577],
        'fillcolor' : 2,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "",
        'weight': [1.],
        'plot': True,
        },

    }


def FindIntegral(filename):
    filename = prefix + '/' + filename
    infile_ = TFile(filename,'READ')
    h_mJ = TH1F()
    histname = 'h_met_0'
    h_mJ = infile_.Get(histname)
    h_total = infile_.Get('h_total_weight')
    return [h_mJ.Integral(),h_total.Integral()]

    
##############################################################
## Loop over all files and fill weights and cross-sections
##############################################################
def setweights():
    for isample in samples:
        #print 'isample = ', isample
        ixsec=0
        for ifile in samples[isample]['files']:
            #print ifile 
            integral_ =  FindIntegral(ifile)
            weight = samples[isample]['xsec'][ixsec] * lumi  / integral_[1]
            #print "ifile = ", ifile
            if samples[isample] != 'data_obs': samples[isample]['weight'][ixsec] = weight
            if samples[isample] == 'data_obs': samples[isample]['weight'][ixsec] = 1.0
            
            ixsec=ixsec+1
    return 0




if __name__ == "__main__":
    print ("running the models of Util.py directly to test them. ")
    setweights()
    print "samples = ",samples
else :
    print ("Utils.py is being imported as a module......")
        
