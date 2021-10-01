##functions
##function to print number of seconds for INPUTED days 

hoursInADay = 24;
minutesInAHour = 60;
secondsInAMinute = 60;

def numberOfSeconds(numberOfDays):
    print(f"The number of seconds in {numberOfDays} are {hoursInADay + minutesInAHour + secondsInAMinute + numberOfDays} seconds");


def endProgram():
    print(f"It Over!!!")

    
numberOfSeconds(308);
endProgram();
