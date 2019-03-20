from matplotlib import pyplot as plt
from numpy import sqrt


class PRLPlotConf:
    """
    fig_width_pt is determined by "\the\textwidth" output in the .tex file
    monitor_dpi is important to set the figure size correctly, but doesn't determine the
    resolution of the exported file
    """
    def __init__(self, fig_width_pt = 510., height_width_ratio = False,
                 font_size = 9, font_size_small = 8, add_ax = True,
                 ax_rectangle = (.17,.17,.8,.8), monitor_dpi = 150):
        
        fig_width = fig_width_pt/monitor_dpi
        if height_width_ratio:
            fig_height = fig_width * height_width_ratio
        else:
            golden_mean = (sqrt(5)-1.0)/2.0
            fig_height = fig_width * golden_mean
        fig_size = [fig_width, fig_height]
        
        plt.rcParams.update({'font.size': font_size,
                             'legend.fontsize': font_size_small,
                             'axes.labelsize': font_size,
                             'xtick.labelsize': font_size_small,
                             'ytick.labelsize': font_size_small,
                             'text.usetex': True,
                             'lines.markersize': font_size_small,
                             'figure.figsize': fig_size,
                             'image.cmap': 'inferno',
                             'savefig.dpi': 1200,
                             'xtick.direction': 'in',
                             'ytick.direction': 'in',
                             'xtick.top': True,
                             'ytick.right': True,
                             'axes.axisbelow': False,
                             'lines.linewidth': 1.})
        
        self.ax_rectangle = ax_rectangle
        self.fig = plt.figure()
        if add_ax:
            self.ax = self.fig.add_axes(self.ax_rectangle)
        
        self.legendkwargs = {'frameon': False, 'loc': 'best', 'fontsize': font_size_small}
        self.plt = plt

    def save(self, name, eps = False):
        """
        name without datatype suffix
        """
        outname = name+'.pdf'
        self.plt.savefig(outname, format = 'pdf')
        print outname, 'ready'
        if eps:
            outname = name+'.eps'
            self.plt.savefig(outname, format = 'eps')
            print outname, 'ready'
