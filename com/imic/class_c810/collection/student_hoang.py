##Sample data: https://i.stack.imgur.com/7KTR7.png

#1. Store sample data using Dict, List, Tuple
import pprint
import json

student = {
  'ID':'867-509',
  'Name':'Rebecca Morton',
  'Age': 29,
  'Email':'rebecca.morton@example.com',
  'Biography':'Rebecca started life as a typical girl in a country house with a while picket fence.',
  'Project': {
     'A':'Mission to Mars',
     'B':'Teaching a dog new tricks',
     'C':'One trick Pony',
     'D':"Sky's the limit"
  }
}
#print(student)
#pp = pprint.PrettyPrinter()
#pp.pprint(student)
print(json.dumps(student, indent=4, sort_keys=True))


#2. Copy 10 similar records with ID from 1 to 10
students = []
count = 0
while (count < 10):
  students.append(student.copy())
  count = count + 1

count = 0
while (count < 10):
  students[count]['ID'] = count + 1
  print(students[count]['Name'])
  count = count + 1

print ("Good bye!")

#3. Collect 10 names, age, & email from internet then replace 10 current records.
names_buffers = ["Thắng"
  , "Ngân"
  , "Anh"
  , "Huyền"
  , "Vân"
  , "Thanh"
  , "Đức"
  , "Huệ"
  , "Trang"
  , "Nam"
  , "Sơn"
  ]
  
ages_buffer = [47
  , 13
  , 35
  , 46
  , 21
  , 17
  , 17
  , 20
  , 29
  , 16
  , 19
  ]
  
count = 0
while (count < 10):
  students[count]['Name'] = names_buffers[count]
  students[count]['Age'] = ages_buffer[count]
  print("name: ", students[count]['Name']
     , "age: ", students[count]['Age'])
  count = count + 1


print(json.dumps(students, indent=4, sort_keys=True))


























#3b. Show sum of Agesz
#4. Input name, show full details of given name.