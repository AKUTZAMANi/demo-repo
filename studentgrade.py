class ABUstudent(student):

    nextIdNum = 0 #identification number
    def __init__(self, name):
        self.name = name
    try:
        lastBlank = name.rindex(' ')
        self.lastName = name[lastBlank+1:]
    except:
        self.lastName = name

        student.__init__(self, name)
        self.student = []
        self.idNum = ABUstudent.nextIdNum
        ABUstudent.nextIdNum += 1

    def getName(self):
        """Returns self's first name"""
        return self.name

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def getIdNum(self):
        return self.idNum

    def __str__(self):
        """Returns self's name"""
        return self.name



class grades(student):
     def __init__(self): #creating files
        #file = open("Staffrecord.txt", "w")
        self.student = []
        self.grades = {}
        self.isSorted = True

     def addStudent(self, student):

        if student in self.students:
             raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

     def addGrade(self, student, grade):

        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

     def getGrades(self, student):
        """Return a list of grades for student"""
        try: #return copy of list of student's grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')


     def getStudents(self):
        """Return a sorted list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

     def finalscores(self, coursework):
        """Assumes course is of type Grades"""
        report = ''
        for s in coursework.getStudents():
            tot = 0.0
            numGrades = 0
            for g in coursework.getGrades(s):
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades
                report = report + '\n'\
                    + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n'\
                    + str(s) + ' has no grades'
    return report

if __name__ == '__main__':
