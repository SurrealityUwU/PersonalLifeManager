from PySide6.QtWidgets import *
import sys

from Property import *
from Task import *
import datetime
import ZODB, ZODB.FileStorage
import persistent
from peewee import SqliteDatabase, Model, TextField, IntegerField
import os
from sqlalchemy import ARRAY, Date, Time, TupleType, create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class ToDoList(persistent.Persistent):
    def __init__(self):
        print("Create Todolist") # TODO remove
        self.tasks = persistent.list.PersistentList()

    def __str__(self) -> str:
        for task in self.tasks:
            print(task)
        return ""
        
    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)

    def sort(self, attribute, desc = False):
        if attribute == "Title":
            self.tasks.sort(reverse=desc, key=self.sort_title)
        elif attribute == "Priority":
            self.tasks.sort(reverse=desc, key=self.sort_priority)

    def sort_title(self, x):
        return x.title

    def sort_priority(self, x):
        return x.priority

    def remove_task(self, taskTitle):
        for i in range(len(self.tasks)):
            if self.tasks[i].title == taskTitle:
                print("Removed " + self.tasks[i].title)
                del self.tasks[i]
                print("LEN: " + str(len(self.tasks)))
                return

    def update_task(self, taskTitle, newTitle = "", tag = "", desc = "", startDate = QDate(), endDate = QDate(), time = QTime(), status = "Upcoming"):
        print("Update")
        if newTitle == "": newTitle = taskTitle
        for i in range(len(self.tasks)):
            if self.tasks[i].title == taskTitle:
                print("Changed")
                self.tasks[i] = Task(newTitle, tag, desc, startDate, endDate, time, status)
                return

    def group_by(self):
        pass

    def already_contains(self, tasktitle, oldtitle = ""):
        count = 0
        for task in self.tasks:
            if task.title == tasktitle:
                if oldtitle == tasktitle:
                    count += 1
                else:
                    return True
        if count > 1:
            return True
        return False
        
    def getIndex(self, task):
        if not task in self.tasks: return -1
        return self.tasks.index(task)
