#Problem 2
#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print:
#"Number of times bob occurs is: 2"

found = 0
count = 0
length = len(s)
for count in range(length-2):
    if s[count] == "b":
        if s[count+1] == "o":
            if s[count+2] == "b":
                found+=1
        
print("Number of times bob occurs is: " + str(found))