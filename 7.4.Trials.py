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

#Создание 2 экземпляра класса студентов  c реализацией возможности сравнения по средней оценке за домашнее задание
Ivan_Ivanov = Student('Иван', 'Иванов', 'Male')
Ivan_Ivanov.finished_courses = ['Экономика', 'Право', 'Информатика']
Ivan_Ivanov.courses_in_progress = ['Физика', 'Химия']
Ivan_Ivanov.grades = {'Экономика':[7.0,8.0,9.0,5.0],
                      'Право': [9,5,3,2],
                      'Информатика': [6,1,7,10],
                      'Физика': [9, 8, 7, 6],
                      'Химия': [2,3,4,5]}
Anna_Petrova = Student('Анна','Петрова', 'Female')
Anna_Petrova.finished_courses = ['Экономика', 'Физика', 'Химия']
Anna_Petrova.courses_in_progress = ['Право', 'Информатика']
Anna_Petrova.grades = {'Экономика':[5,5,5,5],
                      'Право': [6,6,6,6],
                      'Информатика': [7,7,7,7],
                      'Физика': [8, 8, 8, 8],
                      'Химия': [9,9,9,9]}
print('ДВА ЭКЗЕМПЛЯРА КЛАССА СТУДЕНТОВ (в порядке убывания средней оценки за домашнее задание):')
if average(Ivan_Ivanov.grades) > average (Anna_Petrova.grades):
    print(f'{Ivan_Ivanov} \n{Anna_Petrova}')
else:
    print(f'{Anna_Petrova} \n{Ivan_Ivanov}')

#Создание 2 экземпляра класса лекторов c реализацией возможности сравнения по средней оценке за лекции
Stas_Medvedev = Lecturer('Станислав','Медведев', ['Экономика'])
Stas_Medvedev.courses_attached = ['Экономика']
Stas_Medvedev.grades = {'Экономика':[7.0,8.0,9.0,5.0]}
Kate_Novikova = Lecturer('Екатерина','Новикова', ['Право'])
Kate_Novikova.courses_attached = ['Право']
Kate_Novikova.grades = {'Право': [3,10,5,7,5,9]}
print('ДВА ЭКЗЕМПЛЯРА КЛАССА ЛЕКТОРОВ (в порядке убывания средней оценки за лекции):')
if average(Stas_Medvedev.grades) > average (Kate_Novikova.grades):
    print(f'{Stas_Medvedev} \n{Kate_Novikova}')
else:
    print(f'{Kate_Novikova} \n{Stas_Medvedev}')
#Создание 2 экземпляра класса экспертов
Karl_Lewis = Reviewer('Карл', 'Льюис', ['Химия'])
Ben_Johnson = Reviewer('Бен', 'Джонсон', ['Физика'])
print('ДВА ЭКЗЕМПЛЯРА КЛАССА ЭКСПЕРТОВ:')
print(Karl_Lewis)
print(Ben_Johnson)
