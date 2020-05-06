import sqlite3

class ExercisesWithStudents():

    def __init__(self):
        self.db_path = "/Users/MainTechPiece/workspace/python/student_exercises/studentexercises.db"

    def student_exercises(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.First_Name,
                    s.Last_Name
                from Exercise e
                join Assigned_Exercises se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId;
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')
                print("\n")

report = ExercisesWithStudents()

report.student_exercises()
