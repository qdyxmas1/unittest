

def is_convex(polygon):
    try:
        if polygon.geom_type != "Polygon":
            raise ValueError("input is not a polygon")
    except AttributeError:
            raise ValueError("input is not a shapely object")

    coords = list(polygon.exterior.coords)
    n = len(coords) 

    # 局部优化
    if n == 4:
        return True

    # https://stackoverflow.com/questions/471962/how-do-i-efficiently-determine-if-a-polygon-is-convex-non-convex-or-complex
    return polygon.convex_hull.area == polygon.area
    # sign = False;
    # for i in range(n):
        # dx1 = coords[ (i + 2) % n ][0] - coords[ (i + 1) % n ][0]
        # dy1 = coords[ (i + 2) % n ][1] - coords[ (i + 1) % n ][1]
        # dx2 = coords[i][0] - coords[ (i + 1) % n ][0]
        # dy2 = coords[i][1] - coords[ (i + 1) % n ][1]
        # zcrossproduct = dx1 * dy2 - dy1 * dx2

        # if i == 0:
            # sign = zcrossproduct > 0
        # elif sign != (zcrossproduct > 0):
            # return False

    return True;

