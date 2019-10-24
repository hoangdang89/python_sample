##Sample data: https://i.stack.imgur.com/7KTR7.png

#1. Store sample data using Dict, List, Tuple
student = {'ID': '867-5309', 'name': 'Rebecca Morton', 'age': 29}
#print(student)

#2. Copy 10 similar records
students = ["student 1","student 2","student 3","student 4","student 5", "student 6", "student 7", "student 8","student 9", "student 10"]

# student1 = ID1, name
# Student2 = id2,


count = 0
while (count < 10):
   studentx = student.copy()
   studentx['ID'] = count+1
   print('student', studentx)
   students[count] = studentx
   count = count+1

print(students[2])
print ("Good bye!")

#3. Collect 10 names, age, & email from internet then replace 10 current records.
#3b. Show sum of Agesz
#4. Input name, show full details of given name.