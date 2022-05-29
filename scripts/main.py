from re import I
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from Task import Task
import ZODB, ZODB.FileStorage
import persistent
import transaction
from BTrees import OOBTree
from persistent.mapping import PersistentMapping
from peewee import SqliteDatabase, Model, TextField, IntegerField
sys.path.append('../PersonalLifeManager')
from UserInterface.UIFile import Ui_Form
from ToDoList import ToDoList, engine
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        # t = Task("Task1", "", "", "", "", "")
        # root.tasks["Task1"] = t
        # transaction.commit()

        self.storage = ZODB.FileStorage.FileStorage('data.fs')
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        del self.root["ToDoList"] # TODO remove
        del self.root["History"]

        if "ToDoList" not in self.root:
            print("Not IN")
            self.root["ToDoList"] = ToDoList() # TODO Parameters
            # self.root["ToDoList"].add_task(Task("t1", "Assignment", "awdawgawgagagdgsfs", QDate(2022, 3, 30), QDate(2022, 6, 20), QTime.currentTime()))
            # self.root["ToDoList"].add_task(Task("t2", "Project", "dawadawdawdadad", QDate(2022, 5, 25), QDate(2022, 6, 4), QTime.currentTime()))
            # self.root["ToDoList"].add_task(Task("t3", "Project", "dawadawdawdadad", QDate(2022, 5, 25), QDate(2022, 5, 30), QTime.currentTime()))
            # self.root["ToDoList"].add_task(Task("t4", "Project", "dawadawdawdadad", QDate(2022, 5, 25), QDate(2022, 7, 29), QTime.currentTime()))
            # self.show_tasks()

            self.root["History"] = ToDoList()
        else: # TODO remove
            print("In") 

        self.ui.searchBar.returnPressed.connect(lambda: self.search(self.ui.searchBar.text()))
        self.ui.sort_button.clicked.connect(self.sort)
        self.ui.sort_button_2.clicked.connect(self.sort_prio)
        self.ui.todolist_button.clicked.connect(self.todolist_page)
        self.ui.add_button.clicked.connect(self.task_page)
        self.ui.history_button.clicked.connect(self.history_page)
        self.ui.scheduleButton.clicked.connect(lambda: self.schedule_page("Today"))
        self.ui.todayButton.clicked.connect(lambda: self.schedule_page("Today"))
        self.ui.weekButton.clicked.connect(lambda: self.schedule_page("Week"))
        self.ui.monthButton.clicked.connect(lambda: self.schedule_page("Month"))

    def show_tasks(self, group = ""):
        if group == "":
            group = self.root["ToDoList"].tasks
        while self.ui.tasksLayout.count():
            child = self.ui.tasksLayout.takeAt(0)
            print("Child")
            if child.widget():
                print("Delete Later")
                child.widget().deleteLater()

        print(self.ui.tasksLayout.count())
        for task in group:
            print("OwO")
            frame = QFrame()
            layout = QGridLayout()

            title = QLabel()
            title.setText(task.title)
            layout.addWidget(title, 0, 0, 1, 2)

            status = QLabel()
            status.setText(task.status)
            layout.addWidget(status, 0, 2, 1, 1)

            desc = QLabel() 
            desc.setText(task.tag)
            layout.addWidget(desc, 1, 0, 1, 2)

            date = QLabel()
            date.setText(task.endDate.toString())
            layout.addWidget(date, 1, 2, 1, 1)

            frame.setLayout(layout)
            frame.setFixedHeight(60)

            if task.priority >= 0.66:
                frame.setStyleSheet("background-color: red")
            elif task.priority < 0.33:
                frame.setStyleSheet("background-color: green")
            else:
                frame.setStyleSheet("background-color: orange")

        
            frame.mousePressEvent = lambda event, t=task: self.edit_task_page(t)
            # frame.show()
            self.ui.tasksLayout.addWidget(frame)
        self.ui.tasksLayout.setAlignment(Qt.AlignTop)
        # self.ui.scrollArea_2.setWidget(self.ui.tasksLayout)


    def show_history(self):

        while self.ui.historyLayout.count():
            child = self.ui.historyLayout.takeAt(0)
            print("Child")
            if child.widget():
                print("Delete Later")
                child.widget().deleteLater()

        print(self.ui.historyLayout.count())
        for task in self.root["History"].tasks:
            print("OwO")
            frame = QFrame()
            layout = QGridLayout()

            title = QLabel()
            title.setText(task.title)
            layout.addWidget(title, 0, 0, 1, 2)

            status = QLabel()
            status.setText(task.status)
            layout.addWidget(status, 0, 2, 1, 1)

            desc = QLabel() 
            desc.setText(task.tag)
            layout.addWidget(desc, 1, 0, 1, 2)

            date = QLabel()
            date.setText(task.endDate.toString())
            layout.addWidget(date, 1, 2, 1, 1)

            frame.setLayout(layout)
            frame.setFixedHeight(60)

            frame.setStyleSheet("background-color: white")

        
            # frame.mousePressEvent = lambda event, t=task: self.edit_task_page(t)
            # frame.show()
            self.ui.historyLayout.addWidget(frame)
        self.ui.historyLayout.setAlignment(Qt.AlignTop)
        # self.ui.scrollArea_2.setWidget(self.ui.tasksLayout)

    def history_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.show_history()

    def sort(self):
        if not hasattr(self, "sort_title_count"):
            self.sort_title_count = 0
        if self.sort_title_count % 2 == 0: self.root["ToDoList"].sort("Title")
        elif self.sort_title_count % 2 == 1: self.root["ToDoList"].sort("Title", True)
        self.sort_title_count += 1
        self.show_tasks()

    def sort_prio(self):
        if not hasattr(self, "sort_prio_count"):
            self.sort_prio_count = 0
            print("Create")
        if self.sort_prio_count % 2 == 0: 
            self.root["ToDoList"].sort("Priority")
            print("00000")
        elif self.sort_prio_count % 2 == 1: self.root["ToDoList"].sort("Priority", True)
        self.sort_prio_count += 1
        self.show_tasks()

    def search(self, query):
        group = []
        for task in self.root["ToDoList"].tasks:
            if query in task.title or query in task.tag or query in task.status:
                group.append(task)
        self.show_tasks(group)

    def schedule_page(self, group = ""):
        if not group == "":
            self.group = group
        else:
            group = self.group

        self.ui.stackedWidget.setCurrentIndex(2)

        while self.ui.scheduleLayout.count():
            child = self.ui.scheduleLayout.takeAt(0)
            print("Child")
            if child.widget():
                print("Delete Later")
                child.widget().deleteLater()

        print(self.ui.scheduleLayout.count())
        for task in self.root["ToDoList"].tasks:
            if group == "Today":
                if QDate.currentDate().daysTo(task.endDate) > 1: continue
            elif group == "Week":
                if QDate.currentDate().daysTo(task.endDate) > 7: continue
            elif group == "Month":
                if QDate.currentDate().daysTo(task.endDate) > 30: continue

            print("OwO")
            frame = QFrame()
            layout = QGridLayout()

            title = QLabel()
            title.setText(task.title)
            layout.addWidget(title, 0, 0, 1, 2)

            status = QLabel()
            status.setText(task.status)
            layout.addWidget(status, 0, 2, 1, 1)

            desc = QLabel() 
            desc.setText(task.tag)
            layout.addWidget(desc, 1, 0, 1, 2)

            date = QLabel()
            date.setText(task.endDate.toString())
            layout.addWidget(date, 1, 2, 1, 1)

            frame.setLayout(layout)
            frame.setFixedHeight(60)

            if task.priority >= 0.66:
                frame.setStyleSheet("background-color: red")
            elif task.priority < 0.33:
                frame.setStyleSheet("background-color: green")
            else:
                frame.setStyleSheet("background-color: orange")

        
            frame.mousePressEvent = lambda event, t=task: self.edit_task_page(t, "Schedule")
            # frame.show()
            self.ui.scheduleLayout.addWidget(frame)
        self.ui.scheduleLayout.setAlignment(Qt.AlignTop)
        # self.ui.scrollArea_2.setWidget(self.ui.tasksLayout)

         

    def edit_task_page(self, task, origin = "ToDoList"):
        print("PRESSED") 
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.label_2.setText("Edit Task")
        self.ui.remove_button.show()
        self.ui.duration_label.show()
        self.ui.duration_value.show()
        self.ui.priority_label.show()
        self.ui.priority_value.show()

        self.ui.titleLineEdit.setText(task.title)
        self.ui.descText.setPlainText(task.desc)
        self.ui.dateEdit_start.setDate(task.startDate)
        self.ui.dateEdit_end.setDate(task.endDate)
        self.ui.timeEdit.setTime(task.time)
        self.ui.comboBox.setCurrentText(task.status)
        self.ui.duration_value.setText(str(QDate.currentDate().daysTo(task.endDate)))
        self.ui.priority_value.setText(str(task.priority))

        self.ui.remove_button.clicked.connect(lambda: self.remove(origin))
        self.ui.doneButton.clicked.connect(lambda: self.update(task.title, origin))
        self.ui.doneButton.setText("Update")

    def todolist_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.show_tasks()

    def task_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.titleLineEdit.setText("")
        self.ui.descText.setPlainText("")
        self.ui.tagLineEdit.setText("")
        self.ui.dateEdit_start.setDate(QDate.currentDate())
        self.ui.dateEdit_end.setDate(QDate.currentDate())
        self.ui.comboBox.setCurrentText("Upcoming")
        self.ui.timeEdit.setTime(QTime(23, 59))
 
        self.ui.remove_button.hide()
        self.ui.duration_label.hide()
        self.ui.duration_value.hide()
        self.ui.priority_label.hide()
        self.ui.priority_value.hide()
        self.ui.doneButton.clicked.connect(self.done)
        self.ui.doneButton.setText("Done")

    def done(self):
        self.ui.doneButton.clicked.disconnect()
        if self.ui.titleLineEdit.text() == "" or self.root["ToDoList"].already_contains(self.ui.titleLineEdit.text()):
            self.todolist_page()
            return
        
        task = Task(self.ui.titleLineEdit.text(), self.ui.tagLineEdit.text(), self.ui.descText.toPlainText(), self.ui.dateEdit_start.date(), self.ui.dateEdit_end.date(), self.ui.timeEdit.time(), self.ui.comboBox.currentText())
        if self.ui.comboBox.currentText() == "Finished":
            self.root["History"].add_task(task)
        else:
            self.root["ToDoList"].add_task(task)
        
        transaction.commit() 
        self.todolist_page()


    def update(self, oldtitle, origin = "ToDoList"):
        if self.ui.titleLineEdit.text() == "" or self.root["ToDoList"].already_contains(self.ui.titleLineEdit.text(), oldtitle):
            self.todolist_page()
            return

        if self.ui.comboBox.currentText() == "Finished":
            self.root["ToDoList"].remove_task(oldtitle)
            self.root["History"].add_task(Task(self.ui.titleLineEdit.text(), self.ui.tagLineEdit.text(), self.ui.descText.toPlainText(), self.ui.dateEdit_start.date(), self.ui.dateEdit_end.date(), self.ui.timeEdit.time(), self.ui.comboBox.currentText()))
        else:
            self.root["ToDoList"].update_task(oldtitle, self.ui.titleLineEdit.text(), self.ui.tagLineEdit.text(), self.ui.descText.toPlainText(), self.ui.dateEdit_start.date(), self.ui.dateEdit_end.date(), self.ui.timeEdit.time(), self.ui.comboBox.currentText())
        transaction.commit() 
        self.ui.doneButton.clicked.disconnect()
        if origin == "ToDoList":
            self.todolist_page()
        elif origin == "Schedule":
            self.schedule_page()

    def remove(self, origin = "ToDoList"):
        self.root["ToDoList"].remove_task(self.ui.titleLineEdit.text())
        transaction.commit()
        self.ui.remove_button.clicked.disconnect()
        self.ui.doneButton.clicked.disconnect()
        if origin == "ToDoList":
            self.todolist_page()
        elif origin == "Schedule":
            self.schedule_page()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
 




# 327


 
    # def new_property(self):
    #     if self.numproperty >= 2: return
    #     self.numproperty += 1

    #     print("Create new Property")
    #     frame = QFrame()
    #     layout = QHBoxLayout()
    #     layout.setContentsMargins(0,0,0,0)
    #     layout.setAlignment(Qt.AlignLeft)

    #     title = QLineEdit()
    #     title.setMinimumWidth(100)
    #     title.setPlaceholderText("Title")
    #     title.setStyleSheet("background-color: white")
    #     layout.addWidget(title)

    #     text = QLineEdit()
    #     text.setMinimumWidth(200)
    #     text.setPlaceholderText("Text")
    #     text.setStyleSheet("background-color: white")
    #     layout.addWidget(text)
        
    #     frame.setLayout(layout)
    #     frame.show()
    #     frame.setFixedHeight(40)
    #     self.ui.propertyLayout.setAlignment(Qt.AlignTop)
    #     self.ui.propertyLayout.addWidget(frame)

    #     self.propertyList.append((title, text))