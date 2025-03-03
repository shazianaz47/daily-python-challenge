import time

def smart_calculator():
    while True:
        print("\nSmart Arithmetic Calculator 🧮")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '5':
            print("Exiting... Goodbye! 👋")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter valid numbers.")
            continue
        
        print("\n🧮 Calculating...")
        time.sleep(1)
        
        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '*'
        elif choice == '4':
            if num2 == 0:
                print("❌ Error: Division by zero is not allowed!")
                continue
            result = num1 / num2
            operation = '/'
        
        print(f"📌 Result: {num1} {operation} {num2} = {round(result, 2)}")

smart_calculator()
