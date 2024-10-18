n=int(input("enter any number\n"))
tot=0
while(n>0):
   d=n%10
   tot=tot+d
   n=n/10
print("total sum of digits is:\n",tot)
