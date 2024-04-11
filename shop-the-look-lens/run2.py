#Shop-The-Look Lens Assignment 
#2.For the given array [9,33,0,7,2,82,77], WAP to divide each number of the array by the 
#next number. Divide the last number by first number of array. Provide proper 
#exceptional handling for 0
def divide_numbers(arr):
    result = []
    for i in range(len(arr)-1):
        try:
            division_result = arr[i] / arr[i+1]
            result.append(division_result)
        except ZeroDivisionError:
            result.append("Division by zero error")
        try:
            division_result_last = arr[-1] / arr[0]
            result.append(division_result_last)
        except ZeroDivisionError:
            result.append("Division by zero error")
    return result

# Test the function with the given array
arr = [9, 33, 0, 7, 2, 82, 77]
output = divide_numbers(arr)
print(output)
