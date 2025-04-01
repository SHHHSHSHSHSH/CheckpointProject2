import math


Answer1 = int(input("==================\nArea Calculator\n==================\n1)\tSquare\n2)\tRectangle\n3)\tTriangle\n4)\tCircle\n5)\tQuit"))
if Answer1 == 1:
    side = int(input("Give me the size of a side in cm"))
    print("The area is" , (side ** 2) )
elif Answer1 == 2:
    length = int(input("Lenght?"))
    width = int(input("Width?"))
    print("The area is", (length * width))
elif Answer1 == 3:
    height = int(input("Height?"))
    base = int(input("Base?"))
    print("The area is", ((height * base) / 2 ))
elif Answer1 == 4:
    radius = int(input("Radius?"))
    print("The area is", ((radius ** 2) * math.pi))
else:
    Goodbye
