import numpy as np
print("Hello World!")

def Rigged_RNG(x, xchance, bound):

    """
    Function that returns a random INT but is rigged to make x more likely to be returned.
    :param x: INT you want to rig the RNG for
    :param bound: Upper boundary of RNG, e.g. setting this to 100 will return a random INT between 0 and 100
    :param xchance: Likelihood that the RNG returns x, should be between 0 and 1
    :return: Random INT between 0 and bound, with higher likelihood of returning x
    """

    seed = np.random.rand()

    if seed < xchance:
        numb = x

    else:
        numb = np.random.randint(bound)

    return numb
