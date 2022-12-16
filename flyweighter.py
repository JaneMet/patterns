class Patient(object):
    def __init__(self, name):
        self.name = name


class Disease:
    diseases = dict()

    @staticmethod
    def illness(name):
        return Disease.diseases.setdefault(name, Patient(name))


class Floor(object):
    def __init__(self, floor):
        self.floor = floor

    def care_of(self, patient):
        print(f'Next:')
        print(f"    Hospital takes care of {patient.name} on floor №{self.floor}")
        print(f'    Patient ID is {id(patient)}')


class Hospital(object):
    def __init__(self):
        self.diseases_care = 0
        self.branches = {}

    def get_floor(self, number):
        return self.branches.setdefault(number, Floor(number))

    def get_new_patient(self):
        self.got_patient("Mister Holmes", 1)
        self.got_patient("Miss Watson", 5)
        self.got_patient("Donna", 2)

    def got_patient(self, name, floor):
        self.get_floor(floor).care_of(Disease.illness(name))
        self.diseases_care += 1


if __name__ == '__main__':
    Hospital().get_new_patient()
