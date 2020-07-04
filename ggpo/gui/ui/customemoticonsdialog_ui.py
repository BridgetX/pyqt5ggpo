# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ggpo/gui/ui/customemoticonsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmoticonDialog(object):
    def setupUi(self, EmoticonDialog):
        EmoticonDialog.setObjectName("EmoticonDialog")
        EmoticonDialog.resize(300, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(EmoticonDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(EmoticonDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.uiEmoticonTextEdit = QtWidgets.QTextEdit(EmoticonDialog)
        self.uiEmoticonTextEdit.setObjectName("uiEmoticonTextEdit")
        self.verticalLayout.addWidget(self.uiEmoticonTextEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(EmoticonDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EmoticonDialog)
        self.buttonBox.accepted.connect(EmoticonDialog.accept)
        self.buttonBox.rejected.connect(EmoticonDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EmoticonDialog)

    def retranslateUi(self, EmoticonDialog):
        _translate = QtCore.QCoreApplication.translate
        EmoticonDialog.setWindowTitle(_translate("EmoticonDialog", "Custom Emoticons"))
        self.label.setText(_translate("EmoticonDialog", "One emoticon per line"))
