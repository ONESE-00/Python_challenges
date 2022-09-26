def zap(list1,list2):
    final_list,temp_list=[],[]
    for loop in range(len(list1)):
        temp_list.append(list1[loop])
        temp_list.append(list2[loop])
        temp_tuple=tuple(temp_list)
        tuple(temp_list)
        final_list.append(temp_tuple)
        temp_list=[]
    return final_list
print(zap([1,2,3,4],[2,4,6,8]))

