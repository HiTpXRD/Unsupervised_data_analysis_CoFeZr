# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren

Impremented from two papers:
1. "Predictin of high-entropy stabilized solid-solution in multi-component alloys"
X Yang, et al
Journal of Materials Chemistry and Physics

(Enthalpy of mixing data found in Table 2 in "Classiﬁcation of Bulk Metallic Glasses by Atomic Size Diﬀerence,
Heat of Mixing and Period of Constituent Elements and Its Application
to Characterization of the Main Alloying Element" by A Takeuchi)

2. "Thermodynamic prediction of bulk metallic glass forming alloys in ternary Zr–Cu–X
(X=Ag, Al, Ti, Ga) systems"
S Vincent
Journal of Non-Crystalline Solids
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Publications\\Combinatorial Search for Metallic Glasses in Co-V-Zr ternary systems\\theory\\'

def twoD_visualize(path):
    """
    Extract chemical compositions from the master csv
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
#        if basename(filename)[0] == '1':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            Co = data[:,54]
            V = data[:,55]
            Zr = data[:,56]
    return Co, V, Zr
             
           
Co, V, Zr = twoD_visualize(path)

Co_c = Co/100.0
V_c = V/100.0
Zr_c = Zr/100.0

###############
### paper 1 ###
###############
# enthalpy of mixing for binary systems found in A Takeuchi's paper. omega calculated from equation (2)
omega_Co_V = -14 * 4
omega_Co_Zr = -41 * 4
omega_V_Zr = -4 * 4
enthalpy_of_mixing = omega_Co_V * Co_c * V_c + omega_Co_Zr * Co_c * Zr_c + omega_V_Zr * V_c * Zr_c

# calculating from equation (3)
entropy_of_mixing = - 8.314 * (Co_c*np.log(Co_c) + V_c * np.log(V_c) + Zr_c * np.log(Zr_c))

# melting temperature found in wikipedia
# https://en.wikipedia.org/wiki/Cobalt
# https://en.wikipedia.org/wiki/Vanadium
# https://en.wikipedia.org/wiki/Zirconium
# calculating from equation (5)
Tm_Co = 1768
Tm_V = 2183
Tm_Zr = 2128
Tm = Tm_Co * Co_c + Tm_V * V_c + Tm_Zr * Zr_c

# calculating from equation (4)
OMEGA = Tm * entropy_of_mixing / np.abs(enthalpy_of_mixing) / 1000.0

# calculating from equation (6)
r_Co = 1.25
r_V = 1.34
r_Zr = 1.6

r_mean = r_Co * Co_c + r_V * V_c + r_Zr * Zr_c

delta = np.sqrt(Co_c*(1-r_Co/r_mean)**2 + V_c*(1-r_V/r_mean)**2 + V_c*(1-r_V/r_mean)**2)

                
solid_solution_formation = (OMEGA) > 1.1 * (delta <= 0.066)

## visualization for entropy of mixing, enthalpy of mixing, delta and OMEGA, and solid solution formation possibility
#ternary_data = np.concatenate(([Co],[V],[Zr],[entropy_of_mixing]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='entropy of mixing',
#                       cbl='Scale', cmap='jet_r', cb=True, style='h')
#
#
#
#ternary_data = np.concatenate(([Co],[V],[Zr],[enthalpy_of_mixing]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='enthalpy of mixing',
#                       cbl='Scale', cmap='jet_r', cb=True, style='h')
#
#            
#
#ternary_data = np.concatenate(([Co],[V],[Zr],[OMEGA]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='OMEGA',
#                       cbl='Scale', cmap='jet_r', cb=True, style='h')
#
#
#ternary_data = np.concatenate(([Co],[V],[Zr],[delta]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='delta',
#                       cbl='Scale', cmap='jet_r', cb=True, style='h')
#
#
#ternary_data = np.concatenate(([Co],[V],[Zr],[solid_solution_formation]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='solid solution formation',
#                       cbl='Scale', cmap='jet_r', cb=True, style='h')



###############
### paper 2 ###
###############
kB = 1.38E-23
R = 8.314

zeta = 1/(1-0.64)
Co_d = 1.25
V_d = 1.34
Zr_d = 1.6

sigma_square = Co_c * Co_d **2 + V_c * V_d **2 + Zr_c * Zr_d**2
sigma_cubic = Co_c * Co_d **3 + V_c * V_d **3 + Zr_c * Zr_d**3

y1 = 1/sigma_cubic * ((Co_d+V_d)*(Co_d-V_d)**2*Co_c*V_c + (Co_d+Zr_d)*(Co_d-Zr_d)**2*Co_c*Zr_c +\
(V_d+Zr_d)*(V_d-Zr_d)**2*V_c*Zr_c)

y2 = sigma_square/sigma_cubic**(Co_d*V_d*(Co_d-V_d)**2*Co_c*V_c + Co_d*Zr_d*(Co_d-Zr_d)**2*Co_c*Zr_c +\
V_d*Zr_d*(V_d-Zr_d)**2*V_c*Zr_c)

y3 = sigma_square**3 / sigma_cubic**2

mismatch_entropy = kB*(3/2*(zeta**2-1)*y1 + 3/2*(zeta-1)**2*y2-(1/2*(zeta-1)*(zeta-3)+np.log(zeta))*(1-y3))

PHS = enthalpy_of_mixing * mismatch_entropy / kB

configuration_entropy_range = (entropy_of_mixing/R > 0.9) * (entropy_of_mixing/R <1.0)

BMG = PHS * configuration_entropy_range

ternary_data = np.concatenate(([Co],[V],[Zr],[configuration_entropy_range]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='configuration entropy',
                       cbl='Scale', cmap='jet_r', cb=True, style='h')


ternary_data = np.concatenate(([Co],[V],[Zr],[PHS]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='PHS',
                       cbl='Scale', cmap='jet_r', cb=True, style='h')

ternary_data = np.concatenate(([Co],[V],[Zr],[BMG]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='BMG formation',
                       cbl='Scale', cmap='jet_r', cb=True, style='h')


plt.close('all')