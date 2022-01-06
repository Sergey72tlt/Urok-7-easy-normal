class School:

    def __init__(self, name, classes=()):
        self.name = name
        self.classes = classes

    def get_all_classes(self):
        return self.classes

    def __str__(self):
        return self.name


class Room:

    def __init__(self, teachers=(), pupils=(), name=''):
        self.pupils = pupils
        for pupil in self.pupils:
            pupil.room = self
        self.teachers = []
        self.name = name

        for teacher in teachers:
            if name in teacher.classes:
                self.teachers.append(teacher)
            else:
                print(teacher, 'не может преподавать в классе', self.name)

    def __str__(self):
        return self.name

    def get_all_pupils(self):
        return self.pupils

    def get_all_teachers(self):
        return self.teachers

    def get_all_subjects(self):
        subjects = []
        for teacher in self.teachers:
            subjects.append(teacher.subject)
        return subjects


class Pupil:

    def __init__(self, father=None, mother=None, name=''):
        self.father = father
        self.mother = mother
        self.name = name

    def __str__(self):
        return f'имя ученика: {self.name}, родители: {self.father}, {self.mother}'


class Parent:

    def __init__(self, name=''):
        self.name = name

    def __str__(self):
        return f'имя родителя: {self.name}'


class Teacher:
    def __init__(self, name='', subject=None, classes=()):
        self.name = name
        self.subject = subject
        self.classes = classes

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Subject:
    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


parent1 = Parent(name='Владимир')
parent2 = Parent(name='Светлана')

parent3 = Parent(name='Игорь')
parent4 = Parent(name='Ольга')

pupil1 = Pupil(father=parent1, mother=parent2, name='Иван')
pupil2 = Pupil(father=parent3, mother=parent4, name='Денис')
pupil3 = Pupil(father=parent1, mother=parent2, name='Николай')
pupil4 = Pupil(father=parent3, mother=parent4, name='Олег')

subject_math = Subject(name='Математика')
teacher1 = Teacher(name='Мария Владимировна', subject=subject_math, classes=("6А",))

subject_rus = Subject(name='Русский язык')
teacher2 = Teacher(name='Жанна Петровна', subject=subject_rus, classes=("7А",))

subject_fiz = Subject(name='Физика')
teacher3 = Teacher(name='Марфа Ваильевна', subject=subject_fiz, classes=("8А",))

subject_fizra = Subject(name='Физкультура')
teacher4 = Teacher(name='Анна Петровна', subject=subject_fizra, classes=("9А", ))

room1 = Room(teachers=(teacher1, teacher2, teacher3, teacher4), pupils=(pupil1, pupil2, pupil3, pupil4), name="6А",)
room2 = Room(teachers=(teacher1, teacher2, teacher3, teacher4), pupils=(pupil1, pupil2, pupil3, pupil4), name="7А",)
room3 = Room(teachers=(teacher1, teacher2, teacher3, teacher4), pupils=(pupil1, pupil2, pupil3, pupil4), name="8А",)
room4 = Room(teachers=(teacher1, teacher2, teacher3, teacher4), pupils=(pupil1, pupil2, pupil3, pupil4), name="9А",)

my_school1 = School(classes=(room1, room2, room3, room4), name='№ 56')

print('Классы школы ', my_school1)

for class_obj in my_school1.get_all_classes():
    print(class_obj)
    for pupil in class_obj.get_all_pupils():
        print(pupil)
    print('Учитель в этом классе: ')
    print(class_obj.get_all_teachers())
    print('Изучаемые предметы: ')
    print(class_obj.get_all_subjects())