#given number is prime or not
num=int(input("Enter Number:"))
if num==1:
    print(num,"Is Not Prime Number")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"Is Not Prime Number")
            break
    else:
        print(num,"Is Prime Number")

#find the prime numbers in betweeen 1 to 100
x=int(input("Enter Number:"))
y=int(input("Enter Number:"))
for n in range(x,y+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)


