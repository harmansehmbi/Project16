print(">> App Started")

numbers = [10, 20, 30, 40 ,50]
a = 10; b = 20; c = 0
c = a//b

idx = int(input("Enter index to view data : "))

try:
    print(numbers[idx])

except IndexError as iRef:
    print("Some Error is occured")

print("c is : ", c)

print(">> App Ended")


# No Crash
