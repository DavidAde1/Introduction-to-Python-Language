# Introduction-to-Python-Language
<<<<<<< HEAD
## Agree.py
This code prompts the user to input whether they agree or not by displaying the message "Do you Agree?" and then waits for the user to input a response.

Then, the code checks if the user's response is either "Y" or "y" (which means Yes) by using an if statement and checking if the response is in the list ["Y", "y"]. If the response is in the list, the code will print "Agreed."

If the user's response is not "Y" or "y", the code checks if the response is either "N" or "n" (which means they did not agree) using an elif 
statement and checking if the response is in the list ["N", "n"]. If the response is in the list, the code will print "Not Agreed."

## Avrgscores.py
This code prompts the user to input three scores, one at a time using a for loop. It then stores these scores in a list called scores. Afterward, it calculates the average of the scores by summing the scores and dividing by the number of scores. Finally, it prints out the average score.

## calculator.py
This code prompts the user to enter two integer values for x and y using the input() function. It then converts the user input from a string to an integer using the int() function and assigns the values to the variables x and y. Finally, it adds the values of x and y together using the + operator and prints the result of the addition to the console using the print() function.

## compare.py
This code prompts the user to input two integer values for x and y. It then uses an if statement with logical operators to compare the values of x and y. If x is less than y, it prints the message "x is less than y". If x is greater than y, it prints the message "x is greater than y". If x is neither less than nor greater than y, it prints the message "x is equal to y".

## list.py
This code creates a list called my_list with three elements: "January", "February", and "March". The code then prints the second element of the list, which is "February". The append() function is used to add the element "April" to the end of the list. The code then prints the third element of the list, which is now "April". The last element of the list is printed using the index -1. The insert() function is used to add the element "May" to the fourth position (index 3) of the list. The code then prints the entire list, which now contains four elements: "January", "February", "March", and "May". Finally, the pop() function is used to remove the last element of the list, "May", and the updated list is printed.

## main.py
This code prompts the user to input a number of days, converts the number of days to minutes, and then prints the result. The code defines a function called "days_to_units" that takes in a number of days and returns a string that says how many minutes are in that many days. The code also defines a function called "validate_and_execute" that takes in user input, converts it to an integer, and then checks if the integer is positive. If the integer is positive, it calls the "days_to_units" function and prints the result. The code then uses a while loop to continuously prompt the user to input a number of days until the user types "exit". The code splits the user's input into a list of strings, converts each string to an integer, and then calls the "validate_and_execute" function for each integer in the list.

## mario.py
This code prompts the user to input a positive integer value for the height using a while and for loop. If the user inputs a non-integer value, the code will print "Not a valid integer" and prompt the user to input a valid integer value again. Once the user inputs a valid integer value greater than 0, the code will print "#" for the number of times specified by the user's input value.

## names.py
This code imports the sys library and creates a list of names. It then prompts the user to input a name and checks if the name is in the list of names using the if statement. If the name is found in the list, the code prints "Found" and exits with a status code of 0. If the name is not found in the list, the code prints "Not Found" and exits with a status code of 1. The sys library is used to exit the program with a status code.

## phonebook.py
This code creates a dictionary called "people" that stores the names and phone numbers of four individuals. It then prompts the user to enter a name. If the entered name is found in the dictionary, the corresponding phone number is retrieved and printed to the console. If the entered name is not found in the dictionary, nothing is printed.

## phonebook1
This code imports the csv module, which provides functionality to read and write CSV files . The code then opens a file named "phonebook.csv" in append mode using the with statement, which automatically closes the file when the block of code is finished executing.

The user is then prompted to enter a name and a number, which are stored in the name and number variables.

The csv.DictWriter class is used to write the name and number variables to the phonebook.csv file as a new row. The fieldnames parameter specifies the column names for the CSV file. The writerow method writes a dictionary of values to the CSV file as a new row.

## practice1.py
This code prompts the user to input a number as a string, which is then converted to an integer and stored in the variable b. The code then defines a function called show_meow that takes an input parameter a. The function checks if the input integer is greater than or equal to 3, and if so, it prints the string "meow". If the input integer is less than 3, it prints the string "Number cannot print word". If the input is not a valid integer, it prints the string "Not valid input". Finally, the function is called with the integer value stored in b as its input parameter.

## practice2.py
This code is a Python script that uses a while loop to print the word "meow" three times.

The script initializes a variable i to 0, and then enters a while loop that continues as long as i is less than 3. Within the loop, the script prints the string "meow" using the print() function, and then increments the value of i by 1 using the += operator.

This process repeats until i is no longer less than 3, at which point the loop exits and the script terminates.

## practice3.py
This code is a for loop that prints the string "meow" three times. The loop iterates three times, with the variable i taking on the values 0, 1, and 2. Each time through the loop, the print() function is called with the argument "meow", causing the string "meow" to be printed to the console three times.

## set.py
This code defines a set of three elements, "January", "February", and "March", and then iterates through each element in the set and prints it out.

Then, the code adds a new element "April" to the set using the add() method and prints out the updated set.

Finally, the code removes the element "March" from the set using the remove() method and prints out the updated set.
=======

>>>>>>> de2b3205b568cebfaff7208babd0038b325c4af0
