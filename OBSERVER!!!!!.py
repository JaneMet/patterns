from abc import ABC, abstractmethod


class Libary:

    def __init__(self):
        self.__students = set() #создано пустое множество

    def new_visit(self, stud):
        self.__students.add(stud) #студент пришел

    def go_away(self, stud):
        print(f'Студент покинул библиотеку')
        self.__students.remove(stud) #студент ушел

    def update(self):
        print(f'Количество студентов в библиотеке: {len(self.__students)} ')
        for stud in self.__students: #оповестим - обновим записи
            stud.get_book()

    def update_p(self):
        for stud in self.__students: #оповестим - обновим записи
            stud.get_check()


class AbstractVisiter(ABC):
    @abstractmethod
    def get_book(self):
        pass


class TableVisits(AbstractVisiter):

    def __init__(self, name):
        self.name = name

    def get_book(self):
        print('{} получил книгу'.format(self.name))


student1 = TableVisits('Студент 1:')
student2 = TableVisits('Студент 2:')
student3 = TableVisits('Студент 3:')

table_visits = Libary()

table_visits.new_visit(student1)
table_visits.update()
table_visits.go_away(student1)
table_visits.update()

table_visits.new_visit(student2)
table_visits.new_visit(student3)
table_visits.update()
table_visits.go_away(student3)
table_visits.update()