#!/usr/bin/python3


from math import sqrt


class Coordinate:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def set_from_list(self, xyz):
        self.x, self.y, self.z = xyz[0], xyz[1], xyz[2]

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def print(self):
        print(self.x, ' ', self.y, ' ', self.z)

    def equals(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False


class Sphere:
    center = Coordinate()
    radius = 0

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Line:
    begin = Coordinate()
    end   = Coordinate()

    def __init__(self, begin, end):
        self.begin = begin
        self.end   = end

    def get_length(self):
        dx = self.begin.x - self.end.x
        dy = self.begin.y - self.end.y
        dz = self.begin.y - self.end.z
        return sqrt( dx * dx + dy * dy + dz * dz )

#useless
class Vector(Coordinate):

    def __init__(self, end, begin = Coordinate()):
        super().__init__()
        self.x = end.x - begin.x
        self.y = end.y - begin.y
        self.z = end.z - begin.z

    def get_length(self):
        return sqrt( self.x * self.x + self.y * self.y + self.z * self.z )

    def get_cos_of_angle(self, other):
        return self.inner_product(other) / ( self.get_length() * other.get_length() )

    def get_sin_of_angle(self, other):
        return sqrt( 1 - pow(self.get_cos_of_angle(other), 2) )

    def inner_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.get_length() * other.get_length() * self.get_sin_of_angle(other)
