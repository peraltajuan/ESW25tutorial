from fodMC.pyfodmc import pyfodmc
from fodMC.pyfodmc.mol2fodmc import mol2fodmc
from rdkit import Chem
from rdkit.Chem import rdDetermineBonds
from rdkit.Chem import AllChem


smiles = "CC=O"
mol = Chem.MolFromSmiles(smiles)
molH =Chem.rdmolops.AddHs(mol)

AllChem.EmbedMolecule(molH)
AllChem.UFFOptimizeMolecule(molH)

rdDetermineBonds.DetermineBonds(molH,charge=0)


m = smiles+".mol"
Chem.MolToMolFile(molH, m )


mol2fodmc(m)
tmp_name = str(m).split('/')[-1].split('.')[0]
output_name = m.split('/')[-1].replace('.mol','_fodMC.xyz')


pyfodmc.get_guess('PyFLOSIC',output_name)



#### END ####

# The original code uses "He" for spin-down FODs. We want to change them to Z to visualize them in Vesta.

import os

with open(smiles+'_fodMC.xyz', 'r') as file:
    file_data = file.read().replace('He ', 'Z  ')
with open(smiles+'_fodMC.xyz', 'w') as file:
    file.write(file_data)


