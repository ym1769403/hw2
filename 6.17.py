word = input()
password = ''

for x in word:
    if x == 'i':
        password = password + '!'
    elif x == 'a':
        password = password + '@'
    elif x == 'm':
        password = password + 'M'
    elif x == 'B':
        password = password +'8'
    elif x == 'o':
        password = password + '.'
    else:
        password = password + x
password = password + 'q*s'
print(password)