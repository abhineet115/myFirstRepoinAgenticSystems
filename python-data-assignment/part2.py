contact={
     "Ravi": "9876543210",
     "Anita": "9123456780",
     "Abhineet": "707947693"
    }
print("All Contacts:", contact)
user_input = input("Enter name of contact person:")
if user_input in contact:
    print(f"Phone number: {contact[user_input]}")
else:
    print("Contact not found")
