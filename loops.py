# While loop syntax

#while(testExpression):
  #code inside the loop

lst=[10,20,30,40]
i=0
while i<4:
    print(lst[i])
    i=i+1     #Here there is no increment or decrement operators in python


#----------------------------------------------------------------------------------


# for loop syntax

# for var in iterable:
 #body of for loop

lst1=[11,12,13,14,15]

for i in lst1:
    print(i)


# when we know the condition but not the number of iterations we use while loop

#example

balance=15500
min_balance=500
print("before transaction:",balance)
while min_balance<balance:
    balance=balance-1000
print("after transaction:",balance)


#now exactly i withdraw 5000 so i will use for loop
balance=15500
min_balance=500
print("before transaction:",balance)
for i in range(5):
    balance=balance-1000
print("after transaction:",balance)






