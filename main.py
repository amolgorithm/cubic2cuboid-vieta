import math
import time
import draw_cuboid #personal module


# user inputs coefficients and constant of cubic equation
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
d = int(input("Enter constant d: "))

# This calculation helps to determine if a cubic equation has at least one complex root.
discriminant = (b**2) * (c**2) - 4*a*(c**3) - 4 * (b**3) * d - 27*(a**2)*(d**2) + 18*a*b*c*d

# If the discriminant is less than or equal to zero, then the cubic equation has at least one complex root.
# All roots must be real to be edge lengths of a prism.
if discriminant <= 0:
	print("\nGiven cubic equation has at least one complex root! All roots must be real to be edge lengths of a prism.")
	exit() #As this is invalid scenario, the program ends here by exiting.


# Derived using Vieta's formulas
volume = -d/a
surface_area = 2*c/a
diagonal_square = (-b/a)**2 - 2*c/a


# Checks if each of Volume, Surface Area and the square of the space diagonal are non-negative, which they cannot be.
# - Volume cannot be negative as it is a measurement
# - Surface Area, again, cannot be negative as it is a measurement
# - Square of the length of the diagonal cannot be negative, as the square root of it will be imaginary, but the length of the diagonal must be real.
for geo_property_pair in [("Volume", volume), ("Surface Area", surface_area), ("Length of Diagonal Squared", diagonal_square)]:
	if geo_property_pair[1] < 0:
		print(f"{geo_property_pair[0]} is a negative value!")
		exit()

diagonal_length = math.sqrt(diagonal_square)

print("\nThe volume of the rectangular prism:", volume, "cm^3")
print("The surface area of the rectangular prism:", surface_area, "cm^2")
print("The length of the space diagonal:", diagonal_length, "cm")

print(f"\nRatio of surface areas of the prism and of a sphere with same volume (approx.): {surface_area} / {round(4*(((0.75*volume)/math.pi)**(1/3))**2, 3)}*π")
print(f"Ratio of volumes of the prism and of a sphere with same surface area (approx.): {volume} / {round((4/3)*math.pi*math.sqrt(volume/(4*math.pi))**3, 3)}")
print(f"Ratio of space diagonal length to radius of sphere with same volume as prism (approx.): {round(diagonal_length, 3)}/{round(((0.75*volume)/math.pi)**(1/3), 3)}")

time.sleep(1) #creates one second pause

draw_cuboid_consent = str(input("\nWould you like to find the roots to draw the prism? (Y/n): "))

if draw_cuboid_consent == "Y":
	import numpy as np
	roots = np.roots([a, b, c, d])

	for root in roots:
		if isinstance(root, complex):
			print("\nCubic equation has complex root(s)! Cannot be plotted on 3D Cartesian grid!")
			exit()
	
	#approx. no. of pixels per inch for average computer
	length_scale_factor = 38
	
	draw_cuboid.draw(tuple([root*length_scale_factor for root in roots]))

