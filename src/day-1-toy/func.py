# Write a function is_even that will return true if the passed in number is even.
def is_even(num):
    if num%2==0:
        return True
# Read a number from the keyboard
num = input("Enter a number: ")
print ("Your number is",num)
type(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even_or_odd():
    if num%2==0:
        print ('Even!')
    elif num%2!=0:
        print ('Odd')