#import regex to determine if the input is binary or decimal
import re as regex

# the analyzer which it decides if the input is binary or a hex
def input_analyzer (raw_input):
    #the [01] means we are only accepting inputs of 01 while may mga hex na 01 din
    #nag lagay tayo ng {8,} which means ang minimum length para matawag na binary siya is dapa 8 ang length niya
    if regex.fullmatch(r'^[01]{8,}$', raw_input):
        return 'Binary'
    elif regex.fullmatch(r'^[0-9A-Fa-f]+$', raw_input):
        return 'Hexadecimal'
    else:
        return 'Invalid'

# a function to convert hex to binary using bitwise operators
def hex_to_bin (hexa):
    hexcode = int(hexa, 2)
    binary = bin(hexcode)
    complete_binary = binary.zfill(21)
    return complete_binary

# a function to convert binary to hex using bitwise operators
def bin_to_hex (binary):
    bitcode = int(binary, 16)
    hexacode = hex(bitcode)
    return hexacode

#the process (ucs),(utf-8),(utf-16)
def process():
    pass

def main():
    print("choose what encoding scheme:")
    print("unicode  [1]")
    print("utf-8    [2]")
    print("utf-16   [3]")
    user_input = input("Your choice: ")
    #at dahil unpredictable ang user maglalagay tayo ng .replace() method para lahat ng spaces
    #ay matatanggal
    raw_input = input("Enter a Binary/Hexadecimal: ").replace(" ","")
    print(input_analyzer(raw_input))
    

if __name__ == '__main__':
    main()

