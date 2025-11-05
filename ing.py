str=input("enter a string :")
if str.endswith ("ing") :
    str = str + "ly"
else :
    str = str + "ing"
print("modified string :" , str)



output:
enter a string :playing
modified string : playingly
enter a string :play
modified string : playing
