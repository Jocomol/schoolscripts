import re
filename = ("./greek_letters")
with open(filename) as file:
    for line in file:
        line = re.sub("\s+", ",", line.strip())
        line = line.split(",")
        print("print(\"" + line[0] + " " + line[1] + " " + line[2].strip() + "\")")
