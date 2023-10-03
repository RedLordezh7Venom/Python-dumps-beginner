'''program for sorting a list WITHOUT using sort func'''
list1=eval(input("Enter a list"))
list2=[]
list3=[]
len1=len(list1)

def sort():
    while list1:
        min = list1[0]  
        for m in list1: 
            if m < min:
                min = m
        list3.append(min)
        list1.remove(min)    
  
def reverse():
    for i in range (len1-1,-1,-1):
        list2.append(list1[i])
        
    
y=str(input("Do you want to reverse the listy/n"))
if y=="y":
    reverse()
    print(list2)
x=str(input("Do you want the list be sorted ? "))
if x=="y":
    sort()
    print(list3)




