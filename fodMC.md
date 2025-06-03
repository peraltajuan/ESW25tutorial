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


<!--- ***

<> **Install atomic simulation environment (ASE) package:**

ASE is a library for atomistic modeling and simulation. We will use it 

`python3.10 -m pip install ase`
-->



***

** Example 01 **
Download the file 

