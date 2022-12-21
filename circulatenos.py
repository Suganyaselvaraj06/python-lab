# Circulate the values of n variables
n = int(input("Enter number of values : "))
list1 = []
for val in range(0,n,1):
    ele = int(input("Enter integer : "))
    list1.append(ele)
print("Circulating the elements of list ", list1)
r=int(input("Enter how many rotation"))
for val in range(0,r,1):
    ele = list1.pop(0)
    list1.append(ele)
    print(list1)