#Python sample code 
#the prime number finder 
a=input("enter a number to check the prime or not\n")
b=int(a)//2
#print(b)
for i in range(2,b+1):
    if(int(a)%i == 0):
        print (" the numer is not a prime number")
        break
#print(i)
if(i==b):
    print(" it is a prime number")
