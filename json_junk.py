import json

info = {"name": "Ur mum", "alliases": ["Caseoh", "Gorlock", "GYAATT"], "Hunger": "Infinite"}
#json.dumps makes the stuff into json format
#you can make different indentations for the json
personJSN = json.dumps(info, indent=4, sort_keys=True)
print(personJSN)
print("\n")

#creates a json file with this info
with open("person.json", "w") as file:
    json.dump(info, file)

#convert json to dictionary/list/whatever
person = json.loads(personJSN)

#see whats in the json
with open("person.json", "r") as file:
    person = json.load(file)
    print(person)

