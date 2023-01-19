#Average Height V2 without using loops

student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(f" The average height is: {average_height}\n")