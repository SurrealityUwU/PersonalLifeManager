import datetime
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

sys.path.append('../PersonalLifeManager')
from UserInterface.UIFile import Ui_Form

class Task:
    def __init__(self, title, tag, desc = "", startDate = QDate(), endDate = QDate(), time = QTime(), status = "Upcoming"):
        print("New Task")
        self.show = True

        self.title = title
        self.desc = desc
        self.startDate = startDate
        self.endDate = endDate
        self.time = time
        self.tag = tag
        self.status = status
        self.calc_priority()

    def calc_priority(self):
        if (self.startDate.daysTo(self.endDate) == 0):
            self.priority = 1
        else:
            self.priority = 1 - (QDate.currentDate().daysTo(self.endDate) / self.startDate.daysTo(self.endDate))

    def __str__(self):
        return f"Title: {self.title} {self.priority}"