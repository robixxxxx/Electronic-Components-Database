# from PySide6.QtCore import QVariant
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import QModelIndex
from database import *
from addComponentForm_ui import Ui_addComonentForm
import copy



#TO DO:
#Duplicates in combobox not allowed
class NewComponentForm(QWidget, Ui_addComonentForm):
    def __init__(self, index:QModelIndex=None):
        super(NewComponentForm, self).__init__()
        self.setupUi(self)
        self.index=index
        # self.db = QSqlDatabase("components")
        self.model = QSqlTableModel()
        self.setWindowTitle("Add Component Window")
        self.setWindowIcon(QIcon("icons/icon.png"))
        if(self.index!= None):
            print(self.model.record(self.index.row()).field(0).value())
            # self.componentInput.setEditText()
            # self.valueInput.setText(self.model.record(self.index.row()).field(1).value())
            # self.categoryInput.setEditText(self.model.record(self.index.row()).field(2).value())
            # self.mountTypeInput.setEditText(self.model.record(self.index.row()).field(3).value())
            # self.packageInput.setEditText(self.model.record(self.index.row()).field(4).value())
            # self.priceInput.setText(self.model.record(self.index.row()).field(5).value())
            # self.quantityInput.setText(self.model.record(self.index.row()).field(6).value())
            # self.unitInput.setEditText(self.model.record(self.index.row()).field(7).value())
            # self.minStateInput.setText(self.model.record(self.index.row()).field(8).value())
            # self.packageInput.setText(self.model.record(self.index.row()).field(9).value())
            # self.docsInput.setText(self.model.record(self.index.row()).field(10).value())
            # self.commentInput.setText(self.model.record(self.index.row()).field(11).value())
            # self.locationInput.setEditText()

        


    def save(self):
        record = self.createRecord()
        self.clear()
        return record
    
    def clear(self):
        self.componentInput.clearEditText()
        self.valueInput.clear()
        self.categoryInput.clearEditText()
        self.mountTypeInput.clearEditText()
        self.packageInput.clearEditText()
        self.priceInput.clear()
        self.quantityInput.clear()
        self.unitInput.clearEditText()
        self.minStateInput.clear()
        self.packageInput.clear()
        self.docsInput.clear()
        self.commentInput.clear()
        self.locationInput.clearEditText()

    def saveAndExit(self):
        record = self.createRecord()
        self.close()
        return record
    
    def updateAndExit(self):
        pass
    
    def createRecord(self, record = QSqlRecord()):
        record = QSqlRecord()
        record.append(QSqlField("id"))
        record.setNull("id")
        record.append(QSqlField("element"))
        record.setValue("element", self.componentInput.currentText())
        record.append(QSqlField("value"))
        record.setValue("value", self.valueInput.text())
        record.append(QSqlField("category"))
        record.setValue("category", self.categoryInput.currentText())
        record.append(QSqlField("mount"))
        record.setValue("mount", self.mountTypeInput.currentText())
        record.append(QSqlField("package"))
        record.setValue("package", self.packageInput.currentText())
        record.append(QSqlField("price"))
        record.setValue("price", self.priceInput.text())
        record.append(QSqlField("qty"))
        record.setValue("qty", self.quantityInput.text())
        record.append(QSqlField("unit"))
        record.setValue("unit", self.unitInput.currentText())
        record.append(QSqlField("min"))
        record.setValue("min", self.minStateInput.text())
        record.append(QSqlField("docs"))
        record.setValue("docs", self.docsInput.text())
        record.append(QSqlField("comment"))
        record.setValue("comment", self.commentInput.text())
        return record