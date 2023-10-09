l=[] 
odd=0 
even=0 
n=int(input("Enter the total number of elements of the list: ")) 
for i in range(0,n): 
    s=int(input("Enter the element of the string: "))     
    l.append(s) 
print("The list created is: ",l) 
for i in l:     
    if i%2==0:         
        even=even+i     
    else: 
        odd=odd+i 
print("Sum of even numbers of the list is: ",even) 
print("Sum of odd numbers of the list is: ",odd) 
