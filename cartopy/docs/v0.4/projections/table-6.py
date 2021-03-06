import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3.0, 3))
delta = 0.125
ax = plt.axes([0+delta, 0+delta, 1-delta, 1-delta], projection=ccrs.Gnomonic())
#ax.set_global()
ax.coastlines()
ax.gridlines()