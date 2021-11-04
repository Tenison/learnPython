##Program to separate Even and Odd Number

## Test Cases
## --> NUMBER_LIST = []
## OR
NUMBER_LIST = [1,2,4,5,7,10,13,15,16,19,22,34,55,78,81,88,89,95,96,97,100,104, 109,110,112]
 

even_list = list()
odd_list = list()

def even_and_odd (input_list):
    ## if number list is zero
    if len(input_list) == 0:
        print("There are no numbers in the list")
        return 0
    else:
        for value in input_list:
            if (value % 2) == 0:
                even_list.append(value)
            else:
                odd_list.append(value)
        return 1

if(even_and_odd(NUMBER_LIST)):
    print(f"Even Numbers = {even_list}")
    print(f"Odd Numbers = {odd_list}")


##Delete original list to create space
del(NUMBER_LIST)


