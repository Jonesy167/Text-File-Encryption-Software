#!/usr/bin/env python3.6

import sys

#def function to convert string to integer
def convert(stringname):
    value1 = (stringname.encode('utf-8').hex())
    value2 = int(value1,16)
    return (value2)


####get user to enter password
print ("")
print ("this program will now encrypt the contents of a text file using a password")
print ("")
print ("")
print ("enter a password to encrypt file contents - must be a minimum of 16 charactors and then press enter ***YOU WILL NEED THE SAME PASSWORD TO DECRYPT THE FILE***    ")
print("")
key = input()
length_key = len(str(key))

#check if password is minimum 16 charactors, max 24
while length_key not in range(16, 25):
    if length_key <16:
        print("")
        print("user key to short, must be at least 16 charactors")
        print("")
        print ("enter a password to encrypt file contents - must be a minimum of 16 charactors and then press enter ***YOU WILL NEED THE SAME PASSWORD TO DECRYPT THE FILE***    ")
        print("")
        key = (input())
        length_key = len(str(key))
        if length_key in range(16, 25):
            break

    elif length_key > 24:
        print("")
        print("user password to long, must be no longer than 24 charactors")
        print("")
        print("")
        print ("enter a password to encrypt file contents - must be a minimum of 16 charactors and then press enter ***YOU WILL NEED THE SAME PASSWORD TO DECRYPT THE FILE***    ")
        key = input()
        length_key = len(str(key))
        if length_key in range(16, 25):
            break

    else:
        continue


print ("")
print ("")

#check password isn't symetrical
key_inv = (key[::-1])

if key_inv in key:
    print("")
    print("Symetrical passwords are not allowed e.g. 'dsooooooooooosd', exiting now")
    input("")
    sys.exit(999)


##get user to provide file path to target text file
print("drag and drop file to be encrypted         " )
print ("")
file_path = input()


#chek if file path is valid
from pathlib import Path
file_name = Path(file_path)
if file_name.is_file():
    print ("")
    print ("")
    print("encrypting data now")
    print ("")
else:
    print ("")
    print("File doesn't exit, exiting now - check the filepath is correct")
    print ("example filepath: C:\\users\\admin\\desktop\\secret.txt")
    (input (""))
    sys.exit(888)


# read plain text file from file and key as variable
with open (file_path) as p:
    plaintext = p.read()  # read plaintext from file


########check to make sure plain_text is long enough, if plain_text is to short exit with code 999

length_plaintext = len(str(plaintext))
if length_plaintext < 12:
    print("must be at least 12 charactors of plain text to encrypt, add more charactors and try again")
    (input (""))
    sys.exit(999)


####check to see if key_int is even number of digits
key_int_length = len(str(key))
remainder1 = key_int_length % 2


###### check if key length is even, if it isn't append a charactor to end based on the bellow logic
mixer = key[-6:-5]  # read sixth charactor from end of key as variable mixer
mixer_int = convert(mixer)


if remainder1 is 1:
    key_int_length = key_int_length + 1
    split_value = key_int_length // 2

#padd the key to even length based on the bellow logic
    if mixer_int in range(1, 10):           #for single byte value UTF8 character
        key_padded = key + key[-2:-1]
    elif mixer_int in range(10, 20):
        key_padded = key + key[-3:-2]
    elif mixer_int in range(20, 30):
        key_padded = key + key[-4:-3]
    elif mixer_int in range(30, 40):
        key_padded = key + key[-5:-4]
    elif mixer_int in range(40, 50):
        key_padded = key + key[-6:-5]
    elif mixer_int in range(50, 60):
        key_padded = key + key[-7:-6]
    elif mixer_int in range(60, 70):
        key_padded = key + key[-8:-7]
    elif mixer_int in range(70, 80):
        key_padded = key + key[-9:-8]
    elif mixer_int in range(80, 90):
        key_padded = key + key[-10:-9]
    elif mixer_int in range(90, 100):
        key_padded = key + key[-11:-10]
    elif mixer_int in range(100, 110):
        key_padded = key + key[-12:-11]
    elif mixer_int in range(110, 120):
        key_padded = key + key[-13:-12]
    elif mixer_int in range(120, 130):
        key_padded = key + key[-14:-13]
    elif mixer_int in range(130, 140):
        key_padded = key + key[-15:-14]
    elif mixer_int in range(140, 255):
        key_padded = key + key[-16:-15]
    elif mixer_int in range(255, 4607):  # take into account UTF8 characters of 2 bytes
        key_padded = key + key[-2:-1]
    elif mixer_int in range(4607, 8959):
        key_padded = key + key[-3:-2]
    elif mixer_int in range(8959, 13311):
        key_padded = key + key[-4:-3]
    elif mixer_int in range(13311, 17663):
        key_padded = key + key[-5:-4]
    elif mixer_int in range(17663, 22015):
        key_padded = key + key[-6:-5]
    elif mixer_int in range(22015, 26367):
        key_padded = key + key[-7:-6]
    elif mixer_int in range(26367, 30719):
        key_padded = key + key[-8:-7]
    elif mixer_int in range(30719, 35071):
        key_padded = key + key[-9:-8]
    elif mixer_int in range(35071, 39423):
        key_padded = key + key[-10:-9]
    elif mixer_int in range(39423, 43775):
        key_padded = key + key[-11:-10]
    elif mixer_int in range(43775, 48127):
        key_padded = key + key[-12:-11]
    elif mixer_int in range(48127, 52479):
        key_padded = key + key[-13:-12]
    elif mixer_int in range(52479, 56831):
        key_padded = key + key[-14:-13]
    elif mixer_int in range(56831, 61183):
        key_padded = key + key[-15:-14]
    elif mixer_int in range(61183, 65535):
        key_padded = key + key[-16:-15]
    elif mixer_int in range(65535, 1179647):  #take into account UTF8 characters of 3 bytes
        key_padded = key + key[-2:-1]
    elif mixer_int in range(1179647, 2293759):
        key_padded = key + key[-3:-2]
    elif mixer_int in range(2293759, 3407871):
        key_padded = key + key[-4:-3]
    elif mixer_int in range(3407871, 4521983):
        key_padded = key + key[-5:-4]
    elif mixer_int in range(4521983, 5636095):
        key_padded = key + key[-6:-5]
    elif mixer_int in range(5636095, 6750207):
        key_padded = key + key[-7:-6]
    elif mixer_int in range(6750207, 7864319):
        key_padded = key + key[-8:-7]
    elif mixer_int in range(7864319, 8978431):
        key_padded = key + key[-9:-8]
    elif mixer_int in range(8978431, 10092543):
        key_padded = key + key[-10:-9]
    elif mixer_int in range(10092543, 11206655):
        key_padded = key + key[-11:-10]
    elif mixer_int in range(11206655, 12320767):
        key_padded = key + key[-12:-11]
    elif mixer_int in range(12320767, 13434879):
        key_padded = key + key[-13:-12]
    elif mixer_int in range(13434879, 14548991):
        key_padded = key + key[-14:-13]
    elif mixer_int in range(14548991, 15663103):
        key_padded = key + key[-15:-14]
    elif mixer_int in range(15663103, 16777215):
        key_padded = key + key[-16:-15]
    elif mixer_int in range(16777215, 301989887):  # #take into account UTF8 characters of 4 bytes
        key_padded = key + key[-2:-1]
    elif mixer_int in range(301989887, 587202559):
        key_padded = key + key[-3:-2]
    elif mixer_int in range(587202559, 872415231):
        key_padded = key + key[-4:-3]
    elif mixer_int in range(872415231, 1157627903):
        key_padded = key + key[-5:-4]
    elif mixer_int in range(1157627903, 1442840575):
        key_padded = key + key[-6:-5]
    elif mixer_int in range(1442840575, 1728053247):
        key_padded = key + key[-7:-6]
    elif mixer_int in range(1728053247, 2013265919):
        key_padded = key + key[-8:-7]
    elif mixer_int in range(2013265919, 2298478591):
        key_padded = key + key[-9:-8]
    elif mixer_int in range(2298478591, 2583691263):
        key_padded = key + key[-10:-9]
    elif mixer_int in range(2583691263, 2868903935):
        key_padded = key + key[-11:-10]
    elif mixer_int in range(2868903935, 3154116607):
        key_padded = key + key[-12:-11]
    elif mixer_int in range(3154116607, 3439329279):
        key_padded = key + key[-13:-12]
    elif mixer_int in range(3439329279, 3724541951):
        key_padded = key + key[-14:-13]
    elif mixer_int in range(3724541951, 4009754623):
        key_padded = key + key[-15:-14]
    elif mixer_int in range(4009754623, 4294967295):
        key_padded = key + key[-16:-15]


else:
    split_value = key_int_length // 2
    key_padded = key # no need to add charactor as even number already


#####cut user supplied password in half and create the 2 key values (these will be k1 and k3)
key_str_first = key_padded[(split_value):]

key_str_third = key_padded[:(split_value)]


###create second key by inverting the key string, this will be as k2)
key_str_second = (key[::-1]) #invert key string


#####convert everything to integars so we can do maths #########

##convert first half of key to integers and multipy by 13
k1 = convert(key_str_first)
k1 = k1 *13


#convert key key to integars and multiply by 29
k2 = convert(key_str_third)
k2 =k2 *29

#convert key_str_second to integers and square
k3 = convert(key_str_second)
k3 = k3 **2

#convert plain text to integars
pt = convert(plaintext)


############do some maths to obviscate the plain text
ct1 = pt * k1

######invert integars by converting to string, inverting string, then back to integers
ct1_string = str(ct1)
ct1_string2 = (ct1_string[::-1]) #invert string

#check to see if first charactor is 0 as if it is it will be dropped when converting to integer, so we will replace it with a 1
first_charactor = (ct1_string2[0:1])

if (first_charactor) is "0":
    ct1_string2 = ct1_string2[1:]  #remove leading "0"
    ct1_string2 = "1" + ct1_string2 # add a 1 instead


ct1_string2 = int(ct1_string2)
ct1 = ct1_string2


#more maths
ct2 = ct1 *k2
ct3 = ct2 *k3


#output to file
output = str(ct3)  # convert to string (can't write integars to file)
f = open(file_path, "w+")  # example file creation
f.write(output)
f.close()  # close file


print ("")
print ("")
print ("finished :) have a nice day")
print ("")
print ("")
input("")
sys.exit(111)
