import matplotlib.pyplot as plt
plt.style.use('img/fh_kiel.mplstyle')
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

cmap_kiel = ListedColormap(['#00305D', '#F49E00', '#006A4D'])
cmap_kiel2 = ListedColormap(['#00305D', '#F49E00'])

import numpy as np
np.random.seed(42)

import pandas as pd
import seaborn as sns
import math

# colors
blue = '#00305D'
green = '#006A4D'
orange = '#F49E00'
dark_red = '#B5123E'
alarm_red = '#E20020'
light_green = '#7AB51D'

filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')


# sizes
plot_size = (18, 12)
half_plot_size = (18, 6)

def plot_lines(datadics, size = plot_size, titledic = {}):
    fig, ax = plt.subplots(1, 1, figsize=size)

    for d in datadics:
        ax.plot(d['x'], d['y'], d['format'], label=d['label'])

    plt.title(titledic['title'])
    plt.ylabel(titledic['ylabel'])
    plt.xlabel(titledic['xlabel'])
    plt.legend()
    plt.tight_layout()
    #return plt

def plot_histogramm(data, size = plot_size, n_bin = 20, titledic = {}):
    fig, ax = plt.subplots(1, 1, figsize=size)

    plt.hist(data,n_bin)

    plt.title(titledic['title'])
    plt.ylabel(titledic['ylabel'])
    plt.xlabel(titledic['xlabel'])
    plt.tight_layout()
    #return plt

def plot_labeled_scatter(data, size = plot_size, name_label = '', x_name = '', y_name= '', titledic = {}):
    fig, ax = plt.subplots(1, 1, figsize=size)
    for j, i in enumerate(data[name_label].unique()):
        plt.scatter(data[data[name_label] == i][x_name], data[data[name_label] == i][y_name], marker=filled_markers[j], label=name_label+': ' + str(i))

    ax.legend()

    plt.title(titledic['title'])
    plt.ylabel(titledic['ylabel'])
    plt.xlabel(titledic['xlabel'])
    plt.tight_layout()
