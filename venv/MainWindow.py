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
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPlainTextEdit
from datetime import datetime
from threading import Thread
from time import sleep
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import Worker

class MainWindow():

    def publicPrintMsg(self, msg):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        self.cursor.movePosition(QTextCursor.End)
        self.cursor.insertText(current_time + ": " + msg + "\n")
        self.textbox.verticalScrollBar().setValue(self.textbox.verticalScrollBar().maximum())
        return

    def publicButton1Function(self, window):
        self.publicPrintMsg("Wciśnięto przycisk numer 1")
        window.setStyleSheet("background-color:rgb(224,224,224);")

    def publicButton2Function(self, window):
        self.publicPrintMsg("Wciśnięto przycisk numer 2")
        window.setStyleSheet("background-color:rgb(255,255, 204);")

    def publicHandleShowAuthorsButton(self):
        self.publicPrintMsg("Wyświetlono okno z informacjami o autorach")
        dlg = QDialog()

        text = QLabel("Autorzy: \n Piotr Łasek 235690 \n Dawid Siuda 235069", parent=dlg)
        text.move(50, 15)

        okButton = QPushButton("ok", dlg)
        okButton.clicked.connect(lambda: dlg.done(0))
        okButton.move(60, 70)

        dlg.setWindowTitle("Autorzy")
        dlg.setWindowModality(Qt.ApplicationModal)
        dlg.exec_()

    def publicHandleShowWindowHowToUse(self):
        self.publicPrintMsg("Wyświetlono okno z instrukcją obsługi")
        dlg = QDialog()

        text = QLabel("Instrukcja: TODO ", parent=dlg)
        text.move(50, 15)

        okButton = QPushButton("Ok", dlg)
        okButton.clicked.connect(lambda: dlg.done(0))
        okButton.move(60, 70)

        dlg.setWindowTitle("Instrukcje")
        dlg.setWindowModality(Qt.ApplicationModal)
        dlg.exec_()

    # Function to open top menu options
    def publicOpen_Menu_File(self):
        self.publicPrintMsg("Otworzono Menu --> Pliki")
        point = self.window.mapToGlobal(QPoint(0, 20))
        self.menuFile.exec(point)

    def publicOpen_Menu_Colors(self):
        self.publicPrintMsg("Otworzono Menu --> Kolory")
        point = self.window.mapToGlobal(QPoint(40, 20))
        self.menuColors.exec(point)

    def publicOpen_Menu_Advanced(self):
        self.publicPrintMsg("Otworzono Menu --> Zaawansowane")
        point = self.window.mapToGlobal(QPoint(90, 20))
        self.menuAdvanced.exec(point)

    def publicOpen_Menu_Advanced_ViewOption(self):
        self.publicPrintMsg("Otworzono Menu --> Zaawansowane --> Opcje widoku")
        point = self.window.mapToGlobal(QPoint(230, 20))
        self.submenuViewOption.exec(point)

    def publicOpen_Menu_Advanced_ViewOption_MoveWindowLeft(self):
        self.publicPrintMsg("Otworzono Menu --> Zaawansowane --> Opcje widoku --> Przesun okno w lewo")

    def publicOpen_Menu_Advanced_ViewOption_MoveWindowRight(self):
        self.publicPrintMsg("Otworzono Menu --> Zaawansowane --> Opcje widoku --> Przesun okno w prawo")

    def publicOpen_Menu_Advanced_ViewOption_MoreOptions(self):
        self.publicPrintMsg("Otworzono Menu --> Zaawansowane --> Opcje widoku --> Więcej opcji")
        point = self.window.mapToGlobal(QPoint(510, 60))
        self.submenuViewOption_moreOptions.exec(point)

    def publicOpen_Menu_Advanced_ViewOption_MoreOptions_MaximizeWinow(self):
        self.publicPrintMsg("Otworzono Menu --> Zaawansowane --> Opcje widoku --> Więcej opcji --> Maksymalizuj okno")

    def publicOpen_Menu_Help(self):
        self.publicPrintMsg("Otworzono Menu --> Pomoc")
        point = self.window.mapToGlobal(QPoint(180, 20))
        self.menuHelp.exec(point)

    def publicCloseAllMenus(self):
        self.publicPrintMsg("Zamkniento wszystkie menu DAWID")
        self.submenuViewOption.hide()
        self.menuHelp.hide()
        self.submenuViewOption_moreOptions.hide()
        self.submenuViewOption.hide()
        self.menuAdvanced.hide()
        self.menuColors.hide()
        self.menuFile.hide()

    def runAction(self, functionName):
        if functionName == "publicButton1Function":
            self.publicButton1Function(self.window)
        elif functionName == "publicButton2Function":
            self.publicButton2Function(self.window)
        elif functionName == "publicHandleShowAuthorsButton":
            self.publicHandleShowAuthorsButton()
        elif functionName == "publicHandleShowWindowHowToUse":
            self.publicHandleShowWindowHowToUse()
        elif functionName == "publicOpen_Menu_File":
            self.publicOpen_Menu_File()
        elif functionName == "publicOpen_Menu_Colors":
            self.publicOpen_Menu_Colors()
        elif functionName == "publicOpen_Menu_Advanced":
            self.publicOpen_Menu_Advanced()
        elif functionName == "publicOpen_Menu_Advanced_ViewOption":
            self.publicOpen_Menu_Advanced_ViewOption()
        elif functionName == "publicOpen_Menu_Advanced_ViewOption_MoveWindowLeft":
            self.publicOpen_Menu_Advanced_ViewOption_MoveWindowLeft()
        elif functionName == "publicOpen_Menu_Advanced_ViewOption_MoveWindowLeft":
            self.publicOpen_Menu_Advanced_ViewOption_MoveWindowLeft()
        elif functionName == "publicOpen_Menu_Advanced_ViewOption_MoveWindowRight":
            self.publicOpen_Menu_Advanced_ViewOption_MoveWindowRight()
        elif functionName == "publicOpen_Menu_Advanced_ViewOption_MoreOptions":
            self.publicOpen_Menu_Advanced_ViewOption_MoreOptions()
        elif functionName == "publicOpen_Menu_Advanced_ViewOption_MoreOptions_MaximizeWinow":
            self.publicOpen_Menu_Advanced_ViewOption_MoreOptions_MaximizeWinow()
        elif functionName == "publicOpen_Menu_Help":
            self.publicOpen_Menu_Help()
        elif functionName == "publicCloseAllMenus":
            self.publicCloseAllMenus()

        else:
            print("FALSE")

        # publicPrintMsg // TO DO!!!


    def run(self):
        # Create an instance of QApplication
        app = QApplication(sys.argv)

        # Create an instance of your application's GUI
        self.window = QWidget()
        self.window.setWindowTitle('Aplikacja PyQt5')
        self.window.setGeometry(100, 100, 700, 500)  # (x, y, width, height)

        # Create textbox
        self.textbox = QPlainTextEdit(self.window)
        self.textbox.setReadOnly(True)
        self.textbox.move(100, 340)
        self.textbox.resize(500, 120)
        self.textbox.setStyleSheet("background-color: white;")
        self.msgText = ""
        self.cursor = self.textbox.textCursor()

        # Create button1
        self.button1 = QPushButton("Przycisk 1 kolor szary", parent=self.window)
        self.button1.clicked.connect(lambda: self.publicButton1Function(self.window))
        self.button1.setGeometry(80, 150, 200, 100)
        self.button1.setFont(QFont('Arial', 15))
        self.button1.setStyleSheet("background-color: white;"
                                   "border : 1px solid black;"
                                   "border-radius : 20px;")
        self.button1.show()

        # Create button2
        self.button2 = QPushButton("Przycisk 1 kolor zółty", parent=self.window)
        self.button2.clicked.connect(lambda: self.publicButton2Function(self.window))
        self.button2.setGeometry(420, 150, 200, 100)
        self.button2.setFont(QFont('Arial', 15))
        self.button2.setStyleSheet("background-color: white;"
                                   "border : 1px solid black;"
                                   "border-radius : 20px;")
        self.button2.show()

        # Create menu bar
        self.menuBar = QMenuBar(parent=self.window)

        # Create menu "File"
        self.menuFile= QMenu("&Pliki", parent=self.window)
        exitAction = self.menuFile.addAction("Wyjście", lambda: quit())
        self.menuBar.addMenu(self.menuFile)

        # Create menu "Colors"
        self.menuColors = QMenu("&Kolory", parent=self.window)
        setGreyAction = self.menuColors.addAction("Ustaw szary kolor tła", lambda: self.publicButton1Function(self.window))
        setYellowAction = self.menuColors.addAction("Ustaw żółty kolor tła", lambda: self.publicButton2Function(self.window))
        self.menuBar.addMenu(self.menuColors)

        # Create menu "Advanced"
        self.menuAdvanced = QMenu('Zaawansowane')
        self.menuAdvanced.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submenuViewOption = QMenu('Opcje widoku')
        self.submenuViewOption.addAction('Przesuń okno w lewo(not implementet yet)', lambda: self.publicOpen_Menu_Advanced_ViewOption_MoveWindowLeft())
        self.submenuViewOption.addAction('Przesuń okno w prawo(not implementet yet)', lambda: self.publicOpen_Menu_Advanced_ViewOption_MoveWindowRight())
        self.submenuViewOption_moreOptions = QMenu('Więcej opcji')
        self.submenuViewOption_moreOptions.addAction('Maksymalizuj okno(not implementet yet)', lambda: self.publicOpen_Menu_Advanced_ViewOption_MoreOptions_MaximizeWinow())
        self.submenuViewOption.addMenu(self.submenuViewOption_moreOptions)
        self.menuAdvanced.addMenu(self.submenuViewOption)
        self.advanceMenu = self.menuBar.addMenu(self.menuAdvanced)

        # Create menu "Help"
        self.menuHelp = self.menuBar.addMenu("&Pomoc")
        showWindowHowToUseAction = self.menuHelp.addAction("Instrukcja obsługi", lambda: self.publicHandleShowWindowHowToUse())
        showAuthorsInfoAction = self.menuHelp.addAction("Autorzy", lambda: self.publicHandleShowAuthorsButton())


        # 4. Show your application's GUI
        self.window.show()

        # 5 Create thread Worker to run voice recognition
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker.Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.runAction)
        self.worker.log.connect(self.publicPrintMsg)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        # self.longRunningBtn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.longRunningBtn.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )

        # 6. Run your application's event loop (or main loop)
        sys.exit(app.exec_())

        return



