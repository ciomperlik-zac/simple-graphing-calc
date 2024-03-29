import math

graph = [["◻ "] * 40 for _ in range(40)]

points = []

equation = input("Enter Enquation: ")

for point in range(-20,20):
    equation_copy = equation.replace("X","("+str(point)+")")
    try:
        solution = round(eval(equation_copy))
    except ValueError:
        continue

    if solution < 20 and solution >= -20:
        graph[solution+20][point+20] = "◼ "
    print(point,end=" ")
    print(solution)


graph.reverse()
for row in graph:
    print("".join(row))