import sys
from CalculatorWindow import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QWidget):


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setUpBtnconnect()

    def setUpBtnconnect(self):
        # self.ui.btn_0.clicked.connect(self.wrapper)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_0.clicked.connect(lambda:self.add(0))
        self.ui.btn_1.clicked.connect(lambda:self.add(1))
        self.ui.btn_2.clicked.connect(lambda:self.add(2))
        self.ui.btn_3.clicked.connect(lambda:self.add(3))
        self.ui.btn_4.clicked.connect(lambda:self.add(4))
        self.ui.btn_5.clicked.connect(lambda:self.add(5))
        self.ui.btn_6.clicked.connect(lambda:self.add(6))
        self.ui.btn_7.clicked.connect(lambda:self.add(7))
        self.ui.btn_8.clicked.connect(lambda:self.add(8))
        self.ui.btn_9.clicked.connect(lambda:self.add(9))
        self.ui.btn_add.clicked.connect(self.setAdd)
        self.ui.btn_eql.clicked.connect(self.equal)

    def setNowAction(self, _action):
        global NOW_ACTION
        NOW_ACTION = _action

    def clear(self):
        global ORIGINAL_VAL
        global NOW_VAL
        NOW_VAL = 0
        ORIGINAL_VAL = 0
        self.ui.lcdNumber.display(NOW_VAL)
        print "clear 0"

    def setNowValZero(self):
        global NOW_VAL
        NOW_VAL = 0

    def setOriginalValZero(self):
        global ORIGINAL_VAL
        ORIGINAL_VAL = 0

    def add(self, num):
        global NOW_VAL
        global ORIGINAL_VAL
        global NOW_ACTION

        if NOW_ACTION == "equal":
            self.setNowValZero() #should clear now val for new add after equal
            self.setNowAction("none")

        NOW_VAL = (NOW_VAL * 10) + num
        print NOW_VAL
        self.ui.lcdNumber.display(NOW_VAL)

    def setAdd(self):
        global NOW_VAL
        global ORIGINAL_VAL

        self.ui.label_equation.setText(str(NOW_VAL) + " +") #should have now_val for keep add
        ORIGINAL_VAL = NOW_VAL
        NOW_VAL = 0


    def equal(self):
        global ORIGINAL_VAL
        global NOW_VAL

        self.setNowAction("equal")
        self.ui.label_equation.setText("") #clear equation label
        print NOW_VAL, " + ", ORIGINAL_VAL, " = ", NOW_VAL+ORIGINAL_VAL
        NOW_VAL += ORIGINAL_VAL #do the math
        self.ui.lcdNumber.display(NOW_VAL)

        print "equal= " , NOW_VAL
        ORIGINAL_VAL = NOW_VAL



ORIGINAL_VAL = 0
NOW_VAL = 0
NOW_ACTION = "none"



def setUpWindow():
    print "setUpBtnConnect"
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())