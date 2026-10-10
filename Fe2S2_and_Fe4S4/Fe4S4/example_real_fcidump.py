import numpy
from pyscf import gto,scf

#==================================================================
# MOLECULE
#==================================================================
mol = gto.Mole()
mol.verbose = 5 #6

#==================================================================
# Coordinates and basis
#==================================================================
molname = 'fes' #be' #h2cluster'#h2o3' #c2'

if molname == 'fes':
   mol.atom = '''
S   0.04  -1.78  -1.292   
S  -0.04  1.78  -1.293   
S   1.78  -0.04  1.294   
S  -1.78  0.04   1.295   
Fe  0.05  -1.37  1.016   
Fe  -1.38  0.05  -1.007   
Fe  -0.05  1.38   1.008   
Fe  1.37  -0.05  -1.019   
S   0.24   3.30   2.1410  
S  -0.24  -3.29  2.1411  
S  -3.29  -0.24  -2.1412  
S   3.29   0.24  -2.1413  
C  -3.80  -1.84  -1.3814  
H  -3.91  -1.71  -0.2915  
H  -4.76  -2.17  -1.8116  
H  -3.03  -2.60  -1.5617  
C   3.80   1.83  -1.3818  
H   3.91   1.71  -0.2919  
H   4.76   2.16  -1.8120  
H   3.03   2.59  -1.5521  
C  -1.83  -3.80  1.3822  
H  -2.16  -4.76  1.8123  
H  -2.59  -3.03  1.5524  
H  -1.70  -3.91  0.2925  
C   1.84   3.80   1.3826  
H   2.17   4.76   1.8127  
H   2.60   3.03   1.5628  
H   1.71   3.91   0.29
   '''
   mol.basis = 'tzp-dkh'
   mol.charge = -2
   mol.spin = 18
   mol.build()

mol.symmetry = False #True
mol.build()

#==================================================================
# SCF
#==================================================================
mf = scf.sfx2c(scf.RHF(mol))
mf.init_guess = 'atom'
mf.level_shift = 0.0
mf.max_cycle = 0
mf.conv_tol=1.e-14

#==================================================================
# Dump integrals
#==================================================================
import h5py
f = h5py.File('mole.h5')
mo = f['mo_coeff_spatialAll'].value
f.close()

from pyscf import mcscf
from pyscf.dmrgscf.dmrgci import *

mc = mcscf.CASCI(mf, 36, [27,27])
mc.mo_coeff = mo
mc.fcisolver = DMRGCI(mol)
mc.onlywriteIntegral = True
mc.casci()
