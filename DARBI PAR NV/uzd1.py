from doctest import testmod

def check_cordinates(punkts_x: float, punkts_y: float) -> bool:
    """
    Skatās vai punkti ir figura
    >>> check_cordinates(2, 1)
    Punkt ir robežas figurai
    >>> check_cordinates(1, 0)
    Punkt ir iekšā figūrā
    >>> check_cordinates(4, 0)
    Punkts nav figura 
    >>> check_cordinates(1, 1)
    Punkt ir robežas figurai
    >>> check_cordinates(2, 1)
    Punkt ir robežas figurai
    >>> check_cordinates(2.5, 1.5)
    Punkts nav figura 
    """
# parbauda kur ir punkti 
    if (punkts_y >= -2 and punkts_y <= 1 and (punkts_x == -1 or punkts_x == 3)) or (punkts_x >= -1 and punkts_x <= 3 and (punkts_y == -2 or punkts_y == 1)):
        print("Punkt ir robežas figurai")

    elif punkts_x > -1 and punkts_x < 3 and punkts_y > -2 and punkts_y < 1:
        print("Punkt ir iekšā figūrā")

    else:
        print("Punkts nav figura ")

testmod(verbose=True)

x = float(input("Ieavadi x: "))
y = float(input("Ieavadi y: "))

check_cordinates(x,y)
