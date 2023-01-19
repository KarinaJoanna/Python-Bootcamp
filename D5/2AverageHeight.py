#Average Height

student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height #loop through the list and add each height to the total
#print(f" The total height is: {total_height}\n")

number_of_students = 0
for student in student_heights:
    number_of_students += 1 #loop through the list and add 1 to the total for each student and 1 means add 1 to the number of students
#print(f" The number of students is: {number_of_students}\n")

average_height = round(total_height / number_of_students)
print(f" The average height is: {average_height}\n")