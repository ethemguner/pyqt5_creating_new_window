from PyQt5 import QtWidgets, QtCore
import sys


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        
        self.label = QtWidgets.QLabel("Main Window")
        self.pushbutton = QtWidgets.QPushButton("Go Window 2")
        
        self.a_variable = 268
        self.variable_label = QtWidgets.QLabel("Main window variable value: " + str(self.a_variable))
        
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.variable_label)
        vbox.addWidget(self.pushbutton)
        
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.variable_label.setAlignment(QtCore.Qt.AlignCenter)
        
        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(vbox)

        self.setLayout(hbox)
        self.show()
        
        self.pushbutton.clicked.connect(self.openNewWindow)
        
    def openNewWindow(self):
        window2 = Window2()
        window2.__init__()

class Window2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        variable_from_MainWindow = window.a_variable
        self.secondpageUI(variable_from_MainWindow)
        
    def secondpageUI(self, variable_from_MainWindow):
        self.window2_label = QtWidgets.QLabel("Window 2")
        self.window2_variable = QtWidgets.QLabel()
        self.window2_variable.setText("The variable value which came from main window: " + str(variable_from_MainWindow))
        
        self.left = 200
        self.top = 120
        self.width = 500
        self.height = 500
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.window2_label)
        vbox.addWidget(self.window2_variable)
        self.window2_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.setLayout(vbox)
        self.show()
    

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.move(200, 120)
window.setFixedSize(500, 500)
sys.exit(app.exec_())
