a = int(input("Enter the number"))
b = int(input("Enter the number"))

res = min(a,b)

while res:
    if a%res ==0 and b%res==0:
        break
    res -=1

print(res)