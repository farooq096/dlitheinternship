'''
tuple


v=("aeiou","asdsc")
w=list(v)
w.append("juiedoewh")
w[1]="ascsf"
v=tuple(w)
print(v)
print(type(v))










task
1)

a=int(input(" enter a number:"))
b=int(input(" enter a number:"))
print(a+b)


2


a=int(input(" enter a number:"))
b=int(input(" enter a number:"))
c=int(input(" enter a number:"))
print(a+b+c)



3

a=int(input("enter a number to be checked::"))
if a%2==0:
    print("even")
else:
    print("odd")


4



def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
a=int(input("enter a number::"))
print("the factorial is ::" ,fact(a))



5

a=int(input(" enter a number:"))
b=int(input(" enter a number:"))
c=int(input(" enter a number:"))
if a>b and a>c :
    print("the largest  number is ",a)
elif b>a and b>c:
    print("the largest  number is ",c)
else:
    print("the largest  number is ",c)


6

a=input("enter to check palindrome::")

if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")



7


n=int(input("enter a number:"))
a,b=0,1
print("fibbonacci series:",end=" ")
for _ in range(n):
    print(a,end=" ")
    a,b=b,a+b



8

count=0
vowels="aeiou"
a=input("enter a word:::")
for char in a:
    if char in vowels:
        count=count+1  
print("the count:::",count)



9

count=0
vowels="aeiou"
a=input("enter a word:::")
for char in a:
    if char not in vowels:
        count=count+1  
print("the count:::",count)




10





n=int(input("enter a number"))
if n>1:
    for i in range(2,(n//2)+1):
        if (n%i)==0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")



11


'''

n=int(input("enter a number:"))
for i in range(1,11):
    print(f"{n}×{i}={n*i}")

















































    
