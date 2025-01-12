# Global variables 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
try:
    # Prompt user for temperature
    temperature = input("Enter the temperature to convert: ")
    
    # Validate temperature input
    if not temperature.replace('.', '', 1).isdigit() and not temperature.lstrip('-').replace('.', '', 1).isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    temperature = float(temperature)  # Convert to float for accurate calculations

    # Prompt user for temperature type
    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    # Perform the conversion
    if temp_type == "F":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    elif temp_type == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError as e:
    print(e)