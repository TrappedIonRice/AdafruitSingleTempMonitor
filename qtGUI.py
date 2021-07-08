# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BakingLog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayoutPlot = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPlot.setObjectName("horizontalLayoutPlot")
        self.gridLayout.addLayout(self.horizontalLayoutPlot, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBoxTime = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxTime.setObjectName("groupBoxTime")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxTime)
        self.gridLayout_5.setContentsMargins(2, -1, 2, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelTimeScale = QtWidgets.QLabel(self.groupBoxTime)
        self.labelTimeScale.setObjectName("labelTimeScale")
        self.horizontalLayout.addWidget(self.labelTimeScale)
        self.spinBoxTimeScale = QtWidgets.QSpinBox(self.groupBoxTime)
        self.spinBoxTimeScale.setMaximum(99999999)
        self.spinBoxTimeScale.setProperty("value", 7200)
        self.spinBoxTimeScale.setObjectName("spinBoxTimeScale")
        self.horizontalLayout.addWidget(self.spinBoxTimeScale)
        self.labelTimeAll = QtWidgets.QLabel(self.groupBoxTime)
        self.labelTimeAll.setObjectName("labelTimeAll")
        self.horizontalLayout.addWidget(self.labelTimeAll)
        self.radioButtonTimeAll = QtWidgets.QRadioButton(self.groupBoxTime)
        self.radioButtonTimeAll.setText("")
        self.radioButtonTimeAll.setObjectName("radioButtonTimeAll")
        self.horizontalLayout.addWidget(self.radioButtonTimeAll)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBoxTime)
        self.groupBoxTemp = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxTemp.setObjectName("groupBoxTemp")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxTemp)
        self.gridLayout_4.setContentsMargins(2, -1, 2, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelTempScaleFrom = QtWidgets.QLabel(self.groupBoxTemp)
        self.labelTempScaleFrom.setObjectName("labelTempScaleFrom")
        self.horizontalLayout_4.addWidget(self.labelTempScaleFrom)
        self.spinBoxTempScaleFrom = QtWidgets.QSpinBox(self.groupBoxTemp)
        self.spinBoxTempScaleFrom.setObjectName("spinBoxTempScaleFrom")
        self.horizontalLayout_4.addWidget(self.spinBoxTempScaleFrom)
        self.labelTempScaleTo = QtWidgets.QLabel(self.groupBoxTemp)
        self.labelTempScaleTo.setObjectName("labelTempScaleTo")
        self.horizontalLayout_4.addWidget(self.labelTempScaleTo)
        self.spinBoxTempScaleTo = QtWidgets.QSpinBox(self.groupBoxTemp)
        self.spinBoxTempScaleTo.setObjectName("spinBoxTempScaleTo")
        self.horizontalLayout_4.addWidget(self.spinBoxTempScaleTo)
        self.labelTempAll = QtWidgets.QLabel(self.groupBoxTemp)
        self.labelTempAll.setObjectName("labelTempAll")
        self.horizontalLayout_4.addWidget(self.labelTempAll)
        self.radioButton = QtWidgets.QRadioButton(self.groupBoxTemp)
        self.radioButton.setText("")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBoxTemp)
        self.groupBoxPressure = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxPressure.setObjectName("groupBoxPressure")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxPressure)
        self.gridLayout_3.setContentsMargins(2, -1, 2, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelPressureScaleFrom = QtWidgets.QLabel(self.groupBoxPressure)
        self.labelPressureScaleFrom.setObjectName("labelPressureScaleFrom")
        self.horizontalLayout_3.addWidget(self.labelPressureScaleFrom)
        self.spinBoxPressureScaleFrom = QtWidgets.QSpinBox(self.groupBoxPressure)
        self.spinBoxPressureScaleFrom.setObjectName("spinBoxPressureScaleFrom")
        self.horizontalLayout_3.addWidget(self.spinBoxPressureScaleFrom)
        self.labelPressureScaleTo = QtWidgets.QLabel(self.groupBoxPressure)
        self.labelPressureScaleTo.setObjectName("labelPressureScaleTo")
        self.horizontalLayout_3.addWidget(self.labelPressureScaleTo)
        self.spinBoxPressureScaleTo = QtWidgets.QSpinBox(self.groupBoxPressure)
        self.spinBoxPressureScaleTo.setObjectName("spinBoxPressureScaleTo")
        self.horizontalLayout_3.addWidget(self.spinBoxPressureScaleTo)
        self.labelPressureAll = QtWidgets.QLabel(self.groupBoxPressure)
        self.labelPressureAll.setObjectName("labelPressureAll")
        self.horizontalLayout_3.addWidget(self.labelPressureAll)
        self.radioButtonPressureAll = QtWidgets.QRadioButton(self.groupBoxPressure)
        self.radioButtonPressureAll.setText("")
        self.radioButtonPressureAll.setChecked(True)
        self.radioButtonPressureAll.setObjectName("radioButtonPressureAll")
        self.horizontalLayout_3.addWidget(self.radioButtonPressureAll)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBoxPressure)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuChannels = QtWidgets.QMenu(self.menubar)
        self.menuChannels.setObjectName("menuChannels")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_data = QtWidgets.QAction(MainWindow)
        self.actionSave_data.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSave_data.setShortcutVisibleInContextMenu(True)
        self.actionSave_data.setObjectName("actionSave_data")
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setCheckable(True)
        self.actionChannel_1.setChecked(True)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setCheckable(True)
        self.actionChannel_2.setChecked(True)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setCheckable(True)
        self.actionChannel_3.setChecked(True)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.actionChannel_4 = QtWidgets.QAction(MainWindow)
        self.actionChannel_4.setCheckable(True)
        self.actionChannel_4.setChecked(True)
        self.actionChannel_4.setObjectName("actionChannel_4")
        self.actionChannel_5 = QtWidgets.QAction(MainWindow)
        self.actionChannel_5.setCheckable(True)
        self.actionChannel_5.setChecked(True)
        self.actionChannel_5.setObjectName("actionChannel_5")
        self.actionChannel_6 = QtWidgets.QAction(MainWindow)
        self.actionChannel_6.setCheckable(True)
        self.actionChannel_6.setChecked(True)
        self.actionChannel_6.setObjectName("actionChannel_6")

        self.pressureChannel_1 = QtWidgets.QAction(MainWindow)
        self.pressureChannel_1.setCheckable(True)
        self.pressureChannel_1.setChecked(True)
        self.pressureChannel_1.setObjectName("pressureChannel_1")
        self.pressureChannel_2 = QtWidgets.QAction(MainWindow)
        self.pressureChannel_2.setCheckable(True)
        self.pressureChannel_2.setChecked(True)
        self.pressureChannel_2.setObjectName("pressureChannel_1")
        self.pressureChannel_3 = QtWidgets.QAction(MainWindow)
        self.pressureChannel_3.setCheckable(True)
        self.pressureChannel_3.setChecked(True)
        self.pressureChannel_3.setObjectName("pressureChannel_1")
        self.pressureChannel_4 = QtWidgets.QAction(MainWindow)
        self.pressureChannel_4.setCheckable(True)
        self.pressureChannel_4.setChecked(True)
        self.pressureChannel_4.setObjectName("pressureChannel_1")

        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setShortcutVisibleInContextMenu(True)
        self.actionStart.setObjectName("actionStart")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setShortcutVisibleInContextMenu(True)
        self.actionRefresh.setObjectName("actionRefresh")
        self.menuFile.addAction(self.actionStart)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.actionSave_data)
        self.menuChannels.addAction(self.actionChannel_1)
        self.menuChannels.addAction(self.actionChannel_2)
        self.menuChannels.addAction(self.actionChannel_3)
        self.menuChannels.addAction(self.actionChannel_4)
        self.menuChannels.addAction(self.actionChannel_5)
        self.menuChannels.addAction(self.actionChannel_6)

        self.menuChannels.addAction(self.pressureChannel_1)
        self.menuChannels.addAction(self.pressureChannel_2)
        self.menuChannels.addAction(self.pressureChannel_3)
        self.menuChannels.addAction(self.pressureChannel_4)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuChannels.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxTime.setTitle(_translate("MainWindow", "Time Scale:"))
        self.labelTimeScale.setText(_translate("MainWindow", "Period (s):"))
        self.labelTimeAll.setText(_translate("MainWindow", "All"))
        self.groupBoxTemp.setTitle(_translate("MainWindow", "Temperature Scale"))
        self.labelTempScaleFrom.setText(_translate("MainWindow", "From:"))
        self.labelTempScaleTo.setText(_translate("MainWindow", "To:"))
        self.labelTempAll.setText(_translate("MainWindow", "All"))
        self.groupBoxPressure.setTitle(_translate("MainWindow", "Pressure Scale"))
        self.labelPressureScaleFrom.setText(_translate("MainWindow", "From:"))
        self.labelPressureScaleTo.setText(_translate("MainWindow", "To:"))
        self.labelPressureAll.setText(_translate("MainWindow", "All"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuChannels.setTitle(_translate("MainWindow", "Channels"))
        self.actionSave_data.setText(_translate("MainWindow", "Save data"))
        self.actionSave_data.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionChannel_1.setText(_translate("MainWindow", "Channel 1"))
        self.actionChannel_1.setShortcut(_translate("MainWindow", "Ctrl+F1"))
        self.actionChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_2.setShortcut(_translate("MainWindow", "Ctrl+F2"))
        self.actionChannel_3.setText(_translate("MainWindow", "Channel 3"))
        self.actionChannel_3.setShortcut(_translate("MainWindow", "Ctrl+F3"))
        self.actionChannel_4.setText(_translate("MainWindow", "Channel 4"))
        self.actionChannel_4.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionChannel_5.setText(_translate("MainWindow", "Channel 5"))
        self.actionChannel_5.setShortcut(_translate("MainWindow", "Ctrl+F5"))
        self.actionChannel_6.setText(_translate("MainWindow", "Channel 6"))
        self.actionChannel_6.setShortcut(_translate("MainWindow", "Ctrl+F6"))

        self.pressureChannel_1.setText(_translate("MainWindow", "Pressure Channel 1"))
        self.pressureChannel_1.setShortcut(_translate("MainWindow", "Ctrl+F7"))
        self.pressureChannel_2.setText(_translate("MainWindow", "Pressure Channel 2"))
        self.pressureChannel_2.setShortcut(_translate("MainWindow", "Ctrl+F8"))
        self.pressureChannel_3.setText(_translate("MainWindow", "Pressure Channel 3"))
        self.pressureChannel_3.setShortcut(_translate("MainWindow", "Ctrl+F9"))
        self.pressureChannel_4.setText(_translate("MainWindow", "Pressure Channel 4"))
        self.pressureChannel_4.setShortcut(_translate("MainWindow", "Ctrl+F10"))

        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStart.setShortcut(_translate("MainWindow", "Ctrl+Space"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
