FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    to_celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR 

    return to_celsius 

def convert_to_fahrenheit(celsius):
    to_fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR 

    return to_fahrenheit

temperature = int(input("Enter the temperature to convert: "))

C_OR_F = input("Is this temperature in celsius or fahrenheit? (C/F): ")

if C_OR_F == "F":
    convert_to_celsius()
    print(f"{temperature}F is {to_celsius}C")
else:
    convert_to_fahrenheit()
    print(f"{temperature}C is {to_fahrenheit}F")