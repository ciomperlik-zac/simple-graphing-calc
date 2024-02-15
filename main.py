import math

graph = [["◻ "] * 40 for _ in range(40)]

points = []

equation = input("Enter Enquation: ")

for point in range(20,-21,-1):
    equation_copy = equation.replace("X",str(point))

    points.append(round(eval(equation_copy)))

for point in range(len(points)):
    print("("+str(point-10)+","+str(points[point])+")")

for i in range(1,41):
    if points[i] >= -20 and points[i] < 20:
        graph[points[i]+20][i-1] = "◼ "

for row in graph:
    print("".join(row))