def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) < 2:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
number = input('Введите любое число: ',)
print('Произведение всех цифр числа: ',get_multiplied_digits(number))