# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'componentForm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_comonentForm(object):
    def setupUi(self, comonentForm):
        if not comonentForm.objectName():
            comonentForm.setObjectName(u"comonentForm")
        comonentForm.resize(600, 426)
        icon = QIcon()
        icon.addFile(u"../../../path1.png", QSize(), QIcon.Normal, QIcon.Off)
        comonentForm.setWindowIcon(icon)
        self.valueInput = QLineEdit(comonentForm)
        self.valueInput.setObjectName(u"valueInput")
        self.valueInput.setGeometry(QRect(90, 130, 200, 21))
        self.priceInput = QLineEdit(comonentForm)
        self.priceInput.setObjectName(u"priceInput")
        self.priceInput.setGeometry(QRect(90, 250, 200, 21))
        self.quantityInput = QLineEdit(comonentForm)
        self.quantityInput.setObjectName(u"quantityInput")
        self.quantityInput.setGeometry(QRect(90, 280, 200, 21))
        self.minStateInput = QLineEdit(comonentForm)
        self.minStateInput.setObjectName(u"minStateInput")
        self.minStateInput.setGeometry(QRect(90, 370, 200, 21))
        self.docsInput = QLineEdit(comonentForm)
        self.docsInput.setObjectName(u"docsInput")
        self.docsInput.setGeometry(QRect(90, 400, 200, 21))
        self.commentInput = QLineEdit(comonentForm)
        self.commentInput.setObjectName(u"commentInput")
        self.commentInput.setGeometry(QRect(320, 130, 271, 211))
        self.componentLabel = QLabel(comonentForm)
        self.componentLabel.setObjectName(u"componentLabel")
        self.componentLabel.setGeometry(QRect(10, 100, 75, 20))
        self.valueLabel = QLabel(comonentForm)
        self.valueLabel.setObjectName(u"valueLabel")
        self.valueLabel.setGeometry(QRect(10, 130, 75, 20))
        self.packageLabel = QLabel(comonentForm)
        self.packageLabel.setObjectName(u"packageLabel")
        self.packageLabel.setGeometry(QRect(10, 190, 75, 20))
        self.mountTypeLabel = QLabel(comonentForm)
        self.mountTypeLabel.setObjectName(u"mountTypeLabel")
        self.mountTypeLabel.setGeometry(QRect(10, 220, 75, 20))
        self.priceLabel = QLabel(comonentForm)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setGeometry(QRect(10, 250, 75, 20))
        self.quantityLabel = QLabel(comonentForm)
        self.quantityLabel.setObjectName(u"quantityLabel")
        self.quantityLabel.setGeometry(QRect(10, 280, 75, 20))
        self.unitLabel = QLabel(comonentForm)
        self.unitLabel.setObjectName(u"unitLabel")
        self.unitLabel.setGeometry(QRect(10, 310, 75, 20))
        self.minStateLabel = QLabel(comonentForm)
        self.minStateLabel.setObjectName(u"minStateLabel")
        self.minStateLabel.setGeometry(QRect(10, 370, 75, 20))
        self.docsLabel = QLabel(comonentForm)
        self.docsLabel.setObjectName(u"docsLabel")
        self.docsLabel.setGeometry(QRect(10, 400, 75, 20))
        self.categoryLabel = QLabel(comonentForm)
        self.categoryLabel.setObjectName(u"categoryLabel")
        self.categoryLabel.setGeometry(QRect(10, 160, 75, 20))
        self.commentLabel = QLabel(comonentForm)
        self.commentLabel.setObjectName(u"commentLabel")
        self.commentLabel.setGeometry(QRect(320, 100, 61, 20))
        self.addAndContinueButton = QPushButton(comonentForm)
        self.addAndContinueButton.setObjectName(u"addAndContinueButton")
        self.addAndContinueButton.setGeometry(QRect(460, 350, 131, 61))
        self.addAndExitButton = QPushButton(comonentForm)
        self.addAndExitButton.setObjectName(u"addAndExitButton")
        self.addAndExitButton.setGeometry(QRect(321, 350, 131, 61))
        self.addAndExitButton.setInputMethodHints(Qt.ImhMultiLine)
        self.noneApi = QRadioButton(comonentForm)
        self.noneApi.setObjectName(u"noneApi")
        self.noneApi.setEnabled(False)
        self.noneApi.setGeometry(QRect(40, 70, 84, 19))
        self.tmeApi = QRadioButton(comonentForm)
        self.tmeApi.setObjectName(u"tmeApi")
        self.tmeApi.setEnabled(False)
        self.tmeApi.setGeometry(QRect(190, 70, 84, 19))
        self.mouserApi = QRadioButton(comonentForm)
        self.mouserApi.setObjectName(u"mouserApi")
        self.mouserApi.setEnabled(False)
        self.mouserApi.setGeometry(QRect(320, 70, 84, 19))
        self.digiKeyApi = QRadioButton(comonentForm)
        self.digiKeyApi.setObjectName(u"digiKeyApi")
        self.digiKeyApi.setEnabled(False)
        self.digiKeyApi.setGeometry(QRect(450, 70, 84, 19))
        self.componentInput = QComboBox(comonentForm)
        self.componentInput.setObjectName(u"componentInput")
        self.componentInput.setGeometry(QRect(90, 100, 200, 22))
        self.componentInput.setEditable(True)
        self.locationLabel = QLabel(comonentForm)
        self.locationLabel.setObjectName(u"locationLabel")
        self.locationLabel.setGeometry(QRect(10, 340, 75, 20))
        self.categoryInput = QComboBox(comonentForm)
        self.categoryInput.setObjectName(u"categoryInput")
        self.categoryInput.setGeometry(QRect(90, 160, 200, 22))
        self.categoryInput.setEditable(True)
        self.packageInput = QComboBox(comonentForm)
        self.packageInput.setObjectName(u"packageInput")
        self.packageInput.setGeometry(QRect(90, 190, 200, 22))
        self.packageInput.setEditable(True)
        self.mountTypeInput = QComboBox(comonentForm)
        self.mountTypeInput.setObjectName(u"mountTypeInput")
        self.mountTypeInput.setGeometry(QRect(90, 220, 200, 22))
        self.mountTypeInput.setEditable(True)
        self.unitInput = QComboBox(comonentForm)
        self.unitInput.setObjectName(u"unitInput")
        self.unitInput.setGeometry(QRect(90, 310, 200, 22))
        self.unitInput.setEditable(True)
        self.locationInput = QComboBox(comonentForm)
        self.locationInput.setObjectName(u"locationInput")
        self.locationInput.setGeometry(QRect(90, 340, 200, 22))
        self.locationInput.setEditable(True)
        QWidget.setTabOrder(self.componentInput, self.valueInput)
        QWidget.setTabOrder(self.valueInput, self.categoryInput)
        QWidget.setTabOrder(self.categoryInput, self.packageInput)
        QWidget.setTabOrder(self.packageInput, self.mountTypeInput)
        QWidget.setTabOrder(self.mountTypeInput, self.priceInput)
        QWidget.setTabOrder(self.priceInput, self.quantityInput)
        QWidget.setTabOrder(self.quantityInput, self.unitInput)
        QWidget.setTabOrder(self.unitInput, self.locationInput)
        QWidget.setTabOrder(self.locationInput, self.minStateInput)
        QWidget.setTabOrder(self.minStateInput, self.docsInput)
        QWidget.setTabOrder(self.docsInput, self.commentInput)
        QWidget.setTabOrder(self.commentInput, self.addAndExitButton)
        QWidget.setTabOrder(self.addAndExitButton, self.addAndContinueButton)
        QWidget.setTabOrder(self.addAndContinueButton, self.noneApi)
        QWidget.setTabOrder(self.noneApi, self.tmeApi)
        QWidget.setTabOrder(self.tmeApi, self.mouserApi)
        QWidget.setTabOrder(self.mouserApi, self.digiKeyApi)

        self.retranslateUi(comonentForm)

        QMetaObject.connectSlotsByName(comonentForm)
    # setupUi

    def retranslateUi(self, comonentForm):
        comonentForm.setWindowTitle(QCoreApplication.translate("comonentForm", u"Add Component", None))
        self.componentLabel.setText(QCoreApplication.translate("comonentForm", u"Component", None))
        self.valueLabel.setText(QCoreApplication.translate("comonentForm", u"Value", None))
        self.packageLabel.setText(QCoreApplication.translate("comonentForm", u"Package", None))
        self.mountTypeLabel.setText(QCoreApplication.translate("comonentForm", u"Mounting type", None))
        self.priceLabel.setText(QCoreApplication.translate("comonentForm", u"Price", None))
        self.quantityLabel.setText(QCoreApplication.translate("comonentForm", u"Quantity", None))
        self.unitLabel.setText(QCoreApplication.translate("comonentForm", u"Unit", None))
        self.minStateLabel.setText(QCoreApplication.translate("comonentForm", u"Minimum state", None))
        self.docsLabel.setText(QCoreApplication.translate("comonentForm", u"Documentation", None))
        self.categoryLabel.setText(QCoreApplication.translate("comonentForm", u"Category", None))
        self.commentLabel.setText(QCoreApplication.translate("comonentForm", u"Comment", None))
        self.addAndContinueButton.setText(QCoreApplication.translate("comonentForm", u"Add to database \n"
" and continue", None))
        self.addAndExitButton.setText(QCoreApplication.translate("comonentForm", u"Add to database\n"
" and exit", None))
        self.noneApi.setText(QCoreApplication.translate("comonentForm", u"RadioButton", None))
        self.tmeApi.setText(QCoreApplication.translate("comonentForm", u"RadioButton", None))
        self.mouserApi.setText(QCoreApplication.translate("comonentForm", u"RadioButton", None))
        self.digiKeyApi.setText(QCoreApplication.translate("comonentForm", u"RadioButton", None))
        self.locationLabel.setText(QCoreApplication.translate("comonentForm", u"Location", None))
    # retranslateUi

