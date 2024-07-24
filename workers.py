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

# 5. Student Advisor (SA)
class StudentAdvisor(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("A Student Advisor provides guidance on academic and personal matters to help students succeed.")

student_advisor = StudentAdvisor("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "SA")
student_advisor.work()

# 6. Security
class Security(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("Security involves protecting people, property, and information from harm or unauthorized access.")

security = Security("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "security")
security.work()

# 7. Janitors
class Janitors(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("Janitors clean and maintain buildings, ensuring they are tidy and functional.")

janitors = Janitors("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "janitors")
janitors.work()

# 8. HR
class HR(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("HR (Human Resources) manages employee relations, recruitment, and organizational policies.")

hr = HR("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "hr")
hr.work()

# 9. Marketing
class Marketing(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("Marketing involves promoting and selling products or services, including market research and advertising.")


marketing = Marketing("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "marketing")
marketing.work()

# 10. Academic Adviser
class AcademicAdviser(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("An academic adviser assists students with their educational goals, course selections, and career planning.")


academic_adviser = AcademicAdviser("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "Academic Adviser")
academic_adviser.work()


# 11. Librarian
class Librarian(Staff):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary, title)


    def work(self):
        print("A librarian manages and organizes library resources, assists with research, and supports literacy and learning.")


librarian = Librarian("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "librarian")
librarian.work()