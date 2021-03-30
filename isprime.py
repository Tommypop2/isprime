import math as m
import time as t
isprime = True
done = False
def Run(number): #Returns True or false depending on the number provided
    isprime = True
    done = False
    for x in range(2, int(number/2 + 1)):
        division = number/x #Divides the number by every integer between 2 and 1/2 of itself.
        if (division.is_integer() == True): #Checks if any of the answers are integers, if they are, the number is not prime.
            isprime = False
        if (isprime == False):
            break
    done = True
    return(isprime)