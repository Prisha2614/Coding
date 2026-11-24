#Date: 24 November 2026
#Prisha Mehta
#Strings
#Question 2
first_name = input ('enter your name : ')
first_name.lower
surname = input ('enter your surname: ')
name_1 = first_name+surname
print (name_1)
name_2 = len(name_1)
print(name_2)
#Question 3
name = input ('enter your name:')
surname = input ('enter your surname : ')
name_1 = name.title()
surname_1 = surname.title()
full_name = name_1 + ' ' + surname_1
print (full_name)
#Question 4
nursery = input ('enter the first line of a nursery: ')
nursery_1 = len(nursery)
print ('there are',nursery_1,'letters in',nursery)
#Question 5
word = input ('enter a word: ')
word_1 = word.title()
print(word_1)
#Question 6
name = input ('enter your name:')
surname = input ('enter your surname : ')
name_1 = len(name)
fn = name + ' ' +surname
if name_1 <5:
    v = fn.upper()
    print (v)
else:
    m = fn.lower()
    print(m)
