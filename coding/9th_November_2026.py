#9 November 2026
#Prisha Mehta
#1
name = input ('enter your name: ')
print ('Hello',name,'how are you?')
#2
temperature = input ('enter a temperature: ' )
temperature = float (temperature)
F = (temperature * 1.8) + 32
print (temperature,'degrees Celsius is equal to ',F,'degrees Fahrenheit')
#3
car = input ('enter a car brand: ')
if car == 'Ford' :
    print ('we stock lots of ford')
elif car == 'Hyundi' :
    print (' we stock some Hyundi')
elif car == 'BMW' :
    print ('We stock a few BMW ')
else:
    print ('we dont stock any of ',car)
#4
age = input ('enter your age: ')
age = float (age)
if age == 1:
    print ('you are 1 ')
elif age == 11:
    print ('you are 11')
elif age == 21:
    print ('you are 21')
elif age == 31:
    print ('you are 31')
else:
    (' you are not 1,11,21 or 31')