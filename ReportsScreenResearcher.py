# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportsScreenResearcher.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QInputDialog, QLineEdit, QDialog, QLabel, QComboBox, QPushButton, QTableWidgetItem
import numpy as np

class Ui_FullReportWindow(QMainWindow):
    
    def setupUi(self, MainWindow, listHeaders, listValues):
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
        self.cur_report_display_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cur_report_display_table.sizePolicy().hasHeightForWidth())
        self.cur_report_display_table.setSizePolicy(sizePolicy)
        self.cur_report_display_table.setLineWidth(1)
        self.cur_report_display_table.setObjectName("cur_report_display_table")
        self.cur_report_display_table.setColumnCount(1)
        self.cur_report_display_table.setHorizontalHeaderLabels(["Values:"])

       
        length = len(listHeaders)
        for i in range(length): 
            rowPosition = self.cur_report_display_table.rowCount()
            self.cur_report_display_table.insertRow(rowPosition)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(listHeaders[i])) 
            self.cur_report_display_table.setVerticalHeaderItem(rowPosition, item)

            
            label = QLabel(np.format_float_scientific(listValues[i], 4))
            self.cur_report_display_table.setCellWidget(rowPosition, 0, label)
        
        
        
              
        #self.cur_report_display_table.horizontalHeader().setDefaultSectionSize(300)
        self.verticalLayout_2.addWidget(self.cur_report_display_table)
     
     
        
     
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Full Report Window"))
        #self.cur_report_display_table.resizeColumnsToContents()
        self.label.setText(_translate("MainWindow", "Full Report screen:"))



if __name__ == "__main__":
    listHeaders = ["H1","H2","H3","H4"]
    listValues = [1, 2, 3, 4]
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FullReportWindow()
    ui.setupUi(MainWindow, listHeaders, listValues)
    MainWindow.show()
    sys.exit(app.exec_())

