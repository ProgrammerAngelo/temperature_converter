
def temperature_converter():
    #  method for choosing the convertion type
    while True:
        print("Select a convertion type: \nInput 1 for Celcius to farenhiet \nInput 2 for farenheit to celcius")
        #for getting the user choice
        choice = int(input("Input number 1 or 2: "))
        #for asking to input again when the user input numbers beside 1 and 2
        if choice in [1,2]:
            break
        else:
            print("Invalid. Please input 1 or 2.")
    #for inputing temperature
    temp = float(input("Input temperature: "))

    if choice == 1:
        converted_temp = (temp * 9/5) + 32
        print(f"{temp} °C is equal to {converted_temp} °F")
    elif choice == 2:
        converted_temp = (temp - 32) * 5/9
        print(f"{temp} °F is equal to {converted_temp} °C")

temperature_converter()
# method for selecting the convertion type