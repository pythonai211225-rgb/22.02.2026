

########################################### FUNCTIONS ###########################################

# letters = ['a', 'b', 'z', 'd']
# name = letters.sort()   # does NOT return values
# name = sorted(letters)  # return values
#
# print(name)

# name = 'danny'.upper()
#
# print(name)
#
# result_3 = len([1,2,3])
# result_401 = max([3, 400, -2, 401])
#
# result = print(3)  # None
#
# a = [1, 4, 10]
#
# result = a.append(12)  # None
# print(result)
#
# result = a.clear()
# print(result)

# def add(a = 1, b = 2) -> None:
#     result = a + b
#     print(result)
#     return None

def add(a: int, b: int) -> int:
    result = a + b
    return result

def add(a: int, b: int) -> int:
    return a + b

add(3, 4)  # does nothing
max([5, 400, -1])  # does nothing
len([5, 400, -1])  # does nothing
min([5, 400, -1])  # does nothing

result = add(3, 4)
print(result)

print(add(3, 4))

# -> [type]  is saying this function is returning a value from type <type>
def mul(a: int, b: int) -> int:
    return a * b

print(mul(22, 333))

def biggest(a: int, b: int, c: int) -> int:
    """
    function biggest returns the biggest of 3 numbers
    :param a: number 1
    :param b: number 2
    :param c: number 3
    :return: the biggest number of a, b, c
    """
    pass

# 5, -2, 30

def smallest(a: int, b: int, c: int) -> int:
    """
    function smallest returns the smallest of 3 numbers
    :param a: number 1
    :param b: number 2
    :param c: number 3
    :return: the smallest number of a, b, c
    """
    pass

# 5, -2, 30