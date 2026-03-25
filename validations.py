#use reg ex rather than for loops
import re as regex

def binary (bin):
    binarie = int(bin,2)
    hexa = hex(binarie)
    print(hexa.upper())
def Hexa_to_Binary(val):
    hex = int(val, 16)
    bina = bin(hex)[2:]
    bina = bina.zfill(21)
    print(bina)
    
user_input = input(str("Enter a binary / hexadecimal: "))

#if it is 0 and 1 and greater than 8
if regex.fullmatch(r'^[01]{8,}$', user_input):
    print("It is a Binary you nigga!")
    binary(user_input)
#if less than 8 kase may mga ucs na more than 4 na may 0 and 1
elif regex.fullmatch(r'^[0-9A-Fa-f]+$', user_input):
    print("it is a HEXADECIMAL you nigger!")
    Hexa_to_Binary(user_input)
else:
    print("Invalid input Nigger!")
