import sqlite3

class AssignedExercises():

    def __init__(self):
        self.db_path = "/Users/MainTechPiece/workspace/python/student_exercises/studentexercises.db"

    def instructors_w_exercises(self):

        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    i.Id,
                    i.First_Name,
                    i.Last_Name
                from Exercise e
                join Assigned_Exercises ae on ae.ExerciseId = e.Id
                join Instructor i on i.Id = ae.InstructorId;
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                instructor_id = row[2]
                instructor_name = f'{row[3]} {row[4]}'

                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    instructors[instructor_name].append(exercise_name)

            for instructor_name, exercises in instructors.items():
                print(f'{instructor_name} has assigned:')
                for exercise in exercises:
                    print(f'\t* {exercise}')
                print("\n")

report = AssignedExercises()

report.instructors_w_exercises()
