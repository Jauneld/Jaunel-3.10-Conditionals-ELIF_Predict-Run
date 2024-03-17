#Jaunel Deans
#October 24, 2023
#We are predicting what the code will do when it runs. The predictions should be added to the code as comments.

# Example code 1

number = 7# Assigning the value 7 to the variable number(global variable)
print("I have thought of a number between 1 and 10")# Printing the string "I have thought of a number between 1 and 10"
guess = int(input("Can you guess what it is?"))# Assigning the input to the variable guess. The input can only be an integer/whole number. The computer will print out "Can you guess what it is?"

if guess == number:# If the guess value is equal to the value of number then the indented code will run
  print("Correct!")# Printing the string "Correct!"
elif guess < number:#If the first statement if false then the code will check if the guess value is less than the value of number. If it is then the indented code will run
  print("Too Low!")# Printing the string "Too Low!"
else:#If both codes above are false then the code will run
  print("Too High!")# Printing the string "Too High!"

##My code allows the user to input a number larger the 10 and smaller the 1. An improvement to the code will require the user to stick to numbers between 0 to 10. 
#if guess < 0 or guess > 10:
#  print("Please enter a number between 0 and 10")

# Example code 2

number1 = int(input("Please enter a number"))# Assigning the input to the variable number1. The input can only be an integer/whole number. The computer will print out "Please enter a number"
number2 = int(input("Please enter another number"))# Assigning the input to the variable number2. The input can only be an integer/whole number. The computer will print out "Please enter another number"

if number1 > number2:# If the first statement if false then the code will check if the number1 value is greater than the number2 value. If it is then the indented code will run
  print("Number 1 is bigger than number 2")# Printing the string "Number 1 is bigger than number 2"
elif number2 > number1: #If the first statement if false then the code will check if the number2 value is greater than the number1 value. If it is then the indented code will run
  print("Number 2 is bigger than number 1")# Printing the string "Number 2 is bigger than number 1"
else:#If both codes above are false then the code will run
  print("Both numbers are the same")# Printing the string "Both numbers are the same"

