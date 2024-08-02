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
    print("\n")
    print(person)



class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User("Max", 27)
def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Nah, Id Glitch")
    #W

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
userJSN = json.dumps(user, default=encode_user)
print(userJSN)
print("\n")
UserJSON = UserEncoder().encode(user)
print("\n")
print(UserJSON)

user = json.loads(UserJSON)
print("\n")
print(user.name)