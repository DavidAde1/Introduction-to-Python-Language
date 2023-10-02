calculation_to_seconds = 24 * 60 

user_input = input("Hey user,enter number of days i will convert to minutes!\n")
#function parameters
def days_to_units(num_of_days):
     return  (f"{num_of_days} days are { num_of_days * calculation_to_seconds} minutes")
   
# A function
def validate_and_execute():

    try:
        user_inputnumber = int(number_of_days) 
        
        # conversion of positive numbers to minutes
        if user_inputnumber > 0:
            calculated_hours = days_to_units(user_inputnumber)
            print(calculated_hours)
        elif user_inputnumber == 0:
            print ("You entered 0,please enter a valid integer")
            
    except ValueError:
        print("Your input is not a valid number,please enter a number")    

user_input = ""
while user_input != "exit":
        user_input = input("Hey user,enter number of days i will convert to minutes!\n")
        list_of_days = user_input.split()
       
        print(list_of_days)
        print(set(list_of_days))
        
        print(type(list_of_days))
        print(type(set(list_of_days)))
        
        #list------make sure there are spaces between the numbers
        for number_of_days in set(list_of_days):
            validate_and_execute() 

