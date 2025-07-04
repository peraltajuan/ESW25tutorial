# FOD Monte-Carlo generator (fodMC) tutorial

Based on the work published [here](https://doi.org/10.1002/jcc.26062)

<img width="500" alt="image" src="https://github.com/user-attachments/assets/fd799aff-e2cc-4695-a163-80ae83689f91" />


## Table of Contents 

[Installation](/fodMC.md#Instalation)\
[Example 01](/fodMC.md#Example-01)\
[Example 02](/fodMC.md#Example-02)\
[Example 03](/fodMC.md#Example-03)\
[Example 04](/fodMC.md#Example-04)\
[Exercises](/fodMC.md#Exercises)

***

# Instalation

>[!Note]
>The installation instructions may differ for the Ubuntu USB stick.


Available at
https://gitlab.com/opensic/fodMC

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

Or use any Python>=3.10.

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

ASE is a library for atomistic modeling and simulation. We will use it.

`python3.10 -m pip install ase`.




***

# Example 01

Generate FODs from an xyz file and connectivity (bonding) information.

Download the file [01test.py](/01test.py)

+ Use an xyz file and add the “connectivity” by hand. In this case it is already in the python script.
+ Run fodMC: `python3 01test.py`
+ The script will read the file `acetaldehyde.xyz` with the atomic coordinates in xyz format.
+ The script generates a file `acetaldehyde_fodMC.xyz` with the atomic coordinates plus the FODs.
+ The script also generate a file `fodMC.out` with internal information (useful for debugging if needed).
> [!NOTE]
>The spin-up FODs are labeled as X and the spin-down as He in the original fodMC code.
> There is a segment of code in the script at the end that replaces He-->Z in the file.  
+ Visualize using [VESTA](https://jp-minerals.org/vesta/en/). Use `jmol acetaldehyde_fodMC.xyz` in the Ubuntu USB stick.
  
<p align="center" width="100%">
<img width="200" alt="image" src="https://github.com/user-attachments/assets/994e89cb-6d19-43a1-982a-81990f4cce28" />
</p>


> [!Note]
>Are there any FODs inside the atomic sphere representation?

***

# Example 02

Generate FODs from an xyz file

Download the file [02test.py](/02test.py)


+ Now use the xyz file and RDKit to generate the connectivity. There is no need to know the molecular connectivity.
+ Run fodMC: `python3 02test.py`.
+ The script generates two files: `acetaldehyde.mol` (including connectivity information) and the `acetaldehyde_fodMC.xyz` file as before.

> [!Warning]
> The script [02test.py](/02test.py) will overwrite the files generated by the script [01test.py](/01test.py).

+ Visualize using VESTA (or jmol).


> [!Note]
> What is the difference with the previous test?


***



# Example 03 

Generate FODs from a SMILES string

Download the file [03test.py](/03test.py)

+ Generate xyz coordinates and connectivity directly from a SMILES string. In this case we only need a string that represent the molecule. The script takes care of:
  + SMILES &#8594; mol. The SMILES strin for acetaldehyde is `CC=O`.
  + Add Hs (not in the SMILES information).
  + Adjust structure.
  + Relax using UFF.

+ The resulting mol and connectivity is used for fodMC.
+ Run fodMC: `python3 03test.py`.
+ The script generates a file `CC=O_fodMC.xyz` with the atomic coordinates plus the FODs.


> [!Warning]
> The script [03test.py](/03test.py) will overwrite files.


+ Visualize using VESTA (or jmol)



***




# Example 04


Generate FODs from atoms.

Download the file [04test.py](/04test.py)

+ Generate FODs for neutral atoms.
+ Edit the `04test.py` file as needed (the current file is for C).
+ Run fodMC: `python3 04test.py`.
+ The script generates a file `C_fodMC.xyz` with the atomic coordinate (atom at the origin) plus the FODs.


> [!Note]
> The function `pyfodmc.get_guess` in the script can generate NRLMOL input files by changing the call to `pyfodmc.get_guess('NRLMOL','')`.



***

# Exercises

+ Generate FODs for the SO2 molecule. Use  [01test.py](/01test.py) as the starting point and the xyz file [SO2.xyz](/SO2.xyz).
  + Assume two double bonds C=O and verify that the FOD structure is like this:


<p align="center" width="100%">
<img width="200" alt="Picture1" src="https://github.com/user-attachments/assets/e3644044-0ede-4150-99b7-3e98aa77ae3b" />
<img width="200" alt="image" src="https://github.com/user-attachments/assets/8022e59b-08cd-4306-b031-c02e2f61604f" />

</p>

+ Now attempt to use a different bonding structure:
  
<p align="center" width="100%">
<img width="200" alt="image" src="https://github.com/user-attachments/assets/c43d1e4e-c358-4849-b9de-adeb642996bf" />
</p>




