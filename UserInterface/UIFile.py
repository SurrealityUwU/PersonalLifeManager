# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIFileCuvpaw.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(466, 552)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(70, 20, 331, 451))
        self.stackedWidget.setStyleSheet(u"background-color: #C8B1A5")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 331, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #C8B1A5")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.add_button = QPushButton(self.frame_2)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(150, 410, 35, 35))
        font = QFont()
        font.setPointSize(26)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet(u"background-color: cyan; color: white")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 111, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color:white")
        self.sort_button = QPushButton(self.frame_2)
        self.sort_button.setObjectName(u"sort_button")
        self.sort_button.setGeometry(QRect(280, 30, 21, 21))
        self.sort_button.setStyleSheet(u"background-color:white")
        self.sort_button_2 = QPushButton(self.frame_2)
        self.sort_button_2.setObjectName(u"sort_button_2")
        self.sort_button_2.setGeometry(QRect(250, 30, 21, 21))
        self.sort_button_2.setStyleSheet(u"background-color:white")
        self.searchBar = QLineEdit(self.frame_2)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(130, 30, 113, 22))
        self.searchBar.setStyleSheet(u"background-color: white")
        self.scrollArea_2 = QScrollArea(self.frame_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(30, 60, 271, 351))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setFrameShadow(QFrame.Sunken)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 269, 349))
        self.tasksLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.tasksLayout.setObjectName(u"tasksLayout")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 331, 451))
        self.frame_3.setStyleSheet(u"background-color: #C8B1A5")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 20, 331, 31))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: white")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.titleLineEdit = QLineEdit(self.frame_3)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(20, 60, 141, 22))
        font3 = QFont()
        font3.setPointSize(11)
        self.titleLineEdit.setFont(font3)
        self.titleLineEdit.setStyleSheet(u"color: white")
        self.descText = QPlainTextEdit(self.frame_3)
        self.descText.setObjectName(u"descText")
        self.descText.setGeometry(QRect(20, 90, 291, 81))
        self.descText.setStyleSheet(u"color: white;")
        self.descText.setOverwriteMode(False)
        self.descText.setBackgroundVisible(False)
        self.dateEdit_end = QDateEdit(self.frame_3)
        self.dateEdit_end.setObjectName(u"dateEdit_end")
        self.dateEdit_end.setGeometry(QRect(90, 210, 110, 22))
        self.dateEdit_end.setStyleSheet(u"color: white")
        self.timeEdit = QTimeEdit(self.frame_3)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(90, 240, 118, 22))
        self.timeEdit.setStyleSheet(u"color: white")
        self.timeEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(23, 59, 0)))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 210, 61, 16))
        self.label_3.setStyleSheet(u"color: white")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 240, 61, 16))
        self.label_4.setStyleSheet(u"color: white")
        self.priority_label = QLabel(self.frame_3)
        self.priority_label.setObjectName(u"priority_label")
        self.priority_label.setGeometry(QRect(20, 300, 49, 16))
        self.priority_label.setStyleSheet(u"color: white")
        self.doneButton = QPushButton(self.frame_3)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setGeometry(QRect(250, 410, 75, 24))
        self.doneButton.setStyleSheet(u"background-color: white")
        self.remove_button = QPushButton(self.frame_3)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setEnabled(True)
        self.remove_button.setGeometry(QRect(160, 410, 75, 24))
        self.remove_button.setStyleSheet(u"background-color: white")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 180, 61, 16))
        self.label_7.setStyleSheet(u"color: white")
        self.dateEdit_start = QDateEdit(self.frame_3)
        self.dateEdit_start.setObjectName(u"dateEdit_start")
        self.dateEdit_start.setGeometry(QRect(90, 180, 110, 22))
        self.dateEdit_start.setStyleSheet(u"color: white")
        self.dateEdit_start.setDateTime(QDateTime(QDate(2022, 5, 27), QTime(0, 0, 0)))
        self.duration_label = QLabel(self.frame_3)
        self.duration_label.setObjectName(u"duration_label")
        self.duration_label.setGeometry(QRect(20, 270, 49, 16))
        self.duration_label.setStyleSheet(u"color: white")
        self.duration_value = QLabel(self.frame_3)
        self.duration_value.setObjectName(u"duration_value")
        self.duration_value.setGeometry(QRect(90, 270, 49, 16))
        self.duration_value.setStyleSheet(u"color: white")
        self.priority_value = QLabel(self.frame_3)
        self.priority_value.setObjectName(u"priority_value")
        self.priority_value.setGeometry(QRect(90, 300, 49, 16))
        self.priority_value.setStyleSheet(u"color: white")
        self.tagLineEdit = QLineEdit(self.frame_3)
        self.tagLineEdit.setObjectName(u"tagLineEdit")
        self.tagLineEdit.setGeometry(QRect(170, 60, 141, 22))
        self.tagLineEdit.setFont(font3)
        self.tagLineEdit.setStyleSheet(u"color: white")
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 180, 91, 22))
        self.comboBox.setStyleSheet(u"color: white")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 60, 311, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 309, 369))
        self.scheduleLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scheduleLayout.setObjectName(u"scheduleLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.todayButton = QPushButton(self.page_3)
        self.todayButton.setObjectName(u"todayButton")
        self.todayButton.setGeometry(QRect(100, 30, 75, 24))
        self.weekButton = QPushButton(self.page_3)
        self.weekButton.setObjectName(u"weekButton")
        self.weekButton.setGeometry(QRect(180, 30, 75, 24))
        self.monthButton = QPushButton(self.page_3)
        self.monthButton.setObjectName(u"monthButton")
        self.monthButton.setGeometry(QRect(260, 30, 75, 24))
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 91, 31))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: white")
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.frame_4 = QFrame(self.page_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(40, 90, 251, 281))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.scrollArea_3 = QScrollArea(self.frame_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 251, 281))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 249, 279))
        self.historyLayout = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.historyLayout.setObjectName(u"historyLayout")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 50, 331, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: white")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_4)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 480, 331, 51))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: Grey")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 331, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.todolist_button = QPushButton(self.horizontalLayoutWidget)
        self.todolist_button.setObjectName(u"todolist_button")
        self.todolist_button.setStyleSheet(u"background-color: white")

        self.horizontalLayout.addWidget(self.todolist_button)

        self.scheduleButton = QPushButton(self.horizontalLayoutWidget)
        self.scheduleButton.setObjectName(u"scheduleButton")
        self.scheduleButton.setStyleSheet(u"background-color: white")

        self.horizontalLayout.addWidget(self.scheduleButton)

        self.history_button = QPushButton(self.horizontalLayoutWidget)
        self.history_button.setObjectName(u"history_button")
        self.history_button.setStyleSheet(u"background-color: white")

        self.horizontalLayout.addWidget(self.history_button)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"To-Do List", None))
        self.sort_button.setText("")
        self.sort_button_2.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Add Task", None))
        self.titleLineEdit.setInputMask("")
        self.titleLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Title", None))
        self.descText.setPlainText("")
        self.descText.setPlaceholderText(QCoreApplication.translate("Form", u"Description", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Due Date:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Due Time:", None))
        self.priority_label.setText(QCoreApplication.translate("Form", u"Priority:", None))
        self.doneButton.setText(QCoreApplication.translate("Form", u"Done", None))
        self.remove_button.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Start Date:", None))
        self.duration_label.setText(QCoreApplication.translate("Form", u"Duration:", None))
        self.duration_value.setText(QCoreApplication.translate("Form", u"0", None))
        self.priority_value.setText(QCoreApplication.translate("Form", u"0", None))
        self.tagLineEdit.setInputMask("")
        self.tagLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Tag", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Upcoming", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"On-Going", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Finished", None))

        self.todayButton.setText(QCoreApplication.translate("Form", u"Today", None))
        self.weekButton.setText(QCoreApplication.translate("Form", u"Week", None))
        self.monthButton.setText(QCoreApplication.translate("Form", u"Month", None))
        self.label.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"History list", None))
        self.todolist_button.setText(QCoreApplication.translate("Form", u"ToDoList", None))
        self.scheduleButton.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.history_button.setText(QCoreApplication.translate("Form", u"History", None))
    # retranslateUi

