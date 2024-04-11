#Shop-The-Look Lens Assignment 
#4.There are 100 man making a circle each man is wearing a T-shit with a number 1 to 100 
#in series. Person with Number 1 on his/her T-Shirt got a gun now 1 kill 2 
#and give that gun to 3 and then 3 kill 4 and give that gun to 5.. then so on 
#99 killed 100 and give that gun again to 1.WAP to find which man is left with 
#a gun on his hand at the end ?? 
def find_last_person_with_gun(num_people):
    people = [i + 1 for i in range(num_people)]  
    index = 0  # Starting from the person with the gun (number 1)

    # Iterate until there is only one person left
    while len(people) > 1:
        index_to_remove = (index + 1) % len(people)  # Determine the person to be removed
        people.pop(index_to_remove)                               # Remove the person at the determined index
        index = index_to_remove % len(people)           # Update the index for the next iteration

    return people[0]  # Return the last person remaining with the gun

# Number of people in the circle
num_people = 100
winner = find_last_person_with_gun(num_people)
print("The person left with the gun at the end has T-Shirt number:", winner)
