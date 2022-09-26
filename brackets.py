# test_string = '[({)]}'
# test_string = '[(}{)]'
brackets = [('(',')'),('{','}'),('[',']')]
brackets_string = "(" + ")" + "[" + "]" + "{" + "}"
closed_brackets = ")" + "]" + "}"

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

def paired_brackets_in_string(input_string):
    brackets_count = {'{':0,'}':0, '(':0,')':0, '[':0, ']':0}
    for bracket in input_string:
        brackets_count[bracket] += 1
    if ((brackets_count['{'] == brackets_count['}']) and (brackets_count['('] == brackets_count[')']) and (brackets_count['['] == brackets_count[']'])):
        return True
    else:
        return False

def check_brackets(input_string):
    ok_brackets = 1
    while (ok_brackets == 1) and (len(input_string) > 0):
        if input_string[0] in closed_brackets:
            ok_brackets *= 0
        else:
            for i in range(0,len(brackets)):
                if len(input_string) > 0:
                    if  input_string[0] == brackets[i][0]:
                        input_string = input_string.replace(brackets[i][1],'', 1)[1:]
                        ok_brackets *= 1
    if ok_brackets == 1:
        return(True)
    else:
        return(False)

                
# print(check_brackets(test_string))  # test
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