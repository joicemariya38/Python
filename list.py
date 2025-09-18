numbers=[-3,-1,5,8,0,-4]
print("given input is",numbers)
positive_list=[num for num in numbers if num>0]
squares=[num **2 for num in positive_list]
print("positive numbers",positive_list)
print("squares",squares)
words=input("enter some words")
vowels='aeiouAEIOU'
vowels_list=[char for char in words if char in vowels]
print("vowels in the words are : ",vowels_list)
ordinal_values=[ord(char)for char in words]
print("ordinals values of each character are : ",ordinal_values)