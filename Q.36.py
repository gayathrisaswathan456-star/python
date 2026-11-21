class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

#calculate area:
    def area(self):
        return self.__length * self.__breadth 
#overload < operator
    def __lt__(self, other):
     return self.area() < other.area()

#create objects
r1 = Rectangle(10,5)
r2 = Rectangle(8,6)

#display area
print("Rectangle 1:", r1.area())
print("Rectangle 2:", r2.area())

#compare area
if r1 < r2:
    print("Rectangle 1 has smaller area")
elif r2 < r1:
    print("Rectangle 2 has smaller area")
else:
    print("Both rectangles have equal area")