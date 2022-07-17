import netCDF4 as nc
import matplotlib.pyplot as plt
from matplotlib.colors import from_levels_and_colors
import numpy as np
from matplotlib import animation
from matplotlib.colors import BoundaryNorm
import matplotlib.colors as cols
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from matplotlib import ticker, cm
import seaborn as sns

data1=nc.Dataset('/ihesp/user/xiliangdiao/ihespdata/ocn300/B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02.pop.h.0167-09.TAUX.nc')
TAUX = data1.variables['TAUX'][0,200:600,550:1500]
lont = data1.variables['ULONG'][200:600,550:1500]
latt = data1.variables['ULAT'][200:600,550:1500]
#TAUX = data1.variables['TAUX'][0,200:600,1100:1550]
#lont = data1.variables['ULONG'][200:600,1100:1550]
#latt = data1.variables['ULAT'][200:600,1100:1550]
latt[latt == -1.0] = np.nan
TAUX[TAUX == -1.0] = np.nan
a = np.arange(0,400)
import math
#math.cos(math.radians(latt[:,3][399]))
wholedis = np.zeros(400)
for j in a:
    wholedis[j] = 111.34* math.cos(math.radians(latt[:,0][j]))
    
    
months = [f"{x:02d}" for x in range(1,13)]
years = [f"{x:04d}" for x in range(1975,2000)]
ii =0
result = np.zeros(300)

for yy in years:
    for mm in months:
        #data1=nc.Dataset('/ihesp/user/xiliangdiao/ihespdata/ocn300/B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02.pop.h.'+yy+'-'+mm +'.TAUX.nc')
        data1=nc.Dataset('/ihesp/user/xiliangdiao/ihespdata/ocn1950-2050/B.E.13.B1950TRC5.ne120_t12.cesm-ihesp-1950-2050.013.pop.h.nday1.'+yy+'-'+mm +'-01.TAUX.nc')
        TAUX = data1.variables['TAUX'][0,200:600,550:1500]
        lont = data1.variables['ULONG'][200:600,550:1500]
        latt = data1.variables['ULAT'][200:600,550:1500]
        TAUX[TAUX == -1.0] = np.nan
        TAUX[TAUX >  1000] = np.nan
        ###### (u2-u1)/(y2-y1)
        a = np.arange(0,399)
        A1= np.zeros([400,950])
        for i in a:
            A1[i,:] = (TAUX[i+1,:]-TAUX[i,:])/((latt[i+1,:]-latt[i,:])*110.95)
        ###################################
        #data2=nc.Dataset('/ihesp/user/xiliangdiao/ihespdata/ocn300/B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02.pop.h.'+yy+'-'+mm +'.TAUY.nc')
        data2=nc.Dataset('/ihesp/user/xiliangdiao/ihespdata/ocn1950-2050/B.E.13.B1950TRC5.ne120_t12.cesm-ihesp-1950-2050.013.pop.h.nday1.'+yy+'-'+mm +'-01.TAUY.nc')
        TAUY = data2.variables['TAUY'][0,200:600,550:1500]
        TAUY[TAUY == -1.0] = np.nan
        TAUY[TAUY >  1000] = np.nan
        ####################################
        ###### (v2-v1)/(x2-x1)
        b = np.arange(0,949)
        A2= np.zeros([400,950])
        for j in a:
            for i in b:
                A2[j,i] = (TAUY[j,i+1]-TAUY[j,i])/((lont[j,i+1]-lont[j,i])*wholedis[j])
        #####################################
        #A2 = A2[0:399,:]
        #A3 = (A2 - A1[0:399,:])
        A3 = A2[0:399,0:949] - A1[0:399,0:949]
        
        result[ii] = np.nanmean(A3)
        
        ii = ii + 1
#********************************************************************
        np.savetxt('1975-2000-01new.out',result)
#np.savetxt('eastofmaudrise.out',result)