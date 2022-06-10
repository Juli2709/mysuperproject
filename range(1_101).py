
a = [i for i in range(1, 101)]
b = 1
for x in a:
    if x % 2 == 0:
        b = b*x
print(b)