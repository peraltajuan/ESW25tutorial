# FOD Lego generator (FODLego) tutorial

Based on the MS Thesis work of Angel-Emilio Villegas Sanchez "A Cheminformatics-Based Approach to the Prediction of Fermi-Orbital
Descriptors (FODs) in Fermi-Löwdin Orbital Self Interaction Correction (FLOSIC) Theory"


[Link to the Thesis](https://scholarly.cmich.edu/?a=is&oid=CMUGR2024-068&type=staticpdf&pdfaccesscode=PdSFSCxZMY55HKqnoGoFaos4spHsbb4%2Fj%2Fbx3ETR05iF8%3D&submitted=1&e=-------en-10--1--txt-txIN%7CtxAU%7CtxTI--------&g-recaptcha-response=03AFcWeA7EzT7cn3P02XaJRx9zoS7nCE10lDUFrGql7wi_mt2aIBPYEzZM-Pu0YT__Y4BZ7fqk3Hv1D9mCiIhLtcX1BIQ72aO3pveWAgkVQHNsi7_ZT1FkoJmribtgXXWEuIQCTrbO12bmYdsBS_O6wC_x7O2KeERuD86-KEJGVDNwQyVjwjNHKnMGnhayL6HKJeSRfWRiUsdm2dmjNEIyx0Hp5FM0UtmOumhyln3i-nvP8pXKFaSq0HcBfIW5i-UfrReaLasyDqA7gGLK9jnb4hAryTgXDmQuDIAd-0fnwrJPI7Il3TXfWo76fUkFhJKiBLLRc48QXM2MLqNmMWqCmpTr4RsaNhljnjMwb4GQyTA_1z6UCECEskO7wNZDMz2vTSdrTjLBSeYZs6keJI-T_Im8poxCbrO0hIboXmKK5a60dAjpBGE5R9_ov04Y5yo7hiLDfHHJ7H4vJWiHO9w-WS-1rGudjlRXT84FOBuu9vcEoowPLzDD_ySNuZenxk8TRsjrKP5yRgcS2AI-LDKX7PNnxzzi2KJoHqkuYqexRp1LeuEfn95luXSE-Q6E6OEZKXo13-nvMKZ1FB2laGT_4pkV0mmRD1Sb-ceU8eZRfTZacSu5omsn3X9VlTDMgw5DPEw2DJEfozj5v18-EkQm_ZyRRcIwi-DRypeqSPkB13qyHNL6AqXa2Eop1oAN5wQLkuDURBsNRoJBgC_p3f50SvGtUOOmanlXAE8eadEMhSBv648ZRYH9NFF9doxIfz9ME1vZ4fAIfixs_TXVjO5VrcU02DUcTJIcVQo1PAkdluY4Qpwz5PnY9XoMhTjQQpD6w37xryG1ur8tlQiSAdfA2W4TEkk1sufSl44S-K7CSEvhgsf7cSnhRlR7tGDp8lagGKXw1VkWT_kXaeODOnGvhijpN4nN0TASWeIQlIkEuR5t2MkxNoMeU1F0asf_YjcpLVzkpEReu-EBlUnfZKVfghNId_qbd0LSxy66PzOYKN7Lz0zRL0_5x87cKShVmf2ywNr_pNzV7tWrCAnxn7E3rrFefaGynCPjeQ)



## Table of Contents 

[Installation](/fodMC.md#Instalation)\
[Example 01](/fodMC.md#Example-01)\
[Example 02](/fodMC.md#Example-02)\
[Example 03](/fodMC.md#Example-03)

***

# Instalation


**Install fodMC:**

This is the fodMC code that we will be using.

`python3.10 -m pip install FODLego`


> [!Note]
>It needs RDKit.



***

# Example 01
Download the file [01test.py](/01test.py)

+ Use an xyz file and add the “connectivity” by hand. In this case it is already in the python script.
+ Run fodMC: `python3 01test.py`
+ The script will read the file `SO2.xyz` with the atomic coordinates in xyz format.
+ The script generates a file `SO2_FOD.xyz` with the atomic coordinates plus the FODs.
> [!NOTE]
>The spin-up FODs are labeled as X and the spin-down as He.  
+ Visualize using VESTA (or other)

<img width="180" alt="image" src="https://github.com/user-attachments/assets/12c5ee81-8f1f-4de4-a64e-96c522f49d8b" />


> [!Note]
>Where are the Sulfur 2s2p FODs?

***

