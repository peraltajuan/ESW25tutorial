# FOD from QR generator (FODQR) tutorial

Based on 
**work in progress** 
and [this paper](https://doi.org/10.1063/5.0263003) 

<img width="320" alt="image" src="https://github.com/user-attachments/assets/a0350ceb-6114-4181-9fec-f90a8e2bbaf4" />

> [!Note]
> The current code is experimental!

## Table of Contents 

[Installation](/FODQR.md#Instalation)\
[Example 07](/FODQR.md#Example-07)\
[Example 08](/FODQR.md#Example-08)\
[Example 09](/FODQR.md#Example-09)
***

# Instalation


**Install FODQR:**

First, install PySCF: `python3 -m pip install pyscf==2.6.0`.


This is the FODQR code that we will be using:

`python3.11  -m pip install  git+https://{token}@github.com/peraltajuan/niflosic/`

where `{token}` can be copied from [here](https://people.se.cmich.edu/peral1j/token.txt)


***

# Example 07

Use FODQR to generate FODs starting from an xyz file

+ Download the file [07test.py](/07test.py).
+ Run FODQR: `python3.11 07test.py`.
+ The script will read the file `acetaldehyde.xyz` with the atomic coordinates in xyz format.
+ The script generates a folder named acetaldehyde.
+ In that folder, the files `CLUSTER`, `FRMGRP`, `FRMIDT`, and `NRLMOL_INPUT.DAT` are created to run FLOSIC calculations.
+ The file `acetaldehyde.fods.xyz` containss the molecular structure and the FODs for visualization purposes.
+ The file `ini_fod.txt` contains internal information.
+ The file `submit.sb` is also generated as a starting point for cluster submission if needed.

    

+ Visualize using VESTA (or other)

<p align="center" width="100%">
<img width="326" alt="image" src="https://github.com/user-attachments/assets/1c2f1319-1e85-4af9-9a27-4557ef9ca15b" />
</p>

> [!Warning]
> The old folder will be renamed as acetaldehyde-old.

> [!Note]
> What is the difference with the otehr methods?


***


# Example 08

Use FODQR to generate FODs starting from a SMILES string

+ Download the file [08test.py](/08test.py).
+ Run FODQR: `python3.11 08test.py`.




***



# Example 09: Atoms

Use FODQR to generate FODs for a list of atoms.

+ Download the file [09test.py](/09test.py).
+ Run FODQR: `python3 09test.py`.
+ The script runs a list of atoms (in this case B through Ne) and generates all the folders as in the previous examples.
+ The script also prints some atomic experimental information from the Mendeleev package (to install use `python3 -m pip install mendeleev==0.15.0`).
+ You can control the ionization state by changing the `ionize` variable in the script.

> [!Note]
> The xyz file omits the atom for easier visualization.

***





