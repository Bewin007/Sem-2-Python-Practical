lst = [1,5,4,3]
print(max(lst))
print(min(lst))

a = int(input("Enter the range of numbers"))
number_to_find = int(input("Enter the number to find"))
status = 0
for i in range(0,a):
    if i == number_to_find:
        status = 1

if status ==1:
    print("Exist")
else:
    print("Not found")