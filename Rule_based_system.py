#Rule Based System in AI

# Get input from user
tempe = int(input("Enter temperature: "))

# Apply rules
if tempe > 30:
    print("IF temperature > 30 THEN Weather is Hot")

elif tempe > 20:
    print("IF temperature > 20 THEN Weather is Warm")

else:
    print("IF temperature <= 20 THEN Weather is Cold")
