import unittest
from AppFunctions.UpdateHolds.UpdateHold import UpdateHold
from Classes.Administrator import *
from Classes.StudentClass import *
from Classes.Professor import *


class UpdateHoldTest(unittest.TestCase):

    # Create Objects for testing
    admin = Administrator("Bursar", "Jane", "Doe")
    professor = Professor("CMPT", "Ankur", "Agrawal")
    student = Student("Tim", "Burton", 400, "Science")

    def testAddHold(self):

        holdObj = UpdateHold()

        # Condition if NOT AUTHORIZED to add hold
        expected = -1
        actual = holdObj.addHold(self.professor, self.student, "Payment", "Payment needed to proceed", 999)
        self.assertEqual(expected, actual)

        # Condition if AUTHORIZED to add hold
        expected = 1
        actual = holdObj.addHold(self.admin, self.student, "Payment", "Payment needed to proceed", 999)
        self.assertEqual(expected, actual)

    def testRemoveHold(self):

        holdObj = UpdateHold()

        # Condition if NOT AUTHORIZED to remove hold
        expected = -1
        actual = holdObj.removeHold(self.professor, self.student, 999)
        self.assertEqual(expected, actual)

        # Condition if AUTHORIZED to remove hold
        expected = 1
        actual = holdObj.removeHold(self.admin, self.student, 999)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
