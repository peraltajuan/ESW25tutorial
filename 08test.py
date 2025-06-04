#!/usr/bin/env python
from niflosic.niflosic import run_dft
from niflosic.niflosic import submit_flosic


smiles = "O=CC#CCN"
run_dft(smiles,smiles='smiles',spin=0,charge=0)
submit_flosic(smiles)



