a = int(input())
b = int(input())
c = int(input())

if a + b >= c or b + c >= a:
    print("такого треугольника нет")
elif a != b and a != c and b != c:
    print("разносторонний")
elif a == b and a != c or b == c and b != a:
    print("равнобедренный")
else:
    print("равносторонний")