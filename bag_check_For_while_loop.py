#Python sample code 
# two methoids for the FOR Loop in Python

passinger=5
baggage=2
check=True
for number in range(1,passinger+1):
    bag=1
    while(bag<=baggage):
        if(check==True):
            print("passinger : ",number,"and baggage : ",bag," is cleared")
        else:
            print("passinger : ",number,"and baggage : ",bag," is not cleared")
        bag+=1
        
            
