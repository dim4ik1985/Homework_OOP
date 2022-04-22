class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # пройденные курсы
        self.courses_in_progress = []  # список курсов
        self.grades = {}  # оценки

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:

                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rating(self):
        lst_grades = []
        if self.grades:
            for values in self.grades.values():
                lst_grades.extend(values)
            return round(sum(lst_grades) / len(lst_grades), 1)
        else:
            return 'Нет оценок'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a lecturer')
            return
        elif self.__average_rating() > other.__average_rating():
            return f'Средняя оценка за ДЗ у {self.name} {self.surname} выше'
        else:
            return f'Средняя оценка за ДЗ у {other.name} {other.surname} выше'

    def __str__(self):
        some_student = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}\n' \
                       f'Средняя оценка за домашние задания: {self.__average_rating()}\n' \
                       f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                       f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # ведет курс


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_rating(self):
        lst_grades = []
        if self.grades:
            for values in self.grades.values():
                lst_grades.extend(values)
            return round(sum(lst_grades) / len(lst_grades), 1)
        else:
            return 'Нет оценок'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        elif self.__average_rating() > other.__average_rating():
            return f'Рейтинг лектора {self.name} {self.surname} выше'
        else:
            return f'Рейтинг лектора {other.name} {other.surname} выше'

    def __str__(self):
        some_lecturer = f'Имя: {self.name} \n' \
                        f'Фамилия: {self.surname} \n' \
                        f'Средняя оценка за лекции: {self.__average_rating()}'
        return some_lecturer


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]  # если курс уже есть в списке оценок, добавляем оценку к курсу
            else:
                student.grades[course] = [grade]  # иначе добавляем в словать курс и оценку к нему
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}'
        return some_reviewer


def aver_score_student(list_students, course_name):
    sum_rate = 0
    for student in list_students:
        if student.grades.get(course_name):
            for rating in student.grades[course_name]:
                sum_rate += rating
    return f'Cредняя оценка за домашние задания по всем студентам в рамках курса {course_name}: ' \
           f'{round(sum_rate / len(list_students), 1)}'


def aver_score_lecturer(list_lecturers, course_name):
    sum_rate = 0
    for lecturer in list_lecturers:
        if lecturer.grades.get(course_name):
            for rating in lecturer.grades[course_name]:
                sum_rate += rating
    return f'Cредняя оценка за лекции всех лекторов в рамках  курса {course_name}: ' \
           f'{round(sum_rate / len(list_lecturers), 1)}'


student_alyssa = Student('Alyssa', 'Jones', 'female')
student_colton = Student('Colton', 'Jones', 'male')
student_alyssa.courses_in_progress = ['Python-developer', 'Web-developer', 'SQL-developer']
student_alyssa.finished_courses = ['Android-developer', 'iOS-developer']
student_colton.courses_in_progress = ['Python-developer', 'Android-developer', 'iOS-developer', 'SQL-developer']
student_colton.finished_courses = ['SoftwareTester']
reviewer_steven = Reviewer('Steven', 'Williams')
reviewer_steven.rate_hw(student_alyssa, student_alyssa.courses_in_progress[0], 8)
reviewer_steven.rate_hw(student_alyssa, student_alyssa.courses_in_progress[0], 9)
reviewer_steven.rate_hw(student_alyssa, student_alyssa.courses_in_progress[1], 9)
reviewer_steven.rate_hw(student_colton, student_colton.courses_in_progress[0], 10)
reviewer_steven.rate_hw(student_colton, student_colton.courses_in_progress[1], 10)
reviewer_steven.rate_hw(student_colton, student_colton.courses_in_progress[2], 9)
reviewer_ralph = Reviewer('Ralph', 'Allen')
reviewer_ralph.rate_hw(student_alyssa, student_alyssa.courses_in_progress[0], 10)
reviewer_ralph.rate_hw(student_alyssa, student_alyssa.courses_in_progress[1], 7)
reviewer_ralph.rate_hw(student_alyssa, student_alyssa.courses_in_progress[2], 9)
reviewer_ralph.rate_hw(student_colton, student_colton.courses_in_progress[0], 9)
reviewer_ralph.rate_hw(student_colton, student_colton.courses_in_progress[1], 7)
reviewer_ralph.rate_hw(student_colton, student_colton.courses_in_progress[2], 10)
lecturer_bob = Lecturer('Bob', 'Dilan')
lecturer_bob.courses_attached = ['SQL-developer', 'Web-developer', 'Python-developer', 'Android-developer']
lecturer_owen = Lecturer('Owen', 'Green')
lecturer_owen.courses_attached = ['SQL-developer', 'SoftwareTester', 'Android-developer']
student_alyssa.rate_hw(lecturer_bob, lecturer_bob.courses_attached[0], 10)
student_alyssa.rate_hw(lecturer_bob, lecturer_bob.courses_attached[1], 8)
student_colton.rate_hw(lecturer_bob, lecturer_bob.courses_attached[2], 9)
student_colton.rate_hw(lecturer_bob, lecturer_bob.courses_attached[0], 10)
student_alyssa.rate_hw(lecturer_owen, lecturer_owen.courses_attached[0], 10)
print(student_alyssa)
print('-------------------------------------')
print(student_colton)
print()
print('*****************  Лекторы   *******************')
print(lecturer_bob)
print('----------------------------------')
print(lecturer_owen)
print()
print('****************  Ревьюверы   ****************')
print(reviewer_steven)
print('-------------------------------------')
print(reviewer_ralph)
print('-------------------------------------')
print(lecturer_bob > lecturer_owen)
print(student_colton > student_alyssa)
print()
print(aver_score_student([student_alyssa, student_colton], 'Python-developer'))
print(aver_score_lecturer([lecturer_bob, lecturer_owen], 'SQL-developer'))
