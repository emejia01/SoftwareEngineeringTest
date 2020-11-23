import unittest
from Classes.Professor import *

class ProfessorClassTest(unittest.TestCase):

    professorObj = Professor("CMPT", "John", "Doe")

    def testGetDepartment(self):
        expected = "CMPT"
        actual = self.professorObj.getDepartment()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
