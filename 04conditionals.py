##Conditional Statments(if ..else)
##Bio Data examples
##input validation with the help of try:except:else:finall

DEFAULT_VALUE = 0

user_name = input("Please enter your name : ")

##get user age and ensure it an int(validation)
try:   
    user_age = int(input("Please enter your age: "))
except:
    print("Input is not a number, Default Age 0 will be used!!!")
    user_age = DEFAULT_VALUE


if user_age > 18:
    print(f"{user_name}, you are an adault")
else:
    print(f"{user_name}, you are below 18 years")

