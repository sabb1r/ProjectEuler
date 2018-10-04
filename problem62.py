# Created by Sabbir Ahmed @ September 3, 2018

import math

for digit_len in range(6, 15):
    stack = {}
    num = math.ceil((10 ** (digit_len-1)) ** (1/float(3)))
    cubed_num = str(num ** 3)

    while len(cubed_num) == digit_len:
        stack[num] = sorted(cubed_num)
        num += 1
        cubed_num = str(num ** 3)

    cubes = list(stack.values())

    for cube in cubes:
        occurance = cubes.count(cube)
        if occurance == 5:
            break
    else:
        continue

    match = [k for k,v in stack.items() if v == cube]
    print('The result is =', match[0] ** 3)
    break
    




