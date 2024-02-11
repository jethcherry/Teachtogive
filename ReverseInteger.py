
# Write a program that takes an integer as input and returns an integer with reversed digit 
# ordering.

def reverse_Integer():

    statement=input("Enter a number  ")
    reversed_Number= ''.join(reversed(statement))
    print(reversed_Number)

reverse_Integer()