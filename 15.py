lst = [3,4,5,3,2]
a = int(input("ENter the number to replace"))
for i in range(0,len(lst)):
    if lst[i]%2 !=0:
        lst[i]=a
print(lst)
