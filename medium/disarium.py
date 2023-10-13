s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
if len(s1)==len(s2):
    for i in s1:
        if i not in s2:
            print("Entered strings are not anagram to each other")
            break
        else:
          print("Entered strings are anagram to each other")
else:
          print("Entered strings are not anagram to each other")
