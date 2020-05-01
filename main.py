from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

lists = Exercise("Lists", "Python")
dictionaries = Exercise("Dictionaries", "Python")
tuples = Exercise("Tuples", "Python")
sets = Exercise("Sets", "Python")
debugging_python = Exercise("Debuggin", "Python")

cohort_37 = Cohort("Cohort 37")
cohort_38 = Cohort("Cohort 38")
cohort_39 = Cohort("Cohort 39")
cohort_40 = Cohort("Cohort 40")

william = Student("William", "Green", "William Green", "Cohort 37")
andrew = Student("Andrew", "Green", "Andrew Green", "Cohort 38")
michael = Student("Michael", "Carroll", "Michael Carroll", "Cohort 39")
roxanne = Student("Roxanne", "Nasraty", "Roxanne Nasraty", "Cohort 40")

jisie = Instructor("Jisie", "David", "Jisie David", "Cohort 38", "So cheery")
kristen = Instructor("Kristen", "Norris", "Kristen Norris", "Cohort 38", "Sticking with us until the end")
bryan = Instructor("Bryan", "Nilsen", "Bryan Nilsen", "Cohort 40", "High fives")

jisie.assign_student_exercise(william, lists)
jisie.assign_student_exercise(andrew, dictionaries)
kristen.assign_student_exercise(michael, tuples)
kristen.assign_student_exercise(roxanne, sets)
bryan.assign_student_exercise(william, debugging_python)
bryan.assign_student_exercise(william, sets)

print(f'{william.first_name} {william.last_name} is working on the following exercises:')

for exercise in william.exercises:
    print(f'{exercise.name} {exercise.language}')
