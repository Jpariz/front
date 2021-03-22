# ID is like checking the code's license plate print(id(result)
#mutable and immutable :  bool strings, etc






# name = input("Please enter name")
# print("sup"+ '  ' + name)
# splitString = "This string has been \n split over \n several \n lines"
# print(splitString)
# tabbedString='\t2\t4\t5'
# print(tabbedString)

#Using  """   """  gives you compmlete freedom   and putting \  will connect things that are spaced in SDK
# print("C:\Users\timbul")
# print("C:\\Users\\timbul")
# print(r"C:\\Users\\timbul")   bound or bind means   datavalue --> variable

# print(type(age))

# a=12
# b=3
# print(a/b)
# print(a//b)

# print()
# for i in range(1,9):
#     print(i)

    # parrot = "Norwegian Blue"
    # print(parrot[3])


                    # parrot = 'Norwegian Blue'
                    #
                    #
                    # print(parrot[3])
                    # print(parrot[4])
                    # print(parrot[9])
                    # print(parrot[3])
                    # print(parrot[6])
                    # print(parrot[8])
                                            # print(parrot[-8])  you can go backwards
                                            # print(parrot[7-8])  you can go do math operations

                        #print(parrot[0:6])
                        #print(parrot[:9])
                        #print(parrot[10:])  out put goes "Blue"           "  S L I C I N G "
                        # *print(parrot[0:2:4]) step slicing
                        #print(bignumber[1::4])  cuts the number's commas  1-everything hop 4 times over

#------------------------------------------------------------------------------
# print('New Line!')
# parrot='Noregian Blue'
# number = "9,483,654,453,635,234"
# seperators = number[1::4]
# print(seperators)
#
# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])
#-------------------------------------------------------------------------------

# letters = 'abcdefghijklmnopqrstuvwxyz'
# backwards = letters[25::-1]
# #backwards = letters[::-1]  slicing idioms
# print(backwards)

#-------------------------------------------------------------------------------
# letters = 'abcdefghijklmnopqrstuvwxyz'
# #backwards = letters[-10:-13:-1]
# backwards = letters[16:13:-1]
# #backwards = letters[::-1]  slicing idioms
# print(backwards)
# print(letters[:1])

#-------------------------------------------------------------------------------

# string1 = "he's "
# string2 = 'going '
# string3 = 'to '
# string4 = 'cyber '
# string5 = 'secsasasasasasl;;urity'
# string6 = 'school'
# print(string1 + string2 + string3 + string4 + string5 + string6)
# print("uhhh" * (5 + 4))
#-------------------------------------------------------------------------------
                                   # replacement fields {}
# age = 24
# print("my age is {0} years".format(age))
# print('There is {0} days in {1}, {2}, {3}'.format(31, "Jan", "Mar", "May"))
# print(" cowboys use {0}, ninjas use{1}, bankers use {2}".format('pistols', ' katanas', 'money'))
#-------------------------------------------------------------------------------
# for i in range(1,13):                       # 0:3 makes the print out tidy in the console
#     print('No. {0:2} ninja sword is {1:4} magic flame {2:4}'.format(i, i ** 2, i ** 3))  #2:^4  2:<3

#------------------------------------------------------------------------------- "backport = bring new to old
# name = 'bill'
# age_string= "2 years"
# age = 24
# print(name +f' is {age_string} years old')
# print(name +f' is {age} years old')
# print(type(age))
# print(f'pi is aprox {22 /7:12.50f}')
# pi = 22/7
# print(f'pi is paroxx {pi:12.50f}')
#---------------------------------------------------------------------------------
            # string interpolation  (deprecated)
# age = 24
# print('my age is %d years' % age)
# major = 'years'
# minor = 'months'
# print('my age is %d, %s, %d %s,' % (age, major, 6, minor))
# print('PI is aproxa %f' % (22/7))
# print('PI is aproxa %60.50f' % (22/7))

#-------------------------------------------------------------------------------    FLOW  CUMMULATIVE INT
# for i in range(100,1200):
#     print('no. {} squared i {} and cubed is {}'.format(i, i * 1.05, i * 1.1))
#     print("-" * 80)


#-------------------------------------------------------------------------------  checking requirements
# name = input("whas yo name")
# age = int(input('howolduis?'.format(name)))
# print(age)
#
# if age >= 18:
#     print("Your are old enough to vote")
#     print('please put an x and vote')
# else:
#         print("no, you need {0}".format(18-age))
#---------------------------------------------------------------------------------
# name = input("whas yo name")
# age = int(input('howolduis?'.format(name)))
# print(age)

# if age >= 18:
#     print("Your are old enough to vote")
#     print('please put an x and vote')
# else:
#         print("no, you need {0}".format(18-age))
#         if age < 18:
#             print("no, you need {0}".format(18-age))
#         elif age == 900:
#             print('yoda dies')
#         else:
#             print('your are old enough to vote')
#             print('x in da box')

#also  if age in range (18, 65):
#-----------------------------------------------------------
# answer = 5
# print ('Please guess number between 1 and 10')
# guess = int(input())
#
# if guess < answer:
#     print('Please guess higher')
# elif guess > answer:
#     print('please guess lower')
# else:
#     print('you guessed it')

#-------------------------------------------------------------------------------  AND OR / and not / or not
# day = 'Monday'
# temperature = 30
# raining = True
# if day == 'Saturday' and temperature > 27 and not raining:
#     print('go swimming')
# else:
#     print('Learn python')
#-------------------------------------------------------------------------------   in
# parrot = 'Estonian Blue'
# letter = input('enter a character: ')
# if letter in parrot.casefold():
#     print('{} is in{}'.format(letter, parrot))
# else:
#     print("I don't need that letter")


#-------------------------------------------------------------------------------  weird loop
# sonic = "hedgehog"
# for unit in sonic:
#     print(unit)
#-------------------------------------------------------------------------------  cool isolation

# number = '9,323?555!333#222'
# seperators = ""
# for char in number:
#     if not char.isnumeric():
#         seperators = seperators +char
# print(seperators)
#
# values ="".join(char if char not in seperators else "  " for char in number).split()
# print([int(val) for val in values])
#------------------------------------------------------------------------------- range class
# for i in range(10,0, -2):
#     print('this {} segment'.format(i))
#-------------------------------------------------------------------------------
#
# for i in range(1,4):
#     for j in range(1,4):
#         print('{0} times is {1} is {2}'.format(j, i, i * j))
#     print('-'*20)
#------------------------------------------------------------------------------- continue nearly worthless
# shopping_list = ["sword","pistol","gold","spam","magic","potion"]
# # for unit in shopping_list:
# #     print("buy a "+ unit)
#
# for unit in shopping_list:
#     if unit == 'spam':
#         continue
#     print("buy a " + unit)

#------------------------------------------------------------ break
# shopping_list = ["sword","pistol","gold","spam","magic","potion"]
# # for unit in shopping_list:
# #     print("buy a "+ unit)
#
# for unit in shopping_list:
#     if unit == 'spam':
#         break  # replace this with continue watch what happens
#     print("buy a " + unit)

#------------------------------------------------------------
# shopping_list = ["sword","pistol","gold","spam","magic","potion"]
#
# item_finder = 'spam'
# found_at = None #its empty at first
#
# for unit in range(len(shopping_list)):
#     if shopping_list[unit] == item_finder:
#         found_at = unit
#         break #once it finds spam its out and over saving energy
# print(f'item found at position{found_at}')

#------------------------------------------------------------
# i = 0
# while i <= 20:
#     print('i is ow {}"'.format(i))
#     i += 2

#------------------------------------------------------------
# exits = ['north','south','east']
# choice = ""
# while choice not in exits:
#     choice = input("choose which way you wanna go ")
#     if choice == 'quit':
#         print("game over")
#         break
# print('you eescaped')
#------------------------------------------------------------  random number generator
# import random
# answer = random.randint(1,10)
# highest = 10
# print(answer)
# print("please guess number 1 thru {}: ".format(highest))
# guess = int(input())
#
# if guess == answer:
#     print("you got it !")
# else:
#     if guess < answer:
#         print('try again to low')
#     else:
#         print('too high')

#------------------------------------------------------------ # P  E P 8
#REFACTORING changes shape of code but not how it works
# right click refactor rename (highlight)

#------------------------------------------------------------------ rare else in a loop
# number = [8,16,24]
# for unit in number:
#         if unit % 8 ==0:
#             print('divisible by eight')
#             break
# else:
#     print('all those numbers are fine')
#------------------------------------------------------------------  Lists   done
# computer_Parts = ['computer',
#                   'monitor',
#                   'keyboard',
#                   'mouse',
#                   'mouse mat'
#                   ]
# for part in computer_Parts:
#     print(part)
#
# print()
# print(computer_Parts[2])
# print(computer_Parts[0:3])
# print(computer_Parts[2])

#------------------------------------------------------------------ lists are mutable
# shopping_list = ['star',      #lists are updatable with same license plate MUTABLE
#                  'pasta',     #strings are immutable and cannot be changed
#                  'bread',
#                  'peas',
#                  'rice'
#                  ]
# another_list = shopping_list
# print(id(shopping_list))
# print(id(another_list))
#
# shopping_list += ['cookies']
# print(shopping_list)
# print(id(shopping_list))
#------------------------------------------------------------
# trick = 'mississippi'.count('s')
# print()
# print(trick)

#------------------------------------------------------------  EPIC  shopping cart  verbose
# nowChoice = "-"   # delete the - and watch what happens (??)
# computerParts = []    #elastic
# while nowChoice != 'done':
#     if nowChoice in '12345':
#         print("you are placing this in your basket {}".format(nowChoice))
#         if nowChoice == '1':
#             computerParts.append('computerjj')
#         elif nowChoice == '2':
#             computerParts.append('monitor')
#         elif nowChoice == '3':
#             computerParts.append('keyboard')
#         elif nowChoice == '4':
#             computerParts.append('mouse')
#         elif nowChoice == '5':
#             computerParts.append('mouse mat')
#
#
#     else:   #shows up at the start of the program for viewers to understand wtf is going on
#         print('please add options ')
#         print('1: computer')
#         print('2: monitor')
#         print('3: keyboard')
#         print('4: mouse')
#         print('5: mouse mat')
#         print('0: to finish')
#
#     nowChoice = input()
# print(computerParts)

#------------------------------------------------------------ iterating over a list using methods
# available_parts = ['computer',
#                    'monitor keyboard',
#                    ' mouse',
#                    'mouse mat',
#                    'hdmi',
#                    'cable'
#                    ]
#
# nowChoice = "-"
# computerParts = []
# while nowChoice != '0':
#     if nowChoice in '12345':
#         print("adding {}".format(nowChoice))
#         if nowChoice == '1':
#             computerParts.append('computerjj')
#         elif nowChoice == '2':
#             computerParts.append('monitor')
#         elif nowChoice == '3':
#             computerParts.append('keyboard')
#         elif nowChoice == '4':
#             computerParts.append('mouse')
#         elif nowChoice == '5':
#             computerParts.append('mouse mat')
#
#
#     else:
#         print('please add optionks ')
#         for part in available_parts:
#             print("{0} : {1}".format(available_parts.index(part) +1, part))
#
#     nowChoice = input()
# print(computerParts)

#------------------------------------------------------------ enumerate is lean processing code
# available_parts = ['computer',
#                    'monitor keyboard',
#                    ' mouse',
#                    'mouse mat',
#                    'hdmi',
#                    'cable'
#                    ]
#
# nowChoice = "-"
# computerParts = []
# while nowChoice != '0':
#     if nowChoice in '12345':
#         print("adding {}".format(nowChoice))
#         if nowChoice == '1':
#             computerParts.append('computerjj')
#         elif nowChoice == '2':
#             computerParts.append('monitor')
#         elif nowChoice == '3':
#             computerParts.append('keyboard')
#         elif nowChoice == '4':
#             computerParts.append('mouse')
#         elif nowChoice == '5':
#             computerParts.append('mouse mat')
#
#
#     else:
#         print('please add options ')
#         for number, part in enumerate(available_parts):
#             print("{0} : {1}".format(number+1, part ))
#
#     nowChoice = input()
# print(computerParts)

#------------------------------------------------------------  awesome forloop
#
# for index, character in enumerate('abcdefghikj'):
#     print(index, character)


#------------------------------------------------------------

#
# available_parts = ['computer',
#                    'monitor keyboard',
#                    ' mouse',
#                    'hdmi',
#                    'cable'
#                   ]
# #validChoices= [str(i) for i in range (1, len(available_parts) +1)]   # shitty way
# validChoices = []
# for i in range (1, len(available_parts) + 1):                                   #<---  memorize
#     validChoices.append(str(i))
#
# print(validChoices)
# nowChoice = "-"
# computerParts = []
# while nowChoice != '0':
#     if nowChoice in validChoices:  #changed from '12345'
#         print("adding {}".format(nowChoice))
#         index = int(nowChoice)-1
#         choice = available_parts[index]
#         computerParts.append(choice)
#
#
#     else:
#         print('please add options: ')
#         for number, part in enumerate(available_parts):
#             print("{0} : {1}".format(number+1, part))
#
#     nowChoice = input()
# print(computerParts)
#------------------------------------------------------------adding and removing list

# available_parts = ['computer',
#                     'monitor keyboard',
#                     ' mouse',
#                     'hdmi',
#                     'cable'
#                    ]
# #validChoices= [str(i) for i in range (1, len(available_parts) +1)]  shitty way
# validChoices = []
# for i in range (1, len(available_parts) + 1):
#      validChoices.append(str(i))
#
# print(validChoices)
# nowChoice = "-"
# computerParts = []
# while nowChoice != '0':
#     if nowChoice in validChoices:  #changed from '12345'
#         print("adding {}".format(nowChoice))
#         index = int(nowChoice)-1
#         choice = available_parts[index]
#         if choice in computerParts:
#             print('your remove list now contains : {}.'.format(nowChoice))
#             computerParts.remove(choice)
#         else:
#             computerParts.append(choice)
#         print('your list now contains : {}.'.format(nowChoice))
#     else:
#         print('please add options: ')
#         for number, part in enumerate(available_parts):
#            print("{0} : {1}".format(number+1, part))
#     nowChoice = input()
# print(computerParts)


#------------------------------------------------------------------------------  compound
# compound = 1.05
# start = 1000
# days = 20
# result = start * compound ** days
# print(result)
#----------------------------------------------------------------------------------
# even = [2,4,6,8]
# odd = [1,3,5,7,9]
#
# even.extend(odd)
# print(even)
# even.sort(reverse=True)
# print(even )
# even.sort()
# print()
# print(even)
#-------------------------------------------------------------
#docs.python.org/3/library/functions.html
# somestring = "This is the example of a string being iterated"
# letter = sorted(somestring)
# print(letter)
#capital letters come first, some letters are duplicated
#letters are cloned in the sorted function

#-------------------------------------------------------------
#
# numbers = [2.3, 2.5, 8.7, 3.1, 9.2, 1.6]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
#------------------------------------------------------------- confusing
# numbers = [2.3, 2.5, 8.7, 3.1, 9.2, 1.9]
# numbers.sort()
# print(numbers)   #this is the difference from above
#-------------------------------------------------------------99 sorting
# pancake = "the little hedgehog is a champ"
#
# letter = sorted(pancake)
# print(letter)
#------------------------------------------------------------- case insensitive
randomNames = ['Dude',
               'homie',
               'calvin',
               'chipmunk'
               ]
randomNames.sort(key=str.casefold)
print(randomNames)

#-------------------------------------------------------------
# I'm practicing Cyber security today 3/21
#-------------------------------------------------------------
#-------------------------------------------------------------
