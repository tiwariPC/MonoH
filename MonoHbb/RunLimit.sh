which=$1 ## name of the directory where .root files are saved 
whichmode="cms"  ## mode with which you want to run the code: cms: atlas: comb  
postfix=$2
root -l -b -q plot_Asymptotic_Limit.C\(\"$which\",\"$whichmode\",\"$postfix\"\)