#This Project is develop by mehedi shakeel
#Text To Binarry Using Python
print("##########################################################")
print("Project : Text To Binary Represntation using Python")
print("Name    : Md Mehedi Hasan")
print("ID      : 16201073")
print("SEC     : A2")
print("#########################################################")
print("")
import binascii
text = raw_input("Write Your Text What You Want To Convert in To Binary : ")
print("")
print('You Type : ' + text)
print("")
print("This is the binary Representation of Your Text : ")
print("")
print(' '.join(format(ord(x), 'b') for x in text))
