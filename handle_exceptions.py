#Incorporate the following code into a Python program to handle exceptions.
#Handle exceptions with the method try...except
import math

#ValueError appears if the input isn't an integer and positive
try:
   x = int(input('Please enter a positive number:\n')) #ValueError
   print ('4' / 0) #TypeError and ZeroDivisionError
   name = f #NameError (f is not defined)
   try:
        print(f'Square Root of {x} is {math.sqrt(x)}')
   except ValueError as ve:
        print(f'You entered {x}, which is not a positive number.')
except ValueError as ve:
    print('You are supposed to enter positive number.')

#handle multiple exceptions
except (TypeError, ZeroDivisionError):
   # TypeError and ZeroDivisionError
   print('Exception for typeError and ZeroDvisionError:')
   print('TypeError: cannot concatenate str and int objects')
   print('ZeroDivisionError: integer cannont divide or modulo by zero')
   
#handle all other exceptions
except:
   print("Input wrong try again\n")

