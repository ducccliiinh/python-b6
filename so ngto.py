def prime(a):
    check = False
    if a > 0:
        if a == 1:
            check = False
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                check = False
                break
            else:
                check = True
    return check
            
n = int(input())
count = 0
for i in range(1, n + 1):
    if prime(i):
        count += 1
print(count)