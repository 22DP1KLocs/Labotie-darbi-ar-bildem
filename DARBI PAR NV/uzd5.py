import doctest

def check_cordinates(punkts_x: float, punkts_y: float) -> bool:
    """
    parbaud vai punkti ir iekšā.

    >>> check_cordinates(-4, 4)
    Punkt ir robežas figurai
    >>> check_cordinates(-3, 6)
    Punkt ir iekšā figūrā
    >>> check_cordinates(0, 0)
    Punkts nav figura
    >>> check_cordinates(4, 8)
    Punkt ir robežas figurai
    >>> check_cordinates(-3.4, 5)
    Punkt ir iekšā figūrā
    >>> check_cordinates(4, 5)
    Punkt ir iekšā figūrā
    >>> check_cordinates(6, 4)
    Punkt ir robežas figurai
    >>> check_cordinates(-4, 7)
    Punkts nav figura
    >>> check_cordinates(6, 6)
    Punkts nav figura
    """
# parbauda uz kuras trapeces malas atrodas punkti
    if (punkts_y == 4 and punkts_x >= -4 and punkts_x < 8.3 or 
        punkts_y == 8 and punkts_x >= -2.9 and punkts_x <= 4) or\
        round(punkts_y,4) == round(6/1.1*punkts_x + 26.2/1.1,4 ) or\
        round(punkts_y,4) == round(-6/4.3*punkts_x + 58.4/4.3 ,4):
        print ('Punkt ir robežas figurai')
    elif punkts_x > -4 and punkts_x < 8.3 and punkts_y > 4 and punkts_y < 8 and round(punkts_y,4) < round(6/1.1*punkts_x + 26.2/1.1 ,4) and round(punkts_y,4) < round(-6/4.3*punkts_x + 58.4/4.3 ,4):
        print('Punkt ir iekšā figūrā')
    else:
        print('Punkts nav figura')


doctest.testmod(verbose=True)

x = float(input("Ievadi x:"))

y = float(input("Ievadi y:"))

check_cordinates(x, y)

