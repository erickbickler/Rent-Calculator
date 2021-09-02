import json

OUTPUT_FILE = "monthlydata.json"
INPUT_FILE = "expenses.json"
DEBUG = True

class Person:
    def __init__(self, name):
        self.total = 0
        self.name = name

def expense(name, amount, paid, split):
    for person in paid:
        person.total -= amount/len(paid)
    
    for person in split:
        person.total += amount/len(split)

def match(name):
    for key in roommates:
        if key == name:
            return roommates[key]
    raise Exception(f"{name} roommate not found")

if __name__ == '__main__':
    print("Rent Calculator built on python 3.7")
    print("Made by Erick Bickler Copyright 2021")
    print()
    month = input("Which month is this for? ")

    with open(INPUT_FILE, "r") as input_file:
        print("Loading json...")
        json_in = json.load(input_file)
        roommates = {
            roommate: Person(roommate) for roommate in json_in["roommates"]
        }
        for e_info in json_in["expenses"]:
            expense(e_info["name"], e_info["amount"], [match(i) for i in e_info["paid"]], [match(i) for i in e_info["split"]])
        if not DEBUG:
            with open(OUTPUT_FILE, "r") as output_file:
                json_log = json.load(output_file)
            with open(OUTPUT_FILE, "w") as output_file:
                json_log[month] = json_in
                json.dump(json_log, output_file)

    print()
    print("-----Totals-----")
    out_txt = "{person} total: ${total:,.2f}"
    for person in roommates.values():
        print(out_txt.format(person=person.name.title(), total=person.total))
    