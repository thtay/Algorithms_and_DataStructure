import time
import timeit


def sumOfN(n):
    theSum = 0
    for i in range(1, n + 1):
        theSum += i
    return theSum


print(sumOfN(10))


def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1, n + 1):
        theSum += 1
    end = time.time()

    return theSum, end - start


#
# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sumOfN2(10000000))


def sumOfN3(n):
    """
    Using the mathamatical expression (n*(n+1)/2) to evaluate the answer
    in liue of brute force
    """
    start = time.time()
    result = n * (n * +1) / 2
    end = time.time()
    return result, end - start


# print("\n")
# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sumOfN3(10000000))


"""
Self check exercise.
Write two Python functions to find the minimum number in a list. The first function
should compare each number to every other number on the list O(n^2). The second function
should be linear O(n).
"""


def find_min1(numbers):
    """
    Return the minimum value in a given list with O(n)
    :param numbers:
    :return:
    """
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min


l = [1, 2, 3, 4, 100000, -8989]
print("The min of {} is: {}".format(l, find_min1(l)))

from collections import Counter


def anagramSolution1(s1, s2):
    s1_count = Counter(s1)
    s2_count = Counter(s2)

    if len(s1_count) != len(s2_count):
        return False
    # Add some comments
    for s1c in s1_count:
        if s1_count[s1c] != s2_count[s1c]:
            return False
    return True


print(anagramSolution1("heart", "earth"))
print(anagramSolution1("heart", "easth"))