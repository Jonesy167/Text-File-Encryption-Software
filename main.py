#################  tested with python 3.6 x86 on Win 10 home using text files  ###########################################

#import modules
import os
import sys
import pathlib
import binascii
import subprocess
import warnings


print ("")
print ("")
print ("")

task1 = (input ("Press 1 to encrypt, press 2 to decrypt       "))


if task1 in ["1"]:
    import encrypt

elif task1 in ["2"]:
        import decrypt

#check for valid input i.e 1 or 2
else:
    print ("")
    print("valid options 1 to encrypt, 2 to decrypt only, exiting now")
    sys.exit(888)
	

(input (""))