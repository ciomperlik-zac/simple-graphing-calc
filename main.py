import math

graph = [["◻ "] * 40 for _ in range(40)]

points = []

equation = input("Enter Enquation: ")

for point in range(-20,21):
    equation_copy = equation.replace("X",str(point))
    solution = round(eval(equation_copy))

    if solution < 20 and round(eval(equation_copy)) >= -20:
        graph[solution+19][point+20] = "◼ "

for point in range(len(points)):
    print("("+str(point-10)+","+str(points[point])+")")

for row in graph:
    row.reverse()
    print("".join(row))