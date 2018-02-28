result = [500, 100, 50, 10, 5, 1]
deposit = 1000 - int(input())
for i, v in enumerate(result):
    result[i] = deposit // v
    deposit = deposit % v
print ' '.join(map(str, result))