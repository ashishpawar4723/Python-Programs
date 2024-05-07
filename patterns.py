n=5
def squre_pattern():   
    for i in range(n):
        for j in range(n):
            print('*',end=" ")
        print()
 
def incresing_triangle():
    for i in range(n):
        for j in range(i+1):
            print('*',end="")
        print()

def decreasing_triangle():
    for i in range(n):
        for j in range(n-i):
            print('*',end="")
        print()

def right_side_triangle():
    for i in range(n):
        for j in range(i,n):
            print(' ',end="")
        for j in range(i+1):
            print('*',end="")
        print()

def right_side_decreasing_triangle():
    for i in range(n):
        for i in range(i+1):
            print(' ',end="")
        for j in range(i,n):
            print('*',end='')
        print()

def hil_pattern():
    for i in range(n):
        for j in range(i,n):
            print(' ',end="")
        for j in range(i):
            print('*',end="")
        for j in range(i+1):
            print('*',end="")
        print()

def revers_hii_pattern():
    for i in range(n):
        for j in range(i+1):
            print(' ',end="")
        for j in range(i,n-1):
            print('*',end="")
        for j in range(i,n):
            print('*',end="")
        print()
    
def diamond_pattern():
    for i in range(n-1):
        for j in range(i,n):
            print(' ',end=" ")
        for j in range(i):
            print('*',end=" ")
        for j in range(i+1):
            print('*',end=" ")
        print()
    for i in range(n):
        for j in range(i+1):
            print(' ',end=" ")
        for j in range(i,n-1):
            print('*',end=" ")
        for j in range(i,n):
            print('*',end=" ")
        print()



# squre_pattern()
# incresing_triangle()  
# decreasing_triangle()
#right_triangle():
#right_side_decreasing_triangle()
#hil_pattern()
#revers_hii_pattern()
diamond_pattern()