from fodMC.pyfodmc import pyfodmc

atom = 'C'


pyfodmc.write_pyfodmc_atoms(sys=atom)

pyfodmc.get_guess('PyFLOSIC',atom+ '_fodMC.xyz')
# pyfodmc.get_guess('NRLMOL','')


#### END ####

# The original code uses "He" for spin-down FODs. We want to change them to Z to visualize them in Vesta.
# Use only if the X_fodMC.xyz file exists.


import os

with open(atom+'_fodMC.xyz', 'r') as file:
    file_data = file.read().replace('He ', 'Z  ')
with open(atom+'_fodMC.xyz', 'w') as file:
    file.write(file_data)


