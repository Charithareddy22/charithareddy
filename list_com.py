list = [1,2,3,4,5]
res = [i for i in list if i < 4]
print(res)
res = [i for i in list if i % 2 == 0]
print(res)
#uppercase
words = ["hello","charitha","reddy"]
uppercase = [i.upper() for i in words]
print(uppercase)
#lowercase
words = ["HELLO","CHARITHA","REDDY"]
lowercase = [i.lower() for i in words]
print(lowercase)
#add
list = [1,2,3,4,5]
res = [i+1 for i in list if i < 4]
print(res)
#creating a dictionary comprehension from two lists
keys = ["name","age","city"]
values = ["banglore", 25 , "Hyderabad"]
dictionary = {k:v for k,v in zip(keys,values)}
print(dictionary)