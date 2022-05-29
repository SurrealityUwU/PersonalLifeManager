import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from uiForm_2 import Ui_MainWindow
import ZODB, ZODB.FileStorage
import transaction
import persistent
import datetime
import moneyTransaction
import money
import user

class MoneyManagement(QMainWindow):
    def __init__(self):
        #set up UI
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #set up database
        self.storage = ZODB.FileStorage.FileStorage('wallet.fs')
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        #money management attr
        try:
            self.user = root['user']
            self.currentIncome = root['currentIncome']
            self.currentExpense = root['currentExpense']
        except:
            self.root['user'] = user.User('Admin')
            self.balance = self.root['user'].get_balance()
            self.root['currentIncome'] = money.Money(0, 0)
            self.currentIncome = self.root['currentIncome']
            self.root['currentExpense'] = money.Money(0, 0)
            self.currentExpense = self.root['currentExpense']

        self.today = str(datetime.datetime.now())[:10]
        self.update_listWidget_today()
        self.ui.label_today.setText("Today: " + self.today)
        self.ui.label_balanceAmount.setText(str(self.balance))
        self.ui.label_currentIncomeAmount.setText(str(self.currentIncome))
        self.ui.label_currentExpenseAmount.setText(str(self.currentExpense))

        #page 1
        self.ui.pb_home.clicked.connect(self.change_page)
        self.ui.pb_input.clicked.connect(self.change_page)
        self.ui.pb_history.clicked.connect(self.change_page)

        #page 2
        self.ui.pb_income.clicked.connect(self.add_transaction)
        self.ui.pb_expense.clicked.connect(self.add_transaction)

        #page 3
        self.ui.pb_search.clicked.connect(self.search_history)

    def change_page(self):
        sender = self.sender().objectName()
        if(sender == 'pb_home'):
            self.ui.stackedWidget.setCurrentIndex(0)
        elif(sender == 'pb_input'):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif(sender == 'pb_history'):
            self.ui.stackedWidget.setCurrentIndex(2)   
    
    def add_transaction(self):
        self.ui.label_error.setText("")
        sender = self.sender().objectName()
        try:
            baht = int(self.ui.lineEdit_amountBaht.text())
            satang = int(self.ui.lineEdit_amountSatang.text())
            category = self.ui.lineEdit_category.text()
            memo = self.ui.textEdit_memo.toPlainText()
        except:
            self.ui.label_error.setText("Error: Invalid Input!")
        time = str(datetime.datetime.now())
        transaction_money = money.Money(baht, satang)
        if(sender == 'pb_income'):
            transaction_type = 'income'
            self.update_current_income(transaction_money)
        elif(sender == 'pb_expense'):
            transaction_type = 'expense'
            self.update_current_expense(transaction_money)
        self.root[time] = moneyTransaction.MoneyTransaction(transaction_money, transaction_type, category, memo)
        self.update_balance(transaction_money, transaction_type)
        self.update_listWidget_today()

        # print(self.root.items())
        # print(str(self.root[time]))
    
    def update_balance(self, money, transaction_type): #transaction type = negative/positive
        if(transaction_type == 'income'): 
            self.root['user'].get_balance().deposit(money)
        elif(transaction_type == 'expense'): 
            self.root['user'].get_balance().withdraw(money)
        self.balance = self.root['user'].get_balance()
        self.ui.label_balanceAmount.setText(str(self.balance))

    def update_current_income(self, money):
        self.currentIncome.deposit(money)
        self.root['currentIncome'] = self.currentIncome
        self.ui.label_currentIncomeAmount.setText(str(self.currentIncome))

    def update_current_expense(self, money):
        self.currentExpense.withdraw(money)
        self.root['currentExpense'] = self.currentExpense
        self.ui.label_currentExpenseAmount.setText(str(self.currentExpense)[1:])

    def update_listWidget_today(self):
        self.ui.listWidget_today.clear()
        for key in self.root:
            if(key[:10] == self.today):
                self.ui.listWidget_today.addItem(str(self.root[key]))

    def search_history(self):
        self.ui.listWidget_history.clear()
        year = self.ui.lineEdit_year.text()
        month = self.ui.lineEdit_month.text()
        
        print(self.root.items())
        try:
            int_month = int(month)
            int_year = int(month)
        except:
            self.ui.label_search_error.setText("Error: Invalid Input!")
            return
        
        if(month == ''):
           for key in self.root:
                if(key[:4] == year):
                    self.ui.listWidget_history.addItem(key[:19] + ' ' + str(self.root[key]))
        else:
            for key in self.root:
                if(key[:7] == (year + ':' + month)):
                    self.ui.listWidget_history.addItem(key[:19] + ' ' + str(self.root[key]))
        print(month)

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MoneyManagement()
    w.show()
    sys.exit(app.exec_())

        
    