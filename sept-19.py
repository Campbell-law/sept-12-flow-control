# Boolean values

# 1). Is this valid:

# True = 2+2

#  What about these - are they True:

2 + 2 == 4 
2 + 2 == '4'


#  Binary Operators
# 2). What about these?

2 + 3 == 5 and 4 + 5 == 9
3 + 4 == 7 and 2 + 2 == 5
3 + 4 == 7 or  2 + 2 == 5
3 + 4 == 7 and not 2 + 2 == 5

## Program flow
## Python groups programs into blocks with indentation
##

name = 'Mary'
password = 'crawdad'

if name == 'Mary':
    print("Hello " + name)
    if password == 'crawdad':
        print('Welcome ' + name)
    else:
        print('Sorry ' + name)

# 3). Beer program - write a program that asks for a name and age
## If the person is 21 or older they can buy beer if less than 21 they can't



# 4) Grading program - if score is > 90 you get an A,
##  > 80 < 90 you get a B
##  > 70 < 80 a C
##  > 60 < 70 a D
## anything else you flunk



# 5). Expungement App 
## This is based on last years project. You can only expunge a criminal record under certain conditions
## If you have one conviction you can usually get it expunged
## if you have more than on conviction you can only get them expunged if the convictions 
## occurred on the same day


# 6). Baseball App
## Use a while loop to print strike 1, strike 2, strike 3, You're out

# 7). Now use a for loop and do the same thing
##  This one has a trick -- note that ranges start at 0


# 8). Guessing game -- the book introduce modules and the function random()
## Implement a guessing game that assigns a number between 1 and 10 and
## the user has to guess the number
## Hint you can use while True to keep a loop going then exit it with a break


import random
number = random.randint(1,10)
print(number)
