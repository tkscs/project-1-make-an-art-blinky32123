import turtle
turtle.speed(10)

def draw_square(num_sides):
    for i in range(4):
        turtle.left(90)
        turtle.forward(num_sides)
    
def draw_triangle(number):
    for i in range(4):
        turtle.left(45)
        turtle.forward(number)
        turtle.left(90)
        turtle.forward(number)
        turtle.right(45) 

num_sides = 10.5 # side length of square
num_half_side = num_sides / 2 
num_triangle_sides = (num_half_side **2 + num_half_side **2 )
number = (num_triangle_sides**0.5) # hypotenuse of triangle
print(number)

def shape (num_sides, number):
    draw_square( num_sides )
    #for i in range(4):
    #    turtle.left(90)
    #    turtle.forward(num_sides) #draw square
    
    draw_triangle(number)
    #for i in range(4):
    #    turtle.left(45)
    #    turtle.forward(number)
    #    turtle.left(90)
    #    turtle.forward(number)
    #    turtle.right(45) # draw triangles
    turtle.left(45)
    turtle.forward(number) 
    turtle.left(45)
    turtle.forward(num_sides)

g=6
for j in range(g):
    print(2**j)
    shape(num_sides * 2**j, number * 2**j)
draw_square(num_sides*2**g)




turtle.exitonclick()