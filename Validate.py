'''
Solution validation
The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.
Write a function named validate that takes code represented as a string as its only parameter.
Your function should check a few things:
    the code must contain the def keyword   .... if def not in..
        otherwise return "missing def"
    the code must contain the : symbol      ....if : not in
        otherwise return "missing :"
    the code must contain ( and ) for the parameter list    ...if ( and ) not in
        otherwise return "missing paren"
    the code must not contain ()                            if () in ..
        otherwise return "missing param"
    the code must contain four spaces for indentation
        otherwise return "missing indent"
    the code must contain validate
        otherwise return "wrong name"               ...if validate not in..
    the code must contain a return statement        ....
        otherwise return "missing return"
If all these conditions are satisfied, your code should return True.
Here comes the twist: your solution must return True when validating itself.
'''
def validate(code):
    #check for 'def'
    if 'def' not in code:
        return 'missing def'

    #check for ':'
    if ':' not in code:
        return 'missing symbol'

    #check for (   )
    if '(' and ')' not in code:
        return 'missing paren'

    #check for ()
    if '()' not in code:
        return 'missing param'

    #check for indentation
    if code.startswith('   ') != True:
        return 'missing indent'

    #check for 'validate'
    if 'validate' not in code:
        return 'wrong name'

    #check for 'return'
    if 'return' not in code:
        return 'missing return'

    #if it has passed all tests
    # print(validate())
    return True

print(validate('''    def validate(code):
    #check for 'def'
    if 'def' not in code:
        return 'missing def'

    #check for ':'
    if ':' not in code:
        return 'missing symbol'

    #check for (   )
    if '(' and ')' not in code:
        return 'missing paren'

    #check for ()
    if '()' not in code:
        return 'missing param'

    #check for indentation
    if code.startswith('   ') != True:
        return 'missing indent'

    #check for 'validate'
    if 'validate' not in code:
        return 'wrong name'

    #check for 'return'
    if 'return' not in code:
        return 'missing return'

    #if it has passed all tests
    # print(validate())
    return True

'''))
