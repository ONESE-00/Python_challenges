def largest_difference(list_of_numbers):
   # list_of_numbers.sort()
    #return list_of_numbers[-1] - list_of_numbers[0]
    
    return max(list_of_numbers) - min(list_of_numbers)  #find difference btwn the max and min values of the list

print(largest_difference([2,45,67,34,99,12,7]))
    
