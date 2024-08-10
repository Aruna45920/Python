
# without input - without return values
def mul():
    a=10
    b=20
    c=a*b
    print(c)
mul()

#-------------------------------------

  #with input- without return value

def mul(a,b):
    c=a*b
    print(c)
mul(2,3)

  
#-----------------------------------------------

#without input-with return value

def mul():
    a=10
    b=20
    c=a*b
    return c
res=mul()
print(res)


#with input - with return value

def mul(a,b):
   c=a*b
   return c
res=mul(20,20)
print(res)
    
