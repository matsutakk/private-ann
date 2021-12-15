import math 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter, FuncFormatter
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors

###########################
# PLOT PARAMETERS
###########################
default_width=5
default_height=3
EXTRA_SMALL_SIZE = 12
SMALL_SIZE = 14
MEDIUM_SIZE = 15
BIGGER_SIZE = 16
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=EXTRA_SMALL_SIZE)    # legend fontsize
plt.rc('legend', title_fontsize=EXTRA_SMALL_SIZE)
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

###########################
# COLORS
###########################
# colors = ['#0099CC', '#008000', '#955196', '#ff6e54', '#dd5182',  '#003f5c']
colors = list(mcolors.TABLEAU_COLORS.values())
colors[3] = colors[0]
tmp = colors[1]
colors[0] = colors[2]
colors[2] = tmp
colors[1] = "skyblue"
colors = colors[:5][::-1]

###########################
# MARKERS
###########################
markers = ['', '.',  'x', '2', '+', '3', 's']
hatches = ['////', '\\\\\\\\', 'xxxx', '//////////', '', '//']

###########################
# PLOT BACKGROUND CONFIG
###########################
linestyle = 'dashed'
gridcolor = 'lightgray'
linewidth=2
edgecolor='gray'

###########################
# MISC
###########################
error_opacity = 0.3
title_font_size=10


###########################
# UNIT CONVERSIONSs
###########################
MICRO_TO_MILLI = 1.0/1000.0
MILLI_TO_SECONDS = 1.0 / 1000.0
SECONDS_TO_MILI = 1000.0
MILLI_TO_HOURS = 1.0 / 3600000
BYTES_TO_MB = 1.0 / (10**6)
BYTES_TO_KB = 1.0 / (10**3)


###########################
# FUNCTIONS
###########################
def confidence95(x, n): 
    return 1.96 * x / math.sqrt(n)