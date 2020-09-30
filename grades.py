#!/usr/bin/env python3
import argparse
import json


# TODO Flake8 and Documentation
gradefile_path = "/home/joco/.grades/grades.json"

# TODO short flags
parser = argparse.ArgumentParser(description='Script to add grades and to calculate grades')
parser.add_argument('--add', help='adds grade', type=float, default=0.0, action="store")
parser.add_argument('--course', help='specifies course', type=str, default="", action="store")  # TODO better input here
parser.add_argument('--list', help='lists all grades', action='store_true')

args = parser.parse_args()

with open(gradefile_path) as json_file:
    data = json.load(json_file)

if args.add != 0.0:
    grade = args.add
    course_name = ""
    if args.course != "":
        course_name = args.course
    else:
        # TODO better input here
        course_name = input("Please enter the course you want to add the grade too: ")

    try:
        data[course_name]["grades"].append(grade)
        print("Adding " + str(grade) + " to course " + course_name)
    except KeyError:
        print("Class: " + course_name + " not found")
        # TODO print all courses
        parser.print_help()
        exit(1)

    with open(gradefile_path, 'w') as outfile:
        json.dump(data, outfile)

elif args.list:
    # TODO Beautiful output
    mean_sum = 0
    number_off_courses = 0
    for course in data.items():
        number_off_courses += 1
        print(course[1]["name"])
        grade_sum = 0
        number_of_grades = 0
        for grade in course[1]["grades"]:
            grade_sum += grade
            number_of_grades += 1
            print("-" + str(grade))
        mean = grade_sum / number_of_grades
        print("Durchschnitt: " + str(mean) + "\n")
        mean_sum += mean
    print("Gesamtdurchschnitt " + str((mean_sum / number_off_courses).__round__(2)))
else:
    parser.print_help()
