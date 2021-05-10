import math


def sum1(values):
    """
    calculates the sum of values(count is sum)
    :param values: list that contains numbers
    :return: the sum
    """
    count = 0
    for i in values:
        count += i
    return count


def mean(values):
    """
    calculate the mean of values
    :param values:list that contains numbers
    :return: the mean
    """
    return sum1(values) / len(values)


def median(values):
    """
    the function calculates the median of values
    if the num of values is even we calculate the mean of the middle values sortes
    else we return the middle
    :param values:list that contains numbers
    :return:
    """
    mid = int(len(values) / 2)
    organized_list = sorted(values)
    if len(values) % 2 != 0:
        return organized_list[math.ceil(mid)]
    else:
        return (organized_list[mid] + organized_list[mid - 1]) / 2