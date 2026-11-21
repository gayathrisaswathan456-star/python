def find_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
         if((greater %x==0)and(greater %y==0)):
              lcm=greater
              break
         greater += 1
    return lcm
a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
print("lcm is",find_lcm(a,b))