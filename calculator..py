num1=int(input('enter number:'))
num2=int(input('enter number:'))
operator=input('enter operator:')

if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    result=num1/num2
else:
    result='Invalid Operation'

print('Result',result)