# Write a program in Python to convert any temperature from Celcius to Fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Invalid temperature: Cannot be less than absolute zero."
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
print(f"{celsius} degree Celsius is equal to {convert_celsius_to_fahrenheit(celsius)} degree Fahrenheit.")
