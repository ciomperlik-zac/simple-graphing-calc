graph = [[" "," "," "," "," ", " "," "," "," "," "],
         [" "," "," "," "," ", " "," "," "," "," "],
         [" "," "," "," "," ", " "," "," "," "," "],
         [" "," "," "," "," ", " "," "," "," "," "],
         [" "," "," "," "," ", " "," "," "," "," "],

         [" "," "," "," "," ", " "," "," "," "," "],
         [" "," "," "," "," ", " "," "," "," "," "],
         [" "," "," "," "," ", " "," "," "," "," "],
         [" "," "," "," "," ", " "," "," "," "," "],
         [" "," "," "," "," ", " "," "," "," "," "]]

points = []

equation = input("Enter Enquation: ")

for point in range(-5,6):
    equation_copy = equation.replace("X",str(point))

    points.append(round(eval(equation_copy)))

for point in range(len(points)):
    print("("+str(point-5)+","+str(points[point])+")")