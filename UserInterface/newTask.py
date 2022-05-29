# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newTaskaScmSb.ui'
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
        Form.resize(379, 252)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 60, 341, 111))
        self.frame_3.setStyleSheet(u"background-color: grey")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 341, 136))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white; margin-left: 5px; padding-left: 5px; padding-top: 5px")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setMargin(0)
        self.label.setIndent(0)

        self.verticalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: white; margin-left: 5px; margin-right: 5px;")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(1157, 16777215))
        self.textEdit.setStyleSheet(u"color: white; margin-left: 5px; margin-right: 5px;")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Add Task", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Task Name", None))
#if QT_CONFIG(accessibility)
        self.textEdit.setAccessibleName(QCoreApplication.translate("Form", u"d", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.textEdit.setAccessibleDescription(QCoreApplication.translate("Form", u"d", None))
#endif // QT_CONFIG(accessibility)
    # retranslateUi

