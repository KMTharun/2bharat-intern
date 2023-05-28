def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

print("Select conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2): ")

    # Check if choice is one of the two options
    if choice in ('1', '2'):
        temperature = float(input("Enter temperature: "))

        if choice == '1':
            converted_temperature = celsius_to_fahrenheit(temperature)
            print("{}°C = {}°F".format(temperature, converted_temperature))

        elif choice == '2':
            converted_temperature = fahrenheit_to_celsius(temperature)
            print("{}°F = {}°C".format(temperature, converted_temperature))
        break
    else:
        print("Invalid Input")

