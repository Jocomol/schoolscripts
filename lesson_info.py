#!/usr/bin/env python3
import json
from datetime import datetime
import colorful

lessonsfile_path = "/home/joco/.school/lessons.json"
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

with open(lessonsfile_path) as json_file:
    data = json.load(json_file)
    weekday = datetime.today().weekday()
    now = datetime.now()
    timeTillBreak = None
    foundLesson = False
    if weekday >= 5:
        print("Hooray, no school today")
        exit(0)
    for lesson in data[weekday]:
        starttime = now.replace(hour=lesson["starttimehour"], minute=lesson["starttimeminute"], second=0, microsecond=0)
        endtime = now.replace(hour=lesson["endtimehour"], minute=lesson["endtimeminute"], second=0, microsecond=0)
        if starttime > now < endtime:
            print(colorful.bold(". ") + lesson["name"] + ", " + lesson["room"] + ", " + str(lesson["starttimehour"]) + ":" + str(lesson["starttimeminute"]) + "-" + str(lesson["endtimehour"]) + ":" + str(lesson["endtimeminute"]))
        elif starttime < now < endtime:
            print("---")
            print(colorful.bold_green("Weekday: ") + days[weekday])
            print(colorful.bold_green("Current time: ") + str(now.strftime("%H:%M")))
            print("---")
            print(colorful.bold_green("Lesson: ") + lesson["name"])
            print(colorful.bold_green("Teacher: ") + lesson["teacher"])
            print(colorful.bold_green("Room: ") + lesson["room"])
            print(colorful.bold_green("Starttime: ") + str(lesson["starttimehour"]) + ":" + str(lesson["starttimeminute"]))
            print(colorful.bold_green("Endtime: ") + str(lesson["endtimehour"]) + ":" + str(lesson["endtimeminute"]))
            print(colorful.bold_green("Time till break: ") + str(timeTillBreak))
            print("---")
            print("Upcoming Lessons:")


