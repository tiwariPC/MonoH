storepath=/hdfs/store/user/khurana/Raman/SkimmedTuples/
dirname=$1
mkdir /nfs_scratch/khurana/Raman/Merged_Skim/$dirname
filename=dirname_raman.txt
rm $filename
fullpath=$storepath/$dirname
ls -1 $fullpath >& $filename
for which in `less $filename`
do 
    files=`find  $fullpath/$which  -name "*.root" | gawk '{ORS=" "}{print $1}'`
    hadd Merged_${which}.root $files
    mv Merged_${which}.root /nfs_scratch/khurana/Raman/Merged_Skim/$dirname
done 

#cd $dirname
#hadd Merged_MET.root Merged_crab_MET*
#cd ..
