import sys 
import os 
if len(sys.argv) < 2 :
    print "insufficient options provided see help function "
    exit (1)

if len(sys.argv) > 1 :
    print ('You are running limits for ')
    for i in range(len(sys.argv)):
        print sys.argv[i]




dirname=sys.argv[1]


nargv = len(sys.argv) -2
print nargv
print sys.argv[2]
regions=[]
for iargv in range(0,nargv):
    if sys.argv[iargv+2] != 'runlimit':
        if sys.argv[iargv+2] != 'obs':
            regions.append(sys.argv[iargv+2])
    
print regions
ZpB_NameList = ['signalMZp_500_Mdm_1',
                'signalMZp_500_Mdm_150',
                'signalMZp_500_Mdm_500',
                
                'signalMZp_1000_Mdm_1',
                'signalMZp_1000_Mdm_150',
                'signalMZp_995_Mdm_500',
                #'signalMZp_1000_Mdm_1000',                                                                                                                                      

                'signalMZp_10000_Mdm_1',
                'signalMZp_10000_Mdm_10',
                'signalMZp_10000_Mdm_50',
                'signalMZp_10000_Mdm_150',
                'signalMZp_10000_Mdm_500',
                'signalMZp_10000_Mdm_1000',
                
                #'signalMZp_10_Mdm_1',                                                                                                                                           
                'signalMZp_10_Mdm_10',
                'signalMZp_10_Mdm_50',
                'signalMZp_10_Mdm_150',
                'signalMZp_10_Mdm_500',
                'signalMZp_10_Mdm_1000',
                
                'signalMZp_15_Mdm_10',
                
                'signalMZp_1995_Mdm_1000',
                'signalMZp_2000_Mdm_1',
                'signalMZp_2000_Mdm_500',
                
                'signalMZp_200_Mdm_1',
                'signalMZp_200_Mdm_50',
                'signalMZp_200_Mdm_150',
                
                'signalMZp_20_Mdm_1',
                
                'signalMZp_300_Mdm_1',
                #'signalMZp_300_Mdm_50',                                                                                                                                         
                'signalMZp_295_Mdm_150',
                
                
                'signalMZp_50_Mdm_1',
                'signalMZp_50_Mdm_10',
                'signalMZp_50_Mdm_50',
                
                ]


#os.system('mkdir -p oneplustwo')
for imass in ZpB_NameList:
    checkname= 'dummy'
    allregions=[]
    for iregion in regions:
        checkname = dirname+'/'+iregion+'_DataCard_'+imass+'GeV_MonoHbb_13TeV.txt'
        print checkname
        print ('checkname ', checkname, bool(os.path.exists(checkname)))
        tmpname = iregion+'='+checkname+' '
        print (imass, tmpname)
        allregions.append(tmpname)
        print 'inside inner loop'
    rateparm='rateparam.txt'
    
    if len(regions)>0:
        if not bool(os.path.exists(checkname)): continue 

    splusbFitdir = dirname
    datacardnamefit=splusbFitdir+'/DataCard_S_Plus_B_M'+imass+'GeV_MonoHbb_13TeV.txt'
    tmpdcard = 'tmpcard.txt'
    if len(regions)==0:
        if not bool(os.path.exists(datacardnamefit)): continue
        
    ###
    allcards = ''.join(allregions)
    print allcards
    if (len(sys.argv) >= 2) & (not ('runlimit' in sys.argv )) :
        os.system('combineCards.py  '+allcards+' >& '+tmpdcard)
        os.system('cat '+tmpdcard+' '+rateparm+' >& '+  datacardnamefit)
        
    nargv = len(sys.argv)
    if sys.argv[nargv-1] == 'runlimit':
        print ('combine -M Asymptotic '+datacardnamefit+' -t -1')
        os.system('combine -M Asymptotic '+datacardnamefit+' -t -1')
        os.system('mv higgsCombineTest.Asymptotic.mH120.root '+dirname+'/higgsCombineTest_Asymptotic_'+imass+'GeV_MonoHbb_13TeV.root')

    if ((str(sys.argv[nargv-1]) == 'runlimit') & (str(sys.argv[nargv-2]) == 'obs')) | ((str(sys.argv[nargv-2]) == 'runlimit') & (str(sys.argv[nargv-1]) == 'obs')) :
        print ('combine -M Asymptotic '+datacardnamefit)
        os.system('combine -M Asymptotic '+datacardnamefit)
        os.system('mv higgsCombineTest.Asymptotic.mH120.root '+dirname+'/higgsCombineTest_Asymptotic_'+imass+'GeV_MonoHbb_13TeV.root')

        
