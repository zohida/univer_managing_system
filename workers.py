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