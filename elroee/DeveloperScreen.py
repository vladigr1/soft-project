# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeveloperScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QInputDialog, QLineEdit, QDialog, QLabel, QComboBox, QPushButton

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



      
class Ui_MainWindow(QMainWindow):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.choose_alg_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.choose_alg_comboBox.setObjectName("choose_alg_comboBox")
        self.choose_alg_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.choose_alg_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.cur_filter_setting_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cur_filter_setting_table.sizePolicy().hasHeightForWidth())
        self.cur_filter_setting_table.setSizePolicy(sizePolicy)
        self.cur_filter_setting_table.setObjectName("cur_filter_setting_table")
        self.cur_filter_setting_table.setColumnCount(1)
        self.cur_filter_setting_table.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.cur_filter_setting_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_filter_setting_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_filter_setting_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_filter_setting_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_filter_setting_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_filter_setting_table.setHorizontalHeaderItem(0, item)
        
      
        self.verticalLayout_2.addWidget(self.cur_filter_setting_table)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.choose_report_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.choose_report_comboBox.setObjectName("choose_report_comboBox")
        self.choose_report_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.choose_report_comboBox)
        self.show_full_report_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_full_report_btn.setObjectName("show_full_report_btn")
        self.horizontalLayout_2.addWidget(self.show_full_report_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.choose_model_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_model_comboBox.sizePolicy().hasHeightForWidth())
        self.choose_model_comboBox.setSizePolicy(sizePolicy)
        self.choose_model_comboBox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.choose_model_comboBox.setObjectName("choose_model_comboBox")
        self.choose_model_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.choose_model_comboBox)
        self.show_ev_graph_btn = QtWidgets.QPushButton(self.centralwidget, clicked = self.showEnvGraph)
        self.show_ev_graph_btn.setObjectName("show_ev_graph_btn")
        self.horizontalLayout_4.addWidget(self.show_ev_graph_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Researcher screen:"))
        self.label_2.setText(_translate("MainWindow", "algorithm"))
        self.choose_alg_comboBox.setItemText(0, _translate("MainWindow", "least squares + spearman correlation"))
        
        
        item = self.cur_filter_setting_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "cognitive load"))
        item = self.cur_filter_setting_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "amount of sleep"))
        item = self.cur_filter_setting_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "water consumption"))
        item = self.cur_filter_setting_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "physical activity"))
        item = self.cur_filter_setting_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "time socializing"))
        item = self.cur_filter_setting_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "filter"))
        __sortingEnabled = self.cur_filter_setting_table.isSortingEnabled()
        self.cur_filter_setting_table.setSortingEnabled(False)
        
        
        
        cb = QComboBox()
        cb.addItems(["Option 1","Option 2","Option 3"])
        self.cur_filter_setting_table.setCellWidget(0, 0, cb)
        cb = QComboBox()
        cb.addItems(["Option A","Option B","Option C"])
        self.cur_filter_setting_table.setCellWidget(1, 0, cb)
        cb = QComboBox()
        cb.addItems(["Option E","Option F","Option G"])
        self.cur_filter_setting_table.setCellWidget(2, 0, cb)
        cb = QComboBox()
        cb.addItems(["Option H","Option I","Option J"])
        self.cur_filter_setting_table.setCellWidget(3, 0, cb)
        cb = QComboBox()
        cb.addItems(["Option K","Option L","Option M"])
        self.cur_filter_setting_table.setCellWidget(4, 0, cb)

        

        self.cur_filter_setting_table.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "update system configuration"))
        self.label_3.setText(_translate("MainWindow", "choose report:"))
        self.choose_report_comboBox.setItemText(0, _translate("MainWindow", "sleep analysis 1"))
        self.show_full_report_btn.setText(_translate("MainWindow", "show full report"))
        self.label_4.setText(_translate("MainWindow", "choose model:"))
        self.choose_model_comboBox.setItemText(0, _translate("MainWindow", "sleep analysis"))
        self.show_ev_graph_btn.setText(_translate("MainWindow", "show evaluate graph"))
        
        
    def showEnvGraph(self):
        pop = Popup(self)
        pop.show()
        

class Popup(QDialog):
   def __init__(self, parent):
       super().__init__(parent)
       self.resize(600,300)
       self.chart = Graph(self)
       self.chart.resize(550, 250)
       
       
       
class Graph(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)
        
        self.ax.plot(t, s)

        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title='About as simple as it gets, folks')
        self.ax.grid()
  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

