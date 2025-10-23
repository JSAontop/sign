teams = ["Arsenal", "Liverpool", "Tottenham", "AFC Bournemouth", "Manchester City"]
points = [16, 15, 14, 14, 12]
# def output():
#     for i in range (0,len(teams)):
#         print(teams[i])
def search(team):
    notFound = True
    for x in range (0, len(teams)):
        if teams[x] == team:
            notFound = False
    if notFound == False:
        print("Found")
    else:
        print("Not found")
team = input("Enter a team in the top 5: ")
search(team)
# def leagueTable():
#     for x in range (0, len(teams)):
#         print(teams[x] + ": " + str(points[x]))
# leagueTable()