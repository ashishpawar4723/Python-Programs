def check_leep_year(year):
    if (year%400)==0:
        return True
    elif (year%4)==0:
        if (year%100)!=0:
            return True
        else:
            return False

year=int(input("enter Year:"))
if check_leep_year(year):
    print("Leep Year")
else:
    print("Not Leep Year")