class Student:
    sum = 0

    def __init__(self, inputName, inputSore):
        self.name = inputName
        self.score = inputSore
        self.subjectName = "Math"
        Student.sum = Student.sum + 1
        pass;

    def getStudentName(self):
        return self.name
