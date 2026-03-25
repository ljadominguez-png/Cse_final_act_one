#importing reg ex
import re as regex

#needed binary converter for both binary and hexa to binary.add()
#no Binary to hexa
#realization (the proper use of bitwise operations)
def Binary_to_hex (bin):
    Binary = int(bin,16)#16 kase base 16
    Hex = hex(Binary)
    return hex
    #hex_chars = "0123456789ABCDEF"
    #temp_val = bin
    #raw_hex = ""
    
    #if temp_val == 0: 
    #    raw_hex = "0"
        
    #while temp_val > 0:
    #    remainder = temp_val % 16
    #    raw_hex = hex_chars[remainder] + raw_hex
    #    temp_val = temp_val // 16

    #while len(raw_hex) < 4:
    #    raw_hex = '0' + raw_hex 
    #print()

#no i convert Hexa to binary
def Hexa_to_binary (hex):
    Hexadecimal = int(hex,16)# yong base 16 convert into binary
    binary = bin(Hexadecimal)[2:]#originally kase may 0b siya so need tangalin yon
    binary.zfill(21)#if kulang dag dagas
    return binary
    

def unicode (ucs):
    x =''
    y = ''
    z = ''
    byte_1 = ''
    byte_2 = ''
    byte_3 = ''
    byte_4 = ''
    print()

def utf_eight (utf8):
    x =''
    y = ''
    z = ''
    byte_1 = ''
    byte_2 = ''
    byte_3 = ''
    byte_4 = ''
    print()
    
def utf_sixteen(utf16):
    x =''
    y = ''
    z = ''
    byte_1 = ''
    byte_2 = ''
    byte_3 = ''
    byte_4 = ''
    print()

def decider (option):
    if option == "Unicode[1]":
        unicode(input(str('[Unicode] Enter a Hexadecimal or Binary: ')))
    elif option == "utf-8[2]":
        utf_eight(input(str('[utf-8] Enter a Hexadecimal or Binary: ')))
    elif option == "utf-16[3]":
        utf_sixteen(input(str('[utf-16] Enter a Hexadecimal or Binary: ')))
    #do nothing
    else:
        pass

def binary_or_hexa(code):
    if regex.fullmatch(r'^[01]{8,}$', code):
        print("Detected it is a Binary")
    elif regex.fullmatch(r'^[0-9A-Fa-f]+$', code):
        print("Detected it is a Hexadecimal")
    else:
        print("invalid input") 

#user input nalang muna
user_input = input(str("choose what encoding scheme: (Unicode[1], utf-8[2], utf-16[3]: )"))
choice = user_input
options =""
if choice == '1':
    options = "Unicode[1]"
elif choice == '2':
    options = 'utf-8[2]'
elif choice == '3':
    options == 'utf-16[3]'
else:
    options = 'invalid'

decider(options)

print(f" You choose: {options}")