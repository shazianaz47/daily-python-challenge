# Task 4 – Even or Odd Checker
# Task Date : 01/03/2025

# 🚀 Mission:
# Create a simple program that checks whether a number is Even or Odd.

# 💡 Instructions:
# 1️⃣ Ask the user to enter a number.
# 2️⃣ Check if the number is even or odd using the modulus (%) operator.
# 3️⃣ Display the result in a friendly message.


# Step 1: Ask the user for a number
num = int(input("Enter a number: "))

# Step 2: Check if the number is even or odd using modulus operator
if num % 2 == 0:
    result = "Even"

else:
    result = "Odd"

# Step 3️⃣: Display the result in a friendly message
print(f"🔢 You entered: {num}")
print(f"✅ {num} is an {result} number.")