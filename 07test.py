#!/usr/bin/env python
from niflosic.niflosic import run_dft
from niflosic.niflosic import submit_flosic
import numpy as np


filename = 'acetaldehyde'

run_dft(filename,smiles='xyz',spin=0,charge=0)  

submit_flosic(filename)



