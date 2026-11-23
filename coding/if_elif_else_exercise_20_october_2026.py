#prisha mehta
# date:20 october 2026
# is elif else exercisee
#exercise 1
number = input ('enter a number:  ')
number = int (number)
if number > 0 :
    print (number,'is a positive number')
elif number < 0 :
    print (number,'is a negative number')
else:
    print ('number is zero')
print (' program finished')

# exercise 2
grade = input ('enter a grade:  ')
grade = int (grade)
if grade >= 90 :
    print (' you got an A in your test')
elif grade >= 80:
    print(' you got a B in your test')
elif grade >= 70:
    print (' you got a C in your test')
elif grade >= 60:
    print(' you got a D in your test')
else:
    print (' you failed your test')
print ('program finished')

# exercise 3
season = input (' enter a season of the year:  ')
if season ==  'spring' :
    print (' March , April , May')
elif season == 'summer':
    print (' June , July , August ')
elif season == ' autum':
    print (' September , October , November')
elif season == 'winter':
    print (' December , January , Febuary')
else:
    print (' you have not entered a valid season')
print (' program finished' )

# exercise 4
number_ = input (' enter a  number from 1 to 7 :  ')
number_ = int (number_)
if number_ == 1 :
    print (' Sunday')
elif number_ == 2 :
    print ('Monday')
elif number_ == 3 :
    print(' Tuesday')
elif number_ == 4 :
    print ('Wednesday')
elif number_ == 5 :
    print (' Thursday')
elif number_ == 6 :
    print ('Friday')
elif number_ == 7 :
    print (' Saturday ')
else:
    print (' error message')
print (' program finished')

#exercise 5
 
length = float(input('Enter the length: '))
breadth = float(input('Enter the breadth: '))

area = length * breadth
perimeter = 2 * length + 2 * breadth

if area > perimeter:
    print("The area is greater than the perimeter")
elif area < perimeter:
    print("The area is less than the perimeter")
else:
    print("The area is equal to the perimeter")
print ('program finished')

#exercise 6

days = int(input("How many days late is the book? "))

if days <= 0:
    print("No fine - the book is on time")
elif days <= 5:
    print("Fine: €0.50")
elif days <= 10:
    print("Fine: €1")
elif days <= 30:
    print("Fine: €5")
else:
    print("Your membership has been cancelled")
print ('program finished')
