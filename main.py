# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0
num_of_int = 0

for num in student_heights:
  total += num
num_of_int = n + 1
total /= num_of_int
print(round(total))

