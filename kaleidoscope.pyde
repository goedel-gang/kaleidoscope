from datetime import datetime

from EqTriangle import EqTriangle
from triangle_tiling import triangle_tiling

TRI_BASE = 100
SHAPES = 50

def setup():
    global tri, draw_gen, cont
    size(1600, 800)
    tri = EqTriangle(TRI_BASE, SHAPES)
    background(0)
    colorMode(HSB, 255, 255, 255)
    draw_gen = triangle_tiling(TRI_BASE, tri.draw)
    cont = True

def draw():
    global cont
    if cont:
        try:
            next(draw_gen)
        except StopIteration:
            cont = False

def keyPressed():
    if keyCode == ord(' '):
        setup()
    elif keyCode == ord('S'):
        stamp = datetime.now().strftime("data/%H:%M:%S-%d-%m-%Y")
        with open(stamp + ".txt", "w") as ser_file:
            ser_file.write(str(tri))
        save(stamp + ".tiff")
        print("saved")