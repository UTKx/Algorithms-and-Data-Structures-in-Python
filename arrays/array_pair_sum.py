def arsum(lst, sum):
    if len(lst) < 2:
        return "No pairs"

    visited = set()
    out = set()

    for num in lst:
        pair = sum - num

        if pair not in visited:
            visited.add(num)
        else:
            out.add((min(num, pair), max(num, pair)))

    for pairs in out:
        print(pairs)

print(arsum([1,3,2,4,6,-1], 5))