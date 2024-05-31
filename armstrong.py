i=int(input("Enter the Number:"))
origin=i
sum=0
while(i>0):
    sum=sum+(i%10)**3
    i=i//10
if sum==origin:
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")    
