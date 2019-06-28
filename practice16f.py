print(">> App Started")

numbers = [10, 20, 30, 40 ,50]
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = 0


idx = int(input("Enter index to view data : "))

try:
    print(numbers[idx])
    c = a//b


except Exception as eRef:
    print("Some Error Ocurred:", eRef)

finally:
    print("This is Awesome")


# Finally is the block which runs always .. either the exception occurs or not