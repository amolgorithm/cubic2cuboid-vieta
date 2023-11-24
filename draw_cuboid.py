import turtle
import time


def draw(dimensions):
	# Creating  window screen 
	tut = turtle.Screen() 

	# Setting background color to light green
	tut.bgcolor("lightgreen") 

	# window title
	tut.title("Drawing of Cuboid (Rectangular Prism)") 
	my_pen = turtle.Turtle() 
	
	# setting pen thickness to 3 px
	my_pen.width(3)

	# setting pen color to black
	my_pen.color("black") 
	
	tut = turtle.Screen()
	
	# dimensions is a tuple with three values; doing this, we can access each value as an individual variable.
	length, height, width = dimensions

	# drawing front rectangle face 
	for i in range(2): 
		my_pen.forward(width) 
		my_pen.left(90) 
		my_pen.forward(height) 
		my_pen.left(90) 


	# bottom left side 
	my_pen.goto(length/2, length/2) 

	# drawing back rectangle face 
	for i in range(2): 
		my_pen.forward(width) 
		my_pen.left(90) 
		my_pen.forward(height) 
		my_pen.left(90) 

	# drawing bottom right side 
	my_pen.goto(length/2 + width, length/2) 
	my_pen.goto(width, 0) 


	# drawing top right side 
	my_pen.goto(width,height) 
	my_pen.goto(width + length/2, height + length/2) 


	# drawing top left side 
	my_pen.goto(length/2, height + length/2) 
	my_pen.goto(0, height)
	
	my_pen.width(1)
	
	my_pen.goto(width + length/2, length/2)
	
	length_scale_factor = 37.795275591
	
	turtle.setposition(0, -150)
	turtle.write(f"Length = {round(length/length_scale_factor, 3)}\nHeight = {round(height/length_scale_factor, 3)}\nWidth = {round(width/length_scale_factor, 3)}\nVolume = {round((length/length_scale_factor)*(width/length_scale_factor)*(height/length_scale_factor), 3)}", move = False, font=("Arial", 18, "normal"), align="right")

	# Sustaining window (commanding it to not close automatically)
	turtle.done()
