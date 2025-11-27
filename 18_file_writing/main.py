# w mode: Write Mode

# x mode: create a new file with the specified name.

# a mode: If file exists, new data is appended. If file not exists, file is created and data is written

txt_data = "I like pizza!"

file_path = "output.json"

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "Cook"
}

try:
    with open(file=file_path, mode="a") as file:
        # file.write("\n"+txt_data)
        # for employee in employees:
            # file.write('\n' + employee)
        json.dump(employee, file, indent=4)
        print("file updated")
except FileExistsError:
    print("That file already exists")

import csv

employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployeed"],
    ["Sandy", 27, "Scientist"]
]
file_path = "output.csv"
try:
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f'csv file {file_path} as created')
except FileExistsError:
    print("That file already exsists")