employee = (101, "Abhineet", "admin")

print(f"ID: {employee[0]}")
print(f"Name: {employee[1]}")
print(f"Department: {employee[2]}")

if "admin" in employee:
    access_status = "Yes"
else:
    access_status = "No"
print(f"Admin Access: {access_status}")
