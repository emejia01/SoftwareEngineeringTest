
from Classes.EmployeeClass import *

class Professor(Employee):

    def __init__(self, department, first_name, last_name):
        super(Professor, self).__init__(first_name, last_name)

        self.department = department

    def getDepartment(self):
        return self.department

