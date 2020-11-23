
class Student:

    def __init__(self, first_name, last_name, student_id, school, concentration=None, major=None, minor=None):

        self.first_name = first_name
        self.last_name = last_name
        self.student_ID = student_id
        self.major = major
        self.minor = minor
        self.concentration = concentration
        self.school = school

        self.holds = {}

    def getName(self):
        first_name = self.first_name
        last_name = self.last_name

        return [first_name, last_name]

    def setMajor(self, major):
        self.major = major

    def setMinor(self, minor):
        self.minor = minor

    def setConcentration(self, concentration):
        self.concentration = concentration

    def getMajor(self):
        return self.major

    def getMinor(self):
        return self.minor

    def getConcentration(self):
        return self.concentration

    def getSchool(self):
        return self.school

    def addHold(self, hold_title, hold_description, reference_number):
        hold_info = (hold_title, hold_description, reference_number)
        self.holds[reference_number] = hold_info

    def removeHold(self, reference_number):
        if reference_number in self.holds:
            del self.holds[reference_number]

    def hasHolds(self):
        return len(self.holds) > 0

    def getHolds(self):
        return self.holds

    def getStudentID(self):
        return self.student_ID