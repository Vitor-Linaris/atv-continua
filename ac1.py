import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())

print("i)", round(((((a*a)+(3*b))/c)+d), 4))

print("ii)", round(math.log10(a)+(math.e**(-b/c))-((d*d)/math.pi), 4))

print("iii)", round(((((a*a)**(1/3))*(b**(1/3)))+(c*d))/(a+b+c+d) ,4))

print("iv)", round(((a+b)*(c+d))/(a*b*c*d) ,4))

print("v)", round((((a*a)+(b*b))/(c*d))-(((c*c)+(d*d))/(a*b)) ,4))

print("vi)", round((a+b+c+d)*(a+b+c+d) ,4))

print("vii)", round(((a*a)+(b*b)+(c*c)+(d*d)) ,4))

print("viii)", round((a*b*c*d)**(1/3) ,4))

