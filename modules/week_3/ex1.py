from numpy import random
import csv
import json

class Student():
    def __init__(self, data_sheet, name, gender, image_url):
        self.data_sheet = data_sheet
        self.name = name
        self.gender = gender
        self.image_url = image_url

        
    def get_average_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        return (sum(grades)/len(grades))

class DataSheet():
    def __init__(self, courses = []):
        self.courses = courses

    def get_grades_as_list(self):
        lst = [value for value.grade in self.courses]
        return lst

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

names = ["Azaghâl", "Balin", "Bifur", "Blacklocks", "Bodruith", "Bofur", "Bombur", "Borin", "Broadbeams", "Dís", "Dori", "Dwalin", "Farin", "Gimli"]
genders = ["Boy", "Girl", "Other"]
name = random.choice(names)
gender = random.choice(genders)


c1 = Course("Engelsk", "B12", "Hanne", 10, 10)
c2 = Course("Dansk", "B14", "Osvald", 20, -3)
c3 = Course("Matematik", "A12", "Trine", 10, 12)
c4 = Course("psyko-druk", "A33", "Skank-ie", 2, 7)
c5 = Course("Brætspil", "C4", "Jason", 0, 2)
course_list = [c1, c2, c3, c4, c5]

def write_list_to_file(output_file, student_obj):
    with open(output_file, 'w') as file_object:
        writer = csv.writer(file_object)
        for s in student_obj:
            writer.writerow([s.name, s.gender, s.data_sheet.courses[0].name, s.data_sheet.courses[0].classroom, s.data_sheet.courses[0].teacher, s.data_sheet.courses[0].ETCS, s.data_sheet.courses[0].grade, s.image_url])
            writer.writerow([s.name, s.gender, s.data_sheet.courses[1].name, s.data_sheet.courses[1].classroom, s.data_sheet.courses[1].teacher, s.data_sheet.courses[1].ETCS, s.data_sheet.courses[1].grade, s.image_url])
            writer.writerow([s.name, s.gender, s.data_sheet.courses[2].name, s.data_sheet.courses[2].classroom, s.data_sheet.courses[2].teacher, s.data_sheet.courses[2].ETCS, s.data_sheet.courses[2].grade, s.image_url])

def generate_student(number):
    student_list = list()


    for n in (range(0, number)):
        
        name = random.choice(names)
        gender = random.choice(genders)
        student_courses = []
        for x in range(3):
            student_courses.append(random.choice(course_list))

        data = DataSheet(student_courses)
        student_list.append(Student(data, name, gender, "imgurl7"))
        

        write_list_to_file("./students.csv", student_list)
        
##generate_student(8)

def read_csv(input_file):
    lst = []
    list_courses = []
    count = 0
    with open(input_file) as file_object:
        reader = csv.reader(file_object)

        for row in reader:
            count = count +1
            exp_courses = Course(row[2], row[3], row[4], row[5], row[6])
            list_courses.append(exp_courses)
            if ((count%3)==0):
                data = DataSheet(list_courses)
                lst.append(Student(data, row[0], row[1], row[7]))
                list_courses = []
    return lst

stdn_lst = read_csv("students.csv")
for s in stdn_lst:
    print(stdn_lst[s].name)