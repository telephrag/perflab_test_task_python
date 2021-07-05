#!/usr/bin/python3


from SRC.geometric_objects import Sphere, Line, Coordinate


sphere_str = "sphere"
line_str   = "line"
center_str = "center"
radius_str = "radius"


def parse_line(data):
    line_init = data.find(line_str)
    temp = data[line_init:]

    line_begin = temp.find('{')
    temp = temp[line_begin:]

    line_end = temp.find('}') + 1
    temp = temp[:line_end]

    cords = parse_coordinates(temp)

    return Line(cords[0], cords[1])


def parse_sphere(data):
    sphere_init = data.find(sphere_str)
    temp = data[sphere_init:]

    sphere_begin = temp.find('{')
    temp = temp[sphere_begin:]

    sphere_end = temp.find('}') + 1
    temp = temp[:sphere_end]

    center = parse_coordinates(temp)[0]
    radius = parse_radius(temp)

    return Sphere(center, radius)


def parse_coordinates(data):
    cords = []

    while data.find('[') != -1:
        begin = data.find('[')
        end = data.find(']') + 1

        num, xyz = '', []

        for i in range(begin, end):
            if data[i].isnumeric() or data[i] == '.' or data[i] == '-':
                num = num + data[i]
            elif data[i] == ',':
                xyz.append(float(num))
                num = ''
            elif data[i] == ']':
                xyz.append(float(num))
                cords.append(Coordinate(xyz[0], xyz[1], xyz[2]))
                num, xyz = '', []

        data = data[end + 1:]

    return cords


def parse_radius(data):

    bracket_left = data.find('[')
    first_numeric = [char.isdigit() for char in data].index(True)

    num = ''
    if first_numeric < bracket_left:
        for i in range(first_numeric, bracket_left):
            if data[i].isnumeric() or data[i] == '.':
                num += data[i]
    else:
        bracket_right = data.find(']')
        for i in range(bracket_right, len(data) - 1):
            if data[i].isnumeric() or data[i] == '.':
                num += data[i]

    return float(num)


def parse_file(filename):

    file = open(filename, "r", 1)
    data = file.read()

    return parse_sphere(data), parse_line(data)
