class stack:
    def __init__(self,val):
        self.stack = []
        self.lenght = int(val)
    def push(self,val):
        if(self.lenght > len(self.stack)):
            self.stack.append(val)
        else:
            return "stack is full"
        return "201"
    def pop(self):
        if(len(self.stack)==0):
            return "stack is empty"
        data = self.stack[-1]
        self.stack = list(list([self.stack[i] for i in range(0,len(self.stack)-1,1) ]))
        return(data)
inputStackLenght=int(input("stack lenght :"))
newStack = stack(inputStackLenght)
inp = input("Enter pop or push or exit>0 :")

while inp!='0' and inp!='exit':
    inp = input("Enter pop or push or exit>0 :")
    if(inp.split(' ')[0]=='push'):
        print(newStack.push(inp.split(' ')[1]))
    elif(inp=='pop'):
        print(newStack.pop())
    else:
        inp = input("The request is incorrect > Enter pop or push or exit>0 :")
