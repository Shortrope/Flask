students = [
    {
        'name': "Josie",
        'school': 'MIT',
        'grades': (66, 77, 88)
    },
    {
        'name': "Jenna",
        'school': 'MIT',
        'grades': (92, 86, 88)
    },
    {
        'name': "Jackie",
        'school': 'MIT',
        'grades': (76, 73, 81)
    },
    {
        'name': "Jasmine",
        'school': 'MIT',
        'grades': (96, 97, 98)
    }
]


def avg_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)

def avg_grade_all(student_list):
    total = 0
    count = 0

    for student in student_list:
        total += avg_grade(student)
        count += 1
        
    return total / count


#print(avg_grade_all(students))

print("Total Avg Grade: {}".format(avg_grade_all(students)))



