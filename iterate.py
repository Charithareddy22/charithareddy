list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
iterate=iter(list)
print(iterate)
type(iterate)
for i in iterate:
    if (i%20 == 0):
        print(i)
