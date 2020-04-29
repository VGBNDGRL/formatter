# Formatter.py
class Formatter:
    'Formatter superclass for formatting single input lines'
    # add class variables here

    # define constructor (notice the use of
    # optional parameters instead of multiple
    # constructors)
    def __init__(self, currentworkingline):
        # define instance variables
        self.currentline= currentworkingline

    # define class methods
    @classmethod
    def formatline(cls, inputline):
        print("formatline")

    # define instance methods

    # # Employee.py
    # class Employee:
    #     'Employee superclass for all employees'
    #     lastId = 0  # class variable
    #
    #     # define constructor (notice the use of
    #     # optional parameters instead of multiple
    #     # constructors)
    #     def __init__(self, name, salary, prefix="", exempt=1):
    #         # define instance variables
    #         self.namePrefix = prefix
    #         self.name = name
    #         self.salary = salary
    #         self.exemptions = exempt
    #         self.id = Employee.generateID()
    #
    #     # define class methods
    #     @classmethod
    #     def generateID(cls):
    #         if Employee.lastId == 0:
    #             Employee.lastId = 111  # db.getLastId()
    #         Employee.lastId += 1
    #         return Employee.lastId

    #     # define instance methods
    #     def getFormattedName(self):
    #         if self.namePrefix == "":
    #             return self.name
    #         else:
    #             return self.namePrefix + " " + self.name
    #
    #     def calculatePay(self):
    #         if self.exemptions == 1:
    #             return self.salary / 12
    #         else:
    #             return self.salary / 12 * 0.9

