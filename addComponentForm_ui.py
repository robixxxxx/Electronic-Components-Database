# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Robert\repos\Electronic\addComponentForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addComonentForm(object):
    def setupUi(self, addComonentForm):
        addComonentForm.setObjectName("addComonentForm")
        addComonentForm.resize(600, 426)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Robert\\repos\\Electronic\\../../../path1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addComonentForm.setWindowIcon(icon)
        self.valueInput = QtWidgets.QLineEdit(addComonentForm)
        self.valueInput.setGeometry(QtCore.QRect(90, 130, 200, 21))
        self.valueInput.setObjectName("valueInput")
        self.priceInput = QtWidgets.QLineEdit(addComonentForm)
        self.priceInput.setGeometry(QtCore.QRect(90, 250, 200, 21))
        self.priceInput.setObjectName("priceInput")
        self.quantityInput = QtWidgets.QLineEdit(addComonentForm)
        self.quantityInput.setGeometry(QtCore.QRect(90, 280, 200, 21))
        self.quantityInput.setObjectName("quantityInput")
        self.minStateInput = QtWidgets.QLineEdit(addComonentForm)
        self.minStateInput.setGeometry(QtCore.QRect(90, 370, 200, 21))
        self.minStateInput.setObjectName("minStateInput")
        self.docsInput = QtWidgets.QLineEdit(addComonentForm)
        self.docsInput.setGeometry(QtCore.QRect(90, 400, 200, 21))
        self.docsInput.setObjectName("docsInput")
        self.commentInput = QtWidgets.QLineEdit(addComonentForm)
        self.commentInput.setGeometry(QtCore.QRect(320, 130, 271, 211))
        self.commentInput.setObjectName("commentInput")
        self.componentLabel = QtWidgets.QLabel(addComonentForm)
        self.componentLabel.setGeometry(QtCore.QRect(10, 100, 75, 20))
        self.componentLabel.setObjectName("componentLabel")
        self.valueLabel = QtWidgets.QLabel(addComonentForm)
        self.valueLabel.setGeometry(QtCore.QRect(10, 130, 75, 20))
        self.valueLabel.setObjectName("valueLabel")
        self.packageLabel = QtWidgets.QLabel(addComonentForm)
        self.packageLabel.setGeometry(QtCore.QRect(10, 190, 75, 20))
        self.packageLabel.setObjectName("packageLabel")
        self.mountTypeLabel = QtWidgets.QLabel(addComonentForm)
        self.mountTypeLabel.setGeometry(QtCore.QRect(10, 220, 75, 20))
        self.mountTypeLabel.setObjectName("mountTypeLabel")
        self.priceLabel = QtWidgets.QLabel(addComonentForm)
        self.priceLabel.setGeometry(QtCore.QRect(10, 250, 75, 20))
        self.priceLabel.setObjectName("priceLabel")
        self.quantityLabel = QtWidgets.QLabel(addComonentForm)
        self.quantityLabel.setGeometry(QtCore.QRect(10, 280, 75, 20))
        self.quantityLabel.setObjectName("quantityLabel")
        self.unitLabel = QtWidgets.QLabel(addComonentForm)
        self.unitLabel.setGeometry(QtCore.QRect(10, 310, 75, 20))
        self.unitLabel.setObjectName("unitLabel")
        self.minStateLabel = QtWidgets.QLabel(addComonentForm)
        self.minStateLabel.setGeometry(QtCore.QRect(10, 370, 75, 20))
        self.minStateLabel.setObjectName("minStateLabel")
        self.docsLabel = QtWidgets.QLabel(addComonentForm)
        self.docsLabel.setGeometry(QtCore.QRect(10, 400, 75, 20))
        self.docsLabel.setObjectName("docsLabel")
        self.categoryLabel = QtWidgets.QLabel(addComonentForm)
        self.categoryLabel.setGeometry(QtCore.QRect(10, 160, 75, 20))
        self.categoryLabel.setObjectName("categoryLabel")
        self.commentLabel = QtWidgets.QLabel(addComonentForm)
        self.commentLabel.setGeometry(QtCore.QRect(320, 100, 61, 20))
        self.commentLabel.setObjectName("commentLabel")
        self.addAndContinueButton = QtWidgets.QPushButton(addComonentForm)
        self.addAndContinueButton.setGeometry(QtCore.QRect(460, 350, 131, 61))
        self.addAndContinueButton.setObjectName("addAndContinueButton")
        self.addAndExitButton = QtWidgets.QPushButton(addComonentForm)
        self.addAndExitButton.setGeometry(QtCore.QRect(321, 350, 131, 61))
        self.addAndExitButton.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.addAndExitButton.setObjectName("addAndExitButton")
        self.noneApi = QtWidgets.QRadioButton(addComonentForm)
        self.noneApi.setEnabled(False)
        self.noneApi.setGeometry(QtCore.QRect(40, 70, 84, 19))
        self.noneApi.setObjectName("noneApi")
        self.tmeApi = QtWidgets.QRadioButton(addComonentForm)
        self.tmeApi.setEnabled(False)
        self.tmeApi.setGeometry(QtCore.QRect(190, 70, 84, 19))
        self.tmeApi.setObjectName("tmeApi")
        self.mouserApi = QtWidgets.QRadioButton(addComonentForm)
        self.mouserApi.setEnabled(False)
        self.mouserApi.setGeometry(QtCore.QRect(320, 70, 84, 19))
        self.mouserApi.setObjectName("mouserApi")
        self.digiKeyApi = QtWidgets.QRadioButton(addComonentForm)
        self.digiKeyApi.setEnabled(False)
        self.digiKeyApi.setGeometry(QtCore.QRect(450, 70, 84, 19))
        self.digiKeyApi.setObjectName("digiKeyApi")
        self.componentInput = QtWidgets.QComboBox(addComonentForm)
        self.componentInput.setGeometry(QtCore.QRect(90, 100, 200, 22))
        self.componentInput.setEditable(True)
        self.componentInput.setObjectName("componentInput")
        self.locationLabel = QtWidgets.QLabel(addComonentForm)
        self.locationLabel.setGeometry(QtCore.QRect(10, 340, 75, 20))
        self.locationLabel.setObjectName("locationLabel")
        self.categoryInput = QtWidgets.QComboBox(addComonentForm)
        self.categoryInput.setGeometry(QtCore.QRect(90, 160, 200, 22))
        self.categoryInput.setEditable(True)
        self.categoryInput.setObjectName("categoryInput")
        self.packageInput = QtWidgets.QComboBox(addComonentForm)
        self.packageInput.setGeometry(QtCore.QRect(90, 190, 200, 22))
        self.packageInput.setEditable(True)
        self.packageInput.setObjectName("packageInput")
        self.mountTypeInput = QtWidgets.QComboBox(addComonentForm)
        self.mountTypeInput.setGeometry(QtCore.QRect(90, 220, 200, 22))
        self.mountTypeInput.setEditable(True)
        self.mountTypeInput.setObjectName("mountTypeInput")
        self.unitInput = QtWidgets.QComboBox(addComonentForm)
        self.unitInput.setGeometry(QtCore.QRect(90, 310, 200, 22))
        self.unitInput.setEditable(True)
        self.unitInput.setObjectName("unitInput")
        self.locationInput = QtWidgets.QComboBox(addComonentForm)
        self.locationInput.setGeometry(QtCore.QRect(90, 340, 200, 22))
        self.locationInput.setEditable(True)
        self.locationInput.setObjectName("locationInput")

        self.retranslateUi(addComonentForm)
        QtCore.QMetaObject.connectSlotsByName(addComonentForm)
        addComonentForm.setTabOrder(self.componentInput, self.valueInput)
        addComonentForm.setTabOrder(self.valueInput, self.categoryInput)
        addComonentForm.setTabOrder(self.categoryInput, self.packageInput)
        addComonentForm.setTabOrder(self.packageInput, self.mountTypeInput)
        addComonentForm.setTabOrder(self.mountTypeInput, self.priceInput)
        addComonentForm.setTabOrder(self.priceInput, self.quantityInput)
        addComonentForm.setTabOrder(self.quantityInput, self.unitInput)
        addComonentForm.setTabOrder(self.unitInput, self.locationInput)
        addComonentForm.setTabOrder(self.locationInput, self.minStateInput)
        addComonentForm.setTabOrder(self.minStateInput, self.docsInput)
        addComonentForm.setTabOrder(self.docsInput, self.commentInput)
        addComonentForm.setTabOrder(self.commentInput, self.addAndExitButton)
        addComonentForm.setTabOrder(self.addAndExitButton, self.addAndContinueButton)
        addComonentForm.setTabOrder(self.addAndContinueButton, self.noneApi)
        addComonentForm.setTabOrder(self.noneApi, self.tmeApi)
        addComonentForm.setTabOrder(self.tmeApi, self.mouserApi)
        addComonentForm.setTabOrder(self.mouserApi, self.digiKeyApi)

    def retranslateUi(self, addComonentForm):
        _translate = QtCore.QCoreApplication.translate
        addComonentForm.setWindowTitle(_translate("addComonentForm", "Add Component"))
        self.componentLabel.setText(_translate("addComonentForm", "Component"))
        self.valueLabel.setText(_translate("addComonentForm", "Value"))
        self.packageLabel.setText(_translate("addComonentForm", "Package"))
        self.mountTypeLabel.setText(_translate("addComonentForm", "Mounting type"))
        self.priceLabel.setText(_translate("addComonentForm", "Price"))
        self.quantityLabel.setText(_translate("addComonentForm", "Quantity"))
        self.unitLabel.setText(_translate("addComonentForm", "Unit"))
        self.minStateLabel.setText(_translate("addComonentForm", "Minimum state"))
        self.docsLabel.setText(_translate("addComonentForm", "Documentation"))
        self.categoryLabel.setText(_translate("addComonentForm", "Category"))
        self.commentLabel.setText(_translate("addComonentForm", "Comment"))
        self.addAndContinueButton.setText(_translate("addComonentForm", "Add to database \n"
" and continue"))
        self.addAndExitButton.setText(_translate("addComonentForm", "Add to database\n"
" and exit"))
        self.noneApi.setText(_translate("addComonentForm", "RadioButton"))
        self.tmeApi.setText(_translate("addComonentForm", "RadioButton"))
        self.mouserApi.setText(_translate("addComonentForm", "RadioButton"))
        self.digiKeyApi.setText(_translate("addComonentForm", "RadioButton"))
        self.locationLabel.setText(_translate("addComonentForm", "Location"))
