# Sophia Toliver

import os

classGrade = 0.00

grades = {'PEs': {'PointsPossible': 160, 'Weight': 3, 'EarnedPoints': 0, 'Grade': 0.00},
          'Assignments': {'PointsPossible': 210, 'Weight': 10, 'EarnedPoints': 0, 'Grade': 0.00},
          'Projects': {'PointsPossible': 100, 'Weight': 17, 'EarnedPoints': 0, 'Grade': 0.00},
          'Quizzes': {'PointsPossible': 80, 'Weight': 25, 'EarnedPoints': 0, 'Grade': 0.00},
          'Exams': {'PointsPossible': 200, 'Weight': 36, 'EarnedPoints': 0, 'Grade': 0.00},
          'Final Exam': {'PointsPossible': 100, 'Weight': 9, 'EarnedPoints': 0, 'Grade': 0.00}
          }
categories = ['Pts Earned', 'Total Pts', 'Weight', 'Grade']

print('\nAdd up all points earned for each category. For programming exercises, assignments, and quizzes,'
      ' drop your lowest score.\n')

for x in grades:
    # Convert earned points to float
    grades[x]['EarnedPoints'] = float(input(f'Enter total points earned for {x}: '))
    grades[x]['Grade'] = round((grades[x]['EarnedPoints'] / grades[x]['PointsPossible']) * grades[x]['Weight'], 2)
    # Add category grade, rounded to 2 decimals, to total grade
    classGrade += grades[x]['Grade']

os.system('cls')

print('\n\nGrade Information:\n')

print(f'{"Categories": <12}', end="|")

for x in range(len(categories)):
    print(f'{categories[x]: ^12}', end="|")

print('\n')
print('='*65)

for x in grades:
    print(f'\n{x: <12}', end="|")
    print(f'{grades[x]["EarnedPoints"]: >12}', end="|")
    print(f'{grades[x]["PointsPossible"]: >12}', end="|")
    print(f'{grades[x]["Weight"]: >12}', end="|")
    print(f'{grades[x]["Grade"]: >12}', end="|")

print(f'\n\nFinal Grade: {round(classGrade,2)}')
