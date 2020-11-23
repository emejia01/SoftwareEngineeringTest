
from Classes.EmployeeClass import *

class Administrator(Employee):

    def __init__(self, office, first_name, last_name):
        super(Administrator, self).__init__(first_name, last_name)

        self.office = office

    def getOffice(self):
        return self.office

