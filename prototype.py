class KinderGarden():

    def Comment(self):
        return "Детский сад"

    def __str__(self):
        return "Явно не 5 лет  |||"


class School():

    def Comment(self):
        return "Школа"

    def __str__(self):
        return "Явно не 10 лет |||"


class University():

    def Comment(self):
        return f'Университет'

    def __str__(self):
        return "Явно не 15 лет |||"

if __name__ == "__main__":
    small_age = KinderGarden()
    middle_age = School()
    older_age = University()

    print(f'Какой возраст? {older_age} Где учится? {older_age.Comment()}')
    print(f'Какой возраст? {middle_age} Где учится? {middle_age.Comment()}')
    print(f'Какой возраст? {small_age} Где учится? {small_age.Comment()}')
