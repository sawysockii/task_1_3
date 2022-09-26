def only_brackets_in_string(input_string):
    only_brackets = 1
    if len(str(input_string)) > 0:
        for char_i in str(input_string):
            if char_i in brackets_string:
                only_brackets *= 1
            else:
                only_brackets *= 0
        if only_brackets == 1:
            return(True)
        else:
            return(False)
    else:
        return(False)


run = True
while run:
    our_string = input('Введите последовательность скобок: ')
    if ((our_string == 'exit') or (our_string == 'quit')):
        print('Счастливо!')
        break
    else:
        if only_brackets_in_string(our_string):
            if paired_brackets_in_string(our_string):
                if check_brackets(our_string):
                    print('Все ok!')
                else:
                    print('Неверное расположение скобок')
            else:
                print('Ваши скобки скучают без пары')
        else:
            print('Должны быть скобки! Попробуйте еще раз.')