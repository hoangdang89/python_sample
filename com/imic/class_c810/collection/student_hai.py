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
