class Exercise:
    def __init__(self, id, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name}, {self.language}'