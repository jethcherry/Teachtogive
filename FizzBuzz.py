
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
# "FizzBuzz"



def fizz_Buzz():
   i=1
   while i < 100:
      
      if i%3==0 and i%5==0:
       print(f"{i} fizzbuzz")
      elif i%3==0:
       print(f"{i} fizz")
      elif i%5==0:
       print(f"{i} buzz")
      else:
       print(f"{i} not divisible ")

      i+=1

fizz_Buzz()