class Cohort:
    def __init__(self, id, name):
        self.name = name
        # self.students = list()
        # self.instructors = list()

    def __repr__(self):
        return f'{self.name}'