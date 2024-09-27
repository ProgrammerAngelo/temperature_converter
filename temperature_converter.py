# method for inputing temperature
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
    
    temp = float(input("Input temperature: "))

temperature_converter()
# method for selecting the convertion type