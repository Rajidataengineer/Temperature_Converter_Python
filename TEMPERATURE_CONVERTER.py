# Display options to user
print("\nAvailable Conversions :")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheitto Celsius")
# Get User Choice
choice = input("select your temperature celsius,fahrenheit:")
if choice == "1":
    value = float(input("enter the temperature:"))
    F=((value*1.8)+32)
    print("%.1f°C is equal to %.1f°F" %(value,F))
elif choice == "2":
    value = float(input("enter the temperature:"))
    C=((value-32)/1.8)
    print("%.1f°F is equal to %.1f°C" %(value,C))
else:
    print("Invalid Choice!Please select 1 or 2.")
