from mpltotex import PRLPlotConf
import numpy as np


mplcfg = PRLPlotConf()
ax = mplcfg.ax
mesh = np.linspace(0,2*np.pi, 200)
ax.plot(mesh, np.cos(mesh), label ='$\cos$')
ax.plot(mesh, np.sin(mesh), label ='$\sin$')
ax.legend(**mplcfg.legendkwargs)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
mplcfg.save('example')
