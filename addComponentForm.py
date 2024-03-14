from PyQt5.QtCore import QVariant
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtGui import QIcon
from database import *
from addComponentForm_ui import Ui_addComonentForm



#TO DO:
#Duplicates in combobox not allowed
class NewComponentForm(QWidget, Ui_addComonentForm):
    def __init__(self):
        super(NewComponentForm, self).__init__()
        self.setupUi(self)
        self.addAndExitButton.clicked.connect(lambda: self.saveAndExit())
        self.addAndContinueButton.clicked.connect(lambda: self.save())
        self.db = QSqlDatabase("components")
        self.model = QSqlTableModel()
        self.setWindowTitle("Add Component Window")
        self.setWindowIcon(QIcon("icons/icon.png"))
        
    def save(self):
        record = self.createRecord()
        return record
    
    def saveAndExit(self):
        record = self.createRecord()
        self.close()
        return record
    
    def createRecord(self):
        record = QSqlRecord()
        record.append(QSqlField("id", QVariant.String))
        record.setNull("id")
        record.append(QSqlField("element", QVariant.String))
        record.setValue("element", self.componentInput.currentText())
        record.append(QSqlField("value", QVariant.String))
        record.setValue("value", self.valueInput.text())
        record.append(QSqlField("category", QVariant.String))
        record.setValue("category", self.categoryInput.currentText())
        record.append(QSqlField("mount",QVariant.String))
        record.setValue("mount", self.mountTypeInput.currentText())
        record.append(QSqlField("package",QVariant.String))
        record.setValue("package", self.packageInput.currentText())
        record.append(QSqlField("price", QVariant.String))
        record.setValue("price", self.priceInput.text())
        record.append(QSqlField("qty", QVariant.String))
        record.setValue("qty", self.quantityInput.text())
        record.append(QSqlField("unit", QVariant.String))
        record.setValue("unit", self.unitInput.currentText())
        record.append(QSqlField("min", QVariant.String))
        record.setValue("min", self.minStateInput.text())
        record.append(QSqlField("docs", QVariant.String))
        record.setValue("docs", self.docsInput.text())
        record.append(QSqlField("comment", QVariant.String))
        record.setValue("comment", self.commentInput.text())
        return record