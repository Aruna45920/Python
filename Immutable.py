a=10
print(a)
print(id(a))
a=20
print(a)
print(id(a))
# Here we are assigning the values to a single one but their reference value is different

#-----------------------------

a=10
print(a)
print(id(a))
b=10
print(b)
print(id(b))
print(a is b)
#Here the address is same for a and b


