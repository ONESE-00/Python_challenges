'''
Create a function in Python that accepts a single word and returns the number of vowels in that word. 
In this function, only a, e, i, o, and u will be counted as vowels — not y.

'''
def count_vowels(word):
    vowel_counter=0
    for letter in word:
        if letter =='a' or letter =='A' or letter =='E' or letter =='e' or letter =='i' or letter =='I' or letter =='O' or letter =='o' or letter =='U' or letter =='u':
            vowel_counter+=1
        '''
        #method 2
        if letter in 'aeiouAEIOU':
            vowel_counter+=1
        
        #method 3
        if letter == 'a':
            vowel_counter+=1
        elif letter == 'e':
            vowel_counter+=1
        elif letter == 'i':
            vowel_counter+=1
        elif letter == 'o':
            vowel_counter+=1
        elif letter == 'u':
            vowel_counter+=1
        else:
            vowel_counter+=0
        '''
    return vowel_counter
print(count_vowels('onEse gachogu'))
