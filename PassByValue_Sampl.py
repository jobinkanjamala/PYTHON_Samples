# Sample program to see the PASS BY VALUE method to a function 
def change_val(arg):
    arg+=20
    print('value of arg inside function = ',arg)
num=10
print("before function call, Num = ",num)
change_val(num)
print('After the functino call , Num =',num)
