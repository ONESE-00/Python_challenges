'''
Create a function in Python that accepts two parameters. 
The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
If it's "desc," then the list should be in descending order
if it's "none," it should return the original list unaltered.

'''
def sort_list(number_list,sort_type):
    if sort_type == 'asc':
        number_list.sort()
        return number_list

    elif sort_type == 'desc':
        number_list.sort(reverse=True)
        return number_list

    elif sort_type == 'none':
        return number_list

print(sort_list([10,30,7,545,98,78,900],'none'))
