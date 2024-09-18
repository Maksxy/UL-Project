import matplotlib.pyplot as plt
import random
import time

start1 = time.time()
file_path = 'StudentInfo.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    data_array = [line.strip() for line in lines]

student_array = [x.lower() for x in data_array]
first_names = [x.split() for x in student_array]
sorted_array = sorted(first_names, key=lambda row: row[1], reverse=False)

def printIt(var):
    for row in var:
        print(row)

printIt(sorted_array)

end1 = time.time()

print()

start2 = time.time()

runtime1 = end1 - start1
print(f"Time to execute surename sort: {runtime1} seconds ")

hackathon_group = ([])
for i in range(0, len(sorted_array)):
    for j in range(0, len(sorted_array[i])):
        if sorted_array[i][j] == "23363185":
            hackathon_group.append(sorted_array[i])

        if sorted_array[i][j] == "23362901":
            hackathon_group.append(sorted_array[i])

        if sorted_array[i][j] == "23365684":
            hackathon_group.append(sorted_array[i])

        if sorted_array[i][j] == "23375493":
            hackathon_group.append(sorted_array[i])

        if sorted_array[i][j] == "23390573":
            hackathon_group.append(sorted_array[i])

        if sorted_array[i][j] == "23327936":
            hackathon_group.append(sorted_array[i])

end2 = time.time()

runtime2 = end2 - start2
print(f"Time to execute module sort: {runtime2} seconds ")

print()

start3 = time.time()

def ranNum(n, i):
    n[i].append(random.randint(0,100))


for i in range(0, len(hackathon_group)):
    hackathon_group[i].append("CS4222, Software Development")
    ranNum(hackathon_group, i)
    hackathon_group[i].append("CS4221, Introduction to programming")
    ranNum(hackathon_group, i)
    hackathon_group[i].append("CS4141, Foundation of Computer Science")
    ranNum(hackathon_group, i)

print("Hackathon Group")
printIt(hackathon_group)
Software_dev = sorted(hackathon_group, key=lambda row: row[4], reverse=True)
print("Highest mark for Software Development")
for row in Software_dev:
    print(row)
    Intro_prog = sorted(hackathon_group, key=lambda row: row[6], reverse=True)
print("Highest mark for Introduction to programming")
for row in Intro_prog:
    print(row)
    found_computer = sorted(hackathon_group, key=lambda row: row[8], reverse=True)
print("Highest mark for Foundation of Computer Science")
for row in found_computer:
    print(row)

end3 = time.time()

runtime3 = end3 - start3
print(f"Time to execute Student Modules: {runtime3} seconds ")

print()

soft_score = ([])
intro_to_pro = ([])
fond_comp = ([])
for i in range(0, len(hackathon_group)):
    soft_score.append(hackathon_group[i][4])
for i in range(0, len(hackathon_group)):
    intro_to_pro.append(hackathon_group[i][6])
for i in range(0, len(hackathon_group)):
    fond_comp.append(hackathon_group[i][8])
students = ([])
for i in range(0, len(hackathon_group)):
    students.append(hackathon_group[i][2])

Algorithms = ["Search Operation","Time Sort for Sort"]
timing = [runtime1, runtime2]

plt.title("Foundations of Computer Science=yellow, Software Development =blue ,Introduction to Programming=green")
plt.bar(Algorithms,timing, )
plt.title("Time Complexity Analysis", fontsize = 14)
plt.xlabel("Algorithms",  fontsize = 14)
plt.ylabel("Running Time (ms)", fontsize = 14)
plt.show()

plt.scatter(students,soft_score)
plt.scatter(students,intro_to_pro)
plt.scatter(students,fond_comp)

plt.ylabel("Grades")
plt.xlabel("Students")

plt.show()