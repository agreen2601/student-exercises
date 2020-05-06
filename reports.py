import sqlite3
from cohort import Cohort
from exercise import Exercise
from student import Student
from instructor import Instructor

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""          

    def __init__(self):
        self.db_path = "/Users/MainTechPiece/workspace/python/student_exercises/studentexercises.db"


    def all_cohorts(self):

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.Id, c.Name
            FROM Cohort c
            ORDER BY c.Id;
            """)

            all_cohorts = db_cursor.fetchall()

            [print(c) for c in all_cohorts]


    def all_exercises(self):

        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id, e.Name, e.Language
            FROM Exercise e
            ORDER BY e.Id;
            """)

            all_exercises = db_cursor.fetchall()

            [print(e) for e in all_exercises]


    def javascript_exercises(self):

        """Retrieve Javascript exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id, e.Name, e.Language
            FROM Exercise e
            WHERE LANGUAGE = "JavaScript"
            ORDER BY e.Id;
            """)

            js_exercises = db_cursor.fetchall()

            [print(e) for e in js_exercises]


    def python_exercises(self):

        """Retrieve all Python exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id, e.Name, e.Language
            FROM Exercise e
            WHERE LANGUAGE = "Python"
            ORDER BY e.Id;
            """)

            py_exercises = db_cursor.fetchall()

            [print(e) for e in py_exercises]


    def react_exercises(self):

        """Retrieve all React exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id, e.Name, e.Language
            FROM Exercise e
            WHERE LANGUAGE = "React"
            ORDER BY e.Id;
            """)

            react_exercises = db_cursor.fetchall()

            [print(e) for e in react_exercises]


    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[0], row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId;
            """)

            all_students = db_cursor.fetchall()

            [print(s) for s in all_students]


    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[0], row[1], row[2], row[3], row[5], row[6])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.First_Name,
                i.Last_Name,
                i.Slack_Handle,
                i.Specialty,
                i.CohortId,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId;
            """)

            all_instructors = db_cursor.fetchall()

            [print(i) for i in all_instructors]

reports = StudentExerciseReports()

print('1. Display all cohorts.')
reports.all_cohorts()
print('\n2. Display all exercises.')
reports.all_exercises()
print('\n3. Display all JavaScript exercises.')
reports.javascript_exercises()
print('\n4. Display all Python exercises.')
reports.python_exercises()
print('\n5. Display all React exercises.')
reports.react_exercises()
print('\n6. Display all students with cohort name.')
reports.all_students()
print('\n7. Display all instructors with cohort name.')
reports.all_instructors()
print('\n')
