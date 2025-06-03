from fodMC.pyfodmc import pyfodmc
from fodMC.pyfodmc.mol2fodmc import mol2fodmc
from rdkit import Chem
from rdkit.Chem import rdDetermineBonds

xyz = Chem.MolFromXYZFile('SO2.xyz')
mol = Chem.Mol(xyz)
#rdDetermineBonds.DetermineBonds(mol,charge=0)


m = "SO2.mol"
Chem.MolToMolFile(mol, m )



mol2fodmc("SO2.mol")
tmp_name = str(m).split('/')[-1].split('.')[0]
output_name = m.split('/')[-1].replace('.mol','_FOD.xyz')


pyfodmc.get_guess('PyFLOSIC',output_name)


