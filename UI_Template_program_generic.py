from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QWidget, QStackedLayout


class Program_generic_layout(QStackedLayout):
    # any signals between program and UI go here

    # signal for onsizeChanged function for UI_Template (must be here, unless this function is removed from Main UI File)
    sizeChanged = pyqtSignal(int, int)

    # add any other signals between program and UI go here

    def __init__(self, parent):
        super(Program_generic_layout, self).__init__(parent)
        self.program_generic_mainwork_UI()

    def program_generic_mainwork_UI(self):
        self.page1()
        self.page2()
        self.page3()
        self.program_generic_setuppage()

    def page1(self):
        # add widget(Page) to Qstackedlayout
        # self.addWidget()
        pass

    def page2(self):
        # add widget(Page) to Qstackedlayout
        # self.addWidget()
        pass

    def page3(self):
        # add widget(Page) to Qstackedlayout
        # self.addWidget()
        pass

    # for setup page of program, adding as i want every program to have a setup page
    def program_generic_setuppage(self):
        # things to do here
        """
        ---- Set default settings in variables
        ---- create layout for the page that includes save/default buttons for user to change settings
        ---- look for user defined txt settings file if found, default file if not, read it and change the default variables
        ---- change states of the widgets in settings based on the txt
        ---- above can be done in different function call outs
        """

        # add widget(Page) to Qstackedlayout
        # self.addWidget()
        pass

    # emit for pyqtsignal to main UI
    def start_program_generic(self):
        # changes window size when program clicked on if used
    #    self.sizeChanged.emit(int, int)
        pass