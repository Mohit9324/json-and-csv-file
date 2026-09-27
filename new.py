import json
import csv

students = [
    {"name": "Diego", "age": 14, "grade": "8th"},
    {"name": "Farah", "age": 15, "grade": "9th"},
    {"name": "Kwame", "age": 13, "grade": "7th"},
]

with open("students.json", "w") as f:
    json.dump(students, f)

def convert_json_to_csv(json_path, csv_path):
    with open(json_path, "r") as f:
        students = json.load(f)

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "grade"])
        for s in students:
            writer.writerow([s["name"], s["age"], s["grade"]])

if __name__ == "__main__":
    convert_json_to_csv("students.json", "students.csv")

    with open("students.csv", "r") as f:
        print(f.read())

       



          
          
        