import math
import doctest

def check_cordinates(punkts_x : float, punkts_y : float) -> bool:
    """
    >>> check_cordinates(0, 0)
    Punkt ir iekšā figūrā
    >>> check_cordinates(1, 1) 
    Punkts nav figura
    >>> check_cordinates(1, 0)
    Punkt ir robežas figurai
    >>> check_cordinates(0.5, 0.8660254037844386)
    Punkt ir iekšā figūrā
    >>> check_cordinates(-0.5, -0.8660254037844386)
    Punkt ir iekšā figūrā
    >>> check_cordinates(0.3, 0.9539392014169456)
    Punkt ir iekšā figūrā
    >>> check_cordinates(-0.3, 0.9539392014169456)
    Punkt ir iekšā figūrā
    >>> check_cordinates(-0.3, -0.9539392014169456)
    Punkt ir iekšā figūrā
    """

    l, k = 0, 0  
    radius = 1   
#  parbuada distanci
    distance = math.sqrt((punkts_x - l)**2 + (punkts_y - k)**2)
# parbauda vai kur ir punkti
    if distance == radius:
        print("Punkt ir robežas figurai")
    elif distance < radius:
        print("Punkt ir iekšā figūrā")
    else:
        print("Punkts nav figura")
    
doctest.testmod(verbose=True)

x = float(input("Ievadi x:"))
y = float(input("Ievadi y:"))
check_cordinates(x, y)