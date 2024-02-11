
# Write a program that accepts a string as input, capitalizes the first letter of each word in the 
# string, and then returns the result string.

def Capitalize():
    statement = input("enter a sentence :") 
    words = statement.split()
    

    capitalword = [word.capitalize() for word in words ]
 
    resultstatement = '  '.join(capitalword)
    print(resultstatement)

Capitalize()