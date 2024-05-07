l=[1,2,3,4,5]
# a=max(l)
# b=min(l)

# print('highest number ',a)
# print('lowest number',b)
# print('addition',a+b)


def max(list):
    max=list[0]
    min=list[0]
    for i in l:
        if i>max:
            max=i
        if i<min:
            min=i
    return max,min

# def min(list):
#     min=list[0]
#     for i in l:
#         if i<min:
#             min=i
#     return min

a,b=max(l)
print(a+b)
# b=min(l)

# print('highest number ',a)
# print('lowest number',b)
# print('addition',a+b)

