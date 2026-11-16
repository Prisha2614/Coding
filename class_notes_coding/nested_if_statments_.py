#Date: 16 November 2026
#Prisha Mehta
#Nested if statments
#1
name = input ('enter your name: ' )
password = input ('enter your password: ')
if name =='admin':
    if password == '1234':
        print ('welcome, you will have administration access')
    else:
        print ('incorrect password fpr admin you will have standard user access')
else:
    print('unknown user')
#2
age = input ('enter your age: ')
age = int(age)
height = input ('enter your height in cm: ')
height = float (height)
if age >= 12:
    if height >140:
        print ('you can go on the ride')
    else:
        print('you are too small')
else:
    print ('you are too young')
#3
pool = input ('is the pool open: ')
if pool == 'yes':
    wb = input ('do you have a wb')
    
    

    