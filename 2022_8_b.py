# Finding the biggest among three numbers...
def big_num (a, b, c):
    if (a>b & a>c ):
        big = a
    elif (b>c):
        big = b
    else:
        big = c
    return(big)

a = 5
b = 3
c = -8
result = big_num(a, b, c)
print("Biggest number is: ", result)