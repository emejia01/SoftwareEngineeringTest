
class Course:

    def __init__(self, course_name, CRN, section, department, seats):
        self.name = course_name
        self.CRN = CRN
        self.section = section
        self.dept = department
        self.seat_limit = seats
        self.currentCount = 0

    def getCourseName(self):
        return self.name

    def getCRN(self):
        return self.CRN

    def isFull(self):
        return (self.currentCount >= self.seat_limit)

    def addStudent(self):
        if self.currentCount < self.seat_limit:
            self.currentCount += 1

    def removeStudent(self):
        if self.currentCount > 0:
            self.currentCount -= 1

    def getClassCount(self):
        return self.currentCount

    def getCourseInfo(self):
        course_name = self.name
        CRN_number = self.CRN
        section = self.section
        department = self.dept
        seat_limit = self.seat_limit
        current_seats = self.currentCount

        return [course_name, CRN_number, section, department, seat_limit, current_seats]

