#Display the factors of a number 
a=int(input("enter anumber "))
def factorial(a):
    c=0
    for b in range (2,a//2):
        if(a%b == 0):
            print(b)
            c=1
    return c
if(factorial(a)==0):
    print("there is no factors. it is a prime number ")
