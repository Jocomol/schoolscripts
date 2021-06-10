filename = ("./greek_letters")
with open(filename) as file:
    for line in file:
        line = ' '.join(line.strip().split())
        print(f'print("{line}")')
