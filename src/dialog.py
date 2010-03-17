# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Mar 16 17:51:25 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from PyKDE4.kio import KUrlRequester
from PyKDE4.kdeui import KLineEdit

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 160)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 10, 354, 121))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.dPfad = KUrlRequester(self.groupBox)
        self.dPfad.setObjectName("dPfad")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.dPfad)
        self.dNeuerName = KLineEdit(self.groupBox)
        self.dNeuerName.setEnabled(True)
        self.dNeuerName.setObjectName("dNeuerName")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.dNeuerName)
        self.dDateiEndung = QtGui.QLineEdit(self.groupBox)
        self.dDateiEndung.setObjectName("dDateiEndung")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.dDateiEndung)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 80, 351, 64))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dAbbrechen = QtGui.QPushButton(self.groupBox_2)
        self.dAbbrechen.setObjectName("dAbbrechen")
        self.horizontalLayout.addWidget(self.dAbbrechen)
        self.dAusfuehren = QtGui.QPushButton(self.groupBox_2)
        self.dAusfuehren.setDefault(False)
        self.dAusfuehren.setObjectName("dAusfuehren")
        self.horizontalLayout.addWidget(self.dAusfuehren)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Renamer", None, QtGui.QApplication.UnicodeUTF8))
        self.dNeuerName.setText(QtGui.QApplication.translate("Dialog", "Neuer Name", None, QtGui.QApplication.UnicodeUTF8))
        self.dDateiEndung.setText(QtGui.QApplication.translate("Dialog", "Dateiendung", None, QtGui.QApplication.UnicodeUTF8))
        self.dAbbrechen.setText(QtGui.QApplication.translate("Dialog", "Abbrechen", None, QtGui.QApplication.UnicodeUTF8))
        self.dAusfuehren.setText(QtGui.QApplication.translate("Dialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))

