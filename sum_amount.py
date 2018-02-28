result = [50, 10, 5, 1]
for i in range(4):
    result[i] = int(input()) * result[i]
print sum(result)