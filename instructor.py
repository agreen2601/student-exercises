from nss_person import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, id, first, last, slack, specialty, cohort):
        self.id = id
        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.specialty = specialty
        self.cohort = cohort

    def assign_student_exercise(self, student, exercise):
        student.exercises.append(exercise)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'