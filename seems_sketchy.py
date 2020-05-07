import sqlite3

class PopularExercises():

    def __init__(self):
        self.db_path = "/Users/MainTechPiece/workspace/python/student_exercises/studentexercises.db"

    def exercises_w_students(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.First_Name,
                    s.Last_Name,
                    i.Id,
                    i.First_Name,
                    i.Last_Name
                from Exercise e
                join Assigned_Exercises ae on ae.ExerciseId = e.Id
                join Student s on s.Id = ae.StudentId
                join Instructor i on i.Id = ae.InstructorId;
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                assigned_from_to = f'{row[6]} {row[7]} assigned this to {row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [assigned_from_to]
                else:
                    exercises[exercise_name].append(assigned_from_to)

            for exercise_name, students in exercises.items():
                print(f'{exercise_name}:')
                for student in students:
                    print(f'\t* {student}')
                print("\n")

report = PopularExercises()

report.exercises_w_students()
