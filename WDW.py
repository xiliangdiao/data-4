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

months = [f"{x:02d}" for x in range(1,13)]
years = [f"{x:04d}" for x in range(21,71)]
i =0
result = np.zeros(600)

for yy in years:
    for mm in months:
        data=nc.Dataset('/ihesp/user/xiliangdiao/ihespdata/ocn300/B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02.pop.h.'+yy+'-'+mm +'.SST.nc')
        plotvar = data.variables['TEMP'][0,:,:]
        lont = data.variables['TLONG']
        latt = data.variables['TLAT']
        lont = lont[426:603,1300:1600]
        latt = latt[426:603,1300:1600]
        plotvar = plotvar[20:37,426:603,1300:1600]
        aveplot = plotvar.mean(axis=0)
        aveplot = aveplot.mean(axis=0)
        aveplot = aveplot.mean(axis=0)
        result[i] = aveplot
        
        i = i + 1
        
        
np.savetxt('/scratch/user/xiliangdiao/plot/WDWbig21-71.out',result)