import sqlite3

class StudentWorkload():

    def __init__(self):
        self.db_path = "/Users/MainTechPiece/workspace/python/student_exercises/studentexercises.db"

    def students_w_exercises(self):

        students = dict()

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
                join Assigned_Exercises ae on ae.ExerciseId = e.Id
                join Student s on s.Id = ae.StudentId;
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(f'{student_name} is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')
                print("\n")

report = StudentWorkload()

report.students_w_exercises()
