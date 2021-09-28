from pandas.core.common import flatten
from statistics import mean

# Функция расчета среднего исходя из условий задачи (словарь с ключами и списками оценок)
def average(myDict):
    valuesList = []
    for key in myDict:
        valuesList.append(myDict[key])
    return round(mean(list(flatten(valuesList))),2)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    #Реализация метода оценок лекторам у студентов в соответствии с условиями задачи №2
    # (оценки по 10ти бальной шкале, хранятся в атрибуте словаре у лекторов,в котором ключи - названия курсов, значения
    #  - списки оценок). Лектор при этом должен быть закреплен за тем курсом, в который записан студент
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress\
and (grade >= 0 and grade <=10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    # Реализация магического метода __str__ у класса студентов в соответствии с условиями задачи №3
    def __str__(self):
        average_students_grade = average(self.grades)
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: \
{average_students_grade} \nКурсы в процессе изучения: {self.courses_in_progress} \n\
Завершенные курсы: {self.finished_courses}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
# Реализация магического метода __str__ у класса менторов, в условиях задач отсутствует, для отладки кода
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nЗакрепленные курсы: {self.courses_attached} '
        return res

#Создание нового класса Лекторов в соответствии с условиями задачи №1
# Определение атрибута - словаря у лекторов, в котором ключи-назвария курсов,значения - списки оценок
# #в соответствии с условиями задачи №2
class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name,surname)
        self.grades = {}
    # Реализация магического метода __str__ у класса лекторов в соответствии с условиями задачи №3
    def __str__(self):
        average_lecturer_grade = average(self.grades)
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average_lecturer_grade}'
        return res

#Создание нового класса экспертов в соответствии с условиями задачи №1
class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.grades = {}
    #Перенос функции выставления оценок за задания экспертам в соответствии с условиями задачи №2
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    # Реализация магического метода __str__ у класса экспертов в соответствии с условиями задачи №3
    def __str__(self):
       res = f'Имя: {self.name} \nФамилия: {self.surname}'
       return res
