import time, sys


def getNumberOfDigits(number1, count =0):
    if number1<10:
        return count+1
    return getNumberOfDigits(number1//10, count+1)



def getRandomInteger(lower, upper):
    """

    :param lower: take lower bound of the range
    :param upper: take upper bound of the range
    :return: an integer in the range
    """
    t = time.time()
    t = t-int(t)
    num = t * 10 ** (getNumberOfDigits(upper))
    if num >= upper:
        num = num//10
    if num < lower:
        num = (lower | int(num))
    return int(num)

lower = 500
upper = 657
for iter in range(100000):
    var = getRandomInteger(lower, upper)
    if (var < lower or var > upper):
        print(var)