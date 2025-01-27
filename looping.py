n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, ":")
for i in range(1, n + 1):
    print(i)
sum_numbers = 0
counter = 1
while counter <= n:
    sum_numbers += counter
    counter += 1
print("The sum of all numbers from 1 to", n, "is:", sum_numbers)