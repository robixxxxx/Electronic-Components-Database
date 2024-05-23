# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stateChangeForm.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QSizePolicy, QSpinBox, QWidget)

class Ui_increaseReduce(object):
    def setupUi(self, increaseReduce):
        if not increaseReduce.objectName():
            increaseReduce.setObjectName(u"increaseReduce")
        increaseReduce.resize(400, 117)
        self.buttonBox = QDialogButtonBox(increaseReduce)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(220, 90, 166, 21))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.spinBox = QSpinBox(increaseReduce)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(130, 40, 251, 22))
        self.label = QLabel(increaseReduce)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 101, 41))

        self.retranslateUi(increaseReduce)
        self.buttonBox.clicked.connect(self.spinBox.close)

        QMetaObject.connectSlotsByName(increaseReduce)
    # setupUi

    def retranslateUi(self, increaseReduce):
        increaseReduce.setWindowTitle(QCoreApplication.translate("increaseReduce", u"Form", None))
        self.label.setText(QCoreApplication.translate("increaseReduce", u"TextLabel", None))
    # retranslateUi

