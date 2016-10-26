import ROOT
ROOT.gROOT.LoadMacro('Loader.h+')

vi2 = ROOT.std.vector('int')()
vi3 = ROOT.std.vector('int')()
for i in range(5):
    vi2.push_back(i**2)
    vi3.push_back(i**3)

vvi = ROOT.std.vector('std::vector<int>')()

vvi.push_back(vi2)
vvi.push_back(vi3)

f = ROOT.TFile("testfile.root","RECREATE")
t = ROOT.TTree('t','t')
t.Branch('vi2',vi2)
t.Branch('vi3',vi3)
t.Branch('vvi',vvi)

t.Fill()
ROOT.gDirectory.Write()
f.Close()
