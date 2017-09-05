from EqTriangle import s3, s32

def triangle_tiling(base, tri):
    pushMatrix()
    for rot in range(6):
        for x in range(2 + int(width // (base * 1.5))):
            for y in range(2 + int(height // (base * 2))):
                yield
                pushMatrix()
                if x & 1:
                    translate(x * base * 1.5, (y + 0.5) * base * s3)
                else:
                    translate(x * base * 1.5, y * base * s3)
                if rot & 1:
                    rotate(TWO_PI / 6.0 * (rot + 1))
                    scale(1, -1)
                else:
                    rotate(TWO_PI / 6.0 * rot)
                tri()
                popMatrix()
    popMatrix()