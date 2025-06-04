#!/usr/bin/env python
from niflosic import run_dft
from niflosic import submit_flosic
import numpy as np



smiles = "O=CC#CCN"
run_dft(smiles,smiles='smiles',spin=0,charge=0)
submit_flosic(smiles)



