#!/usr/bin/env python

from niflosic.niflosic import run_atoms
import mendeleev
import pandas as pd

ionize = 0      # 0-3

atom_list= slice(5,10) # B to Ne

summary = run_atoms(atom_list,ionize)

PD = pd.DataFrame(summary)

PD = PD.set_axis(['NE', 'SYM', 'SPN','NU','ND','CONV', 'ELECTRON CONFIGURATION'],axis=1)
PD.index.name=None
print(PD)



