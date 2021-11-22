"""Simple Hello World example with PyQt5."""

import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtGui import *
from PyQt5 import QtCore

# window = QWidget()

def button1Function(window):
    print("button1 has been clicked")
    window.setStyleSheet("background-color:rgb(224,224,224);")

def button2Function(window):
    print("button2 has been clicked")
    window.setStyleSheet("background-color:rgb(255,255, 204);")

def printMsg(windowParent, msg, x = 80, y = 350):
    helloMsg = QLabel('<h1>' + msg + '</h1>', parent=windowParent)
    helloMsg.move(x, y)
    return

def constructWindow():
    # 2. Create an instance of QApplication
    app = QApplication(sys.argv)

    # 3. Create an instance of your application's GUI
    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(100, 100, 700, 500)  # (x, y, width, height)

    #  Print message
    printMsg(window, "Message")

    # Create button1
    button1 = QPushButton("Button 1 color: gray", parent=window)
    button1.clicked.connect(lambda: button1Function(window))
    button1.setGeometry(80, 150, 200, 100)
    button1.setFont(QFont('Arial', 15))
    button1.show()

    # Create button2
    button2 = QPushButton("Button 1 color: yellow", parent=window)
    button2.clicked.connect(lambda: button2Function(window))
    button2.setGeometry(420, 150, 200, 100)
    button2.setFont(QFont('Arial', 15))
    button2.show()

    # Create menu bar
    menuBar = QMenuBar(parent=window)

    # Create menu "File"
    fileMenu = QMenu("&File", parent=window)
    exitAction = fileMenu.addAction("Exit", lambda: quit())
    menuBar.addMenu(fileMenu)

    # Create menu "Colors"
    colorsMenu = QMenu("&Colros", parent=window)
    setGreyAction = colorsMenu.addAction("Set background grey", lambda: button1Function(window))
    setYellowAction = colorsMenu.addAction("Set background yellow", lambda: button2Function(window))
    menuBar.addMenu(colorsMenu)

    # Create menu "Advanced"
    menu = QMenu('Advanced')
    menu.setLayoutDirection(QtCore.Qt.LeftToRight)
    submenu = QMenu('Level 1')
    submenu.addAction('Level 2 - 1')
    submenu.addAction('Level 2 - 2')
    subsubmenu = QMenu('Level 1')
    subsubmenu.addAction('Level 3 - 1')
    submenu.addMenu(subsubmenu)
    menu.addMenu(submenu)
    advanceMenu = menuBar.addMenu(menu)

    # Create menu "Help"
    helpMenu = menuBar.addMenu("&Help")
    showWindowHowToUseAction = helpMenu.addAction("How to use")
    showAuthorsInfoAction = helpMenu.addAction("Authors")

    # 4. Show your application's GUI
    window.show()

    # Open file menu
    fileMenu.exec()

    # 5. Run your application's event loop (or main loop)
    sys.exit(app.exec_())

    return

def main():
    constructWindow()

if __name__ == "__main__":
    main()


