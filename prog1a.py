l = []
n=int(input("Enter the no of elements : "))
print("Enter the elements in the list :\n")
for i in range(0,n):
    ele=int(input())
    l.append(ele)
a = []
for i in range(0,n):
    if l[i]%2==0:
        a.append(l[i])
print(a)
