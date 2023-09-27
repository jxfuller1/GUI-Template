from PyQt5.QtCore import Qt, QPropertyAnimation, QSize, pyqtSignal
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton, \
    QTextEdit, QComboBox, QCheckBox, QStackedLayout
import getpass
import os

import UI_Template_Program1_dostuff

# get computer user name
user = getpass.getuser()
# get current working directory (needed if using on different computers
my_path = os.path.abspath(os.path.dirname(__file__))


class Program1_Layout(QStackedLayout):
    sizeChanged = pyqtSignal(int, int)

    def __init__(self, parent):
        super(Program1_Layout, self).__init__(parent)
        self.program1_mainwork_UI()


    def program1_mainwork_UI(self):
        # each item added to the stacked widget is separated by "=======" for easier reading
        # can separate out these into separate functions if needed to add a lot of layouts/widgets to each page
        # NOTE: these must end inside Widgets because you can only pass Widgets into QStackedLayout

        # ================================================================================================
        # ================================================================================================

        # UI tab widget mainwork page

        # create scroll area so that window can be made smaller regardless of widgets added to UI
        self.tab_scroll = QScrollArea()

        # upper level widget to be added to scrollarea
        self.tab_widget = QWidget()

        # set resizable to true (otherwise widget will just take up small area instead of full layout) and
        # set the widget of the scroll area
        self.tab_scroll.setWidgetResizable(True)
        self.tab_scroll.setWidget(self.tab_widget)

        # layout for this mainwork page, setting margins so theres no space around edges
        self.layout_tabs = QVBoxLayout()
        self.layout_tabs.setContentsMargins(0, 0, 0, 0)

        # Initialize tabs
        self.tabs_total = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # change background color of tab
        self.tab2.setAutoFillBackground(True)
        p = self.tab2.palette()
        p.setColor(self.tab2.backgroundRole(), Qt.gray)
        self.tab2.setPalette(p)

        # change background color of tab
        self.tab1.setAutoFillBackground(True)
        self.tab1.setPalette(p)

        # add UI elements to tab1
        self.program1_mainwork_UI_mainpage_tab1()

        # Add tabs
        self.tabs_total.addTab(self.tab1, "Tab1")
        self.tabs_total.addTab(self.tab2, "Tab2")

        # Add tabs to widget
        self.layout_tabs.addWidget(self.tabs_total)
        self.tab_widget.setLayout(self.layout_tabs)

        # add widget to the stacked layout for the main part of the UI, tied to the "main" button when it's clicked on
        # left side button of UI
        self.addWidget(self.tab_scroll)


        # ================================================================================================
        # ================================================================================================
        # UI setup mainwork page

        # create scroll area so that window can be made smaller regardless of widgets added to UI
        self.setup_scroll = QScrollArea()

        # upper level widget to be added to scrollarea
        self.setup_widget = QWidget()

        # set resizable to true (otherwise widget will just take up small area instead of full layout) and
        # set the widget of the scroll area
        self.setup_scroll.setWidgetResizable(True)
        self.setup_scroll.setWidget(self.setup_widget)

        # setup placeholder color background to see different in mainwork page clicked on when leftside buttons clicked in UI
        self.setup_widget.setAutoFillBackground(True)
        p = self.setup_widget.palette()
        p.setColor(self.setup_widget.backgroundRole(), Qt.gray)
        self.setup_widget.setPalette(p)

        # setup stuff to put into main setuppage for program1
        self.program1_mainwork_UI_setuppage()

        self.addWidget(self.setup_scroll)
        # ================================================================================================
        # ================================================================================================

        # UI misc mainwork page

        # create scroll area so that window can be made smaller regardless of widgets added to UI
        self.misc_scroll = QScrollArea()

        # upper level widget to be added to scrollarea
        self.misc_widget = QWidget()

        # set resizable to true (otherwise widget will just take up small area instead of full layout) and
        # set the widget of the scroll area
        self.misc_scroll.setWidgetResizable(True)
        self.misc_scroll.setWidget(self.misc_widget)

        # upper level layout to be added to upper level widget
        self.misc_layout = QVBoxLayout()

        myfont = QFont()
        myfont.setPointSize(14)
        self.misc_label = QLabel("<b>This is where miscellaneous stuff for program will go</b>")
        self.misc_label.setFont(myfont)
        self.misc_label.setAlignment(Qt.AlignCenter)

        self.misc_layout.addWidget(self.misc_label)
        self.misc_widget.setLayout(self.misc_layout)

        # setup placeholder color background to see different in mainwork page clicked on when leftside buttons clicked in UI
        self.misc_widget.setAutoFillBackground(True)
        p = self.misc_widget.palette()
        p.setColor(self.misc_widget.backgroundRole(), Qt.blue)
        self.misc_widget.setPalette(p)

        self.addWidget(self.misc_scroll)
        # ================================================================================================
        # ================================================================================================

        # UI about mainwork page

        # create scroll area so that window can be made smaller regardless of widgets added to UI
        self.about_scroll = QScrollArea()

        # upper level widget to be added to scrollarea
        self.about_widget = QWidget()

        # set resizable to true (otherwise widget will just take up small area instead of full layout) and
        # set the widget of the scroll area
        self.about_scroll.setWidgetResizable(True)
        self.about_scroll.setWidget(self.about_widget)

        # upper level layout to be added to upper level widget
        self.about_layout = QVBoxLayout()

        myfont = QFont()
        myfont.setPointSize(14)
        self.about_label = QLabel("<b>This is explanation about how program works will go or whatever</b>")
        self.about_label.setFont(myfont)
        self.about_label.setAlignment(Qt.AlignCenter)

        self.about_layout.addWidget(self.about_label)
        self.about_widget.setLayout(self.about_layout)

        # setup placeholder color background to see different in mainwork page clicked on when leftside buttons clicked in UI
        self.about_widget.setAutoFillBackground(True)
        p = self.about_widget.palette()
        p.setColor(self.about_widget.backgroundRole(), Qt.magenta)
        self.about_widget.setPalette(p)

        self.addWidget(self.about_scroll)
        # ================================================================================================
        # ================================================================================================

        # UI extra mainwork page

        # create scroll area so that window can be made smaller regardless of widgets added to UI
        self.extra_scroll = QScrollArea()

        # upper level widget to be added to scrollarea
        self.extra_widget = QWidget()

        # set resizable to true (otherwise widget will just take up small area instead of full layout) and
        # set the widget of the scroll area
        self.extra_scroll.setWidgetResizable(True)
        self.extra_scroll.setWidget(self.extra_widget)

        # upper level layout to be added to upper level widget
        self.extra_layout = QVBoxLayout()

        myfont = QFont()
        myfont.setPointSize(14)
        self.extra_label = QLabel("<b>Extra window for anything not though of</b>")
        self.extra_label.setFont(myfont)
        self.extra_label.setAlignment(Qt.AlignCenter)

        self.extra_layout.addWidget(self.extra_label)
        self.extra_widget.setLayout(self.extra_layout)

        # setup placeholder color background to see different in mainwork page clicked on when leftside buttons clicked in UI
        self.extra_widget.setAutoFillBackground(True)
        p = self.extra_widget.palette()
        p.setColor(self.extra_widget.backgroundRole(), Qt.cyan)
        self.extra_widget.setPalette(p)

        self.addWidget(self.extra_scroll)


    # set layout for setuppage
    def program1_mainwork_UI_setuppage(self):
        # program1 setuppage default settings, will change depending on txt file settings further below
        # basically this just here in case default txt file is gone
        self.program1_window_width = 910
        self.program1_window_height = 715
        self.program1_fileslocto_read = "NA"
        self.program1_filetemploc = "NA"
        self.program1_combooption_set = 0
        self.program1_checkbox1_set = True
        self.program1_checkbox2_set = False
        self.program1_checkbox3_set = False

        # user settings for program1 name of txt file
        program1_user_settings = "\\program1_settings_" + user + ".txt"

        # default settings for program1 name of txt file
        program1_default_settings = "\\program1_settings.txt"

        # this would be the user settings path relative to exe location (note my path from beginning of program)
        self.program1_user_path_settings = my_path + program1_user_settings

        # default path for program1 settings default settings
        self.program1_default_path_settings = my_path + program1_default_settings

        # setup toplevel mainwork page layout
        self.toplevel_mainwork_setup_layout = QVBoxLayout()

        # setup page label name with font size
        self.options_label = QLabel("<u><b>Setup Options for program<u><b>")
        self.options_label.adjustSize()
        myfont = QFont()
        myfont.setPointSize(12)
        self.options_label.setFont(myfont)
        self.options_label.setAlignment(Qt.AlignHCenter)

        # width/height label
        self.width_height_label = QLabel("Set the Width/Height of Window When Program1 Started")
        self.width_height_label.adjustSize()
        self.width_height_label.setAlignment(Qt.AlignHCenter)

        # some option ideas widgets to be added to mainwork setup page layout
        # layout for items in horizontal layout to be added to mainwork setup page layout

        self.setuppage_layout_size = QHBoxLayout()

        # first add stretch to remove , this is called later after widgets are added.... it has to be called once
        # here and then again after widgets are added to make the horizontal widgets stay all grouped together in the
        # center as the window is stretched... i don't know the exact reason you have to call it at the outset
        # and then against afterwards.......
        self.setuppage_layout_size.addStretch()

        self.setup_mainwork_width_label = QLabel("Width:")
        self.setup_mainwork_width_label.adjustSize()

        self.setup_mainwork_width_edit = QLineEdit()
        self.setup_mainwork_width_edit.setMaximumWidth(50)
        # set edit text to default settings
        self.setup_mainwork_width_edit.setText(str(self.program1_window_width))
      #  print(self.setup_mainwork_width_edit.text())

        self.setup_mainwork_height_label = QLabel("Height:")
        self.setup_mainwork_height_label.adjustSize()

        self.setup_mainwork_height_edit = QLineEdit()
        self.setup_mainwork_height_edit.setMaximumWidth(50)
        # set edit text to default settings
        self.setup_mainwork_height_edit.setText(str(self.program1_window_height))

        # add widgets to layout
        self.setuppage_layout_size.addWidget(self.setup_mainwork_width_label)
        self.setuppage_layout_size.addWidget(self.setup_mainwork_width_edit)
        self.setuppage_layout_size.addWidget(self.setup_mainwork_height_label)
        self.setuppage_layout_size.addWidget(self.setup_mainwork_height_edit)

        # add stretch so horizontal items are all next to each other (see note for the 1st time this is called for
        # why this has to be called a second time after widgets are added).
        self.setuppage_layout_size.addStretch()

        # for choosing a file location
        self.setuppage_layout_file = QHBoxLayout()

        self.file_label = QLabel("Location of File(s) to read:")
        self.file_label.adjustSize()

        self.file_label_loc = QLineEdit()
        self.file_label_loc.setText(self.program1_fileslocto_read)

        self.setuppage_layout_file.addWidget(self.file_label)
        self.setuppage_layout_file.addWidget(self.file_label_loc)


        # for choosing a save location
        self.setuppage_layout_save = QHBoxLayout()

        self.save_label = QLabel("Save or Temp Save Location for File(s):")
        self.save_label.adjustSize()

        self.save_label_loc = QLineEdit()
        self.save_label_loc.setText(self.program1_filetemploc)

        self.setuppage_layout_save.addWidget(self.save_label)
        self.setuppage_layout_save.addWidget(self.save_label_loc)

        # layout for additional options purely so that setalignment can be done...can't do setalignment with certain
        # widgets apparentely
        self.additional_options = QVBoxLayout()

        self.combo_option_label = QLabel("Pick an option")
        self.combo_option_label.adjustSize()

        self.combo_option = QComboBox()
        self.combo_option.addItems(["One", "Two", "Three"])
        self.combo_option.setMaximumWidth(100)
        self.combo_option.setCurrentIndex(self.program1_combooption_set)

        self.checkbox1 = QCheckBox("checkbox placeholder")
        self.checkbox1.setChecked(self.program1_checkbox1_set)
        self.checkbox2 = QCheckBox("checkbox placeholder")
        self.checkbox2.setChecked(self.program1_checkbox2_set)
        self.checkbox3 = QCheckBox("checkbox placeholder")
        self.checkbox3.setChecked(self.program1_checkbox3_set)

        #=====================================================================
        # ====================================================================
        self.program1_settings_buttons_layout = QHBoxLayout()

        self.program1_save_settings_button = QPushButton("Save Settings")
        self.program1_save_settings_button.adjustSize()
        self.program1_save_settings_button.clicked.connect(self.program1_change_settings)

        self.program1_default_settings_button = QPushButton("Restore Defaults")
        self.program1_default_settings_button.adjustSize()
        self.program1_default_settings_button.clicked.connect(self.program1_change_settings)

        self.program1_settings_buttons_layout.addWidget(self.program1_save_settings_button)
        self.program1_settings_buttons_layout.addWidget(self.program1_default_settings_button)
        # ======================================================================
        # ======================================================================

        self.additional_options.addWidget(self.combo_option_label)
        self.additional_options.addWidget(self.combo_option)
        self.additional_options.addSpacing(10)
        self.additional_options.addWidget(self.checkbox1)
        self.additional_options.addSpacing(10)
        self.additional_options.addWidget(self.checkbox2)
        self.additional_options.addSpacing(10)
        self.additional_options.addWidget(self.checkbox3)
        self.additional_options.addSpacing(10)
        self.additional_options.addLayout(self.program1_settings_buttons_layout)

        self.additional_options.setAlignment(Qt.AlignHCenter)

        # add to upper level layout of the mainwork setuppage layout
        self.toplevel_mainwork_setup_layout.addWidget(self.options_label)
        self.toplevel_mainwork_setup_layout.addSpacing(50)
        self.toplevel_mainwork_setup_layout.addWidget(self.width_height_label)
        self.toplevel_mainwork_setup_layout.addLayout(self.setuppage_layout_size)
        self.toplevel_mainwork_setup_layout.addSpacing(20)
        self.toplevel_mainwork_setup_layout.addLayout(self.setuppage_layout_file)
        self.toplevel_mainwork_setup_layout.addSpacing(20)
        self.toplevel_mainwork_setup_layout.addLayout(self.setuppage_layout_save)
        self.toplevel_mainwork_setup_layout.addSpacing(20)
        self.toplevel_mainwork_setup_layout.addLayout(self.additional_options)

        # add stretch after widgets so the widgets are at the top of the mainwork page instead of bottom
        self.toplevel_mainwork_setup_layout.addStretch()

        # add to top level widget (widget then goes into the stacked layout)
        self.setup_widget.setLayout(self.toplevel_mainwork_setup_layout)

        # if path exists get settings for the interface to populate UI elements
        if os.path.exists(self.program1_user_path_settings):
            self.getprogram1_settings(self.program1_user_path_settings)
        else:
            if os.path.exists(self.program1_default_path_settings):
                self.getprogram1_settings(self.program1_default_path_settings)

    def getprogram1_settings(self, path):
        # get initial settings on UI loadup for program1 and populate those UI widgets
        program1_settings = open(path, "r")
        program1_settings_list = program1_settings.readlines()

        # pass all settings for txt file to global variables
        for i in program1_settings_list:
            if "program1_window_width" in i:
                self.program1_window_width = int(i.split("=")[1])
                # set text in settings for this item on the UI
                self.setup_mainwork_width_edit.setText(str(self.program1_window_width))

            if "program1_window_height" in i:
                self.program1_window_height = int(i.split("=")[1])
                # set text in settings for this item on the UI
                self.setup_mainwork_height_edit.setText(str(self.program1_window_height))

            if "program1_fileslocto_read" in i:
                self.program1_fileslocto_read = str(i.split("=")[1])
                # set text in settings for this item on the UI
                self.file_label_loc.setText(str(self.program1_fileslocto_read))

            if "program1_filetemploc" in i:
                self.program1_filetemploc = str(i.split("=")[1])
                # set text in settings for this item on the UI
                self.save_label_loc.setText(str(self.program1_filetemploc))

            if "program1_combooption_set" in i:
                self.program1_combooption_set = int(i.split("=")[1])
                # set combobox in settings for this item on the UI
                self.combo_option.setCurrentIndex(self.program1_combooption_set)

            if "program1_checkbox1_set" in i:
                self.program1_checkbox1_set = eval(i.split("=")[1])
                # set checkbox in settings for this item on the UI
                self.checkbox1.setChecked(self.program1_checkbox1_set)

            if "program1_checkbox2_set" in i:
                self.program1_checkbox2_set = eval(i.split("=")[1])
                # set checkbox in settings for this item on the UI
                self.checkbox2.setChecked(self.program1_checkbox2_set)

            if "program1_checkbox3_set" in i:
                self.program1_checkbox3_set = eval(i.split("=")[1])
                # set checkbox in settings for this item on the UI
                self.checkbox3.setChecked(self.program1_checkbox3_set)


    # if default or save settings hit, activate this function to change txt init files for program1
    def program1_change_settings(self):
        # get which button was hit
        sender = self.sender()

        # pass UI values to list to be saved to program1 user init txt file
        if "Save" in sender.text():
            # list of all values currently in settings to save to txt user file
            self.user_program1_settings = []
            self.user_program1_settings.append("program1_window_width=" + str(self.setup_mainwork_width_edit.text()))
            self.user_program1_settings.append("program1_window_height=" + str(self.setup_mainwork_height_edit.text()))
            self.user_program1_settings.append("program1_fileslocto_read=" + str(self.file_label_loc.text()))
            self.user_program1_settings.append("program1_filetemploc=" + str(self.save_label_loc.text()))
            self.user_program1_settings.append("program1_combooption_set=" + str(self.combo_option.currentIndex()))
            self.user_program1_settings.append("program1_checkbox1_set=" + str(self.checkbox1.isChecked()))
            self.user_program1_settings.append("program1_checkbox2_set=" + str(self.checkbox2.isChecked()))
            self.user_program1_settings.append("program1_checkbox3_set=" + str(self.checkbox3.isChecked()))

            # create new text file and write to it the settings and values
            # note: user_settings variable for name of txt file is a global variable
            output_file = open(self.program1_user_path_settings, 'w')
            for i in self.user_program1_settings:
                output_file.write(str(i) + "\n")
            output_file.close()

            # emit to mainwindow UI to activate change in size of window
            self.sizeChanged.emit(int(self.setup_mainwork_width_edit.text()),
                                  int(self.setup_mainwork_height_edit.text()))


        if "Defaults" in sender.text():
            # program1 setuppage default settings
            self.program1_window_width = 910
            self.program1_window_height = 715
            self.program1_fileslocto_read = "NA"
            self.program1_filetemploc = "NA"
            self.program1_combooption_set = 0
            self.program1_checkbox1_set = True
            self.program1_checkbox2_set = False
            self.program1_checkbox3_set = False

            # reset defaults on UI
            self.setup_mainwork_width_edit.setText(str(self.program1_window_width))
            self.setup_mainwork_height_edit.setText(str(self.program1_window_height))
            self.file_label_loc.setText(self.program1_fileslocto_read)
            self.save_label_loc.setText(self.program1_filetemploc)
            self.combo_option.setCurrentIndex(self.program1_combooption_set)
            self.checkbox1.setChecked(self.program1_checkbox1_set)
            self.checkbox2.setChecked(self.program1_checkbox2_set)
            self.checkbox3.setChecked(self.program1_checkbox3_set)

            # reset user settings text file
            self.user_program1_settings = []
            self.user_program1_settings.append("program1_window_width=" + str(self.setup_mainwork_width_edit.text()))
            self.user_program1_settings.append("program1_window_height=" + str(self.setup_mainwork_height_edit.text()))
            self.user_program1_settings.append("program1_fileslocto_read=" + str(self.file_label_loc.text()))
            self.user_program1_settings.append("program1_filetemploc=" + str(self.save_label_loc.text()))
            self.user_program1_settings.append("program1_combooption_set=" + str(self.combo_option.currentIndex()))
            self.user_program1_settings.append("program1_checkbox1_set=" + str(self.checkbox1.isChecked()))
            self.user_program1_settings.append("program1_checkbox2_set=" + str(self.checkbox2.isChecked()))
            self.user_program1_settings.append("program1_checkbox3_set=" + str(self.checkbox3.isChecked()))

            # create new text file and write to it the settings and values
            # note: user_settings variable for name of txt file is a global variable
            output_file = open(self.program1_user_path_settings, 'w')
            for i in self.user_program1_settings:
                output_file.write(str(i) + "\n")
            output_file.close()

            # emit to mainwindow UI to activate change in size of window
            self.sizeChanged.emit(int(self.setup_mainwork_width_edit.text()),
                                  int(self.setup_mainwork_height_edit.text()))


    def program1_mainwork_UI_mainpage_tab1(self):
        # setup of UI elements for mainwork page on UI for tab1

        self.tab1_top_level_layout = QVBoxLayout()

        self.tab1_secondary_level_layout = QHBoxLayout()

        self.tab1_label = QLabel("This is where your main program work goes")
        self.tab1_label.adjustSize()

        myfont = QFont()
        myfont.setPointSize(10)
        self.tab1_label.setFont(myfont)
        self.tab1_label.setAlignment(Qt.AlignHCenter)

        # wrapping button in a layout in order to do setalignment
        self.placeholder_button_layout_wrapper = QHBoxLayout()

        self.placeholder_button = QPushButton("Start")
        self.placeholder_button.adjustSize()
        self.placeholder_button.clicked.connect(self.program1_dostuff)
        self.placeholder_button.setFixedWidth(70)
        self.placeholder_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.placeholder_button_layout_wrapper.addWidget(self.placeholder_button)
        self.placeholder_button_layout_wrapper.setAlignment(Qt.AlignHCenter)

        self.placeholder_lineedit = QTextEdit()
        self.placeholder_lineedit.setText("placeholder")
        self.placeholder1_lineedit = QTextEdit()
        self.placeholder1_lineedit.setText("placeholder2")

        self.tab1_secondary_level_layout.addWidget(self.placeholder_lineedit)
        self.tab1_secondary_level_layout.addSpacing(30)
        self.tab1_secondary_level_layout.addWidget(self.placeholder1_lineedit)

        self.tab1_top_level_layout.addWidget(self.tab1_label)
        self.tab1_top_level_layout.addSpacing(10)
        self.tab1_top_level_layout.addLayout(self.placeholder_button_layout_wrapper)
        self.tab1_top_level_layout.addSpacing(20)
        self.tab1_top_level_layout.addLayout(self.tab1_secondary_level_layout)
        self.tab1_top_level_layout.setAlignment(Qt.AlignHCenter)

        self.tab1.setLayout(self.tab1_top_level_layout)

    # activates when main UI hits program1 button , to auto change the size of window
    def start_program1(self):
        self.sizeChanged.emit(int(self.setup_mainwork_width_edit.text()),
                              int(self.setup_mainwork_height_edit.text()))

    # execute Qthread for doing stuff, needed so UI doesn't lock up while stuff is being done
    def program1_dostuff(self):
        self.program1_execute = UI_Template_Program1_dostuff.DATA()
        self.program1_execute.tabletextChanged.connect(self.ontableChanged)
        self.program1_execute.start()

    # when stuff in table changes
    def ontableChanged(self, value):
        self.placeholder_lineedit.setText("update UI here")

