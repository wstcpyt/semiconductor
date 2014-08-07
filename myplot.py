#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GuofuNiu
#
# Created:     16/01/2012
# Copyright:   (c) GuofuNiu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


from __future__ import print_function, division
from itertools import cycle
import matplotlib
matplotlib.use('Qt4Agg')

##matplotlib.interactive(True)
##matplotlib.use("WXAgg")


from matplotlib.pyplot import figure, show, draw, ion, ioff, setp, gcf, \
    get_cmap

from numpy import linspace
import numpy as np


from enthought.chaco.example_support import COLOR_PALETTE

#from matplotlib import rc
#rc('text', usetex=True)

#matplotlib.use("QT4Agg")
##import pylab


cbrewer = [
    (0.65098039,  0.80784314,  0.89019608, 1.0),
    (0.12156863,  0.47058824,  0.70588235, 1.0),
    (0.69803922,  0.8745098 ,  0.54117647, 1.0),
    (0.2       ,  0.62745098,  0.17254902, 1.0),
    (0.98431373,  0.60392157,  0.6       , 1.0),
    (0.89019608,  0.10196078,  0.10980392, 1.0),
    (0.99215686,  0.74901961,  0.43529412, 1.0),
    (1.        ,  0.49803922,  0.        , 1.0),
    (0.79215686,  0.69803922,  0.83921569, 1.0),
    (0.41568627,  0.23921569,  0.60392157, 1.0),
    ]


SHOW_PLOT = False

def show_plot(always = False):
    global SHOW_PLOT
    SHOW_PLOT = True

colors = ['r', 'b', 'g', 'c', 'k', 'm']

chaco_colors = ['red', 'blue', 'green', 'cyan', 'black', 'magenta']

linestyles = ['-', '--', '-.', ':']


class ChacoColorCycler(object):
    def __init__(self,):
        mycolors = chaco_colors[:]
#        mycolors = COLOR_PALETTE[:]
#        mycolors = cbrewer[:]
        self.cycler = cycle(mycolors)
    def next(self):
        return next(self.cycler)



class ColorCycler(object):
    def __init__(self, use_color_map = False, num_colors = 10):
        if use_color_map:
            cm = get_cmap('gist_rainbow')
            mycolors = []
            for idx in range(num_colors):
                color = cm(1.0*idx/num_colors)
                mycolors.append(color)
        else:
            mycolors = colors[:]
        self.cycler = cycle(mycolors)
    def next(self):
        return next(self.cycler)

class LineStyleCycler(object):
    def __init__(self):
        mystyles = linestyles[:]
        self.cycler = cycle(mystyles)
    def next(self):
        return next(self.cycler)

def new_ax():
    fig = figure()
    ax = fig.add_subplot(111)
    return ax

def myplot(
    x = None,
    y = None,
    xlabel = '',
    ylabel = '',
    label = '',
    xlog = False,
    ylog = False,
    linestyle = '-',
    linewidth = 2.0,
    color = 'red',
    marker = None,
    ax = None,
    fig = None,
    **kwargs):

    if ax == None:
        fig = figure()
        ax = fig.add_subplot(1, 1, 1)
    else:
        fig = ax.get_figure()

    if ylog:
        y = np.abs(y)
    line = ax.plot(x, y, **kwargs)
    ax.hold(True)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    if xlog == True:
        ax.set_xscale('log')
    if ylog == True:
        ax.set_yscale('log')
    if marker != None:
        setp(line, marker = marker )
    setp(line, linewidth=linewidth, linestyle=linestyle, color=color)
    if label:
        setp(line, label = label)
        ax.legend(loc='best')

    ax.autoscale()


    if SHOW_PLOT:
##        print('drawing')
        ()
    return line, ax, fig



def annotate(ax, x_special, y_special, str_special):

    line, ax, fig = myplot(ax = ax, x = x_special, y = y_special,
             linestyle ='', marker = '+',
             label = '', color = 'green')
    setp(line, markersize = 30)

    for p, q, t in zip(x_special, y_special, str_special):
        ax.annotate(t, xy=(p, q), xycoords='data',
    					xytext=(p, q), textcoords='data',
    					arrowprops=dict(facecolor='black', shrink=0.025),
    					horizontalalignment='left', verticalalignment='top',
    					)


def demo_new_plot():
    x = np.linspace(0,10,50)
    y = np.sin(x)
    myplot(x, y, marker = '+', markersize = 20)




def new_ax_demo():
    ax = new_ax()
    x = np.linspace(0,10,50)
    y = np.sin(x)
    myplot(ax = ax, x = x, y = y, marker = '+', markersize = 20)


def color_cycler_demo():
    num_omegas = 7
    omegas = linspace(0, 5, num_omegas)

    xs = linspace(0, 10, 200)

    color_cycler = ColorCycler()

#    color_cycler = ChacoColorCycler()

    from numpy import sin
    ax = new_ax()

    for omega in omegas:
        color = color_cycler.next()
        myplot(ax = ax,
               x=xs,
               y=sin(xs*omega),
               color=color,
               label='$\omega = {omega}$'.format(**locals())
               )

    ax.set_xlabel('$x$')
    ax.set_ylabel('$sin(\omega x)$')
    




def color_cycler_using_colormap_demo():
    num_omegas = 10
    omegas = linspace(0, 5, num_omegas)

    xs = linspace(0, 10, 200)

    color_cycler = ColorCycler(use_color_map = True, num_colors = num_omegas)

    from numpy import sin
    ax = new_ax()

    for omega in omegas:
        color = color_cycler.next()
        myplot(ax = ax,
               x=xs,
               y=sin(xs*omega),
               color=color,
               label='$\omega = {omega}$'.format(**locals())
               )

    ax.set_xlabel('$x$')
    ax.set_ylabel('$sin(\omega x)$')
    
    
    
    
def line_style_cycler_demo():
    num_omegas = 4
    omegas = linspace(0, 10, num_omegas)

    xs = linspace(0, 10, 200)

    line_cycler = LineStyleCycler()

    from numpy import sin
    import time

    ax = new_ax()
    
    for omega in omegas:
        linestyle = line_cycler.next()
        ax = new_ax()
        myplot(ax = ax,
               x=xs,
               y=sin(xs*omega),
               color='b',
               linestyle = linestyle,
               )




def main():
    demo_new_plot()


    new_ax_demo() # demonstrate how to use new_ax()

    color_cycler_demo() # use of ColorCycle with just regular colors
    
    color_cycler_using_colormap_demo() # demonstrate how to use ColorCycler()

    line_style_cycler_demo() # how to use LineStyleCycler()


if __name__ == '__main__':
#    print('dummy line to debug')

##    ion()
    main()
    show()
