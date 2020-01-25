# Problem: Write a program for calculating pay where overtime after 40 hours is 1.5x regular rate.


# My solution:
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate) # if h is inputted as a string, this line won't run because line 9 will jump straight to except.
except:
    print("Error: please enter numeric input")
    quit() # this stops us from continuing and getting a traceback error due to r never being defined above.

# if we make it out of the try/except block with no error, move on to here:
if h > 40 :
    reg = r * h
    ot = (h-40)+r*(r*.5)
    pay = reg + ot
else:
    pay = r * h

print("Your total pay is" , pay)
