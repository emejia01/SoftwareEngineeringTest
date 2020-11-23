import unittest
from Classes.EmployeeClass import *

class EmployeeClassTest(unittest.TestCase):

    employeeObj = Employee("Jane", "Doe")

    def testSetFirstName(self):
        new_name = "Alice"
        self.employeeObj.setFirstName(new_name)
        expected = new_name
        actual = self.employeeObj.getName()[0]

        self.assertEqual(expected, actual)

    def testSetLastName(self):
        new_last_name = "Smith"
        self.employeeObj.setLastName(new_last_name)
        expected = new_last_name
        actual = self.employeeObj.getName()[1]

        self.assertEqual(expected, actual)

    def testGetName(self):
        expected = ["Jane", "Doe"]
        actual = self.employeeObj.getName()

        self.assertEqual(expected, actual)

    def testGetIDNumber(self):
        expected = max(EMPLOYEE_ID_NUMBERS)
        actual = self.employeeObj.getIDNumber()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
