import datetime

class Task:
    near_warning_days = 3

    def __init__(self, property_values):
        self.property_values = property_values
        self.recurring = 0
        self.show = True
        self.urgency = 0

        self.start_date = datetime.datetime.today()
        self.completed_date = self.start_date
        self.due_date = self.start_date

    def __str__(self):
        return "Task Name: {}\nProperties: {}\nRecurring: {}\nShow: {}\nUrgency: {}\nStart Date: {}\nCompleted Date: {}\nDue Date: {}".format(
            self.name, self.property_values, self.recurring, self.show, self.urgency, self.start_date, self.completed_date, self.due_date)

    def calculate_points(self):
        # TODO
        pass

    def calculate_urgency(self):
        # TODO
        pass

    def filter(self, object1, condition, object2, connector):
        # TODO
        pass



if __name__ == "__main__":
    t = Task()
    print(t)