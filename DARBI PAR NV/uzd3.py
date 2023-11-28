import doctest

def check_cordinates(punkts_x : float, punkts_y : float) -> bool:
    '''

    >>> check_cordinates(0,0)
    Punkt ir robežas figurai
    >>> check_cordinates(1,-1)
    Punkts nav figura
    >>> check_cordinates(0.2,-0.9)
    Punkts nav figura
    >>> check_cordinates(-1, 4)
    Punkt ir robežas figurai
    >>> check_cordinates(-3, 0.6)
    Punkts nav figura
    >>> check_cordinates(1.5, 0.9)
    Punkts nav figura
    >>> check_cordinates(0, -1)
    Punkts nav figura
    >>> check_cordinates(0.2, 2.7)
    Punkt ir robežas figurai
    >>> check_cordinates(1, 1.5)
    Punkt ir robežas figurai
    >>> check_cordinates(0.7, 1.95)
    Punkt ir robežas figurai
    >>> check_cordinates(0.3, 2.55)
    Punkt ir robežas figurai
    >>> check_cordinates(-1, 4.5)
    Punkt ir robežas figurai
    >>> check_cordinates(-0.6, 3.9)
    Punkt ir robežas figurai
    >>> check_cordinates(2, 3)
    Punkts nav figura
    >>> check_cordinates(-0.1, 3.1)
    Punkt ir iekšā figūrā
    '''

    if ((punkts_x == -1 and 0 <= punkts_y <= 4.5) or (punkts_y == 0 and -1 <= punkts_x <= 2) or (punkts_y + 1.5 * punkts_x - 3 == 0)):
         print("Punkt ir robežas figurai")
    elif -1 < punkts_x < 2 and 0 < punkts_y < 4.5 and (punkts_y + 1.5 * punkts_x - 3) < 0:
        print("Punkt ir iekšā figūrā")
    else:
        print("Punkts nav figura")


doctest.testmod(verbose=True)

x = float(input("Ievadi x:"))
y = float(input("Ievadi y:"))
check_cordinates(x, y)
