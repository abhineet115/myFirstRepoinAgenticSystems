total = 0
while True:
    number = int(input("For exit Press 0 \n Enter a number:"))
    if number==0:
        break
    total += number
print(f"Total:{total}")