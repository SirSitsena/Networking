students = {}

for line in open('score2.txt').readlines():
    elems = line.strip().split(" ")
    name = elems[2] + " " + elems[3]
    if name in students:
        students[name] += int(elems[4])
    else:
        students[name] = int(elems[4])

maxScore = max(students.values())

for name, score in students.items():
    if score == maxScore:
        print(name, "has the score: ", score)