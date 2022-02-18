#Functional Programming Assignment #1
#Author: Juwan Hollingsworth

#Calculate triangle area function...
def calc_area(side):
    #calculate the perimeter
    perimeter = side + side + side
    #calculate semi-perimeter 
    s = (perimeter)/2
    #calculate the area
    area = (s*(s-side)*(s-side)*(s-side))**0.5
    #return value formatted with only two decimal places
    return (format(area, '.2f'))

#Step 1. - Make Sample Data ..

    #Given Triangles
triangle1= [1,2,3]
triangle2=[5,5,5]
triangle3= [3,2,1]
triangle4=[6,6,6]
    # Concatenate list of Triangles
triangleList= [triangle1, triangle2, triangle3, triangle4]

# STEP 2. - Generate a list w/ only equilateral triangles

# Using list comprehesion + condition (new list)...
equilateral_List = [x for x in triangleList if x[0] == x[1]== x[2]]

# STEP 3. Calculate areas of equilateral triangles using area f(x) & list comprehension...
area_List = [calc_area(triangles[0]) for triangles in equilateral_List]
print(area_List)