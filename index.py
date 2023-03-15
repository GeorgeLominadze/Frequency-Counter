from collections import Counter

ctr = Counter(input() for i in range(int(input())))
print(len(ctr))
print(*ctr.values())



