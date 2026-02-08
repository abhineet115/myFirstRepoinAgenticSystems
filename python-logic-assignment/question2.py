age = int(input("Enter your age:"))

id = input("Has ID:").strip().lower()
if id =="true":
    id = True
elif  id == "false":
    id = False
else:
        print("Invalid input. Please type 'True' or 'False'.")

if age>=18 and id ==True:
    print("Entry allowed")
else :
    print("Entry Not allowed")
