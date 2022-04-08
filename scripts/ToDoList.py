from asyncio import tasks
from statistics import harmonic_mean
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QApplication
import sys

from Property import *
from Task import *
import datetime

class ToDoList(QWidget):
    remove_after_days = 3
    log_remove_number_days = 30

    def __init__(self):
        QWidget.__init__(self, None)
        self.setLayout(QVBoxLayout())

        self.tasks = []
        self.properties = [Text("Title"), Text("Comment")]
        self.filters = []
        self.groups = []
        self.history_log = []
        self.highlight_of_day = Task([])
        self.optimal_day_off = datetime.datetime.today()

        self.update()

        
    def update(self):
        while self.layout():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        horizontal_layout = QHBoxLayout()
        for p in self.properties:
            label = QLabel(p.value)
            horizontal_layout.addWidget(label)
        self.layout().addLayout(horizontal_layout)

        for task in self.tasks:
            horizontal_layout = QHBoxLayout()
            for p in task.property_values:
                label = QLabel(p)
                horizontal_layout.addWidget(label)
            self.layout().addLayout(horizontal_layout)
        
        self.show()


    def add_filter(self, String, String2 ,String3, String4):
        #TODO
        pass

    def consequences_day_off(self, Date):
        #TODO
        pass

    def create_property(self, String):
        #TODO
        pass

    def add_task(self, property_values):
        t = Task(property_values)
        self.tasks.append(t)

    def delete_property(self, String):
        #TODO
        pass

    def delete_task(self, Task):
        #TODO
        pass

    def determine_due_date(self, Date):
        #TODO
        pass

    def find_free_day(self, int):
        #TODO
        pass

    def finish_task(self, Task):
        #TODO
        pass

    def move_property(self, String, int):
        #TODO
        pass

    def move_task(self, Task, int):
        #TODO
        pass

    def reset_filter(self):
        #TODO
        pass

    def sort(self, Property, Property2):
        #TODO
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tdl = ToDoList()
    tdl.add_task(["Task1", "Comment1"])
    tdl.update()
    tdl.update()
    sys.exit(app.exec())