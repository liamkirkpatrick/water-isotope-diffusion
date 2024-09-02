#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 07:14:36 2024

@author: Liam
"""

import pandas as pd
import pandas
import matplotlib.pyplot as plt


# set file
file = open('data_proc.pkl', 'rb')

# read data
data = pd.read_pickle(file)
alhic1901 = data['ALHIC1901_22_30min']
depth = alhic1901[0]
temp = alhic1901[3]

# Plot
fig,axs = plt.subplots()
axs.plot(temp,depth)
axs.set_ylim([150,0])
axs.set_xlabel('Temperature (C)')
axs.set_ylabel('Depth (m)')

