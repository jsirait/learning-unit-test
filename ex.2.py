var = input("Please enter a value: ")

print(var.upper())
print(len(var))
print(var.isdecimal())

# question 2
from math import pi, tan, cos
g = 9.81
barrel_height = 1
x = 0.5
deg = 80
v0 = 44

theta = deg * pi/180

def projectile(y0, v0, theta, x):
    return y0 + (x * tan(theta) - (g*x*x/(2*((v0*cos(theta))**2))))

print(projectile(barrel_height, v0, theta, x))