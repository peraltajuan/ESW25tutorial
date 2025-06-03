# FOD Monte-Carlo generator (fodMC) tutorial



Available at
https://gitlab.com/opensic/fodMC


***

**It needs a FORTRAN compiler installed**

Macs: Install homebrew (https://brew.sh) 

After brew is installed:

`brew install gfortran` (takes a few minutes)

Linux:

Check that a FORTRAN version is installed

***

**Install fodMC:**

This is the fodMC code that we will be using.

`python3.10 -m pip install fodMC`

> [!TIP]
> for some MAcs you may need:
> 
> `python3.10 -m pip install wheel`
> 
> `python3.10 -m pip install --no-build-isolation fodMC`


***

**Install RDKit:**

RDKit is a toolkit for cheminformatics. We will use it to extract bonding information, to manipulate molecular files, and to convert SMILES (Simplified Molecular Input Line Entry System)
to 3D molecules. 


`python3.10  -m pip install rdkit`


***

**Install atomic simulation environment (ASE) package:**

ASE is a library for atomistic modeling and simulation. We will use it 

`python3.10 -m pip install ase`




***

** Example 01 **
Download the file [01test.py](/01test.py)

+ Use an xyz file and add the “connectivity” by hand. In this case it is already in the python script.
+ Run fodMC: `python3 01test.py`
+ The script will read the file `SO2.xyz` with the atomic coordinates in xyz format.
+ The script generates a file `S)2_FOD.xyz` with the atomic coordinates plus the FODs.
  + >[!Note]
    >The spin-up FODs are labeled as X and the spin-down as He.  
+ Visualize using VESTA (or other)

***

** Example 02 **
Download the file [02test.py](/02test.py)



***

** Example 03 **
Download the file [03test.py](/03test.py)





