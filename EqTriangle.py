s3 = sqrt(3)
s32 = sqrt(3) * 0.5

SHRINK_FACTOR = 0.9
ATTEMPTS = 10

def polarVertex(r, th):
    vertex(r * sin(th), r * cos(th))

def drawPolygon(x, y, sides, r, aofs):
    pushMatrix()
    translate(x, y)
    rotate(aofs)
    beginShape()
    for i in range(sides):
        polarVertex(r, i * TWO_PI / float(sides))
    endShape(CLOSE)
    popMatrix()

def random_triangle_coord(base):
    x = random(0.5 * base)
    y = random(s32 * base)
    if y > x * s3:
        x = base * 0.5 + x
        y = base * s32 - y
    return x, y

a3 = atan(3)

def tan_random_sides():
    return int(tan(random(a3, HALF_PI)))

def touches(x1, y1, x2, y2, r1, r2):
    return dist(x1, y1, x2, y2) < (r1 + r2)

class EqTriangle(object):
    def __init__(self, base, n):
        self.base = float(base)
        self.max_rad = self.base / 8.0
        self.n = n
        self.randomise()

    def randomise(self):
        self.shapes = []
        for _ in xrange(self.n):
            self._add_shape()

    def _add_shape(self, attemps=ATTEMPTS):
        sides, c, r, (x, y), aofs = (tan_random_sides(),
                                         random(255),
                                         random(self.max_rad / 2.0, self.max_rad),
                                         random_triangle_coord(self.base),
                                         random(TWO_PI))

        if not any(touches(x, y, _x, _y, r, _r) for _sides, _c, _r, _x, _y, _aofs in self.shapes):
            self.shapes.append((sides, c, r, x, y, aofs))
        else:
            if attemps:
                self._add_shape(attemps - 1)
            else:
                self.max_rad *= SHRINK_FACTOR
                self._add_shape()
    
    def draw(self):
        noStroke()
        for sides, c, r, x, y, aofs in self.shapes:
            fill(c, 255, 255)
            drawPolygon(x, y, sides, r, aofs)
    
    def __str__(self):
        return ("{{base: {},\n shapes: [".format(self.base)
              + ",\n          ".join("{{sides: {}, colour: {}, r: {}, x: {}, y: {}, angle: {}}}".format(*shape_) for shape_ in self.shapes)
              + "\n         ]\n}")