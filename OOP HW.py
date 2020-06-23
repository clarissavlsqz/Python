class Line:
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2
    
    def distance (self):
        return ((self.coord2[0] - self.coord1[0]) ** 2 + (self.coord2[1] - self.coord1[1]) ** 2) ** 0.5
    
    def slope (self):
        return (self.coord2[1] - self.coord1[1]) / (self.coord2[0] - self.coord1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print("The distance of the line is {}".format(li.distance()))

print("The slope of the line is {}".format(li.slope()))

class Cylinder:
    pi = 3.14

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.height
    
    def surface_area(self):
        return (2 * Cylinder.pi * (self.radius ** 2)) + (2 * Cylinder.pi * self.radius * self.height)

c = Cylinder(2,3)

print("The volume of the cylinder is {}".format(c.volume()))
print("The surface area of the cylinder is {}".format(c.surface_area()))