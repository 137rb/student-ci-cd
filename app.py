def add(lst):
    total = 0
    for value in lst:
        if value % 2 == 0:
            total += value ** 2
        else:
            total += value ** 3
    return total

import random
if __name__ == "__main__":
    list1 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
    print(add(list1))
