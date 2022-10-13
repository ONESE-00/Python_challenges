
def arithmetic_operation(expression):
    exp = expression.split()
    #if sum
    if exp[1] == '+':
        op1,op2=int(exp[0]),int(exp[2])
        return op1 + op2

    #if substraction
    if exp[1] == '-':
        op1, op2 = int(exp[0]), int(exp[2])
        return op1 - op2
    #if multiplication
    if exp[1] == '*':
        op1, op2 = int(exp[0]), int(exp[2])
        return op1 * op2
    #if division
    if exp[1] == '//':
        if exp[2] == '0':
            return -1
        else:
            op1, op2 = int(exp[0]), int(exp[2])
            return op1 // op2

print(arithmetic_operation('12 // 0'))
