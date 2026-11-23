#2nd november 2026
# Prisha mehta
#8
number_1 = input ('Enter a number: ')
number_1 = float (number_1)
number_2 = input ('Enter a second number: ')
number_2 = float (number_2)
number_3 = input ('Enter a third number: ')
number_3 = float (number_3)
if number_1 +  number_2 ==  number_3 :
    print ( number_1,'+', number_2,'=', number_3)
elif  number_2 + number_3 == number_1 :
    print ( number_2,'+' ,number_3,'=', number_1)
elif  number_1 +  number_3 == number_2:
    print( number_1,'+', number_3,'=', number_2)
print ('program finished')
#9
season = input ('enter a season: ')
chrysanthemums = input ('how many chrysanthemums do you want:')
chrysanthemums = float (chrysanthemums)
roses = input ('how many roses do you what: ')
roses = float (roses)
tulips = input (' how many tulips do you want: ')
tulips = float (tulips)
if season == 'spring' or season == 'summer':
    cost = chrysanthemums * 2.00 + roses * 4.10 + tulips * 2.50 + 2
    print('The bouquet costs €', round(cost, 2))
elif season == 'autumn' or season == 'winter':
    cost = chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15 + 2
    print('The bouquet costs €', round(cost, 2))
else:
    print('That is not a valid season')
print('program finished')

