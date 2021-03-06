# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren

contributed by T Williams
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp
import scipy
from scipy import interpolate


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\Masterfiles\\high\\'
save_path = path + 'plots\\'

basename1 = 'Sample1_master_metadata.csv'
basename2 = 'Sample3_master_metadata.csv'
basename3 = 'Sample16_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = np.concatenate((data1[:, :69], data2[:, :69], data3[:, :69]))
ROI = data[:, 15]
data = data[ROI > 20000]

Co = data[:,58]*100
Fe = data[:,59]*100
Zr = data[:,60]*100

peak_number = data[:, 55]
nearest_neighbor = data[:, 57]
texture_sum = data[:, 53]
crystallinity = data[:, 51]
peak_position = data[:,64]
peak_width = data[:,65]
peak_intensity = data[:,66]




ternary_data = np.concatenate(([Co],[Fe],[Zr],[np.log(crystallinity)]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='crystallinity',
                       cbl='Scale', vmin = 0.2, vmax = 1.4, cmap='viridis', cb=True, style='h')

ternary_data = np.concatenate(([Co],[Fe],[Zr],[np.log(texture_sum)]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='texture_sum',
                       cbl='Scale', vmin = -11.1, vmax = -10.3, cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([Co],[Fe],[Zr],[np.log(nearest_neighbor)]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='nearest_neighbor',
                       cbl='Scale', vmin =-10.4, vmax = -2.55, cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_number]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_number',
                       cbl='Scale', vmin = 1, vmax = 11, cmap='viridis', cb=True, style='h')



ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_width]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_width',
                       cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')



ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_intensity]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_intensity',
                       cbl='Scale', cmap='viridis', cb=True, style='h')

ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_position]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_position',
                       cbl='Scale', vmin = 2.51, vmax = 3.14, cmap='viridis', cb=True, style='h')

# ternary_data = np.concatenate(([Co],[Fe],[Zr],[[1]*len(Co)]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                        sv=True, svpth=save_path, svflnm='empty_high',
#                        cbl='Scale', cmap='gray', cb=True, style='h')
