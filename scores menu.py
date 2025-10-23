daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
scores = [[33, 44, 23, 77, 88, 19, 89],
          [23, 13, 88, 65, 38, 19, 99],
          [33, 36, 38, 38, 36, 78, 85],
          [67, 43, 44, 23, 89, 38, 77],
          [3, 36, 65, 78, 46, 39, 88],
          [1, 19, 17, 60 ,68, 89, 100],
          [8, 15, 18, 79, 56, 80, 100],
          [47, 58, 43, 42, 48, 80, 47],
          [67, 79, 84, 85, 88, 88, 99],
          [50, 68, 70, 79, 67, 88, 40]]
people = ["Adam", "Bob", "Charles", "Donny", "Eddie", "Florence", "George", "Henry", "Inan", "Jasmine"]
# interface design
# def printIndividualScores():
#     for i in range (len(names)):
#         print(str(i) + ": " + names[i])
    
#     print("__________________________")
#     scores = int(input("Enter Person PIN"))
# printIndividualScores()
# access every item in a 2d array

for i in range(len(scores)):
    print(people[i])
    for j in range(len(scores[0])):
        if j < 6:
            print("||", str(scores[i][j]), end=" || ")
        else:
            print(str(scores[i][j]) + " ||")
    print("===========================================================")