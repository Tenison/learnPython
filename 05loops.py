##while and for loops
## 01) while loop example 
## 02) for loop example 

###while examples below 
def printNumbers () :
    count = 0
    while(count <= 10) :
        print(f"the number is {count} \n")
        count += 1

##Run the program here
##printNumbers()



##find average of user inputs
def average ():
    total = 0
    count = 0
    while True:
        input_value = input("Please enter a number : ")
        
        if(input_value == "calc"):
            break
        else :
            try:
                total += int(input_value)
                count += 1
            except :
                print("Not a valid input")
                continue
    if count == 0 :
        count += 1 ##so that we don't get undefined in  our calculation
    print(count)
    print(f"The average of the values entered are {total/count}")


##Run the program here
##average()


##
##For loop examples below
##

def printValues () :
    for values in range(5) :
        print(f"the number is {values} \n")


##Run  the program here
printValues()


