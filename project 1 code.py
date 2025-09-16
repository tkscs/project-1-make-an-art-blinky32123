import turtle

#for i in range(4):
  #  turtle.forward(100)
 #   turtle.left(90)
#for i in range(4):
    #turtle.right(45)
    #turtle.forward(70.72)
   # turtle.left(90)
  #  turtle.forward(70.72)
 #   turtle.left(45)
#turtle.right(45)
#turtle.forward(70.71)
#turtle.left(45)
#turtle.forward(100)
#for i in range(4):
    #turtle.left(90)
   # turtle.forward(200)




#turtle.exitonclick()


num_sides = 45
num_half_side = num_sides / 2
num_triangle_sides = (num_half_side **2 + num_half_side **2 )
number = (num_triangle_sides**0.5)
print(number)
#num_triangle_sides = 70.72
#((2* (num_sides / 2)^2))
import turtle
turtle.speed(5)
for i in range(4):
    turtle.forward(num_sides)
    turtle.left(90)
for i in range(4):
    turtle.right(45)
    turtle.forward(number)
    turtle.left(90)
    turtle.forward(number)
    turtle.left(45)
turtle.right(45)
turtle.forward(number)
turtle.left(45)
turtle.forward(num_sides)
for i in range(4):
        turtle.left(90)
        turtle.forward(num_sides * 2)

for i in range(4):
    turtle.left(45)
    turtle.forward(number*2)
    turtle.left(90)
    turtle.forward(number*2)
    turtle.right(45)
turtle.left(45)
turtle.forward(number*2)
turtle.left(45)
turtle.forward(num_sides*2)
for i in range(4):
        turtle.left(90)
        turtle.forward(num_sides * 4)

for i in range(4):
    turtle.left(45)
    turtle.forward(number*4)
    turtle.left(90)
    turtle.forward(number*4)
    turtle.right(45)
turtle.left(45)
turtle.forward(number*4)
turtle.left(45)
turtle.forward(num_sides*4)
for i in range(4):
        turtle.left(90)
        turtle.forward(num_sides*8)



turtle.exitonclick()