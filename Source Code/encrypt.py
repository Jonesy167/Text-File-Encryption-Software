print ("***by Jonesy167 https://github.com/Jonesy167***")
print ("")
import sys

def convert(stringname):                                # def function to convert string to integer
    value1 = (stringname.encode('utf-8').hex())
    value2 = int(value1,16)
    return (value2)


####get user to enter password
print ("")
print ("this executable will encrypt the contents of a text file with a user supplied password")
print ("")
print ("")
key = (input ("enter password to encrypt file contents - a minimum of 12 charactors and press enter ***YOU WILL NEED THE SAME PASSWORD TO DECRYPT THE FILE***    "))



#check if password is minimum 16 charactors
length_key = len(str(key))
if length_key < 12:
    print ("")
    print("user key to short, must be at least 12 charactors, exiting now")
    input("")
    sys.exit(999)

if length_key > 24:
    print("")
    print("user password to long, must be no longer than 24 charactors, exiting now")
    input ("")
    sys.exit(999)


print ("")
print ("")

#check key isn't symetrical
key_inv = (key[::-1])
if key_inv in key:
    print("")
    print("Symetrical keys are not allowed e.g. 'dooood', exiting now")
    input("")
    sys.exit(999)

file_path = (input ("drag and drop file or enter full path to file to be encrypted         " ))


#chek if file path is valid
from pathlib import Path
file_name = Path(file_path)
if file_name.is_file():
    print ("")
    print ("")
    print("File path valid encrypting data now")
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
if length_plaintext < 8:
    print("must be at least 8 charactors of plain text to encrypt, add more charactors and try again")
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
    if mixer_int in range(1, 16):
        key_padded = key + key[-2:-1]
    elif mixer_int in range(16, 31):
        key_padded = key + key[-3:-2]
    elif mixer_int in range(31, 46):
        key_padded = key + key[-4:-3]
    elif mixer_int in range(46, 61):
        key_padded = key + key[-5:-4]
    elif mixer_int in range(61, 76):
        key_padded = key + key[-6:-5]
    elif mixer_int in range(76, 91):
        key_padded = key + key[-7:-6]
    elif mixer_int in range(91, 106):
        key_padded = key + key[-8:-7]
    elif mixer_int in range(106, 121):
        key_padded = key + key[-9:-8]
    elif mixer_int in range(121, 151):
        key_padded = key + key[-10:-9]


else:
    split_value = key_int_length // 2
    key_padded = key # no need to add charactor as even number already


#####cut user supplied password in half and create the first 2 key values
key_str_first_half = key_padded[(split_value):]

key_str_second_half = key_padded[:(split_value)]


###create third 'key'
key_str_third = (key[::-1]) #invert key string

#####convert everything to integars so we can do maths #########
k1 = convert(key_str_first_half)

#convert second half of key to integars
k2 = convert(key_str_second_half)

#convert 3rd key key to integars
k3 = convert(key_str_third)

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