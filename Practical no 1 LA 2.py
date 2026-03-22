name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

total = 0
print("\nEnter Monthly Purchase Amounts:")

for i in range(12):
    amount = float(input(f"Month {i+1}: "))
    total += amount

print("\n----- Annual Purchase / Billing Report -----")
print("Vendor Name        :", name)
print("Year of Association:", year)
print("Contact Number     :", contact)
print("Email ID           :", email)

print("Annual Purchase    : ₹", total)
