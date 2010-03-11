# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Mar  9 17:21:52 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#from PyQt4 import *
#from PyKDE4.kio import KUrlRequester 

from PyKDE4.kio import KUrlRequester 
from PyKDE4.kdeui import KLineEdit
#from PyKDE4 import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(527, 126)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dPfad = KUrlRequester(self.groupBox)
        self.dPfad.setObjectName("dPfad")
        #self.dPfad.setMode(2)
        self.horizontalLayout.addWidget(self.dPfad)
        self.dNeuerName = KLineEdit(self.groupBox)
        self.dNeuerName.setObjectName("dNeuerName")
        self.horizontalLayout.addWidget(self.dNeuerName)
        self.dAusfuehren = QtGui.QPushButton(self.groupBox)
        self.dAusfuehren.setDefault(False)
        self.dAusfuehren.setObjectName("dAusfuehren")
        self.horizontalLayout.addWidget(self.dAusfuehren)
        self.dAbbrechen = QtGui.QPushButton(self.groupBox)
        self.dAbbrechen.setObjectName("dAbbrechen")
        self.horizontalLayout.addWidget(self.dAbbrechen)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Renamer", None, QtGui.QApplication.UnicodeUTF8))
        self.dAusfuehren.setText(QtGui.QApplication.translate("Dialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.dAbbrechen.setText(QtGui.QApplication.translate("Dialog", "Abbrechen", None, QtGui.QApplication.UnicodeUTF8))


