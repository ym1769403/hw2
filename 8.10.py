my_str = input()
s_str = my_str.replace(" ", "")
reverse_str = reversed(s_str)

if list(s_str) == list(reverse_str):
    print(my_str,'is a palindrome')
else:
    print(my_str,'is not a palindrome')