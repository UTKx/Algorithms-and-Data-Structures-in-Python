# Algo 1
def find(lst1, lst2):

    missing = {}

    for item in lst1:
        if item in missing:
            missing[item] += 1
        else:
            missing[item] = 1

    for item in lst2:
        if item in missing:
            missing[item] -= 1
        else:
            missing[item] = 1

    for i in missing:
        if missing[i] == 1:
            return i

print(find([1,2,3,4], [1,4,3]))
print(find([1,2,3,4,5,6,7], [3,7,2,1,4,6]))


# Algo 2
def find2(lst1, lst2):
    
    if len(lst1) == len(lst2):
        return "Both lists are equal."
    
    sum = 0
    for num in lst1:
        sum += num
    for num in lst2:
        sum -= num
    
    return sum

print(find2([1,2,3,4], [1,4,3]))
print(find2([1,2,3,4,5,6,7], [3,7,2,1,4,6]))