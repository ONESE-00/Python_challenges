#this functions determines whether the index is exclusively -OR in both lists
def list_xor(index,list1,list2):
    '''
    if (index in list1 and index in list2) or (index not in list1 and index not in list2):
        return False
    elif index in list1 or list2:
        return True
    '''

    return (index in list1) ^ (index in list2)  #returns TRUE if they are different

print(list_xor(1,[0,0,0],[4,5,6]))
