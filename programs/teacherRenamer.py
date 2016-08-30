import os, bs4, re

souped = bs4.BeautifulSoup(open("teachers"), "html.parser")

# Per teacher [name, email, webpage, department, position]
pet = ["- name", "  email", "  webpage", "  department", "  position"]
teachers = []

for teacher in souped.findAll('tr'):
    teachers.append([])
    link = 0
    for item in teacher.findAll('td'):
        if link != 3:
            teachers[-1].append(item.text.replace('\n', ""))
        else:
            try:
                teachers[-1].append(re.findall('<a href=\"(.*?)\">', str(item))[0])
            except:
                teachers[-1].append("")
        link += 1
    del teachers[-1][0]

limiter = len(teachers)

for x in range(50):
    doubleBreak = False
    for teacher in range(len(teachers)):
        teacher = teachers[teacher][0]
        counter = 0
        for secTeacher in range(len(teachers)):
            if teacher in teachers[secTeacher]:
                counter += 1
                if counter == 2:
                    del teachers[secTeacher]
                    doubleBreak = True
                    break
        if doubleBreak: break

with open("teacherList2.yml", "r+") as f:
    for teacher in teachers:
        for item in range(len(pet)):
            f.write(pet[item] + ": " + teacher[item] + "\n")
