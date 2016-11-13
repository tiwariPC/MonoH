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
massvec=['600','800','1000','1200','1400','1700','2000','2500']
a0massvec=['300','400','500','600','700','800']
#os.system('mkdir -p oneplustwo')
for imass in range(len(massvec)):
    for ia0mass in a0massvec:
        
        bb='SR='+dirname+'/signal_DataCard_monoHbbM'+(str(massvec[imass]))+'_'+ia0mass+'GeV_MonoHbb_13TeV.txt '
        znunu='ZbCR='+dirname+'/zj_DataCard_monoHbbM'+(str(massvec[imass]))+'_'+ia0mass+'GeV_MonoHbb_13TeV.txt '
        #wjets='WbCR='+dirname+'/wj_DataCard_monoHbbM'+(str(massvec[imass]))+'_'+ia0mass+'GeV_MonoHbb_13TeV.txt '
        #tt='ttCR='+dirname+'/tt_DataCard_monoHbbM'+(str(massvec[imass]))+'_'+ia0mass+'GeV_MonoHbb_13TeV.txt '
        wt='wtCR='+dirname+'/wt_DataCard_monoHbbM'+(str(massvec[imass]))+'_'+ia0mass+'GeV_MonoHbb_13TeV.txt '
        rateparm='rateparam.txt'
        
        #allcards=bb+znunu+wjets+tt
        allcards=bb+znunu+wt


        splusbFitdir = dirname
        
        datacardnamefit=splusbFitdir+'/DataCard_S_Plus_B_M'+(str(massvec[imass]))+'_'+ia0mass+'GeV_MonoHbb_13TeV.txt'
       
        tmpdcard = 'tmpcard.txt'
        os.system('combineCards.py  '+allcards+' >& '+tmpdcard)
        os.system('cat '+tmpdcard+' '+rateparm+' >& '+  datacardnamefit)
        '''
        tmpdcard = 'tmpcard.txt'
        dcard = open(datacardname,'r')
        dcardnew = open(tmpdcard ,'w')
        
        for line in dcard:
            line = line.replace(dirname+'/','')
            line = line.replace('kmax 45','kmax 45')
            dcardnew.write(line)
            
            
        dcard.close()
        dcardnew.close()
        

        
        
        print ('combine -M Asymptotic '+datacardnamefit)
        os.system('combine -M Asymptotic '+datacardnamefit)
        os.system('mv higgsCombineTest.Asymptotic.mH120.root '+dirname+'/higgsCombineTest_Asymptotic_'+(str(massvec[imass]))+'_'+ia0mass+'GeV_MonoHbb_13TeV.root')
        '''
    #os.system('mv ')

