import unittest
from AppFunctions.RegisterCourse.RegisterCourse import *
from Classes.Professor import *

class RegisterCourseTest(unittest.TestCase):

    studentObj = Student("John", "Doe", 500, "Science", major="Computer Science")
    professorObj = Professor("Jane", "Smith", "CMPT")

    def testAddStudent(self):

        registerObj = RegisterCourse()
        student_id = self.studentObj.getStudentID()
        registerObj.addStudent(student_id)

        expected = True
        actual = (student_id in registerObj.course)

        self.assertEqual(expected, actual)

    def testAddCourse(self):

        # Condition to reject course to be added
        registerObj = RegisterCourse()
        expected = -1
        actual = registerObj.addCourse(2121, self.professorObj)

        self.assertEqual(expected, actual)

        # Condition to Successfully add course
        expected = 1
        registerObj.addStudent(500)
        actual = registerObj.addCourse(2121, self.studentObj)

        self.assertEqual(expected, actual)

    def testRemoveCourse(self):

        registerObj = RegisterCourse()
        registerObj.addStudent(self.studentObj.getStudentID())
        registerObj.addCourse(8080, self.studentObj)

        expected = True
        registerObj.removeCourse(8080, self.studentObj)
        actual = (8080 not in registerObj.course)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
