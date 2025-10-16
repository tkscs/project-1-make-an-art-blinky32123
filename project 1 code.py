import turtle

def draw_square( num_sides ):
    for i in range(4):
        turtle.left(90)
        turtle.forward(num_sides) #draw square
    

def draw_triangle( number ):
    for i in range(4):
        turtle.left(45)
        turtle.forward(number)
        turtle.left(90)
        turtle.forward(number)
        turtle.right(45) # draw triangles


turtle.screensize() 
turtle.window_width() 
turtle.window_height()

#turtle.exitonclick()

num_sides = 120
# how big the sides
num_half_side = num_sides / 2
# half of the sides length to do the pythagorean theorem
num_triangle_sides = (num_half_side **2 + num_half_side **2 )
# to get number
number = (num_triangle_sides**0.5)
# formula to get the number
print(number)

import turtle
turtle.speed(10)

def shape ( num_sides, number ):
    draw_square( num_sides )
    #for i in range(4):
    #    turtle.left(90)
    #    turtle.forward(num_sides) #draw square
    
    draw_triangle( number )
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


for j in range(8):
    print(2**j)
    shape( num_sides * 2**j, number * 2**j )


turtle.setposition(number/2,number/2) 
turtle.setposition(-number*64, number*64)
turtle.setposition(number/2,number/2)
turtle.setposition(number*64, -number*64)
turtle.setposition(number/2,number/2)
turtle.setposition (-number*64, -number*64)



turtle.exitonclick()