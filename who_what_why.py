import sqlite3
from student import Student
from instructor import Instructor

class WhoWhatWhy():

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
                exercise_name = row[1]
                student = Student(row[2], row[3], row[4], "", "")
                instructor = Instructor(row[5], row[6], row[7], "", "", "")
                instructor.students = []

                if exercise_name not in exercises:
                    exercises[exercise_name] = [instructor]
                    instructor.students.extend(f'{student.first_name} {student.last_name}')
                else:
                    exercises[exercise_name].append(instructor)
                    instructor.students.extend(f'{student.first_name} {student.last_name}')

            for exercise_name, instructors in exercises.items():
                print(f'{exercise_name}:')
                for instructor in instructors:
                    this = f'\t* {instructor.first_name} {instructor.last_name} assigned this to '
                    for each in instructor.students:
                        this += each
                    print(this)
                print("\n")

report = WhoWhatWhy()

report.exercises_w_students()
