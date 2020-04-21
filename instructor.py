from nss_person import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first, last, slack, cohort, specialty):
        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.cohort = cohort
        self.specialty = specialty

    def add_student_exercise(self, student, exercise):
        student.exercises.append(exercise)