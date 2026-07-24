n = int(input())
sum = 0
for i in range(n):
    k = (input())
    z = int(k[-1])
    y = int(k[-z-1:-1])
    x = int(k[:-z-1])
    sum += x**y
print(sum)
