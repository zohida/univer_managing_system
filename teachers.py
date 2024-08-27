from faculty import Faculty

class TeachingAssistant(Faculty):
    def __init__(self,type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary, title, employee_id, research_topic):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary, title)
        self.set_employee_id(employee_id)
        self.set_research_topic(research_topic)

    def set_employee_id(self, employee_id):
        if employee_id[:2].isupper() and employee_id[2:].isdigit():
            self.__employee_id = employee_id
        else:
            raise ValueError("Employee ID cannot be empty.")

    def set_research_topic(self, research_topic):
        if isinstance(research_topic, str):
            self.__research_topic = research_topic
        else:
            raise Exception("Something gets wrong!!!")

    def get_employee_id(self):
        return self.__employee_id

    def get_research_topic(self):
        return self.__research_topic

    def teaches(self):
        print("Help teachers with lesson planning and student support.")

teachingAssistant = TeachingAssistant("Faculty",
                                      "Tom Smith",
                                      "AA1000011",
                                      "tomsmith@gmail.com",
                                      "1980/04/16",
                                      "male",
                                      "british",
                                      "998999999999",
                                      "physics",
                                      "full-time",
                                      18, 2000,
                                      "teaching assistant",
                                      "AV1233",
                                      "Economy")
teachingAssistant.teaches()


class Lecturers(Faculty):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary,
                 title, research_topic):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary,
                         title)

        self.set_research_topic(research_topic)

    def set_research_topic(self, research_topic):
        if isinstance(research_topic, str):
            self.__research_topic = research_topic
        else:
            raise Exception("Something gets wrong!!!")

    def get_research_topic(self):
        return self.__research_topic

    def teaches(self):
        print("Lecturers teach courses, conduct research, and evaluate students.")

lecturer = Lecturers("Faculty",
                     "Tom Smith",
                     "AA1000011",
                     "tomsmith@gmail.com",
                     "1980/04/16",
                     "male",
                     "british",
                     "998999999999",
                     "physics",
                     "full-time",
                     18,
                     2000,
                     "academician",
                     "Biolife")
lecturer.teaches()


class AssistantProffessor(Faculty):
    def teaches(self):
        print("An assistant professor is a junior faculty member at a college or university, often working toward tenure.")

assistantProfessor = AssistantProffessor("Faculty", "Tom Smith", "AA1000011",
                                         "tomsmith@gmail.com", "1980/04/16", "male",
                                         "british", "998999999999", "physics",
                                         "full-time", 18, 2000, "assistant professor")
assistantProfessor.teaches()

class Academician(Faculty):
    def teaches(self):
        print("An academician is a scholar who specializes in a particular field of study")

academician = Academician("Faculty", "Tom Smith", "AA1000011", "tomsmith@gmail.com",
                          "1980/04/16", "male", "british", "998999999999",
                          "physics", "full-time", 18, 2000, "academician")
academician.teaches()

class FullResearcher(Faculty):

    def teaches(self):
        print("A full researcher conducts advanced studies and publishes findings in their field.")

researcher = FullResearcher("Faculty", "Tom Smith", "AA1000011", "tomsmith@gmail.com",
                            "1980/04/16", "male", "british", "998999999999",
                            "physics", "full-time", 18, 2000, "full researcher")
researcher.teaches()