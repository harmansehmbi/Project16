print(">> App Started")

numbers = [10, 20, 30, 40 ,50]
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = 0


idx = int(input("Enter index to view data : "))

try:
    print(numbers[idx])
    c = a//b

except IndexError as iRef:
    print("Some Error is occured", iRef)

except ZeroDivisionError as zRef:
    print("Some Error Ocurred:", zRef)

finally:
    print("This is Awesome")



print("c is : ", c)

print(">> App Ended")