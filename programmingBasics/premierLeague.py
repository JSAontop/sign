teams = ["Arsenal", "Liverpool", "Tottenham", "AFC Bournemouth", "Manchester City"]
def output():
    for i in range (0,len(teams)):
        print(teams[i])
def search(team):
    if team in teams:
        print("true")
    else:
        print("false")
output()
team = input("Enter a team in the top 5: ")
search(team)
points = []
for i in range (0, len(teams)):
    point = input("Enter points for " + str(teams[i]) +": ")
    points.append(point)
def leagueTable():
    for x in range (0, len(teams)):
        print(teams[x] + ": " + str(points[x]))
leagueTable()