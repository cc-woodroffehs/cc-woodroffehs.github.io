import os, re
info = {
    "name": "",
    "supervisor": "",
    "email": "",
    "link": ""
}
clubs = []
totalClubs = 0
'''
with open("clubsCreator.yml") as inside:
    for line in inside:
        if "clubName" in line:
            clubs.append(info)
            print(line)
            clubs[-1]["name"] = line.replace("- clubName: ", "").replace('\n', '')
        elif "supervisor" in line:
            clubs[-1]["supervisor"] = line.replace("  supervisor: ", "").replace('\n', '')
        elif "email" in line:
            clubs[-1]["email"] = line.replace("  email: ", "").replace('\n', '')
'''
with open("clubsCreator.yml") as inside:
    for line in inside:
        if "clubName" in line:
            clubs.append([])
            print(line)
            clubs[-1].append(line.replace("- clubName: ", "").replace('\n', ''))
        elif "supervisor" in line:
            clubs[-1].append(line.replace("  supervisor: ", "").replace('\n', ''))
        elif "email" in line:
            if line.replace("\n", "") == "  email:":
                clubs[-1].append("")
            else:
                clubs[-1].append(line.replace("  email: ", "").replace('\n', ''))
print(clubs)

for x in range(len(clubs)):
    clubs[x].append("/clubPages/" + clubs[x][0].replace(" ", "-") + ".html")
'''
for club in clubs:
    with open(club[0].replace(" ", "-") + ".html", "w+") as out:
        out.write("---\nlayout: club\n---\n<h4>Well that's embarassing, seems like " + club[0] + " doesn't have a page yet.</h4>")
'''
with open("newClub", "w+") as output:
    for club in clubs:
        output.write("- clubName: " + club[0] + "\n" +
        "  supervisor: " + club[1] + "\n" +
        "  email: " + club[2] + "\n" +
        "  link: " + club[3] + "\n")
