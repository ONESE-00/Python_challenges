#break down strings  to lists
#sort list
#compare index to index list agains list

def is_anagram(txt1,txt2):
    if len(txt1) != len(txt2):  #if not equal in length just return FALSE
        return False

    txt1_list=list()            #declare list for each string
    txt2_list=list()

    for loop in txt1:           #transfer txt1 to a list
        txt1_list.append(loop)

    for loop in txt2:           #transfer txt2 to a list 
        txt2_list.append(loop)
    txt1_list.sort()            #sort both list 
    txt2_list.sort()

    for i in range(len(txt1_list)):     #compare index to index, a single mismatch return FALSE 
        if txt1_list[i] != txt2_list[i]:
            return False

    return True                         #if the above search algorithm doesn't find a FALSE return TRUE 

print(is_anagram('tess','test'))
