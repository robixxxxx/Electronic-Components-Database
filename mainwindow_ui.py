# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 600)
        self.actionConfiguration = QAction(MainWindow)
        self.actionConfiguration.setObjectName(u"actionConfiguration")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAdd_new = QAction(MainWindow)
        self.actionAdd_new.setObjectName(u"actionAdd_new")
        self.actionDocs = QAction(MainWindow)
        self.actionDocs.setObjectName(u"actionDocs")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionRestore_from_db_file = QAction(MainWindow)
        self.actionRestore_from_db_file.setObjectName(u"actionRestore_from_db_file")
        self.actionFrom_csv = QAction(MainWindow)
        self.actionFrom_csv.setObjectName(u"actionFrom_csv")
        self.actionFrom_xls = QAction(MainWindow)
        self.actionFrom_xls.setObjectName(u"actionFrom_xls")
        self.actionTo_csv = QAction(MainWindow)
        self.actionTo_csv.setObjectName(u"actionTo_csv")
        self.actionTo_xls = QAction(MainWindow)
        self.actionTo_xls.setObjectName(u"actionTo_xls")
        self.actionDeleteComponent = QAction(MainWindow)
        self.actionDeleteComponent.setObjectName(u"actionDeleteComponent")
        self.actionIncreaseTheState = QAction(MainWindow)
        self.actionIncreaseTheState.setObjectName(u"actionIncreaseTheState")
        self.actionIncreaseTheStateBy = QAction(MainWindow)
        self.actionIncreaseTheStateBy.setObjectName(u"actionIncreaseTheStateBy")
        self.actionResetState = QAction(MainWindow)
        self.actionResetState.setObjectName(u"actionResetState")
        self.actionReduceTheStateBy = QAction(MainWindow)
        self.actionReduceTheStateBy.setObjectName(u"actionReduceTheStateBy")
        self.actionReduceTheState = QAction(MainWindow)
        self.actionReduceTheState.setObjectName(u"actionReduceTheState")
        self.actionEditComponent = QAction(MainWindow)
        self.actionEditComponent.setObjectName(u"actionEditComponent")
        self.actionUpdateDatabase = QAction(MainWindow)
        self.actionUpdateDatabase.setObjectName(u"actionUpdateDatabase")
        self.actionLookForDocumentationAtTMEeu = QAction(MainWindow)
        self.actionLookForDocumentationAtTMEeu.setObjectName(u"actionLookForDocumentationAtTMEeu")
        self.actionLookForDocumentationAtMouserCom = QAction(MainWindow)
        self.actionLookForDocumentationAtMouserCom.setObjectName(u"actionLookForDocumentationAtMouserCom")
        self.actionLookForDocumentationAtDigiKeyCom = QAction(MainWindow)
        self.actionLookForDocumentationAtDigiKeyCom.setObjectName(u"actionLookForDocumentationAtDigiKeyCom")
        self.actionLookForDocumentationAtFarnellCom = QAction(MainWindow)
        self.actionLookForDocumentationAtFarnellCom.setObjectName(u"actionLookForDocumentationAtFarnellCom")
        self.actionLookForDocumentationAtAllDatasheetCom = QAction(MainWindow)
        self.actionLookForDocumentationAtAllDatasheetCom.setObjectName(u"actionLookForDocumentationAtAllDatasheetCom")
        self.actionCategory_Filter = QAction(MainWindow)
        self.actionCategory_Filter.setObjectName(u"actionCategory_Filter")
        self.actionCategory_Filter.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.typeFilter = QComboBox(self.centralwidget)
        self.typeFilter.setObjectName(u"typeFilter")
        self.typeFilter.setAutoFillBackground(False)
        self.typeFilter.setEditable(True)
        self.typeFilter.setFrame(False)

        self.horizontalLayout.addWidget(self.typeFilter)

        self.categoryFilter = QComboBox(self.centralwidget)
        self.categoryFilter.setObjectName(u"categoryFilter")
        self.categoryFilter.setAutoFillBackground(False)
        self.categoryFilter.setEditable(True)
        self.categoryFilter.setFrame(False)

        self.horizontalLayout.addWidget(self.categoryFilter)

        self.componentFilter = QComboBox(self.centralwidget)
        self.componentFilter.setObjectName(u"componentFilter")
        self.componentFilter.setAutoFillBackground(False)
        self.componentFilter.setEditable(True)
        self.componentFilter.setFrame(False)

        self.horizontalLayout.addWidget(self.componentFilter)

        self.valueFilter = QComboBox(self.centralwidget)
        self.valueFilter.setObjectName(u"valueFilter")
        self.valueFilter.setAutoFillBackground(False)
        self.valueFilter.setEditable(True)
        self.valueFilter.setFrame(False)

        self.horizontalLayout.addWidget(self.valueFilter)

        self.packageFilter = QComboBox(self.centralwidget)
        self.packageFilter.setObjectName(u"packageFilter")
        self.packageFilter.setAutoFillBackground(False)
        self.packageFilter.setEditable(True)
        self.packageFilter.setFrame(False)

        self.horizontalLayout.addWidget(self.packageFilter)

        self.Clear = QPushButton(self.centralwidget)
        self.Clear.setObjectName(u"Clear")

        self.horizontalLayout.addWidget(self.Clear)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        self.tableView.setMouseTracking(False)
        self.tableView.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tableView.setAcceptDrops(True)
        self.tableView.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.tableView.setDragEnabled(True)
        self.tableView.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableView)

        self.verticalLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1300, 21))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuDatabase = QMenu(self.menubar)
        self.menuDatabase.setObjectName(u"menuDatabase")
        self.menu = QMenu(self.menuDatabase)
        self.menu.setObjectName(u"menu")
        self.menuExport = QMenu(self.menuDatabase)
        self.menuExport.setObjectName(u"menuExport")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuComponents = QMenu(self.menubar)
        self.menuComponents.setObjectName(u"menuComponents")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuComponents.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuOptions.addAction(self.actionConfiguration)
        self.menuDatabase.addAction(self.menu.menuAction())
        self.menuDatabase.addAction(self.menuExport.menuAction())
        self.menuDatabase.addAction(self.actionRestore_from_db_file)
        self.menu.addAction(self.actionFrom_csv)
        self.menu.addAction(self.actionFrom_xls)
        self.menuExport.addAction(self.actionTo_csv)
        self.menuExport.addAction(self.actionTo_xls)
        self.menuFile.addAction(self.actionExit)
        self.menuComponents.addAction(self.actionAdd_new)
        self.menuHelp.addAction(self.actionDocs)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.categoryFilter.editTextChanged.connect(self.actionCategory_Filter.trigger)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Electronic Components Database", None))
        self.actionConfiguration.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_new.setText(QCoreApplication.translate("MainWindow", u"Add new", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionDocs.setText(QCoreApplication.translate("MainWindow", u"Docs", None))
#if QT_CONFIG(shortcut)
        self.actionDocs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionRestore_from_db_file.setText(QCoreApplication.translate("MainWindow", u"Restore from *.db file", None))
        self.actionFrom_csv.setText(QCoreApplication.translate("MainWindow", u"From *.csv", None))
        self.actionFrom_xls.setText(QCoreApplication.translate("MainWindow", u"From *.xml", None))
        self.actionTo_csv.setText(QCoreApplication.translate("MainWindow", u"To *.csv", None))
        self.actionTo_xls.setText(QCoreApplication.translate("MainWindow", u"To *.xml", None))
        self.actionDeleteComponent.setText(QCoreApplication.translate("MainWindow", u"Delete Component", None))
#if QT_CONFIG(shortcut)
        self.actionDeleteComponent.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionIncreaseTheState.setText(QCoreApplication.translate("MainWindow", u"Increas the state", None))
#if QT_CONFIG(shortcut)
        self.actionIncreaseTheState.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionIncreaseTheStateBy.setText(QCoreApplication.translate("MainWindow", u"Increase the state by...", None))
        self.actionResetState.setText(QCoreApplication.translate("MainWindow", u"Reset state", None))
        self.actionReduceTheStateBy.setText(QCoreApplication.translate("MainWindow", u"Reduce the state by ...", None))
        self.actionReduceTheState.setText(QCoreApplication.translate("MainWindow", u"Reduce the state", None))
        self.actionEditComponent.setText(QCoreApplication.translate("MainWindow", u"Edit component", None))
        self.actionUpdateDatabase.setText(QCoreApplication.translate("MainWindow", u"Update Database", None))
        self.actionLookForDocumentationAtTMEeu.setText(QCoreApplication.translate("MainWindow", u"Look for documentation at TME.eu", None))
        self.actionLookForDocumentationAtMouserCom.setText(QCoreApplication.translate("MainWindow", u"Look for documentation at Mouser.com", None))
        self.actionLookForDocumentationAtDigiKeyCom.setText(QCoreApplication.translate("MainWindow", u"Look for documentation at DigiKey.com", None))
        self.actionLookForDocumentationAtFarnellCom.setText(QCoreApplication.translate("MainWindow", u"Look for documentation at Farnell.com", None))
        self.actionLookForDocumentationAtAllDatasheetCom.setText(QCoreApplication.translate("MainWindow", u"Look for documentation at AllDatasheet.com", None))
        self.actionCategory_Filter.setText(QCoreApplication.translate("MainWindow", u"Category Filter", None))
        self.typeFilter.setCurrentText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.categoryFilter.setCurrentText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.componentFilter.setCurrentText(QCoreApplication.translate("MainWindow", u"Component", None))
        self.valueFilter.setCurrentText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.packageFilter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package", None))
        self.Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("MainWindow", u"Database", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Import", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Program", None))
        self.menuComponents.setTitle(QCoreApplication.translate("MainWindow", u"Components", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

