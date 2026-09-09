# Program is from Week 1 Task 2 of the python course.

first_number_text = input("Enter the first number: ")
second_number_text = input("Enter the second number: ")
third_number_text = input("enter the third number: ")
# added a third number to the equation and had to add it everywhere else to work
first_number = float(first_number_text)
second_number = float(second_number_text)
third_number = float(third_number_text)

# Where the error was that I'm using for Week 4 Assignment 1
# total = first_number + second_number + third_number_text
total = first_number + second_number + third_number
# mistakenly had third_number auto fill to third_number_text which caused an error
# Enter the first number: 9
#Enter the second number: 45
#enter the third number: 33
#Traceback (most recent call last):
#  File "c:\Users\ube8970\OneDrive - swtc.edu\Attachments\SWTC Class\Python Programming 26-27\Week_4\Task_2.py", line 13, in <module>
#    total = first_number + second_number + third_number_text
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
#TypeError: unsupported operand type(s) for +: 'float' and 'str'
# Listed error code 
# Error solution was to change third_number_text to third_number in the total equation, the third_number_text is a string and the third_number is a float, which I found by getting the original error and rereading my code to see the error

print("first numbers: ", first_number)
print("second numbers: ", second_number)
print("third numbers: ", third_number)
# mistakenly capitalized P causing the third print not to work 
print("total: ", total)