# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\MyPythonFile\SecondTest\CalculatorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(338, 534)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_mod = QtWidgets.QPushButton(Dialog)
        self.btn_mod.setObjectName("btn_mod")
        self.gridLayout_2.addWidget(self.btn_mod, 1, 0, 1, 1)
        self.btn_clearE = QtWidgets.QPushButton(Dialog)
        self.btn_clearE.setObjectName("btn_clearE")
        self.gridLayout_2.addWidget(self.btn_clearE, 2, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(Dialog)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout_2.addWidget(self.btn_clear, 2, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(Dialog)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_2.addWidget(self.btn_5, 4, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(Dialog)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_2.addWidget(self.btn_6, 4, 2, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(Dialog)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_2.addWidget(self.btn_3, 5, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(Dialog)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_2.addWidget(self.btn_0, 6, 1, 1, 1)
        self.btn_backSpace = QtWidgets.QPushButton(Dialog)
        self.btn_backSpace.setObjectName("btn_backSpace")
        self.gridLayout_2.addWidget(self.btn_backSpace, 2, 2, 1, 1)
        self.btn_div = QtWidgets.QPushButton(Dialog)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout_2.addWidget(self.btn_div, 2, 3, 1, 1)
        self.btn_sqt = QtWidgets.QPushButton(Dialog)
        self.btn_sqt.setObjectName("btn_sqt")
        self.gridLayout_2.addWidget(self.btn_sqt, 1, 2, 1, 1)
        self.btn_fract = QtWidgets.QPushButton(Dialog)
        self.btn_fract.setObjectName("btn_fract")
        self.gridLayout_2.addWidget(self.btn_fract, 1, 3, 1, 1)
        self.btn_sqtRoot = QtWidgets.QPushButton(Dialog)
        self.btn_sqtRoot.setObjectName("btn_sqtRoot")
        self.gridLayout_2.addWidget(self.btn_sqtRoot, 1, 1, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(Dialog)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(Dialog)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout_2.addWidget(self.btn_dot, 6, 2, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(Dialog)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 3, 2, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(Dialog)
        self.btn_mul.setObjectName("btn_mul")
        self.gridLayout_2.addWidget(self.btn_mul, 3, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(Dialog)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_2.addWidget(self.btn_add, 5, 3, 1, 1)
        self.btn_min = QtWidgets.QPushButton(Dialog)
        self.btn_min.setObjectName("btn_min")
        self.gridLayout_2.addWidget(self.btn_min, 4, 3, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(Dialog)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_2.addWidget(self.btn_1, 5, 0, 1, 1)
        self.btn_eql = QtWidgets.QPushButton(Dialog)
        self.btn_eql.setObjectName("btn_eql")
        self.gridLayout_2.addWidget(self.btn_eql, 6, 3, 1, 1)
        self.btn_addMin = QtWidgets.QPushButton(Dialog)
        self.btn_addMin.setObjectName("btn_addMin")
        self.gridLayout_2.addWidget(self.btn_addMin, 6, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(Dialog)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_2.addWidget(self.btn_2, 5, 1, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(Dialog)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_2.addWidget(self.btn_4, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_equation = QtWidgets.QLabel(Dialog)
        self.label_equation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_equation.setText("")
        self.label_equation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_equation.setObjectName("label_equation")
        self.verticalLayout.addWidget(self.label_equation)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(16)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_mod.setText(_translate("Dialog", "%"))
        self.btn_clearE.setText(_translate("Dialog", "CE"))
        self.btn_clear.setText(_translate("Dialog", "C"))
        self.btn_5.setText(_translate("Dialog", "5"))
        self.btn_6.setText(_translate("Dialog", "6"))
        self.btn_3.setText(_translate("Dialog", "3"))
        self.btn_0.setText(_translate("Dialog", "0"))
        self.btn_backSpace.setText(_translate("Dialog", "BackSpace"))
        self.btn_div.setText(_translate("Dialog", "/"))
        self.btn_sqt.setText(_translate("Dialog", "sqt"))
        self.btn_fract.setText(_translate("Dialog", "1/x"))
        self.btn_sqtRoot.setText(_translate("Dialog", "sqtRoot"))
        self.btn_8.setText(_translate("Dialog", "8"))
        self.btn_dot.setText(_translate("Dialog", "."))
        self.btn_9.setText(_translate("Dialog", "9"))
        self.btn_mul.setText(_translate("Dialog", "x"))
        self.btn_7.setText(_translate("Dialog", "7"))
        self.btn_add.setText(_translate("Dialog", "+"))
        self.btn_min.setText(_translate("Dialog", "-"))
        self.btn_1.setText(_translate("Dialog", "1"))
        self.btn_eql.setText(_translate("Dialog", "="))
        self.btn_addMin.setText(_translate("Dialog", "+-"))
        self.btn_2.setText(_translate("Dialog", "2"))
        self.btn_4.setText(_translate("Dialog", "4"))
