n = int(input("Enter the number you want to find the power of: "))
p = int(input("Enter the power you want: "))

r = 1
for i in range(p):
    r = r * n

print("The result is: ", r)