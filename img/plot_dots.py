#!bin/python
from IPython import embed
import numpy
import matplotlib.pyplot as plt
import scipy.stats as stats
import ss_plotting.make_plots as ss;
data = numpy.loadtxt(open("./dot_data.txt", "rb"), delimiter=' ');

theta = numpy.linspace(0, 3.14 * 2)
xes = numpy.sin(theta) * 2
yes = numpy.cos(theta) * 2

ss.plot(series=[(xes, yes), (data[:, 0], data[:, 1]), (data[:, 2], data[:, 3])], 
                series_colors=['red', 'blue', 'green'], 
                series_labels=['Dot Perimeter', 'Touches -- Dense Tracking', 'Touches -- Open Loop'],
                 plot_xlabel='X error (cm)', 
                 plot_ylabel="Y error (cm)", 
                 savefile="./dots.pdf",
                 line_styles=['-', '', ''],
                 plot_markers=['', '.', 'x'],
                 plot_xlim=(-8, 8),
                 plot_ylim=(-8, 8),
                  savefile_size = (3, 3));

plt.show();
