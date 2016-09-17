#!/usr/bin/env python                                                                                                                                                                
#from MonoHBranchReader import AnalyzeDataSet, CheckFilter, MakeTable, DeltaR, Phi_mpi_pi
import os

inputfilename = os.environ['INPUT']
outfilename   = os.environ['OUTPUT']

os.system('./MonoHBranchReader.py  -m 100 -M 150 -i '+inputfilename+' -o '+outfilename+'  -a -j 0 -J 2 -l 0 -L 1 -F')

