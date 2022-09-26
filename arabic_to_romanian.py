from curses.ascii import isdigit


roman_coding = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def arabic_to_roman(input_number):
    arabic_string = ''
    while input_number > 0:
        for i in range(0,len(roman_coding)):
            while input_number - roman_coding[i][0] >= 0:
                arabic_string += roman_coding[i][1]
                input_number -= roman_coding[i][0]
                print(input_number)
    return(arabic_string)

run = True
while run:
    input_ = input('Введите арабское число: ')
    if input_.isdigit():
        print(arabic_to_roman(int(input_)))
    elif input_ == 'exit' or input_ == 'quit':
        print('Счастливо!')
        break
    else:
        print('Это не арабское число, попробуйте еще раз')