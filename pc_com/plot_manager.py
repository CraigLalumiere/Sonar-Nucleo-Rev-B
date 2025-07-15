from PySide6 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg
import numpy as np
from messages.AddXYToPlot_pb2 import AddXYToPlot
from messages.AddToBodePlot_pb2 import AddToBodePlot
from messages.ClearPlots_pb2 import ClearPlots
from messages.ConfigPlot_pb2 import ConfigPlot
from messages.DrawBodePlot_pb2 import DrawBodePlot
from messages.DrawPlot_pb2 import DrawPlot
from messages.LogToPlot_pb2 import LogToPlot
import random
import math




class PlotManager:
    def __init__(self, plot_window: pg.GraphicsLayoutWidget):
        self.plot_win = plot_window

        self.plots = []
        self.plot_data = []

        self.plot_win.setBackground(QtGui.QColor('#FFFFFF'))

        self.colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k']


    def update_data(self, msg):
        plot_number = msg.plot_number

        # check if this plot exists
        while plot_number+1 > len(self.plots):
            self.add_new_plot()

        data_label = msg.data_label
        # check if we've not seen this label before
        if not data_label in self.plot_data[plot_number]:
            self.add_curve_to_plot(plot_number, data_label, data_label)

        plot_data = self.plot_data[plot_number][data_label]

        if isinstance(msg, LogToPlot):
            if len(self.plot_data[plot_number][data_label]['x']) < 50:
                plot_data['x'].append(msg.milliseconds_tick/1000)
                plot_data['y'].append(msg.data_y)
            else:
                plot_data['x'][:-1] = plot_data['x'][1:]
                plot_data['x'][-1] = msg.milliseconds_tick/1000
                plot_data['y'][:-1] = plot_data['y'][1:]
                plot_data['y'][-1] = msg.data_y

        if isinstance(msg, AddXYToPlot):
            # if len(self.plot_data[plot_number][data_label]['x']) < 100:
                plot_data['x'].append(msg.data_x)
                plot_data['y'].append(msg.data_y)
            # else:
            #     plot_data['x'][:-1] = plot_data['x'][1:]
            #     plot_data['x'][-1] = msg.data_x
            #     plot_data['y'][:-1] = plot_data['y'][1:]
            #     plot_data['y'][-1] = msg.data_y
        
        if isinstance(msg, DrawPlot):
            plot_data['x'] = msg.data_x._values
            plot_data['y'] = msg.data_y._values

    def update_bode_data(self, msg):
        plot_number = msg.plot_number

        # bode plot will draw magnitude on plot_number and phase on plot_number+1

        # ensure both of these plots exists
        while plot_number+2 > len(self.plots):
            self.add_new_plot()
        
        mag_plot = self.plots[plot_number]
        phase_plot = self.plots[plot_number+1]
        # set the first plot (magnitude) to log-log
        mag_plot.setLogMode(True, True)
        # set the second plot (phase) to log-lin
        phase_plot.setLogMode(True, False)

        data_label = msg.data_label
        # add the magnitude plot if it doesnt already exist
        if not data_label in self.plot_data[plot_number]:
            self.add_curve_to_plot(plot_number, data_label, '|'+data_label+'|')
        
        # add the phase plot if it doesnt already exist
        if not data_label in self.plot_data[plot_number+1]:
            self.add_curve_to_plot(plot_number+1, data_label, '∠'+data_label)

        mag_data = self.plot_data[plot_number][data_label]
        phase_data = self.plot_data[plot_number+1][data_label]

        if isinstance(msg, AddToBodePlot):
            mag_data['x'].append(msg.data_freq)
            mag_data['y'].append(msg.data_mag)
            phase_data['x'].append(msg.data_freq)
            phase_data['y'].append(msg.data_phase)

            # mag_data['x'][:-1] = mag_data['x'][1:]
            # mag_data['x'][-1] = msg.data_freq
            # mag_data['y'][:-1] = mag_data['y'][1:]
            # mag_data['y'][-1] = msg.data_mag
            # phase_data['x'][:-1] = phase_data['x'][1:]
            # phase_data['x'][-1] = msg.data_freq
            # phase_data['y'][:-1] = phase_data['y'][1:]
            # phase_data['y'][-1] = msg.data_phase
        if isinstance(msg, DrawBodePlot):
            mag_data['x'] = msg.data_freq._values
            phase_data['x'] = msg.data_freq._values
            mag_data['y'] = msg.data_mag._values
            phase_data['y'] = msg.data_phase._values
        
        x = mag_data['x']
        mag = mag_data['y'] 
        
        xRange = math.log10(math.sqrt(max(x)/min(x)))
        yCenter = math.log10(math.sqrt(max(mag)*min(mag)))
        mag_plot.setYRange(yCenter-xRange, yCenter+xRange, padding=0)
        phase_plot.setYRange(-180, 180, padding=0)
        # self.plots[plot_number].setXRange(math.log10(min(x)), math.log10(max(x)), padding=0)
        # self.plots[plot_number+1].setXRange(math.log10(min(x)), math.log10(max(x)), padding=0)


    def update_plot(self):
        for data in self.plot_data: # loop through each plot
            for data_label in data: # loop through each curve on this plot
                x = data[data_label]['x']
                y = data[data_label]['y']
                data[data_label]['curve'].setData(x, y)

    def add_curve_to_plot(self, plot_number, data_label, display_label):
        # Generate a random colour if we've run out of hard-coded ones
        if (len(self.plot_data[plot_number]) >= len(self.colours)):
            self.colours.append((random.random()*256, random.random()*256, random.random()*256))
        thisColour = self.colours[len(self.plot_data[plot_number])]

        thisCurve = self.plots[plot_number].plot([],
                                                [],
                                                pen=thisColour,
                                                name=display_label)
        self.plot_data[plot_number][data_label] = {'x':[], 'y':[], 'curve':thisCurve} # empty

    def add_new_plot(self):
        self.plots.append(self.plot_win.addPlot(row=len(self.plots), col=0)) # title="Title"
        self.plots[-1].addLegend()
        self.plots[-1].showGrid(x=True, y=True, alpha=0.5)
        self.plot_data.append({}) # empty dictionary
    
    def reset_plots(self):
        for plot in self.plots:
            self.plot_win.removeItem(plot)
            plot.deleteLater()
        self.plots = []
        self.plot_data = []

        
    def configure_plot(self, msg):
        plot_number = msg.plot_number

        # check if this plot exists
        while plot_number+1 > len(self.plots):
            self.add_new_plot()
        
        self.plots[plot_number].setLabel('bottom', msg.x_label, msg.x_units)
        self.plots[plot_number].setLabel('left', msg.y_label, msg.y_units)
        self.plots[plot_number].setTitle(msg.plot_title)

