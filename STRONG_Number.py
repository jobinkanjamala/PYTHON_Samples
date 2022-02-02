# to check the given number is a power number

def power(a):
    sum=0
    bkp=a
    while(a!=0):
        d=factorial(a%10)
        sum+=d
        a//=10
    print("the number is  : ",bkp)
    print("the sum offactorial of each number is :",sum)
    if(bkp==sum):
        print("this is a strong number ")
    else:
        print("this is not a strong number")
        
def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
po=power(145)
