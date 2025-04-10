"""
    Name:
    Date:
    Course: COSC-010
    Assignment: Project 1
"""

from turtle import *  # Necessary here at the beginning in order to use Turtle


#  Your code goes here...
begin_fill()
forward (110)
left (120)
forward (110)
left(120)
forward (110)
fillcolor("#041E42") #Use hex for Georgetown Blue #041E42 
end_fill()
print("Georgetown Blue hexidecimal is #041E42")
write("I'm from Springfield, MA", align = "right")
print("Springfield is the home of Basketball and Dr. Suess")

#Part 2 second shape
penup()
goto(-200, -100)
pendown()
setheading(270)
begin_fill()
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
fillcolor("#63666A") #Use hexcode for Georgetown Gray #63666A
end_fill()
print("Georgetown Gray hexidecimal is #63666A")
penup()
goto(-200, -115)
pendown()
write("Lifting as I climb motivates me", align="left")
penup()
goto(-200, -130)
pendown()
write("I'm going: to be an MBA grad in May 2024", align="left")

#Part 3 third shape
#Add shape options below for user to choose
def draw_triangle():
  begin_fill()
  for _ in range(3):
      forward(110)
      left(120)
  fillcolor("#6B8AC8") #Unique color combo with blue, red, and green
  end_fill()

def draw_square():
  begin_fill()
  for _ in range(4):
      forward(100)
      left(90)
  fillcolor("#6B8AC8") #Unique color combo with blue, red, and green
  end_fill()


def draw_circle():
  begin_fill()
  circle(50)
  fillcolor("#6B8AC8") #Unique color combo with blue, red, and green
  end_fill()

# Get the location of shape from the user
location_input = input("Enter the location where you want to draw last shape (x, y) separated by comma: ")
location = tuple(map(float, location_input.split(',')))
# Set the location of the shape
penup()
goto(location)
pendown()
# Get the shape from the user
shape_choice = input("Pick a shape you want to draw out of these three (triangle, square, circle): ").lower()

if shape_choice == "triangle":
  draw_triangle()
elif shape_choice == "square":
  draw_square()
elif shape_choice == "circle":
  draw_circle()
else:
  print("Invalid shape choice")

print("The hexidecimal of my unique color is #6A8AC8")

user_input = input("What is your favorite color?")
print("Your favorite color is", user_input, ", that's a great color!")
print("Thank you for participating in this project!")
done()  # Necessary here so that the picture stays visible
bye()   # Necessary so that the Turtle window exits without crashing

