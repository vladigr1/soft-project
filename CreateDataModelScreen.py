# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateDataModelScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from ast import Raise
from posixpath import basename
from PyQt5 import QtCore, QtGui, QtWidgets
from data_model import DataModel
from param import parms,lparms
import pandas as pd
import numpy as np
from widgets import SaveFileExplorerWidget

class Ui_MainWindow(object):
    dm_path = "./Data/DataModel/" 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 476)


        self.congetive_report_comboBox = QtWidgets.QComboBox()
        self.amount_of_sleep_report_comboBox = QtWidgets.QComboBox()
        self.water_consumption_report_comboBox = QtWidgets.QComboBox()
        self.physical_activity_report_comboBox = QtWidgets.QComboBox()
        self.time_socializing_report_comboBox = QtWidgets.QComboBox()
        self.lcomboBox = [
            self.congetive_report_comboBox,
            self.amount_of_sleep_report_comboBox,
            self.water_consumption_report_comboBox, 
            self.physical_activity_report_comboBox, 
            self.time_socializing_report_comboBox
        ]


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
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.model_name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_name_lineEdit.setObjectName("model_name_lineEdit")
        self.horizontalLayout.addWidget(self.model_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.num_of_days_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.num_of_days_lineEdit.setObjectName("num_of_days_lineEdit")
        self.horizontalLayout_2.addWidget(self.num_of_days_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.choose_parmeter_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_parmeter_table.sizePolicy().hasHeightForWidth())
        self.choose_parmeter_table.setSizePolicy(sizePolicy)
        self.choose_parmeter_table.setObjectName("choose_parmeter_table")
        self.choose_parmeter_table.setColumnCount(2)
        self.choose_parmeter_table.setRowCount(len(lparms))
        # item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.choose_parmeter_table.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        self.choose_parmeter_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # # self.choose_parmeter_table.setItem(0, 1, item)
        # # item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # # self.choose_parmeter_table.setItem(1, 1, item)
        # # item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setItem(2, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setItem(3, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.choose_parmeter_table.setItem(3, 1, item)
        self.verticalLayout_2.addWidget(self.choose_parmeter_table)
        self.save_model_btn = QtWidgets.QPushButton(self.centralwidget, clicked = self.save_mode_to_file)
        self.save_model_btn.setObjectName("save_model_btn")
        self.verticalLayout_2.addWidget(self.save_model_btn)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.choose_model_to_form_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.choose_model_to_form_comboBox.setObjectName("choose_model_to_form_comboBox")
# Set choose_model_to_form_comboBox with Data models
        self.choose_model_to_form_comboBox.addItems(DataModel.lDataModels_names())
        self.horizontalLayout_3.addWidget(self.choose_model_to_form_comboBox)
        self.generate_form_btn = QtWidgets.QPushButton(self.centralwidget, clicked= self.generate_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_form_btn.sizePolicy().hasHeightForWidth())
        self.generate_form_btn.setSizePolicy(sizePolicy)
        self.generate_form_btn.setObjectName("generate_form_btn")
        self.horizontalLayout_3.addWidget(self.generate_form_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Create new data model:"))
        self.label_2.setText(_translate("MainWindow", "model name"))
        self.model_name_lineEdit.setText(_translate("MainWindow", "sleep analysis"))
        self.label_3.setText(_translate("MainWindow", "number of days"))
        self.num_of_days_lineEdit.setText(_translate("MainWindow", "14"))

        for i in range(len(lparms)):
            item = QtWidgets.QTableWidgetItem()
            self.choose_parmeter_table.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem()
            self.choose_parmeter_table.setItem(i, 0, item)
            item = self.choose_parmeter_table.verticalHeaderItem(i)
            item.setText(_translate("MainWindow",lparms[i].title()))
            item = self.choose_parmeter_table.item(i, 0)
            item.setText(_translate("MainWindow", lparms[i].unit()))
        # item = self.choose_parmeter_table.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "amount of sleep"))
        # item = self.choose_parmeter_table.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "water consumption"))
        # item = self.choose_parmeter_table.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "physical activity"))

        
        # item = self.choose_parmeter_table.item(1, 0)
        # item.setText(_translate("MainWindow", "double"))
        # item = self.choose_parmeter_table.item(2, 0)
        # item.setText(_translate("MainWindow", "double"))
        # item = self.choose_parmeter_table.item(3, 0)
        # item.setText(_translate("MainWindow", "integer"))

        item = self.choose_parmeter_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "unit"))
        item = self.choose_parmeter_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "status"))
        __sortingEnabled = self.choose_parmeter_table.isSortingEnabled()
        self.choose_parmeter_table.setSortingEnabled(False)


        # Set table
        self.loptions = [" ","Basic","Derived"]
        self.congetive_report_comboBox.addItems(self.loptions)
        self.choose_parmeter_table.setCellWidget(0, 1, self.congetive_report_comboBox)
        

        self.amount_of_sleep_report_comboBox.addItems(self.loptions)
        self.choose_parmeter_table.setCellWidget(1, 1, self.amount_of_sleep_report_comboBox)
        

        self.water_consumption_report_comboBox.addItems(self.loptions)
        self.choose_parmeter_table.setCellWidget(2, 1, self.water_consumption_report_comboBox)
        
        
        self.physical_activity_report_comboBox.addItems(self.loptions)
        self.choose_parmeter_table.setCellWidget(3, 1, self.physical_activity_report_comboBox)
        

        self.time_socializing_report_comboBox.addItems(self.loptions)
        self.choose_parmeter_table.setCellWidget(4, 1, self.time_socializing_report_comboBox)
        
        self.choose_parmeter_table.setSortingEnabled(__sortingEnabled)
        self.save_model_btn.setText(_translate("MainWindow", "save model"))
        self.label_4.setText(_translate("MainWindow", "model name"))
        #self.choose_model_to_form_comboBox.setItemText(0, _translate("MainWindow", "sleep analysis 1"))
        self.generate_form_btn.setText(_translate("MainWindow", "generate form"))

# devloper define stuff
    def save_mode_to_file(self):
        lbasic = []
        derived = None
        try:
            for i in range(self.choose_parmeter_table.rowCount()):
                if str(self.lcomboBox[i].currentText()) !=' ':
                    if str(self.lcomboBox[i].currentText()) == self.loptions[1]: # 'Basic'
                        lbasic.append(parms[self.choose_parmeter_table.verticalHeaderItem(i).text()])
                    if str(self.lcomboBox[i].currentText()) == self.loptions[2]: # 'Derived'
                        derived = parms[self.choose_parmeter_table.verticalHeaderItem(i).text()]
            if derived is None :
                raise Exception("Didn't pick derived parameter")
            if lbasic == [] :
                raise Exception("Didn't pick  basic parameters")
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText(str(e))
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
            return

                
        dm = DataModel(self.model_name_lineEdit.text(), derived, lbasic,14)
        
        # implment get from UI the dm
        dm.save_to_file()
        self.choose_model_to_form_comboBox.addItem(self.model_name_lineEdit.text())

    def generate_form(self):
        model_name = str(self.choose_model_to_form_comboBox.currentText())
        try:
            num_of_days = int(self.num_of_days_lineEdit.text())
        except Exception:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Input can only be a number')
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        data_model = DataModel.model_name_to_data_model(model_name)
        num_params = len(data_model.basic_parameeters()) + 1

        df = data_model.to_DataFrame()
        luints = [data_model.derivied_parameter().unit()] + [parm.unit() for parm in data_model.basic_parameeters()]
        data = [pd.Series(luints, index=df.columns )]
        data += num_of_days*[pd.Series(num_params*[np.nan], index=df.columns )]
        mod_df  = df.append(data, ignore_index=True)

        # Popup windows for form
        dlg = SaveFileExplorerWidget()
        if dlg.fileName != '':
            mod_df.to_csv(dlg.fileName +'.csv')
            data_model.appendForm(basename(dlg.fileName))

        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
