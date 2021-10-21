##testing validation 

try :
    get_number = int(input("Please enter your input here: \n"))
except ValueError :
    print(f"Invalid Input {ValueError}")
else:
    print(f"the number your entered is {get_number}")


