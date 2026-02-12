def checknum(number):
    if number% 2==0:
        return "Number is Even"
    else:
        return "Number is Odd"
number = int(input("Enter a number:"))
result = checknum(number)
print(result)