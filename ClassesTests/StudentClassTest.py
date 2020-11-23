import unittest
from Classes.StudentClass import Student

class StudentClassTest(unittest.TestCase):

    studentObj = Student("John", "Doe", 200, "Science", "Machine Learning", "Computer Science", "Mathematics")

    def testGetName(self):
        expected = ["John", "Doe"]
        actual = self.studentObj.getName()

        self.assertEqual(expected, actual)

    def testGetMajor(self):
        expected = "Computer Science"
        actual = self.studentObj.getMajor()

        self.assertEqual(expected, actual)

    def testSetMajor(self):
        new_major = "Biology"
        self.studentObj.setMajor(new_major)
        actual = self.studentObj.getMajor()

        self.assertEqual(new_major, actual)

    def testGetMinor(self):
        expected = "Mathematics"
        actual = self.studentObj.getMinor()

        self.assertEqual(expected, actual)

    def testSetMinor(self):
        new_minor = "English"
        self.studentObj.setMinor(new_minor)
        actual = self.studentObj.getMinor()

        self.assertEqual(new_minor, actual)

    def testHold(self):
        hold_title = "Payment Hold"
        hold_description = "Make payment to remove hold"
        hold_reference_number = 100

        # Add hold test
        self.studentObj.addHold(hold_title, hold_description, hold_reference_number)
        expected_hold_info = (hold_title, hold_description, hold_reference_number)
        actual_hold_info = self.studentObj.getHolds()[hold_reference_number]

        self.assertEqual(expected_hold_info, actual_hold_info)

        # HasHold test
        expected = True
        actual = self.studentObj.hasHolds()

        self.assertEqual(expected, actual)

        # Remove Hold Test
        self.studentObj.removeHold(hold_reference_number)
        expected = False
        actual = self.studentObj.hasHolds()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
