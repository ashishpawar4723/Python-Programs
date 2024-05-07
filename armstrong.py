# ARMSTRONG NUMBER

num=int(input("Enter Nubmer:"))
sum=0
order=len(str(num))
temp=num

while temp > 0:
    digit=temp%10
    sum+=digit**order
    temp//=10

if sum==num:
    print('it is armstrong number')
else:
    print('it is not armstrong number')