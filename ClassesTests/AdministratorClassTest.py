import unittest
from Classes.Administrator import *

class AdministratorClassTest(unittest.TestCase):

    administratorObj = Administrator("Bursar", "Jane", "Doe")

    def testGetOffice(self):
        expected = "Bursar"
        actual = self.administratorObj.getOffice()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
