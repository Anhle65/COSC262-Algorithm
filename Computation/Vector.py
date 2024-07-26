import re
from sympy import false


class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    def __mul__(self, scale):
        return Vec(self.x * scale, self.y * scale)
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    def lensq(self):
        return self.dot(self)
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
    
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_on_segment(p, a, b):
    area = signed_area(p, a, b)
    if area == 0:
        length = (b - a).lensq()
        if (p-a).lensq() <= length and (p-b).lensq() <= length:
            return True
    return False

def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0

def classify_points(line_start, line_end, points):
    on_left = 0
    on_right = 0
    for point in points:
        ccl = is_ccw(line_start, line_end, point)
        if ccl is False:
            on_right += 1
        else:
            on_left += 1
    return (on_right, on_left)

def intersecting(a, b, c, d):
    area1 = signed_area(a,b,c)
    area2 = signed_area(a,b,d)
    if(area1 == 0 or area2 == 0):
        return True
    condition_1 = is_ccw(a,d,b) != is_ccw(a,c,b)
    condition_2 = is_ccw(c,a,d) != is_ccw(c,b,d)
    if(condition_1 and condition_2):
        return True
    return False

def is_strictly_convex(vertices):
    for i in range(0, len(vertices)):
        if(is_ccw(vertices[i], vertices[(i+1)%len(vertices)], vertices[(i+2) % len(vertices)]) == False):
            return False
    return True


verts = [
    (0, 0),
    (100, 0),
    (0, 100),
    (1, 50)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))