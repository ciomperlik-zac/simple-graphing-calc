import math

graph = [["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ["◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ ","◻ "],
         ]

points = []

equation = input("Enter Enquation: ")

for point in range(10,-11,-1):
    equation_copy = equation.replace("X",str(point))

    points.append(round(eval(equation_copy)))

for point in range(len(points)):
    print("("+str(point-10)+","+str(points[point])+")")

for i in range(1,21):
    if points[i] >= -10 and points[i] < 10:
        graph[points[i]+10][i-1] = "◼ "

for row in graph:
    print("".join(row))