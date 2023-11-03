def isOperator(c):
    if c != "": return (c in "+-*/")
    else: return False

def checkPriority(c):
    if c in "+-": return 0
    if c in "*/": return 1
    
def isNumber(c):
    if c != "": return (c in "0123456789.")
    else: return False

def runOperator(op, number1, number2):
    if op == "+": return str(float(number1) + float(number2))
    if op == "-": return str(float(number1) - float(number2))
    if op == "*": return str(float(number1) * float(number2))
    if op == "/": return str(float(number1) / float(number2))

def Calculation(expr):
    expr = list(expr)
    stack_o = list()
    stack_n = list()
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if len(expr) > 0: d = expr[0]
        else: d = ""
        if isNumber(c):
            num += c
            if not isNumber(d):
                stack_n.append(num)
                num = ""
        elif isOperator(c):
            while True:
                if len(stack_o) > 0: top = stack_o[-1]
                else: top = ""
                if isOperator(top):
                    if not checkPriority(c) > checkPriority(top):
                        number2 = stack_n.pop()
                        op = stack_o.pop()
                        number1 = stack_n.pop()
                        stack_n.append(runOperator(op, number1, number2))
                    else:
                        stack_o.append(c)
                        break
                else:
                    stack_o.append(c)
                    break
        elif c == "(":
            stack_o.append(c)
        elif c == ")":
            while len(stack_o) > 0:
                c = stack_o.pop()
                if c == "(":
                    break
                elif isOperator(c):
                    number2 = stack_n.pop()
                    number1 = stack_n.pop()
                    stack_n.append(runOperator(c, number1, number2))

    while len(stack_o) > 0:
        c = stack_o.pop()
        if c == "(":
            break
        elif isOperator(c):
            number2 = stack_n.pop()
            number1 = stack_n.pop()
            stack_n.append(runOperator(c, number1, number2))

    return stack_n.pop()


# For Exam : ((4*2)-(3-1))/(8-3*2) = 3.0
my_input = input("Enter String For Calculation : ")
print(Calculation(my_input))
