student_height = input('Input A list of Studen Height :').split()
for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])
 
total_height = 0
length = 0
for i in student_height:  
  total_height = total_height + i
  length = length + 1

average_height = round(total_height / length)
print(f"Total Height of The Student is {total_height } and The Average Height of Student is { average_height}")