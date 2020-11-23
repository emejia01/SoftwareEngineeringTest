import unittest
from Classes.Course import Course


class CourseTest(unittest.TestCase):

    courseObj = Course("Software Engineering", 2121, 1, "CMPT", 30)

    def testGetCourseName(self):
        expected = "Software Engineering"
        actual = self.courseObj.getCourseName()

        self.assertEqual(expected, actual)

    def testGetCRN(self):
        expected = 2121
        actual = self.courseObj.getCRN()

        self.assertEqual(expected, actual)

    def testAddStudent(self):

        expected = 3
        for i in range(3):
            self.courseObj.addStudent()
        actual = self.courseObj.getClassCount()

        self.assertEqual(expected, actual)

    def testRemoveStudent(self):

        expected = 0
        for i in range(3):
            self.courseObj.removeStudent()
        actual = self.courseObj.getClassCount()

        self.assertEqual(expected, actual)

    def testIsFull(self):

        self.courseObj.currentCount = 0
        expected = False
        actual = self.courseObj.isFull()

        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
