# Active space models for Fe2S2,Fe4S4 built from the SP-MPS paper:

FCIDUMP files for the following paper:

"Spin-Projected Matrix Product States: Versatile Tool for Strongly Correlated Systems" \
Zhendong Li & Garnet Kin-Lic Chan, J. Chem. Theory Comput. 2017, 13, 6, 2681–2695 \
doi: 10.1021/acs.jctc.7b00270

Detailed explanations:

E[S=0]:

fe2s2 dmrg(d=8000) -116.6056091

fe4s4 dmrg(d=4000) -327.2396369

The indices for Fe3d orbitals are as follows:

1. Fe2S2: 2*5=10 [2Fe(III)]
[[2,3,4,5,6],[13,14,15,16,17]]

2. Fe4S4: 2*6+2*5=22 [2Fe(III),2Fe(II)]
[[2,3,4,5,6],[7,8,9,10,11],[24,25,26,27,28],[29,30,31,32,33]]

A reasonable guess may be the broken-symmetry determinant with Ms=0:

1.Fe2S2: spin up = {fe1}, spin down={fe2}

2.Fe4S4: spin up = {fe1,fe2}, spin down={fe3,fe4}
