#FIND THE FACTORIAL USEING RECURSION
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

num=int(input('enter no:'))
print(factorial(num))


#FACTORIAL 
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

result=fact(5)
print(result)

