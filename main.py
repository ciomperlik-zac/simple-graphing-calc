graph = [[" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "]]

points = []

equation = input("Enter Enquation: ")

for point in range(-5,6):
    equation_copy = equation
    
    while equation_copy.find("X") != -1:
        point = equation_copy[equation_copy.find("X")]
    
    points.append([point-1,round(eval(equation_copy))-1])

for y in range(10):
    graph[graph[y]][y] = "#"

for row in graph:
    print("".join(row))

