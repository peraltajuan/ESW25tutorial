# FOD from QR generator (FODQR) tutorial

Based on work in progress and [this paper](https://doi.org/10.1063/5.0263003) 

<img width="719" alt="image" src="https://github.com/user-attachments/assets/a0350ceb-6114-4181-9fec-f90a8e2bbaf4" />



## Table of Contents 

[Installation](/FODQR.md#Instalation)\
[Example 07](/FODQR.md#Example-07)
[Example 08](/FODQR.md#Example-08)

***

# Instalation


**Install FODQR:**

This is the FODQR code that we will be using.

`python3.11  -m pip install  git+https://{token}@github.com/peraltajuan/niflosic/`

where `{token}` can be copied from [here](https://people.se.cmich.edu/peral1j/token.txt)


***

# Example 07

Use FODQR to generate FODs starting from an xyz file

+ Dowload 
python3.11 07test.py
+ The script will read the file `SO2.xyz` with the atomic coordinates in xyz format.
+ The script generates a file `lego.xyz` with the atomic coordinates plus the FODs.
+ The script generates a `FRMORB` and a `CLUSTER` files to run FLOSIC calculations.
> [!NOTE]
>The code only considers closed-shell cases and  FODs are labeled as X in the xyz file.  

+ Visualize using VESTA (or other)


> [!Warning]
>Files `lego.xyz`, `FRMORB`, and `CLUSTER` will be overwritten.


***

# Example 06

Use FODLego to generate FODs starting from a SMILES string

+ Run `fodlego "O=CC#CCN"`
+ The script will generate the molecular structure and FODs.
+ The script generates a file `lego.xyz` with the atomic coordinates plus the FODs.
+ The script generates a `FRMORB` and a `CLUSTER` files to run FLOSIC calculations.

+ Visualize using VESTA (or other)

> [!NOTE]
>Repeat the generation of FODs but using the "O=S=O" SMILES string. What is the difference with the previous FODs?



***







