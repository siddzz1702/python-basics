# Day 2: Temperature Converter
# Convert Celsius to Fahrenheit and vice versa

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    choice = input("Convert (C)elsius or (F)ahrenheit? ").strip().upper()
    
    if choice == "C":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
    elif choice == "F":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")






