from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QWidget, QStackedLayout, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, \
    QListView, QScrollArea


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
        # every page needs to have a scroll area, set resizable, with a qwidget
        # Qwidget should be the upper level , set QScrollarea to that widget, then add scrollarea to self
        # if you don't set resizable, UI won't stretch when making window bigger
         self.page1_scroll = QScrollArea()
         self.page1_scroll.setWidgetResizable(True)
         self.page1_widget = QWidget()
         self.page1_scroll.setWidget(self.page1_widget)


        # enter other UI elements here
        
        
        # uncomment and enter layout
         #self.page1_widget.setLayout(***)
        
        # add scrollarea to Qstackedlayout
         self.addWidget(self.page1_scroll)


    def page2(self):
        # every page needs to have a scroll area, set resizable, with a qwidget
        # Qwidget should be the upper level , set QScrollarea to that widget, then add scrollarea to self
        # if you don't set resizable, UI won't stretch when making window bigger
        self.page2_scroll = QScrollArea()
        self.page2_scroll.setWidgetResizable(True)
        self.page2_widget = QWidget()
        self.page2_scroll.setWidget(self.page2_widget)


        # enter other UI elements here



        # uncomment and enter layout
        # self.page2_widget.setLayout(***)
        
        # add scrollarea to Qstackedlayout
        self.addWidget(self.page2_scroll)

    def page3(self):
        # every page needs to have a scroll area, set resizable, with a qwidget
        # Qwidget should be the upper level , set QScrollarea to that widget, then add scrollarea to self
        # if you don't set resizable, UI won't stretch when making window bigger
        self.page3_scroll = QScrollArea()
        self.page3_scroll.setWidgetResizable(True)
        self.page3_widget = QWidget()
        self.page3_scroll.setWidget(self.page3_widget)


        # enter other UI elements here



        # uncomment and enter layout
        # self.page3_widget.setLayout(***)
        
        # add scrollarea to Qstackedlayout
        self.addWidget(self.page3_scroll)

    # for setup page of program, adding as i want every program to have a setup page
    def program_generic_setuppage(self):
        # every page needs to have a scroll area, set resizable, with a qwidget
        # Qwidget should be the upper level , set QScrollarea to that widget, then add scrollarea to self
        # if you don't set resizable, UI won't stretch when making window bigger
        self.setup_scroll = QScrollArea()
        self.setup_scroll.setWidgetResizable(True)
        self.setup_widget = QWidget()
        self.setup_scroll.setWidget(self.setup_widget)


        # enter other UI elements here

        # things to do here
        """
        ---- Set default settings in variables
        ---- create layout for the page that includes save/default buttons for user to change settings
        ---- look for user defined txt settings file if found, default file if not, read it and change the default variables
        ---- change states of the widgets in settings based on the txt
        ---- above can be done in different function call outs
        """
        
        
        
        
        # uncomment and enter layout
        # self.setup_widget.setLayout(***)

        # add scrollarea to Qstackedlayout
        self.addWidget(self.setup_scroll)

    # emit for pyqtsignal to main UI
    def start_program_generic(self):
        # changes window size when program clicked on if used
    #    self.sizeChanged.emit(int, int)
        pass


if __name__ == "__main__":
    pass
