#Shop-The-Look Lens Assignment 
#3Find the sum of all the numbers in a string which is divisible by 3 and also find the last 
#such number. Example "The best 6 of 8 will get 9 points", sum = 12, last=9. 
import re
def sum_and_last_divisible_by_3(input_string):
    # Extract numbers from the string
    numbers = re.findall(r'\d+', input_string)
    
    # Initialize variables
    total_sum = 0
    last_divisible_by_3 = None
    
    # Iterate through the numbers
    for number in numbers:
        number = int(number)
        if number % 3 == 0:
            total_sum += number
            last_divisible_by_3 = number
    
    # Return the total sum and the last number divisible by 3
    return total_sum, last_divisible_by_3

# Test the function with an string
input_string = input()
total_sum, last_divisible_by_3 = sum_and_last_divisible_by_3(input_string)
print("Total sum of numbers divisible by 3:", total_sum)
print("Last number divisible by 3:", last_divisible_by_3)
