first = int(input('First: '))
second = int(input('Second: '))
third = int(input('Third: '))
if first == second == third:
    print('Number: 3')
elif first == second or second == third or first == third:
    print('Number: 2')
else:
    print('Number: 0')