str=input("enter a string :")
word={}
for char in str:
    if char in word:
        word[char] += 1
    else:
        word[char] = 1
print("character frequency:")
for char,count in word.items():
    print(f"{char}:{count}")

    //enter a string :hello
character frequency:
h:1
e:1
l:2
o:1