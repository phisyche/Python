def koch(t, order, size):
    """
    Make turtle t draw a Koch fractal of 'order' and 'size'.
    Leave he turtle facing the same direction.
    """

    if order == 0:
        t.forward(size)
    else:
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)
            return koch()
