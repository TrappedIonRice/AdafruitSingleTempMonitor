import os
import sys
import time
import shutil
import qdarkstyle
from qtGUI import Ui_MainWindow
import matplotlib.pyplot as plt
# from ThermocoupleFit import k_type_fit
from matplotlib.figure import Figure
from SerialManager import SerialManagerArduino, SerialManagerCombine
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import datetime


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, y_scale="linear"):
        with plt.style.context("dark_background"):
            fig = Figure(figsize=(width, height), dpi=dpi)
            self.axes = fig.add_subplot(111, yscale=y_scale)
        super(MplCanvas, self).__init__(fig)


class BakingLogGui(Ui_MainWindow):

    def __init__(self, mainwindow):
        # Initialize the qt designer gui
        self.mainwindow = mainwindow
        self.setupUi(mainwindow)

        # Parameters
        self.channelNum = 1  # Maximum available channels in this app
        self.maxVoltage = 3.3  # (V) arduino due analog reading maximum
        self.bitdepth = 12  # arduino due analog read bit depth
        self.t0 = 0  # To store the start time
        self.isLogging = False
        self.dataFileName = "data.txt"
        self.pressureChannelNum = 4     # Maximum available channels for pressure in this app

        # Initialize data array
        self.channelData = [[[], []] for _ in range(self.channelNum)]   # Actual temperature data
        self.pressureData = [[[], []] for _ in range(self.pressureChannelNum)]  # Actual pressure data
        self.pressureData.append([])

        self.channelData_plotting = self.channelData
        self.pressureData_plotting = [[[], []] for _ in range(self.pressureChannelNum)]     # Pressure data for plotting

        # Track whether this is the first/second update (for boundary conditions in update_plot)
        self.first_update = True
        self.second_update = False

        # Add the temperature canvas and related widgets to the gui
        self.canvasT = MplCanvas(self, width=5, height=4, dpi=100, y_scale="linear")
        self.canvasT.axes.set_xlabel("time (s)")
        self.canvasT.axes.set_title("Temperature ($^\circ$C)")
        toolbarT = NavigationToolbar(self.canvasT, mainwindow)
        layoutT = QtWidgets.QVBoxLayout()

        self.button1 = QPushButton('Toggle Autoscaling')
        self.button1.setCheckable(True)
        self.button1.toggle()
        layoutT.addWidget(self.button1)

        layoutT.addWidget(toolbarT)
        layoutT.addWidget(self.canvasT)

        # Add the temperature and pressure layouts together to finish building the gui
        self.horizontalLayoutPlot.addLayout(layoutT)

        self.actionStart.triggered.connect(self.start_logging)
        self.actionRefresh.triggered.connect(self.refresh)

    def start_logging(self):
        self.first_update = True

        self.isLogging = True
        if self.t0 == 0:
            self.t0 = time.time()
        self.actionStart.setText("Stop")
        self.actionStart.triggered.connect(self.stop_logging)

    def check_logging_status(self):
        return self.isLogging

    def stop_logging(self):
        self.isLogging = False
        self.actionStart.setText("Start")
        self.actionStart.triggered.connect(self.start_logging)

    def refresh(self):
        self.channelData = [[[], []] for _ in range(self.channelNum)]
        self.pressureData = [[[], []] for _ in range(self.pressureChannelNum)]
        if self.check_logging_status():
            self.t0 = time.time()
        else:
            self.t0 = 0
        self.count = 1

        # First/second iteration boundary conditions
        self.first_update = True
        self.second_update = True

        self.update_plot()
        # with open(self.dataFileName, "w") as f:
        #     f.write('time\tT1\tT2\tT3\tT4\tT5\tT6\tP\n')

    def get_arduino(self, input):

        # Calculate the current time
        t = time.time() - self.t0
        s = str(t) + '\t'

        self.channelData[0][0].append(t)
        self.channelData[0][1].append(input)
        self.channelData[-1].append(t)

    # Todo: radio buttons and spin boxes
    def update_plot(self):
        with plt.style.context("dark_background"):

            # Run slightly different code just after starting or refreshing to avoid crashing
            if self.first_update or self.second_update:
                if not self.first_update and self.second_update:
                    self.second_update = False
                self.first_update = False

                # Clear the canvas.
                self.canvasT.axes.cla()

                # Plot the current data
                for i in range(self.channelNum):
                    if len(self.channelData_plotting[i][1]) > 0:
                        self.canvasT.axes.plot(self.channelData_plotting[i][0], self.channelData_plotting[i][1])

                # set the lower x bound and finish building the graph
                self.canvasT.axes.set_xbound(lower=0)
                self.canvasT.axes.legend()
                self.canvasT.axes.set_xlabel("time (s)")
                self.canvasT.axes.set_title("Temperature ($^\circ$C)")
                self.canvasT.draw()

                return

            # Store the legend labels in a list, and retrieve all the lines from the temperature plot
            # labels = []
            lines = self.canvasT.axes.get_lines()

            # These are the channels that are currently being shown on the plot
            active_channels = []

            # Reset the data and update the labels
            for i in range(self.channelNum):
                if len(self.channelData_plotting[i][1]) > 0:
                    if len(lines) > 0:
                        line = lines.pop(0)
                        line.set_data(self.channelData_plotting[i][0], self.channelData_plotting[i][1])
                    else:
                        self.canvasT.axes.plot(self.channelData_plotting[i][0], self.channelData_plotting[i][1])

                    active_channels.append(i)

            # Update scaling if the temperature autoscale is toggled
            if self.button1.isChecked():
                self.button1.setText('Autoscaling Enabled')
                try:
                    self.canvasT.axes.set_xbound(lower=0, upper=max(self.channelData[0][0]) * 1.05)
                    y_max = max(self.channelData[0][1])
                    y_min = min(self.channelData[0][1])
                    self.canvasT.axes.set_ybound(lower=y_min - (y_max - y_min) * 0.05, upper=y_max + (y_max - y_min) * 0.05)
                except ValueError:
                    print('channelData_plotting[0][0] is empty')
            else:
                self.button1.setText('Autoscaling Disabled')

            # Trigger the canvas to update and redraw.
            self.canvasT.draw()
            self.canvasT.flush_events()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = BakingLogGui(MainWindow)
    MainWindow.show()
    manager = SerialManagerArduino(ui.check_logging_status)
    manager.valueChanged.connect(ui.get_arduino)
    manager.update.connect(ui.update_plot)
    app.exec_()
    sys.exit()
