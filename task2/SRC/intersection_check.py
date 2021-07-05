#!/usr/bin/python3


from SRC.geometric_objects import *


def check_intersections(line, sphere):

    dp = Coordinate(
        x = line.end.x - line.begin.x,
        y = line.end.y - line.begin.y,
        z = line.end.z - line.begin.z
    )

    a = dp.x * dp.x + dp.y * dp.y + dp.z * dp.z

    b = 2 * (dp.x * (line.begin.x - sphere.center.x)
           + dp.y * (line.begin.y - sphere.center.y)
           + dp.z * (line.begin.z - sphere.center.z))

    c =  pow(sphere.center.x, 2) \
       + pow(sphere.center.y, 2) \
       + pow(sphere.center.z, 2)

    c += pow(line.begin.x, 2) \
       + pow(line.begin.y, 2) \
       + pow(line.begin.z, 2)

    c -= 2 * (sphere.center.x * line.begin.x
            + sphere.center.y * line.begin.y
            + sphere.center.z * line.begin.z)

    c -= sphere.radius * sphere.radius

    bb4ac = b * b - 4 * a * c
    if bb4ac < 0:
        print('Коллизий не найдено')
        return

    u1 = (-b + sqrt(bb4ac)) / (2 * a)
    u2 = (-b - sqrt(bb4ac)) / (2 * a)

    print(u1, ' ', u2)

    p1 = Coordinate(
        x = line.begin.x + u1 * (line.end.x - line.begin.x),
        y = line.begin.y + u1 * (line.end.y - line.begin.y),
        z = line.begin.z + u1 * (line.end.z - line.begin.z)
    )

    p2 = Coordinate(
        x=line.begin.x + u2 * (line.end.x - line.begin.x),
        y=line.begin.y + u2 * (line.end.y - line.begin.y),
        z=line.begin.z + u2 * (line.end.z - line.begin.z)
    )

    if p1.equals(p2):
        p1.print()
    else:
        p1.print()
        p2.print()

    return