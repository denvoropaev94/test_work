import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1.distance(p2))
print(p1.get_coordinates())
p1.set_coordinates(3, 3)
print(p1.get_coordinates()) 
