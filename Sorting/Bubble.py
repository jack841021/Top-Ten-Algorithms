def bubble_sort(x):
    while True:
        counter = 0
        for bubble in range(len(x) - 1):
            if x[bubble] > x[bubble + 1]:
                x[bubble], x[bubble + 1] = x[bubble + 1], x[bubble]
                counter = counter + 1
        if counter == 0:
            return x

import random
test = []
for n in range(100):
    test.append(random.randint(0,99))
print(bubble_sort(test))