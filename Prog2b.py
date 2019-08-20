def rev1(str):
    lis=str.split(" ")
    lis.reverse()
    a= " "
    s=a.join(lis)
    print(s)

def reverse(str):
    lis=str.split(" ")
    s2=''
    for i in lis:
        s2 += i[::-1] + " "
    print(s2)

a = input("Enter the string : ")
rev1(a)
reverse(a)
