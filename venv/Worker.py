from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep

# METHODS YOU CAN CALL in "self.progress.emit":
# publicButton1Function
# publicButton2Function
# publicHandleShowAuthorsButton
# publicHandleShowWindowHowToUse
# publicOpen_Menu_File
# publicOpen_Menu_Colors
# publicOpen_Menu_Advanced
# publicOpen_Menu_Advanced_ViewOption
# publicOpen_Menu_Advanced_ViewOption_MoveWindowLeft
# publicOpen_Menu_Advanced_ViewOption_MoveWindowRight
# publicOpen_Menu_Advanced_ViewOption_MoreOptions
# publicOpen_Menu_Advanced_ViewOption_MoreOptions_MaximizeWinow
# publicOpen_Menu_Help

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)
    log = pyqtSignal(str)

    def run(self):

        # example
        while True:
            sleep(5)
            self.progress.emit("publicOpen_Menu_Advanced_ViewOption")
            self.log.emit("printt log: publicOpen_Menu_Advanced_ViewOption")
        self.finished.emit()