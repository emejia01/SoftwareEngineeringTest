
EMPLOYEE_ID_NUMBERS = [100, 101, 102, 103]

class Employee:

    def __init__(self, first_name, last_name):

        self.firstName = first_name
        self.lastName = last_name

        # Generate ID number from current list.
        self.ID_number = EMPLOYEE_ID_NUMBERS[-1] + 1
        EMPLOYEE_ID_NUMBERS.append(self.ID_number)

    def getName(self):
        return [self.firstName, self.lastName]

    def setFirstName(self, name):
        self.firstName = name

    def setLastName(self, last_name):
        self.lastName = last_name

    def getIDNumber(self):
        return self.ID_number

