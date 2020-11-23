'''
This class will be the interface/wrapper class that will allow course to be registered/removed for students
within the system. It will check against other classes before registering a student.
'''

from Classes.StudentClass import *

class RegisterCourse:

    def __init__(self):
        # Structure to hold Students and their Courses (SQL Database to be used in Actual project). A dictionary will be used for now
        # Courses[Student_ID] = [List of Registered Courses]
        self.course = {}

    def addStudent(self, student_ID):
        if student_ID not in self.course:
            self.course[student_ID] = []

    def addCourse(self, course_CRN, student):

        if isinstance(student, Student):
            student_id = student.getStudentID()
            if student.hasHolds():
                print("Holds Present on Account. CANNOT REGISTER for course.")
                return -1
            else:
                self.course[student_id].append(course_CRN)
                print("Successfully Registered for course.")
                return 1
        return -1

    def removeCourse(self, course_CRN, student):

        student_id = student.getStudentID()
        if isinstance(student, Student) and student_id in self.course:
            if student.hasHolds():
                print("Hold Present on Account. CANNOT REGISTER for course.")
                return -1
            else:
                if course_CRN in self.course[student_id]:
                    course_index = self.course[student_id].index(course_CRN)
                    self.course[student_id].pop(course_index)
                return 1
