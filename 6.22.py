''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

solution = 0

for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            solution = 1
            print(x, y)

if solution == 0:
    print('No solution')