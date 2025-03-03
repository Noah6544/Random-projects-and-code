#This one took longer
#Pretty messy but it works

import math
def consecutive_pythag_therom(num):
    #num = math.sqrt(a2+b2)
    left_side_equation = (num**2 + (num+1)**2)
    right_side_equation = ((num+2)**2)
    if left_side_equation == right_side_equation: #if there's a remainder (if this isn't a right triangle)
        return True
    else:
        pass

def n_plus_one_pythag_therom(a): #pretty sure this is accurate
    #num = math.sqrt(a2+b2)
    n = ((1 - a ** 2) / -2)
    a = math.sqrt(((n + 1) ** 2) - n ** 2)
    return a, n

#BONUS EQUATIONS
def n_plus_two_pythag_therom(a): #not sure how accurate this formula is
    #num = math.sqrt(a2+b2)
    n = (((a ** 2)/4))
    a = math.sqrt(((n + 2) ** 2) - n ** 2)
    return a, n

def n_plus_three_pythag_therom(a): #not sure how accurate this formula is

    #num = math.sqrt(a2+b2)
    n = (3 - (a ** 2))
    c = ((n + 3) ** 2)
    print(c)
    print(n)
    print(a)
    a = math.sqrt((n**2)-c )
    return a, n


## FIND FUNCTIONS ###
def find_consecutive_triples(range):
    num = -100
    count =0
    while num < range: #go crazy on the zeros, or set to True
        b2 = (num +1)**2
        a2 = num**2
        if consecutive_pythag_therom(num): #if the triple is a triangle
            count += 1
            print("Triple #" + str(count) + " Found!!")
            print("The Triple is: (" + str(num) + ", " + str(num+1) + ", " + str(num+2)+")")
        num += 1

def find_n_plus_one_triples(range):
    a = 1
    count = 0
    while a < range: #go crazy
        if a % 2 == 0: #if a is even
            pass
        else:
            a,b = (n_plus_one_pythag_therom(a))
            print("Triple #" + str(count) + " Found!!")
            print("The Triple is: (" + str(a) + ", " + str(b) + ", " + str(b + 1) + ")")

        a+=1
        count+=1


def find_n_plus_two_triples(range):
    a = 1
    count = 0
    while a < range: #go crazy
        if a % 2 == 0: #if a is even
            pass
        else:
            a,b = (n_plus_three_pythag_therom(a))
            print("Triple #" + str(count) + " Found!!")
            print("The Triple is: (" + str(a) + ", " + str(b) + ", " + str(b + 2) + ")")
        a+=1
        count+=1

def find_n_plus_three_triples(range):
    a = 1
    count = 0
    while a < range: #go crazy
        if a % 2 == 0: #if a is even
            pass
        else:
            a,b = (n_plus_three_pythag_therom(a))
            print("Triple #" + str(count) + " Found!!")
            print("The Triple is: (" + str(a) + ", " + str(b) + ", " + str(b + 3) + ")")
        a+=1
        count+=1

# FIND FUNCTIONS #


running = True

while running:
    print("Hey Mr. Hornbeck...I think?\nWould you like to see:"
          "\n1.) N+1 triples?"
          "\n2.) N+2 Triples? broken"
          "\n3.) N+3 Triples? broken ")
    user = input("Enter a number: ")
    user = int(user)
    if user == 1:
        range = int(input("Enter Max Range to generate: "))
        range = int(range)
        find_n_plus_one_triples(range)
    elif user == 2:
        range = int(input("Enter Max Range to generate: "))
        find_n_plus_two_triples(range)
    elif user == 3:
        range = int(input("Enter Max Range to generate: "))
        find_n_plus_three_triples(range)

    user = input("Do you want to continue? Enter yes/no: ")
    if user == 'yes' or user == 'y':
        running = True
    else:
        running = False
        print("hope this was nice")



