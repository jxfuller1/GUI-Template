from PyQt5.QtCore import QThread, pyqtSignal

# qthread to do work so main UI doens't lock up, pass info via signal
class DATA(QThread):
    tabletextChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        print("do stuff here in qthread")
        self.tabletextChanged.emit("emit to update UI")

