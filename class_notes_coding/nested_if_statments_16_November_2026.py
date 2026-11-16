#Date: 16 November 2026
#Prisha Mehta
#Nested if statments
number = input ('Enter an integer number: ')
number = int (number)
if number > 0:
    if number%2 ==0:
        print(number,'is a positive even number')
    else:
        print (number,'is a positive odd number')
elif number < 0:
    if number%2 ==0:#f string for print
        print(f'{number} is a negative even number')
    else:
        print(f'{number} is a negative odd number')
else:
    if number == 0 :#This is only here for demostration of nesting
        print (number,'is an even number')
print('program finished')

    