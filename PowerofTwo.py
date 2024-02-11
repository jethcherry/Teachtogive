# Write a program that takes an integer as input and returns true if the input is a power of two.



def isPowerofTwo(n):
    return n > 0 and (n & (n - 1)) == 0

def power():
    print("Please enter a number:")
    userinput = int(input())

    if isPowerofTwo(userinput):
        return True  
    
    else:
        return False 

print(power())
