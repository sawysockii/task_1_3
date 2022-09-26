def palindrom(input_string):
    return(str(input_string)[::-1])
    
run = True
while run:
    our_string = input('Введите cтроку: ')
    our_string = our_string.replace(' ','').replace(',','').lower()
    if ((our_string == 'exit') or (our_string == 'quit')):
        print('Счастливо!')
        break
    else:
        if len(our_string) > 0:
            if our_string == palindrom(our_string):
                print('Это палиндром')
            else:
                print('Это не палиндром')
        else:
            print('Строка не должна быть пустой')