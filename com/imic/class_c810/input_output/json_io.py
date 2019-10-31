import json
with open("../../../../data/student.json", "r") as json_file:
    data = json.load(json_file);
    #print(data)
    print(data["Name"])
    print(data["ID"])
