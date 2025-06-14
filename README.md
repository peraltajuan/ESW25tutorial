# ESW25 tutorial

## Generating Fermi-orbital descriptors from scratch for FLOSIC calculations

We will review 3 different approaches to generate FODs for FLOSIC calculations. The idea of the tutorial is to learn how to install the necessary tools and to use them in a few representative examples. The methods include: `fodMC` [J. Comp. Chem. 40, 2843–285 (2019)] and the `FODLego` methods which use molecular bonding information to build FODs structures. This bonding information can be user-provided, or automatically generated by `RDKit`. The `FODQR` uses the electron density from a minimal basis DFT calculation done with `PySCF`. We will test the three methods for molecular systems and atoms. All the tools that we will use automatically generate input files for FLOSIC calculations that can be used as good starting points.


Repository for the ESW25 tutorial:

[1 - fodMC](/fodMC.md)\
[2 - FODLego](/FODLego.md)\
[3 - FODQR](/FODQR.md)


