'''
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
factors to consider..TYPE, VALUE,
'''
def triple_and(item1,item2,item3):
    #first exception of all FALSE
    if item1 == item2 == item3 == False:
        return False
    #compare the type then value
    if type(item1)  == type(item2) == type(item3):
        if item1 == item2 == item3:
            return  True
        else:
            return  False  #if the values don't all match return FALSE
    else:
        return False       #if the types don't match return FALSE

print(triple_and(False,False,False))
