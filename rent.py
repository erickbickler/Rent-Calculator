import json
import os
import sys
import pymongo
import models
from dotenv import load_dotenv, find_dotenv

OUTPUT_FILE = "monthlydata.json"
INPUT_FILE = "expenses.json"

# set debug if set from command line
DEBUG = sys.argv[1] == 'True' if len(sys.argv) > 1 else False

# load environment variables from .env for mongo db instance
load_dotenv(find_dotenv())
CONNECTION_STRING = os.environ.get("CONNECTION_STRING")

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
    if DEBUG:
        print("Running in debug mode")
    print("\nRent Calculator built on python 3.7")
    print("Made by Erick Bickler Copyright 2021 \n")
    month = input("Which month is this for? ")
    year = input("Which year is this for? ")
    print("Loading json...")
    with open(INPUT_FILE, "r") as input_file:
        json_in = json.load(input_file)
        roommates = {
            roommate: models.Person(roommate) for roommate in json_in["roommates"]
        }
        for e_info in json_in["expenses"]:
            expense(e_info["name"], e_info["amount"], [match(i) for i in e_info["paid"]], [match(i) for i in e_info["split"]])
        if not DEBUG:
            try:
                print("Writing to database...")
                client = pymongo.MongoClient(CONNECTION_STRING)
                db = client.rent
                data = {
                    "month": month,
                    "year": year,
                    "expenses": json_in["expenses"]
                }
                db.monthly_data.insert_one(data)
                print("Database entry created!")
            except pymongo.errors.ConnectionFailure:
                print("Database connection failed, writing to local json...")
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
    print()
    
