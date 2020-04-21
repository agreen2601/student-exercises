from nss_person import NSSPerson

class Student(NSSPerson):
    def __init__(self, first, last, slack, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.cohort = cohort
        self.exercises = list()