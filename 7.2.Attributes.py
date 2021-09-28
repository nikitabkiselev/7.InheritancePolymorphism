class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    #Реализация метода оценок лекторам у студентов в соответствии с условиями задачи №
    # (оценки по 10ти бальнной шкале (стр. 11 кода), хранятся в атрибуте словаре у лекторов,
    # в котором ключи - названия курсов, значения - списки оценок). Лектор при этом должен быть закреплен за тем курсом,
    # ев который записан студент
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress\
and (grade >= 0 and grade <=10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#Создание нового класса Лекторов в соответствии с условиями задачи №1
class Lecturer(Mentor):
    #Определение атрибута - словаря у лекторов, в котором ключи-назвария курсов,значения - списки оценок
    #в соответствии с условиями задачи №2
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.grades = {}
#Создание нового класса экспертов в соответствии с условиями задачи №1
class Reviewer(Mentor):
    #Перенос функции выставления оценок за задания экспертам в соответствии с условиями задачи №2
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.grades = {}
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

#Проверка для задачи №1
print('Проверка. Список наследования для Лекторов: ', Lecturer.mro())
print('Проверка. Список наследования для Экспертов: ', Reviewer.mro())


#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']

#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']

#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

#print(best_student.grades)
