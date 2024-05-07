list=[3,7,5,8,4,9]
#direct in build function
print(max(list))
#direct inbuild function
print(min(list))

# creating a function to find out maximum number in given list
def find_max(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max

max=find_max(list)
print(max)

# creating a function to find out manimum number in given list
def find_min(list):
    min=list[0]
    for i in list:
        if i<min:
            min =i
    return min

min=find_min(list)
print(min)

# find out the max  in three number 
x=int(input('enter number'))
y=int(input('enter number'))
z=int(input("enter number"))

if x>y and x>z:
    print(x,"is maximum number")
elif y>x and y>z:
    print(y,"is maximum number")
else:
    print(z,'is maximum number')

# find out the min in three number 

a=int(input('enter number'))
b=int(input('enter number'))
c=int(input("enter number"))

if a<b and a<c:
    print(a,"is manimum number")
elif b<a and b<c:
    print(b,"is manimum number")
else:
    print(c,'is manimum number')