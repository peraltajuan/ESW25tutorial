from fodMC.pyfodmc import pyfodmc
from fodMC.pyfodmc.mol2fodmc import mol2fodmc
from rdkit import Chem
from rdkit.Chem import rdDetermineBonds
from rdkit.Chem import AllChem


smiles = "O=CC#CCN"
mol = Chem.MolFromSmiles(smiles)
molH =Chem.rdmolops.AddHs(mol)

AllChem.EmbedMolecule(molH)
AllChem.UFFOptimizeMolecule(molH)

#rdDetermineBonds.DetermineBonds(mol,charge=0)


m = smiles+".mol"
Chem.MolToMolFile(molH, m )


mol2fodmc(m)
tmp_name = str(m).split('/')[-1].split('.')[0]
output_name = m.split('/')[-1].replace('.mol','_FOD.xyz')


pyfodmc.get_guess('PyFLOSIC',output_name)


