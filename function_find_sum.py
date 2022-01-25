"""Write a Python function,
find_sum() 
that accepts an integer n and 
returns the sum of first n numbers.
Invoke the function and display the sum of first n numbers. """

def find_sum(a):
    sum=0
    for i in range (1,a+1):
        sum+=i
    return sum
    
n=input("Enter a limit to calculate the sum \n ")
print("the sum of ",n," natural numbers is : ",find_sum(int(n)),"")
