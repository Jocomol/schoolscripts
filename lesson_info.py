#/usr/bin/env python3
import json
from datetime import datetime
import colorful

lessonsfile_path = "/home/joco/.school/lessons.json"
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

with open(lessonsfile_path) as json_file:
    data = json.load(json_file)
    weekday = datetime.today().weekday()
    now = datetime.now()
    currentLesson = None
    nextLesson = None
    timeTillBreak = None
    foundLesson = False
    if weekday >= 5:
        print("Hooray, no school today")
        exit(0)
    for lesson in data[weekday]:
        starttime = now.replace(hour=lesson["starttimehour"], minute=lesson["starttimeminute"], second=0, microsecond=0)
        endtime = now.replace(hour=lesson["endtimehour"], minute=lesson["endtimeminute"], second=0, microsecond=0)
        if foundLesson:
            nextLesson = lesson
            break
        elif starttime < now < endtime:
            currentLesson = lesson
            timeTillBreak = endtime - now
            foundLesson = True
    if currentLesson is None:
        print(colorful.red("No Lesson running at the moment"))
        exit(0)

    print("---")
    print(colorful.bold_green("Weekday: ") + days[weekday])
    print(colorful.bold_green("Current time: ") + str(now.strftime("%H:%M")))
    print("---")
    print(colorful.bold_green("Lesson: ") + currentLesson["name"])
    print(colorful.bold_green("Teacher: ") + currentLesson["teacher"])
    print(colorful.bold_green("Room: ") + currentLesson["room"])
    print(colorful.bold_green("Starttime: ") + str(currentLesson["starttimehour"]) + ":" + str(currentLesson["starttimeminute"]))
    print(colorful.bold_green("Endtime: ") + str(currentLesson["endtimehour"]) + ":" + str(currentLesson["endtimeminute"]))
    print(colorful.bold_green("Time till break: ") + str(timeTillBreak))
    print("---")
    if nextLesson is not None:
        print(colorful.bold("Next Lesson: ") + nextLesson["name"] + ", " + nextLesson["room"] + ", " + str(nextLesson["starttimehour"]) + ":" + str(nextLesson["starttimeminute"]) + "-" + str(nextLesson["endtimehour"]) + ":" + str(nextLesson["endtimeminute"]))
        print("---")