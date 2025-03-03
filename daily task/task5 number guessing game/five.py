# Task 5 – Number Guessing Game 🎯🐍
# 📆 Task Date: 03/03/2025
# 🚀 Mission:
# Create a simple number guessing game where the user has to guess a randomly generated number.
# 💡 Instructions:
# 1️⃣ The program will generate a random number between 1 and 100.
# 2️⃣ Ask the user to guess the number.
# 3️⃣ Give hints: “Too high” or “Too low” after each incorrect guess.
# 4️⃣ When the user guesses correctly, display a congratulatory message.



import random  # Import the random module

# Step 1️⃣: Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Step 2️⃣: Ask the user to guess the number
print("🎯 Welcome to the Number Guessing Game!")
print("🤔 I have chosen a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))  # User input
    
    # Step 3️⃣: Check the guess and provide hints
    if guess < secret_number:
        print("📉 Too low! Try again.")
    elif guess > secret_number:
        print("📈 Too high! Try again.")
    else:
        # Step 4️⃣: User guessed correctly
        print(f"🎉 Congratulations! You guessed the correct number: {secret_number}")
        break  # Exit the loop
