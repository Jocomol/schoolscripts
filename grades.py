#!/usr/bin/env python3
import argparse
import json
import colorful

gradefile_path = "/home/joco/.school/grades.json"  # Path of the gradefile
courses = ["Deutsch", "Mathematik", "Physik", "Geschichte und Politik", "Franzoesisch", "Chemie", "Wirtschaft","IDAF","Englisch"]
courses_id = ["german", "math", "phyisk", "history", "french", "chemistry", "economics","idaf","english"]  # ID's of the different courses


def print_courses():
    number = 0
    for course_name_string in courses:
        print(str(number) + ": " + course_name_string)
        number += 1


def colored_grade(grade):
    if grade < 4:
        return colorful.red(grade)
    elif grade < 4.5:
        return colorful.yellow(grade)
    else:
        return colorful.green(grade)


parser = argparse.ArgumentParser(description='Script to add grades and to calculate grades')
parser.add_argument('-a', '--add', help='adds grade', type=float, default=0.0, action="store")
parser.add_argument('-c', '--course', help='specifies course', type=int, default=0, action="store")
parser.add_argument("-l", '--list', help='lists all grades', action='store_true')
parser.add_argument("-C", "--courses", help="list all courses", action='store_true')

args = parser.parse_args()

with open(gradefile_path) as json_file:
    data = json.load(json_file)

if args.add != 0.0:
    grade = args.add
    course_id = 0
    if args.course != 0:
        course_id = args.course
    else:
        print_courses()
        course_id = int(input("Please enter the course id you want to add the grade too: "))

    try:
        data[courses_id[course_id]]["grades"].append(grade)
        print("Adding " + str(grade) + " to course " + courses[course_id])
    except KeyError:
        print("Course ID: " + courses[course_id] + " not found")
        print_courses()
        parser.print_help()
        exit(1)

    with open(gradefile_path, 'w') as outfile:
        json.dump(data, outfile)

elif args.courses:
    print_courses()

elif args.list:
    mean_sum = 0
    number_off_courses = 0
    for course in data.items():
        print(colorful.bold(course[1]["name"]))
        grade_sum = 0
        number_of_grades = 0
        mean = None
        try:
            for grade in course[1]["grades"]:
                grade_sum += grade
                number_of_grades += 1
                print("-" + colored_grade(grade))
            mean = grade_sum / number_of_grades
            number_off_courses += 1
        except TypeError:
            pass

        try:
            print("mean: " + colored_grade(mean.__round__(2)) + "\n")
            mean_sum += mean
        except AttributeError:
            pass

    print("total mean " + colored_grade((mean_sum / number_off_courses).__round__(2)))
else:
    parser.print_help()
