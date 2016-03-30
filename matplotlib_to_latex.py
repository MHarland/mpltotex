#!/usr/bin/env python
from matplotlib import pyplot as plt
from numpy import sqrt

def set_masterthesis_parameters(height_factor = 1):
    to_high_res = 300/72.27
    font_size = 12
    font_size_small = 10
    to_low_res = 1/to_high_res
    fig_width_pt = 455.*to_high_res
    inches_per_pt = 1.0/300.
    golden_mean = (sqrt(5)-1.0)/2.0
    fig_width = fig_width_pt * inches_per_pt
    fig_height = fig_width * golden_mean * height_factor
    fig_size = [fig_width, fig_height]
    params = {'backend': 'pdf',
              'axes.labelsize': font_size,
              'font.size': font_size,
              'legend.fontsize': font_size,
              'xtick.labelsize': font_size_small,
              'ytick.labelsize': font_size_small,
              'text.usetex': True,
              'figure.figsize': fig_size,
              'font.family': 'serif',
              'font.serif': 'Times New Roman'
              }
    plt.rcParams.update(params)

def set_phdlog_parameters(height_factor = 1):
    to_high_res = 300/72.27
    font_size = 12
    font_size_small = 8
    fig_width_pt = 390. * to_high_res
    inches_per_pt = 1.0/300.
    golden_mean = (sqrt(5)-1.0)/2.0
    fig_width = fig_width_pt * inches_per_pt
    fig_height = fig_width * golden_mean * height_factor
    fig_size = [fig_width, fig_height]
    params = {'backend': 'pdf',
              'axes.labelsize': font_size,
              'font.size': font_size,
              'legend.fontsize': font_size_small,
              'xtick.labelsize': font_size_small,
              'ytick.labelsize': font_size_small,
              'text.usetex': True,
              'figure.figsize': fig_size,
              'font.family': 'serif',
              'font.serif': 'Computer Modern Roman'
              }
    plt.rcParams.update(params)

def set_poster_parameters(latex_width_pt = 1012./2.):
    to_high_res = 300/72.27
    to_low_res = 1/to_high_res
    fig_width_pt = latex_width_pt*to_high_res
    inches_per_pt = 1.0/300.
    golden_mean = (sqrt(5)-1.0)/2.0
    fig_width = fig_width_pt * inches_per_pt
    fig_height = fig_width * golden_mean
    fig_size = [fig_width, fig_height]
    font_size = 24
    font_size_small = 20
    params = {'backend': 'pdf',
              'axes.labelsize': font_size,
              'font.size': font_size,
              'legend.fontsize': font_size_small,
              'xtick.labelsize': font_size_small,
              'ytick.labelsize': font_size_small,
              'text.usetex': True,
              'figure.figsize': fig_size,
              'font.family': 'serif',
              'font.serif': 'Times New Roman'
              }
    plt.rcParams.update(params)
