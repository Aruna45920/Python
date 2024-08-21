n=int(input("Enter a number\n"))
for i in range(2,n+1):
    if n%i==0:
        break
if i==n:
    print(n,"is prime")
else:
    print(n,"is not prime")

# short cut operators

sum=5
print(sum)
sum +=5
print(sum)
    
#-------------------------------------------------------------

even_sum,odd_sum=0,0
n=int(input("Enter the value of n\n"))
for i in range(1,n+1):
    if i%2==0:
        even_sum +=i
        continue
    odd_sum+=i

print("Sum of all even numbers:",even_sum)
print("Sum of all odd numbers:",odd_sum)
