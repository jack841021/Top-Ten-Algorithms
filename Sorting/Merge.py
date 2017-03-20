def merge_sort(l):
    for n in range(0, len(l)-1, 2):
        if l[n] > l[n+1]:
            l[n], l[n+1] = l[n+1], l[n]
    new_l = []
    block = 4
    while block//2 < len(l):
        for left_start in range(0, len(l), block):
            left_counter, rightcounter = 0, 0
            while True:
                left_number = left_start + left_counter
                rightnumber = left_start + block//2 + rightcounter
                try:
                    if l[left_number] < l[rightnumber]:
                        new_l.append(l[left_number])
                        left_counter += 1
                    elif l[left_number] == l[rightnumber]:
                        new_l.append(l[left_number])
                        new_l.append(l[rightnumber])
                        left_counter += 1
                        rightcounter += 1
                    else:
                        new_l.append(l[rightnumber])
                        rightcounter += 1
                except:
                    new_l.extend(l[left_number:left_start+block//2])
                    break
                if left_counter >= block//2 or rightcounter >= block//2:
                    left_number = left_start + left_counter
                    rightnumber = left_start + block//2 + rightcounter
                    if left_counter >= block//2 and rightcounter < block//2:
                        new_l.extend(l[rightnumber:left_start+block])
                        break
                    elif left_counter < block//2 and rightcounter >= block//2:
                        new_l.extend(l[left_number:left_start+block//2])
                        break
                    elif left_counter < block//2 and rightcounter < block//2:
                        new_l.extend(l[rightnumber:left_start+block])
                        new_l.extend(l[left_number:left_start+block//2])
                    else:
                        break
        l = new_l
        new_l = []
        block = block * 2
    return l

import random
test = []
for n in range(10000):
    test.append(random.randint(0,100))
print(merge_sort(test))