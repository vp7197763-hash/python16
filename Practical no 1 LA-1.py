name = input("Enter name: ")
emp_id = int(input("Enter employee id: "))
dept = input("Enter department: ")
basic = float(input("Enter basic salary: "))

da = basic * 92 / 100
hra = basic * 58 / 100
ta = basic * 30 / 100
lic = 500

gross = basic + da + hra + ta
net = gross - lic

print("\nEmployee Details")
print("Name:", name)
print("ID:", emp_id)
print("Department:", dept)
print("Net Salary:", net)
print("DA (92/100):", da)
print("Hra (58/100):", hra)
print("TA (30 / 100):", ta)

print("LIC (500/100):", lic)
