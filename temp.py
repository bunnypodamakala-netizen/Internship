def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    celsius = float(input("Enter Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print("Fahrenheit:", result)

elif choice == 2:
    fahrenheit = float(input("Enter Fahrenheit: "))
    result = fahrenheit_to_celsius(fahrenheit)
    print("Celsius:", result)

else:
    print("Invalid choice")
