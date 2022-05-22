import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class FileExplorerWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","CSV (*.csv)", options=options)

    
    # def openFileNamesDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
    #     if files:
    #         print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","CSV (*.csv)", options=options)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileExplorerWidget()
    sys.exit(app.exec_())


class SaveFileExplorerWidget(FileExplorerWidget):
    def __init__(self):
        super().__init__()
    
    def initUI(self):
        super().initUI()
        self.saveFileDialog()

class OpenFileExplorerWidget(FileExplorerWidget):
    def __init__(self):
        super().__init__()
    
    def initUI(self):
        super().initUI()
        self.openFileNameDialog()
