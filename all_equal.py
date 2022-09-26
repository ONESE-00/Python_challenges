'''
Get the input list
If list has length of 0 or 1 == return TRUE
IF the len() is greater than 1 ..
use a range from 1 to the len(list)
compare the first item-type with the next..
    if for this case the types aren't equal return FALSE
    else continue looping until the end

If the list has passed the above check now compare the values..
    compare the first item value with the next one
    if for a single case the item values don't match return FALSE
    else continue to loop till the end

If the list has successfully reached this point.. return TRUE

'''

def all_equal(input_list):
    length=len(input_list)
    check=bool()
    if (length == 0) or (length == 1):   #if len() is 0 or 1 return TRUE
        return True
    else:           #len() is greater than 1
        for loop in range(1,length):        #use this range to compare the type
            if type(input_list[0]) != type(input_list[loop]):
                return False
            else:
                check = True
        for loop2 in range(1,length):
            if input_list[0] != input_list[loop2]:
                return False
            else:check = True
    return True

print(all_equal([1,1,1,1,1,1,1,'1']))

