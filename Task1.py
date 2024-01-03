print("Enter any three numbers")
"""
Користувач вводить три цифри з клавіатури. 
Залежно від вибору користувача програма виводить на екран максимум із трьох, 
мінімум із трьох або середньоарифметичне трьох чисел.
"""
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number"))
third_number = float(input("Enter third number"))

operation = input("Select an operation")

if operation == "min":
    result = min(first_number, second_number, third_number)
    print(f"Minimum {result}")
elif operation == "max":
    result = max(first_number, second_number, third_number)
    print(f"Maximum {result}")
elif operation == "avg":
    result = (first_number + second_number + third_number) / 3
    print(f"Average {result}")


