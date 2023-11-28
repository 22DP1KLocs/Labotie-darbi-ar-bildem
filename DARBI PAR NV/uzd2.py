from doctest import testmod

def check_cordinates(punkts_x : float, punkts_y : float) -> bool:
    """
    Skatās vai punkti ir figura
    >>> check_cordinates(2, 1)
    Punkt ir robežas figurai
    >>> check_cordinates(1, 0)
    Punkt ir iekšā figūrā
    >>> check_cordinates(4, 0)
    Punkts nav figura 
    """
# parbauda kur ir punkti 
    if (punkts_y >= -1 and punkts_y <= 3  and (punkts_x == -5 or punkts_x == 2)) or (punkts_x >= -5 and punkts_x <= 2 and (punkts_y == -1 or punkts_y == 3)):
        print("Punkt ir robežas figurai")

    elif punkts_x > -5 and punkts_x < 2 and punkts_y > -1 and punkts_y < 3:
        print("Punkt ir iekšā figūrā")

    else:
        print("Punkts nav figura ")
testmod(verbose=True)

x = float(input("Ieavadi x: "))
y = float(input("Ieavadi y: "))

check_cordinates(x,y)
