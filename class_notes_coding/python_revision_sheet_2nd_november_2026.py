#2nd november 2026
# Prisha mehta
# 1
name = input (' enter your name:  ')
print ('hi,',name)
#2
number = input ('enter a number: ')
number = float (number)
number_ = input ('enter another number: ')
number_ = float (number_)
total = number + number_
print ('sum:',total)
#3
ticket = 6.00
movie = input ('enter number of tickets you want: ')
movie = float (movie)
total_ = movie * ticket
print('your total is',total_)
#4
marks = input ('enter marks obtained: ')
marks = float (marks)
total_marks = input ('enter total marks: ')
total_marks = float (total_marks)
total__ = marks / total_marks *100
print ('percentage',total__,'%')
#5
gender = input ('enter your gender: ')
if gender == 'male' :
    print ('good morning sir ')
elif gender == 'female':
    print ('good morning madam')
else:
    print ('good morning')
print ('program finished')
#6
secret = input ('enter a secret number: ')
secret = float (secret)
num=5
if secret == num:
    print ('Bingo! correct number')
elif secret == num +1 :
    print ('Close enough to the correct answer')
else:
    print ('Not close enough ')
print ('program finished')
#7
number_2 = input ('enter a number: ')
number_2 = float (number_2)
if number_2 % 3 == 0 :
    print (' this number is diviseble by 3')