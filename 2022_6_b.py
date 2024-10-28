n = 2543
sum = 0
while 1:
    rem = n%10
    sum = sum + int(rem)
    n = n/10
    if n==0:
        break

print(sum)