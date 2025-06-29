FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_Celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELCIUS_FACTOR 

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (Celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperaure = float(temp_input)

        unit = input("Is this temperature in Celsius or Farenheit? (C/F): ").strip().upper()


        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            print("Invalid unit.. Please enter 'C' for Celsius or 'F' for Farenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

        if __name__ == "__main__":
            main()
