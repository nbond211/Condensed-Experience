colors = dict((
    ((196, 2, 51), "RED"),
    ((255, 165, 0), "ORANGE"),
    ((255, 205, 0), "YELLOW"),
    ((0, 128, 0), "GREEN"),
    ((0, 0, 255), "BLUE"),
    ((127, 0, 255), "VIOLET"),
    ((0, 0, 0), "BLACK"),
    ((255, 255, 255), "WHITE"),))


def rgb_to_ycc(r, g, b):  # http://bit.ly/1blFUsF
    y = .299 * r + .587 * g + .114 * b
    cb = 128 - .168736 * r - .331364 * g + .5 * b
    cr = 128 + .5 * r - .418688 * g - .081312 * b
    return y, cb, cr


def to_ycc(color):
    """ converts color tuples to floats and then to yuv """
    return rgb_to_ycc(*[x / 255.0 for x in color])


def color_dist(c1, c2):
    """ returns the squared euklidian distance between two color vectors in yuv space """
    return sum((a - b) ** 2 for a, b in zip(to_ycc(c1), to_ycc(c2)))


def min_color_diff(color_to_match):
    print min(  # overal best is the best match to any color:
        (color_dist(color_to_match, test), colors[test])  # (distance to `test` color, color name)
        for test in colors)
    """ returns the `(distance, color_name)` with the minimal distance to `colors`"""
    return min(  # overal best is the best match to any color:
        (color_dist(color_to_match, test), colors[test])  # (distance to `test` color, color name)
        for test in colors)
