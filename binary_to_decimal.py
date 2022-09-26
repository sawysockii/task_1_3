def only_binary_in_string(input_string):
    is_binary = 1
    if len(str(input_string)) > 0:
        for char_i in str(input_string):
            if ((char_i == '1') or (char_i == '0')):
                is_binary *= 1
            else:
                is_binary *= 0
        if is_binary == 1:
            return(True)
        else:
            return(False)
    else:
        return(False)

def binary_to_decimal(input_number):
    decimal = 0
    for i in range(0,len(input_number)):
        decimal += int(input_number[i])*2**(len(input_number) - 1 - i)
    return(decimal)

run = True
while run:
    first_binary = input('Введите первое двоичное число: ')
    second_binary = input('Введите второе двоичное число: ')
    if (only_binary_in_string(first_binary) and only_binary_in_string(second_binary)):
        result_decimal = binary_to_decimal(first_binary) * binary_to_decimal(second_binary)
        # degree = 0 
        # result_ = result_decimal
        # while result_ > 1:
        #     result_ /= 2
        #     degree += 1 # зачем-то мы дополнительно выяснили степень двойки старшего разряда. это вообще не требовалось...
        result_binary_string = ''
        remains = result_decimal
        while ((remains//2 >= 1) or (remains%2 >= 1)):
            result_binary_string += str(remains%2)
            remains //= 2
        print('Результат умножения: ', result_binary_string[::-1])
    elif ((first_binary == 'exit' or first_binary == 'quit') or (second_binary == 'exit' or second_binary == 'quit')):
        print('Счастливо!')
        break
    else:
        print('Это не двоичные числа, попробуйте еще раз')