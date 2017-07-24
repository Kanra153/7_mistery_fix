from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return -b/2*a
    elif discriminant>0:
        return root1, root2
    else:
        return None, None
