#Middle letter
#Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

#For example, mid("abc") should return "b" and mid("aaaa") should return "".
def mid(text):
    length = len(text)
    empty_string = ''
    if length % 2 ==0:
        return empty_string
    if length % 2 != 0:
        index=length // 2
        index_int=int(index)
        return text[index_int]
word='oneh'
print(mid(word))
