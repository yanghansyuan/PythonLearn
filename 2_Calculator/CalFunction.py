import sys
from CalculatorWindow import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import os #just test call cmd
from enum import Enum

class Cal_Action(Enum):
    Non = 0
    Add = 1
    Min = 2
    Equl = 3 

class Window(QtWidgets.QWidget):
    NOW_ACTION =""
    ORIGINAL_VAL = 0
    NOW_VAL = 0
    LAST_CALACTION = "none"
    LAST_INPUT_NUM = 0

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setUpBtnconnect()

    def setUpBtnconnect(self):
        # self.ui.btn_0.clicked.connect(self.wrapper)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_0.clicked.connect(lambda:self.numberPressed(0))
        self.ui.btn_1.clicked.connect(lambda:self.numberPressed(1))
        self.ui.btn_2.clicked.connect(lambda:self.numberPressed(2))
        self.ui.btn_3.clicked.connect(lambda:self.numberPressed(3))
        self.ui.btn_4.clicked.connect(lambda:self.numberPressed(4))
        self.ui.btn_5.clicked.connect(lambda:self.numberPressed(5))
        self.ui.btn_6.clicked.connect(lambda:self.numberPressed(6))
        self.ui.btn_7.clicked.connect(lambda:self.numberPressed(7))
        self.ui.btn_8.clicked.connect(lambda:self.numberPressed(8))
        self.ui.btn_9.clicked.connect(lambda:self.numberPressed(9))
        self.ui.btn_add.clicked.connect(self.setAdd)
        self.ui.btn_min.clicked.connect(self.setMin)
        self.ui.btn_eql.clicked.connect(self.equal)
        self.ui.btn_fract.clicked.connect(self.callCmd)

    def callCmd(self):
        os.system("ipconfig")

    def setNowAction(self, _action):
        self.NOW_ACTION = _action

    def setLastCalAction(self, _action):
        self.LAST_CALACTION = _action
        self.setNowAction("_action")

    def clear(self):

        self.NOW_VAL = 0
        self.ORIGINAL_VAL = 0
        self.ui.lcdNumber.display(self.NOW_VAL)
        print "clear 0"

    def setNowValZero(self):
        self.NOW_VAL = 0

    def setOriginalValZero(self):
        self.ORIGINAL_VAL = 0

    def numberPressed(self, num):

        if self.NOW_ACTION == "equal":
            self.setNowValZero() #should clear now val for new add after equal
            self.setNowAction("none")

        self.NOW_VAL = (self.NOW_VAL * 10) + num
        print self.NOW_VAL
        self.ui.lcdNumber.display(self.NOW_VAL)
        self.LAST_INPUT_NUM = num

    def setAdd(self):

        self.setLastCalAction("add")
        self.ui.label_equation.setText(str(self.NOW_VAL) + " +") #should have now_val for keep add
        self.ORIGINAL_VAL = self.NOW_VAL
        self.NOW_VAL = 0


    def setMin(self):

        self.setLastCalAction("min")
        self.ui.label_equation.setText(str(self.NOW_VAL) + " -") #should have now_val for keep add
        self.ORIGINAL_VAL = self.NOW_VAL
        self.NOW_VAL = 0

    def equal(self):
        self.ui.label_equation.setText("")

        if self.LAST_CALACTION == "add":
            self.NOW_VAL += self.LAST_INPUT_NUM # do the math
        else:
            self.setNowAction("equal")
            print self.NOW_VAL, " + ", self.ORIGINAL_VAL, " = ", self.NOW_VAL + self.ORIGINAL_VAL
            self.NOW_VAL += self.ORIGINAL_VAL #do the math

        self.ui.lcdNumber.display(self.NOW_VAL)
        print "equal= " , self.NOW_VAL
        self.ORIGINAL_VAL = self.NOW_VAL






def setUpWindow():
    print "setUpBtnConnect"
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())