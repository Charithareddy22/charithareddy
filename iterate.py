list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
iterate=iter(list)
print(iterate)
type(iterate)
for i in iterate:
    if (i%20 == 0):
        print(i)
#without generator
def square(i):
    for i in range(i):
        i = i+2
    return i
res = square(20)
print(res)
#generator
def square(i):
    for i in range(i):
        i = i+2
        yield i
square(10)
for i in square(10):
    print(i)