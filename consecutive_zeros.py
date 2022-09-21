def consecutive_numbers(number):
    number_list = number.split('1')
    number_list.sort()
    return len(number_list[-1])
print(consecutive_numbers('111000010101'))
