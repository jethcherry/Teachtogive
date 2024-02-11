

# Write a program that counts the number of vowels in a sentence

def vowel_Count():
    statement = input("Enter a statement: ")

    statement = statement.lower()

    vowels = ('a', 'e', 'i', 'o', 'u')

    count_vowel = 0

    for char in statement:
        if char in vowels:
            count_vowel += 1

    print("Total number of vowels in the statement is:", count_vowel)

vowel_Count()




 
 



 


