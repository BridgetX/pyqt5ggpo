# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ggpo/gui/ui/savestatesdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SavestatesDialog(object):
    def setupUi(self, SavestatesDialog):
        SavestatesDialog.setObjectName("SavestatesDialog")
        SavestatesDialog.resize(630, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(SavestatesDialog)
        self.verticalLayout.setContentsMargins(2, 0, 2, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SavestatesDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.uiFilterLineEdit = QtWidgets.QLineEdit(SavestatesDialog)
        self.uiFilterLineEdit.setText("")
        self.uiFilterLineEdit.setObjectName("uiFilterLineEdit")
        self.horizontalLayout.addWidget(self.uiFilterLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.uiSavestatesTblv = QtWidgets.QTableView(SavestatesDialog)
        self.uiSavestatesTblv.setObjectName("uiSavestatesTblv")
        self.verticalLayout.addWidget(self.uiSavestatesTblv)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(SavestatesDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.verticalLayout.addWidget(self.uiButtonBox)

        self.retranslateUi(SavestatesDialog)
        self.uiButtonBox.accepted.connect(SavestatesDialog.accept)
        self.uiButtonBox.rejected.connect(SavestatesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SavestatesDialog)
        SavestatesDialog.setTabOrder(self.uiFilterLineEdit, self.uiSavestatesTblv)
        SavestatesDialog.setTabOrder(self.uiSavestatesTblv, self.uiButtonBox)

    def retranslateUi(self, SavestatesDialog):
        _translate = QtCore.QCoreApplication.translate
        SavestatesDialog.setWindowTitle(_translate("SavestatesDialog", "Unsupported game savestates"))
        self.label.setText(_translate("SavestatesDialog", "Filter:"))
