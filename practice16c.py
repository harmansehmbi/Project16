print(">> App Started")

numbers = [10, 20, 30, 40 ,50]
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = 0

c = a//b

idx = int(input("Enter index to view data : "))

try:
    print(numbers[idx])
    c = a//b                  # will give error ... problem not solved when we divide by zero

except IndexError as iRef:
    print("Some Error is occured")

