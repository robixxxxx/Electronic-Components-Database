from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from  deleteDialog_ui import Ui_Dialog

class DeleteDialog(QWidget, Ui_Dialog):
    def __init__(self):
        super(DeleteDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Delete Components")
        self.setWindowIcon(QIcon("icons/icon.png"))
    
    def setText(self, value:int):
        self.label.setText("Do you want to delete "+str(value)+" element/s?")