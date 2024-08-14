#In python we can return more than one than value also

def fun():
    a=10
    b=20
    c=30
    return a,b,c
print(fun())
res=fun()

#Here we get the results as tuple if you want to know let check

print(type(res))

#And now you unpack the values of tuples into individual variables

def fun():
    a=10
    b=20
    c=30
    return a,b,c
res1,res2,res3=fun()
print(res1)
print(res2)
print(res3)



