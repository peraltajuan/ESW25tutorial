#!/usr/bin/env python

from niflosic import run_atoms
import mendeleev
import pandas as pd

ionize = 0      # 0-3

summary = run_atoms(slice(5,10),ionize)

PD = pd.DataFrame(summary)

PD = PD.set_axis(['NE', 'SYM', 'SPN','NU','ND','CONV', 'ELECTRON CONFIGURATION'],axis=1)
PD.index.name=None
print(PD)



