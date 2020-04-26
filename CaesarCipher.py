#The program is written by using the python pycipher module which dowsnt come built-in with IDE's and needs to be installed seperately thru terrminal or cmd using the command - pip install pycipher
from pycipher import Caesar
def caesar(str):
	n=int(input("Enter the key"))
	print("Your encrypted message is:")
	print(Caesar(key=n).encipher(str))

str=input("Enter the message to be encrypted")
caesar(str)