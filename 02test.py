from fodMC.pyfodmc import pyfodmc
from fodMC.pyfodmc.mol2fodmc import mol2fodmc
from rdkit import Chem
from rdkit.Chem import rdDetermineBonds

name ='acetaldehyde'

xyz = Chem.MolFromXYZFile(name+'.xyz')
mol = Chem.Mol(xyz)
rdDetermineBonds.DetermineBonds(mol,charge=0)


m = name+".mol"
Chem.MolToMolFile(mol, m )

mol2fodmc(m)
output_name = m.split('/')[-1].replace('.mol','_fodMC.xyz')


pyfodmc.get_guess('PyFLOSIC',output_name)


#### END ####

# The original code uses "He" for spin-down FODs. We want to change them to Z to visualize them in Vesta.

import os

with open(name+'_fodMC.xyz', 'r') as file:
    file_data = file.read().replace('He ', 'Z  ')
with open(name+'_fodMC.xyz', 'w') as file:
    file.write(file_data)


