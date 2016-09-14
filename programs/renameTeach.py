import bs4

souped = bs4.BeautifulSoup(open("teachers"), "html.parser")

attributes = {
    "name" : "",
    "email": "",
    "website": "",
    "position": "",
    "department": "",
}

teachers = []

for teacher in souped.findAll('tr'):
    teachers.append({})
    perTeachAttributes = teacher.findAll('td')

    teachers[-1]['name'] = str(perTeachAttributes[0]).replace('<td class="ms-vb2">', '').replace('</td>', '') + str(perTeachAttributes[1]).replace('<td class="ms-vb2">', '').replace('</td>', '')
    teachers[-1]['website'] = str(perTeachAttributes[2]).replace('<td class="ms-vb2">', '').replace('</td>', '').replace('<a href="', '').replace('">Webpage</a>', '').replace('\n', '')
    teachers[-1]['email'] = str(perTeachAttributes[3].text.replace('\n', ''))
    teachers[-1]['position'] = str(perTeachAttributes[4]).replace('<td class="ms-vb2">', '').replace('</td>', '')
    teachers[-1]['department'] = str(perTeachAttributes[5]).replace('<td class="ms-vb2">', '').replace('</td>', '')
'''
for x in range(100):
    doubleBreak = False
    for teacher in range(len(teachers)):
        teacher = teachers[teacher]['name']
        counter = 0
        for secTeach in range(len(teachers)):
            if teacher == teachers[secTeach]['name']:
                counter += 1
                if counter == 2:
                    del teachers[secTeacher]
                    doubleBreak = True
                    break
        if doubleBreak: break
'''
with open("out", "r+") as f:
    for teacher in teachers:
        print(teacher)
        f.write("- name: " + teacher['name'] + '\n')
        for item, value in teacher.items():
            if item == "name":
                pass
                # f.write("- name" + ": " + value + "\n")
                # print("writing, " + "- name" + ": " + value)
            else:
                f.write("  " + item + ": " + value + "\n")
                print("writing, " + "  " + item + ": " + value)
