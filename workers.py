from staff import Staff

# 1. Administration

class Administration(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("Administration involves managing and organizing operations within an organization or institution.")

admin = Administration("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "academic adviser")
admin.work()

# 2. Invigilator
class Invigilator(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("An invigilator supervises exams to ensure they are conducted fairly and according to rules.")

invigilator = Invigilator("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "invigilator")
invigilator.work()

# 3.Registrar's Office
class RegistrarOffice(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("The Registrar's Office manages student records, course registrations, and academic transcripts.")

register_office = RegistrarOffice("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "register office")
register_office.work()

# 4.Academic Advisor(AA)
class AcademicAdvisor(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("An academic advisor helps students plan their courses and guide their academic progress.")

academic_advisor = AcademicAdvisor("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "AA")
academic_advisor.work()