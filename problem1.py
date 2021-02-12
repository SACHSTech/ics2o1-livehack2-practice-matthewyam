#This is the title
print("Right Angle Triangle Vertifyer")
print(" ")

#This is where the user inputs their data
first = int(input("Enter first side number: "))
second = int(input("Enter second side number: "))
third = int(input("Enter third side number: "))

#This is the math equation
triangle = first**2+second**2
right = third**2

#This is to determin if the triangle is a right angle triangle
print(" ")
if triangle == right:
  print("This is a right angle triangle")

else:
  print("This is not a right angle triangle")