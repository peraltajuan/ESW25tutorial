from fodMC.pyfodmc import pyfodmc

# Simple test for a molecule

sys = 'acetaldehyde'

con_mat = ['(1-2)-(1-1)',
           '(2-3)-(1-1)',
           '(2-4)-(1-1)',
           '(2-5)-(1-1)',
           '(5-6)-(1-1)',
           '(5-7)-(2-2)\n']
pyfodmc.write_pyfodmc_molecules(sys=sys+'.xyz',con_mat=con_mat)
# Fortran call
pyfodmc.get_guess('PyFLOSIC',sys+'_fodMC.xyz')

#### END ####

# The original code uses "He" for spin-down FODs. We want to change them to Z to visualize them in Vesta.

import os

with open(sys+'_fodMC.xyz', 'r') as file:
    file_data = file.read().replace('He ', 'Z  ')
with open(sys+'_fodMC.xyz', 'w') as file:
    file.write(file_data)

