list= [15, 48, 'hello', 6, 19, 'word']
for i in (15, 48, 6, 19):
    if i % 2 == 0:
        print(i)
n = 48
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n //10
print(sum)

for i1 in (15, 48, 6, 19):
    if i1 % 2 != 0:
        print(i1)

ind1 = list.index(15)
ind2 = list.index(19)
print("индекс числа 1",ind1, "индекс числа 2", ind2)
list.insert(0,1)
list.insert(4,1)
print(list)

a = ("hello world")
gl = 0
sogl = 0
for i in a:
    letter = i.lower()
    if letter == "a" or letter == "e" or letter == "o" or letter == "u":
        gl += 1

    else:
        sogl += 1
print("гласных", gl, "согласных", sogl)


