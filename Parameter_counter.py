#returns the number of arguments passed to the function, args is not a must, one can use any par_name as long as it is preceded by a *
def param_count(*args):
    return len(args)    # method
print(param_count(1,2,3,4,5,6))
