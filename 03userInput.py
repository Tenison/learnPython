##getting input from user
##examples
##get innput from User

##input only accepts strings!!!NOTE
user_name = input("Please enter your name : \n")##use new line charater to move cursor to next line!!!

print(user_name)

##To use other dataTypes with input(), we must use "Type Casting"
##get two number from user and sum them

first_number = int(input("Please enter frist number: "))

##second input on a new line
second_number =  int(input("Please enter second number: "))

##in the future, I will import the function
def sum(a,b):
    return a+b


result = sum(first_number, second_number)

print(f"the sum is {result}")
