import numpy as np

def check_xchance(x):
    if not (0 <= x < 1):
        raise ValueError(f"Value for parameter xchance ({x}) is out of bounds (must be in [0, 1)).")



def Rigged_RNG(x: int, xchance: float, bound:int):

    """
    Function that returns a random INT but is rigged to make x more likely to be returned.
    :param x: INT you want to rig the RNG for
    :param bound: Upper boundary of RNG, e.g. setting this to 100 will return a random INT between 0 and 100
    :param xchance: Likelihood that the RNG returns x, should be between 0 and 1
    :return: Random INT between 0 and bound, with higher likelihood of returning x
    """

    # check that xchance is indeed between 0 and 1 first
    check_xchance(xchance)

    seed = np.random.rand()

    if seed < xchance:
        numb = x

    else:
        numb = np.random.randint(bound)

    return numb

for i in range(10):
    print(Rigged_RNG(5, 0.75, 10))

# test case for the non-permitted input, will throw error
number = Rigged_RNG(700,1.2,800)
print(number)
