class Doctors:
    def __init__(self, name, specialization, experience):
        self.doctor_name = name
        self.doctor_specialization = specialization
        self.doctor_experience = experience


    def information_doctor(self):
        print(f"Name: {self.doctor_name}     Specialization: {self.doctor_specialization}    Experience: {self.doctor_experience} ")


class Patient:
    def __init__(self, name, disease, city):
        self.pat_name = name
        self.pat_disease = disease  # заболевание
        self.pat_city = city

    def information_patient(self):
        print(f"Name: {self.pat_name}     Disease: {self.pat_disease}     City: {self.pat_city}")


class Hospital:
    @staticmethod
    def create_doc_pozition(name, specialization, experience):
        return Doctors(name, specialization, experience)

    @staticmethod
    def create_pat_info(name, disease, city):
        return Patient(name, disease, city)


Hospital.create_doc_pozition('Doctor_first', 'oftalmolog', '20').information_doctor()
Hospital.create_pat_info('Patient_first', 'farsightedness', 'Moscow').information_patient() #дальнозоркость

