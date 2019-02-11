a1 = int(input())
a2 = int(input())
a3 = int(input())
 
if (a1 > a2) and (a1 > a3):
   largest = a1
elif (a2 > a1) and (a2 > a3):
   largest = a2
else:
   largest = a3
 
print("The largest number is",largest)
