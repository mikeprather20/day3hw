#Create a Module in VS Code and Import It into jupyter notebook
#>Module should have the following capabilities:
#1) Has a function to calculate the square footage of a house
#Reminder of Formula: Length X Width == Area
#2) Has a function to calculate the circumference of a circle
#Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

def myStuff():
    return "this is my stuff"
#^this is a module

def squarefoot(length,width):
    length=input("Length:")
    width=input("Width:")
    area = (length) * (width)
    return(int(area))

squarefoot()



#c=pi*d
def circleCircum(dia):
    from math import pi
    dia = input("Diameter")
    circumference = pi * int(dia)
    return(circumference)

circleCircum()