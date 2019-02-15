import math

r = float(input("Enter the sphere's radiu: "))
d = r * 2
c = d * math.pi
sa = 4 * math.pi * r * r
v = (4/3) * math.pi * r * r * r

print("Radius = " + str(r))
print("Diameter: " + str(d))
print("Circumference: " + str(c))
print("Surface Area: "+ str(sa))
print("Volume: "+ str(v))