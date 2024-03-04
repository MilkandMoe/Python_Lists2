#Tasks1:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades)


#Tasks2:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
length_of_grades = len(grades)
average = sum(grades) / length_of_grades
print(average)

#Tasks3:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
        
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
print(grades)