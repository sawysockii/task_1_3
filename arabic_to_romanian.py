from curses.ascii import isdigit


roman_coding = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def arabic_to_roman(input_number):
    arabic_string = ''
    return(arabic_string)

input_ = input('Введите арабское число: ')
while input_ != 'exit' or input_ != 'quit'
    if isdigit(input_):
        output_ = arabic_to_roman(input_)
    else:
        print('Это не арабское число...')
