# positional arguments  -  Here the position is matters the order that we given only taken 

def power_of(a,b):
    c=a**b
    print(c)
power_of(5,2)
power_of(2,5)

#power_of(2) here we get error because we have to pass the 2 arguments

#-----------------------------------------------

#Default arguments 

def power_of(a,b=0):
    c=a**b
    print(c)
power_of(2)
power_of(2,1)

#---------------------------------------------------------

#Keyword arguments : In this we can change the order of arguments by using the keywords

def power_of(a,b):
    c=a**b
    print(c)
power_of(a=2,b=3)
power_of(b=3,a=2)


#-----------------------------------------------------------------

#Variable length or arbitrary arguments

def pizza_toppings(toppings):
    print(toppings)
pizza_toppings("cheese")
#pizza_toppings("cheese","onion","corn")
# here we have 3 arguments but we have to pass one so before the parameter we can add * then it will take the number of parameters


def pizza_toppings(*toppings):
    print(toppings)
pizza_toppings("cheese","Onion","corn")


#-----------------------------------------------------------------------



def pizza_toppings(*toppings,crust):
    print(toppings)
    print(crust)
pizza_toppings("cheese","corn","onion",crust="thin")

#-----------------------------------
#Any argument after variable length argument must treated as keyword argument
def pizza_toppings(name,*toppings,crust):
    print(name)
    print(toppings)
    print(crust)
pizza_toppings("Aruna","cheese","corn","onion",crust="thin")

#--------------------------------------------------------

#Variable keyword length arguments

def student_details_data(**data):
    print(data)
student_details_data(name="aruna",age=22,avg=80,gender='f')

def student_details_data(details,**data):
    print(details)
    print(data)
    
student_details_data("3-31,Vivek colony,vijayawada",name="aruna",age=22,avg=80,gender='f')








