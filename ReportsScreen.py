# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportsScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.import_form_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_form_btn.setObjectName("import_form_btn")
        self.horizontalLayout.addWidget(self.import_form_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
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
        self.all_report_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.all_report_comboBox.setObjectName("all_report_comboBox")
        self.all_report_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.all_report_comboBox)
        self.show_report_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_report_btn.setObjectName("show_report_btn")
        self.horizontalLayout_2.addWidget(self.show_report_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.cur_report_display_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cur_report_display_table.sizePolicy().hasHeightForWidth())
        self.cur_report_display_table.setSizePolicy(sizePolicy)
        self.cur_report_display_table.setObjectName("cur_report_display_table")
        self.cur_report_display_table.setColumnCount(2)
        self.cur_report_display_table.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.cur_report_display_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_report_display_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_report_display_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_report_display_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_report_display_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_report_display_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_report_display_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cur_report_display_table.setItem(1, 1, item)
        self.verticalLayout_2.addWidget(self.cur_report_display_table)
        self.create_new_data_model_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_createDataModelScreen())
        self.create_new_data_model_btn.setObjectName("create_new_data_model_btn")
        self.verticalLayout_2.addWidget(self.create_new_data_model_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # user custom define parameters
        self.CreateDataModelScreen_window = None
        self.CreateDataModelScreen_ui = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Report screen:"))
        self.import_form_btn.setText(_translate("MainWindow", "import form"))
        self.label_3.setText(_translate("MainWindow", "choose report:"))
        self.all_report_comboBox.setItemText(0, _translate("MainWindow", "sleep analysis 1"))
        self.show_report_btn.setText(_translate("MainWindow", "show report"))
        item = self.cur_report_display_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "cognitive load"))
        item = self.cur_report_display_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "physical activity"))
        item = self.cur_report_display_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "rank"))
        item = self.cur_report_display_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "effect"))
        __sortingEnabled = self.cur_report_display_table.isSortingEnabled()
        self.cur_report_display_table.setSortingEnabled(False)
        item = self.cur_report_display_table.item(0, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.cur_report_display_table.item(0, 1)
        item.setText(_translate("MainWindow", "-"))
        item = self.cur_report_display_table.item(1, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.cur_report_display_table.item(1, 1)
        item.setText(_translate("MainWindow", "+"))
        self.cur_report_display_table.setSortingEnabled(__sortingEnabled)
        self.create_new_data_model_btn.setText(_translate("MainWindow", "create new data model"))

    def open_createDataModelScreen(self):
        import CreateDataModelScreen
        self.CreateDataModelScreen_window = QtWidgets.QMainWindow()
        self.CreateDataModelScreen_ui = CreateDataModelScreen.Ui_MainWindow()
        self.CreateDataModelScreen_ui.setupUi(self.CreateDataModelScreen_window)
        self.CreateDataModelScreen_window.show()
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

