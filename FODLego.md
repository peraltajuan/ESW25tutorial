# FOD Lego generator (FODLego) tutorial

Based on the MS Thesis work of Angel-Emilio Villegas Sanchez "A Cheminformatics-Based Approach to the Prediction of Fermi-Orbital
Descriptors (FODs) in Fermi-Löwdin Orbital Self Interaction Correction (FLOSIC) Theory"


[Link to the Thesis](https://scholarly.cmich.edu/?a=is&oid=CMUGR2024-068&type=staticpdf&pdfaccesscode=PdSFSCxZMY55HKqnoGoFaos4spHsbb4%2Fj%2Fbx3ETR05iF8%3D&submitted=1&e=-------en-10--1--txt-txIN%7CtxAU%7CtxTI--------&g-recaptcha-response=03AFcWeA7EzT7cn3P02XaJRx9zoS7nCE10lDUFrGql7wi_mt2aIBPYEzZM-Pu0YT__Y4BZ7fqk3Hv1D9mCiIhLtcX1BIQ72aO3pveWAgkVQHNsi7_ZT1FkoJmribtgXXWEuIQCTrbO12bmYdsBS_O6wC_x7O2KeERuD86-KEJGVDNwQyVjwjNHKnMGnhayL6HKJeSRfWRiUsdm2dmjNEIyx0Hp5FM0UtmOumhyln3i-nvP8pXKFaSq0HcBfIW5i-UfrReaLasyDqA7gGLK9jnb4hAryTgXDmQuDIAd-0fnwrJPI7Il3TXfWo76fUkFhJKiBLLRc48QXM2MLqNmMWqCmpTr4RsaNhljnjMwb4GQyTA_1z6UCECEskO7wNZDMz2vTSdrTjLBSeYZs6keJI-T_Im8poxCbrO0hIboXmKK5a60dAjpBGE5R9_ov04Y5yo7hiLDfHHJ7H4vJWiHO9w-WS-1rGudjlRXT84FOBuu9vcEoowPLzDD_ySNuZenxk8TRsjrKP5yRgcS2AI-LDKX7PNnxzzi2KJoHqkuYqexRp1LeuEfn95luXSE-Q6E6OEZKXo13-nvMKZ1FB2laGT_4pkV0mmRD1Sb-ceU8eZRfTZacSu5omsn3X9VlTDMgw5DPEw2DJEfozj5v18-EkQm_ZyRRcIwi-DRypeqSPkB13qyHNL6AqXa2Eop1oAN5wQLkuDURBsNRoJBgC_p3f50SvGtUOOmanlXAE8eadEMhSBv648ZRYH9NFF9doxIfz9ME1vZ4fAIfixs_TXVjO5VrcU02DUcTJIcVQo1PAkdluY4Qpwz5PnY9XoMhTjQQpD6w37xryG1ur8tlQiSAdfA2W4TEkk1sufSl44S-K7CSEvhgsf7cSnhRlR7tGDp8lagGKXw1VkWT_kXaeODOnGvhijpN4nN0TASWeIQlIkEuR5t2MkxNoMeU1F0asf_YjcpLVzkpEReu-EBlUnfZKVfghNId_qbd0LSxy66PzOYKN7Lz0zRL0_5x87cKShVmf2ywNr_pNzV7tWrCAnxn7E3rrFefaGynCPjeQ)



## Table of Contents 

[Installation](/FODLego.md#Instalation)\
[Example 05](/FODLego.md#Example-05)
[Example 06](/FODLego.md#Example-06)

***

# Instalation


**Install fodMC:**

This is the fodMC code that we will be using.

`python3.10 -m pip install FODLego`


> [!Note]
>It needs RDKit.



***

# Example 05

Use FODLego to generate FODs starting from an xyz file

+ Run `fodlego SO2.xyz`
+ The script will read the file `SO2.xyz` with the atomic coordinates in xyz format.
+ The script generates a file `lego.xyz` with the atomic coordinates plus the FODs.
+ The script generates a `FRMORB` and a `CLUSTER` files to run FLOSIC calculations.
> [!NOTE]
>The code only considers closed-shell cases and  FODs are labeled as X in the xyz file.  

+ Visualize using VESTA (or other)



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







