num=int(input('Enter number:'))
revers_num=0
while num>0:
    reminder=num%10
    revers_num*=10+reminder
    num//10
    
print(revers_num)

