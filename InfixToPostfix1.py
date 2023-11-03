n = input("type infix :")
print(n)
strm = ''
for i in range(0,len(n),1):
    if(n[i] =="*"):
        strm+=n[i-1]+n[i+1]+"*"
for i in range(0,len(n),1):
    if(n[i] =="/"):
        flag = True
        if(len(strm)>0):
            p = False
            m = False
            for j in strm:
                if(n[i-1] == j):
                    p = True
                if(n[i+1] == j):
                    m = True
            if(p and m ):
                strm+="/"
            if(p and not m):
                strm+=n[i+1]+"/"  
            if(m and not p):
                 strm+=n[i-1]+"/"
            if( not p and not m):
                strm+=n[i-1]+n[i+1]+"/"
for i in range(0,len(n),1):
    if(n[i] =="+"):
        flag = True
        if(len(strm)>0):
            p = False
            m = False
            for j in strm:
                if(n[i-1] == j):
                    p = True
                if(n[i+1] == j):
                    m = True
            if(p and m ):
                strm+="+"
            if(p and not m):
                strm+=n[i+1]+"+"  
            if(m and not p):
                 strm+=n[i-1]+"+"
            if( not p and not m):
                strm+=n[i-1]+n[i+1]+"+"
for i in range(0,len(n),1):
    if(n[i] =="-"):
        flag = True
        if(len(strm)>0):
            p = False
            m = False
            for j in strm:
                if(n[i-1] == j):
                    p = True
                if(n[i+1] == j):
                    m = True
            if(p and m ):
                strm+="-"
            if(p and not m):
                strm+=n[i+1]+"-"  
            if(m and not p):
                 strm+=n[i-1]+"-"
            if( not p and not m):
                strm+=n[i-1]+n[i+1]+"-"
print(strm)


# stack



class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def isEmpty(self):
        return True if self.top == -1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self, op):
        self.top += 1
        self.array.append(op)
    def isOperand(self, ch):
        return ch.isalpha()
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
    def infixToPostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while((not self.isEmpty()) and
                      self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
 
        for ch in self.output:
            print(ch, end="")
if __name__ == '__main__':
    exp = input("type is infix : ")
    obj = Conversion(len(exp))
    
    obj.infixToPostfix(exp)
