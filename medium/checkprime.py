a=int(input("Enter a number"))
if a > 1:  
 for j in range(2, int(a/2) + 1):  
  if (a % j) == 0: 
      print(a, "is not a prime number")  
      break    
  elif a==1:
      print(a, "is not a prime number")  
 else:  
  print(a, "is a prime number")
  
