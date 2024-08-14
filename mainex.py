# Here by importing this builin that is also executed line by line here everything in that class is executed
#like if we import math function we can execute every function in that
#to overcome this problem we have to do some thing in the buildin file there i wrote the conditon so now we execute this we will get only one output
import buildin
def get_remainder(num,den):
    '''This functio calculates the remainder of num/den'''
    rem=num%den
    print(rem)
get_remainder(100,6)

#-------------------------------------------------- if i need to call i have to call individually like this below

buildin.power_of(2,5)
buildin.get_quotient(100,2)



