
def temperature_converter():
    #  method for choosing the convertion type
    while True:
        print("Select a convertion type: \nInput 1 for Celcius to farenhiet \nInput 2 for farenheit to celcius")
        #for getting the user choice
        choice = int(input("\nInput number 1 or 2: "))
        #for asking to input again when the user input numbers beside 1 and 2
        if choice in [1,2]:
            break
        else:
            print("\nInvalid. Please input 1 or 2.\n")
    #for inputing temperature
    temp = float(input("\nInput temperature: "))
    #for choosing what convertion based on user choice
    if choice == 1:
        #for converting celcius to farenheit
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C = {converted_temp}°F")
    elif choice == 2:
        #for converting farenheit to celcius
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F = {converted_temp}°C")

temperature_converter()