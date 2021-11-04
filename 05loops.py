## WHILE and O=FOR LOOPS
## -- while loop example 
## -- for loop example 

### -- While examples below

def printNumbers ():
    count = 0
    while(count <= 10) :
        print(f"the number is {count} \n")
        count += 1

##printNumbers()



## -- find average of user inputs
def average ():
    total = 0
    count = 0
    while True:
        input_value = input("Please enter a number : ")
        
        if(input_value == "calc"):
            break
        else:
            try:
                total += int(input_value)
                count += 1
            except:
                print("Not a valid input")
                continue
    if count == 0:
        count += 1 ## so that we don't get undefined in  our calculation
    print(count)
    print(f"The average of the values entered are {total/count}")

##average()


## -- For loop examples below

def printValues () :
    for values in range(5) :
        print(f"the number is {values} \n")

##printValues()


## --- For example Two 

def printList () :
    some_list = [12,13,15,16,20,23,34,44,45,67,77,89,99]

    for value in range(len(some_list)) :
        print(value)

##printList()

## --- For example Three



