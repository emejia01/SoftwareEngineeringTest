'''
This class will be the main interface/wrapper class that will be used when updating holds on a student account. It will
ensure that holds are added/removed ONLY from classes that are authorized to do so.
'''

from Classes.Administrator import *


class UpdateHold():

    def addHold(self, employee, student, hold_title, hold_description, reference_number):

        if isinstance(employee, Administrator):
            student.addHold(hold_title, hold_description, reference_number)
            return 1
        else:
            print("Employee is NOT authorized to add student hold to account.")
            return -1

    def removeHold(self, employee, student, reference_number):

        if isinstance(employee, Administrator):
            student.removeHold(reference_number)
            return 1
        else:
            print("Employee is NOT authorized to remove hold on account.")
            return -1

