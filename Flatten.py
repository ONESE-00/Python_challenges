def flatten(list_of_lists):
    final_list=list()                        #will be the final list
    for index in range(len(list_of_lists)):  #access the inner list
        for i in list_of_lists[index]:       #access the content of the inner list at a time 
            final_list.append(i)
    return final_list                        
  
print(flatten([[1,2,3],[4,5,6],[7],[8],[9],[10,11]]))
