from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtSql import QSqlTableModel, QSqlQuery, QSqlRecord
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QIcon, QAction
import sys
import webbrowser

from mainwindow_ui import Ui_MainWindow
from addComponentForm import NewComponentForm
from stateChangeForm import StateChange
from deleteDialog import DeleteDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icons/icon.png"))
        self.addActionsToWidgets()
        self.setTableModel()
    
    def setTableModel(self)->None:
        self.tableModel = QSqlTableModel()
        self.tableModel.setTable("components")
        self.tableModel.setEditStrategy(QSqlTableModel.OnRowChange)
        self.tableModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.tableModel.setHeaderData(1, Qt.Horizontal, "Element")
        self.tableModel.setHeaderData(2, Qt.Horizontal, "Value")
        self.tableModel.setHeaderData(3, Qt.Horizontal, "Category")
        self.tableModel.setHeaderData(4, Qt.Horizontal, "Mounting Type")
        self.tableModel.setHeaderData(5, Qt.Horizontal, "Package")
        self.tableModel.setHeaderData(6, Qt.Horizontal, "Price")
        self.tableModel.setHeaderData(7, Qt.Horizontal, "Qty.")
        self.tableModel.setHeaderData(8, Qt.Horizontal, "Unit")
        self.tableModel.setHeaderData(9, Qt.Horizontal, "Docs")
        self.tableModel.setHeaderData(10, Qt.Horizontal, "Min")
        self.tableModel.setHeaderData(11, Qt.Horizontal, "Comment")
        self.tableModel.select()
        self.tableView.setModel(self.tableModel)
    
    def addActionsToWidgets(self)->None:
        self.actionExit.triggered.connect(lambda: sys.exit(1))
        self.actionAdd_new.triggered.connect(lambda: self.newComponent())
        self.actionAbout.triggered.connect(lambda: self.docs())
        self.actionDocs.triggered.connect(lambda: self.about())
        
        self.tableView.addAction(self.actionIncreaseTheState)
        self.tableView.addAction(self.actionIncreaseTheStateBy)
        self.tableView.addAction(self.actionReduceTheState)
        self.tableView.addAction(self.actionReduceTheStateBy)
        self.tableView.addAction(self.actionResetState)
        
        self.tableView.addAction(self.actionEditComponent)
        self.tableView.addAction(self.actionDeleteComponent)
        self.tableView.addAction(self.actionUpdateDatabase)
        
        self.tableView.addAction(self.actionLookForDocumentationAtAllDatasheetCom)
        self.tableView.addAction(self.actionLookForDocumentationAtTMEeu)
        self.tableView.addAction(self.actionLookForDocumentationAtMouserCom)
        self.tableView.addAction(self.actionLookForDocumentationAtDigiKeyCom)
        self.tableView.addAction(self.actionLookForDocumentationAtFarnellCom)
        
        self.actionIncreaseTheState.triggered.connect(lambda: self.increaseState(self.getIndexList()))
        self.actionReduceTheState.triggered.connect(lambda: self.reduceState(self.getIndexList()))
        self.actionUpdateDatabase.triggered.connect(lambda: self.tableModel.select())
        self.actionIncreaseTheStateBy.triggered.connect(lambda: self.increaseReduceForm(self.getIndexList(), increase=True))
        self.actionReduceTheStateBy.triggered.connect(lambda: self.increaseReduceForm(self.getIndexList(), increase=False))
        self.actionResetState.triggered.connect(lambda: self.resetState(self.getIndexList()))
        self.actionDeleteComponent.triggered.connect(lambda: self.deleteComponentsDialog(self.getIndexList()))
        self.actionEditComponent.triggered.connect(lambda: self.editComponent(self.getIndex()))
        
        self.actionLookForDocumentationAtFarnellCom.triggered.connect(lambda: self.site(self.getIndexList(),"https://pl.farnell.com/search?st="))
        self.actionLookForDocumentationAtAllDatasheetCom.triggered.connect(lambda: self.site(self.getIndexList(), "https://www.alldatasheet.com/view.jsp?Searchword="))
        self.actionLookForDocumentationAtDigiKeyCom.triggered.connect(lambda: self.site(self.getIndexList()))
        self.actionLookForDocumentationAtMouserCom.triggered.connect(lambda: self.site(self.getIndexList(),"https://eu.mouser.com/c/?q="))
        self.actionLookForDocumentationAtTMEeu.triggered.connect(lambda: self.site(self.getIndexList(),"https://www.tme.eu/pl/katalog/?queryPhrase="))
        
    def newComponent(self)->None:
        form = NewComponentForm()
        form.model.select()
        form.addAndExitButton.clicked.connect(lambda: self.insertRecord(form.saveAndExit()))
        form.addAndContinueButton.clicked.connect(lambda: self.insertRecord(form.save()))
        form.show()
        
    def insertRecord(self, record:QSqlRecord):
        if self.tableModel.insertRecord(-1, record):
            self.tableModel.select()
            
    def getIndexList(self)->list[QModelIndex]:
        return self.tableView.selectionModel().selection().indexes()
    
    def getIndex(self)->QModelIndex:
        return self.tableView.selectionModel().selection().indexes()[0]
    
    def deleteComponentsDialog(self, indexList:list)->None:
        dialog = DeleteDialog()
        dialog.setText(len(indexList))
        dialog.buttonBox.accepted.connect(lambda: self.deleteComponents(indexList))
        dialog.buttonBox.accepted.connect(lambda: dialog.close())
        # dialog.buttonBox.accepted.connect(lambda: self.close())
        dialog.buttonBox.rejected.connect(lambda: dialog.close())
        dialog.show()
    
    def deleteComponents(self, indexList:list)->None:
        for index in indexList:
            self.tableModel.deleteRowFromTable(index.row())
        self.tableModel.select()
        
    def increaseReduceForm(self, indexList:list, increase:bool)->None:
        form = StateChange()
        form.show()
        if increase:
            form.label.setText("Increase value by:")
            form.buttonBox.accepted.connect(lambda: self.increaseState(indexList, form.getValue()))
        else:
            form.label.setText("Reduce value by:")
            form.buttonBox.accepted.connect(lambda: self.reduceState(indexList, form.getValue()))
        form.buttonBox.accepted.connect(lambda: form.close())
        
    def increaseState(self, indexList:list, by:int = 1)->None:
        for index in indexList:
            qtyIndex = self.tableModel.index(index.row(), 7)
            self.tableModel.setData(qtyIndex, int(self.tableModel.data(qtyIndex))+by)
        self.tableModel.submitAll()
        self.tableModel.select()
    
    def reduceState(self, indexList:list, by:int = 1)->None:
        for index in indexList:
            qtyIndex = self.tableModel.index(index.row(), 7)
            self.tableModel.setData(qtyIndex, int(self.tableModel.data(qtyIndex))-by)
        self.tableModel.submitAll()
        self.tableModel.select()
    
    def resetState(self, indexList:list)->None:
        for index in indexList:
            qtyIndex = self.tableModel.index(index.row(), 7)
            self.tableModel.setData(qtyIndex, 0)
        self.tableModel.submitAll()
        self.tableModel.select()
        
    def editComponent(self, index:int):
        form = NewComponentForm(index)
        form.model.select()
        form.addAndExitButton.clicked.connect(lambda: self.updateComponent(index, form.updateAndExit()))
        form.addAndContinueButton.hide()
        form.show()
    
    def updateComponent(self, index:int, record:QSqlRecord):
        if self.tableModel.updateRowInTable(index, record):
            self.tableModel.select()
    
    def updateDatabase(self)->None:
        self.tableModel.setFilter(None)
        self.tableModel.select()
    
    def openSite(self, link:str)->None:
        webbrowser.open(link)
    
    def site(self, indexList:list, searchLink:str="https://letmegooglethat.com/?q=")->None:
        for index in indexList:
            elementNameIndex = self.tableModel.index(index.row(),1)
            elementName = self.tableModel.data(elementNameIndex)
            self.openSite(searchLink+elementName)
    #TO DO
    def importFromCSV(self):
        pass
    #TO DO
    def importFromXML(self):
        pass
    #TO DO
    def exportToCSV(self):
        pass
    #TO DO
    def exportToXML(self):
        pass
    #TO DO
    def restoreFromDb(self):
        pass
    #TO DO
    def configuration(self):
        pass
    
    def docs(self):
        self.openSite("https://github.com/robixxxxx/Electronic-Components-Database/blob/main/README.md")
    
    def about(self):
        self.openSite("https://github.com/robixxxxx/Electronic-Components-Database/blob/main/README.md")
    