name = input('Name: ')
age = input('Age: ')
grades = [float(input(f'Grade {i+1}: ')) for i in range(0,5)]

def getApproved(grades:list):
    if sum(grades)/len(grades) >= 3:
        return True
    else:
        return False

student = {
    "name" : name,
    "age" : age,
    "grades" : grades,
    "approved" : getApproved(grades)
}

print(f'-----Results-----\n{student}')