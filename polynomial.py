

print("polynomial Foramt : 2x**6 + 7x**3 + 3")
inputs = input("Enter your polynomial 1:")
inputs2= input("Enter your polynomial 2:")


def typeTopolynomial(value):
    partion = value.split("+")
    level =0
    for i in range(0,len(partion),1):
           if(1<len(partion[i].split("**"))):
               if (level< int(partion[i].split("**")[1])):
                   level = int(partion[i].split("**")[1])
           
    arryPolynomial = []
    for i in range(level,-1,-1):
        notfind = True
        for j in range(0,len(partion),1):
            if(1<len(partion[j].split("**"))):
               if( i == int(partion[j].split("**")[1]) ):
                   arryPolynomial.append(int(partion[j].split("x")[0]))
                   notfind = False                       
            else:
                if(i == 0):
                    notfind = False
                    arryPolynomial.append(int(partion[j]))
        if(notfind):
            arryPolynomial.append(0)
    return [arryPolynomial,len(arryPolynomial)]
class polynomial:
    def __init__(self,arr,length):
        self.polArry =  arr
        self.length = length
    def __str__(self):
        newStrPoly = ""
        for i in range(0,len(self.polArry),1):
            if(self.polArry[i] > 0 or self.polArry[i] < 0):
                if(i>0):
                    newStrPoly += " + "
                newStrPoly += str(self.polArry[i])
                if(len(self.polArry)-1-i>0):
                    newStrPoly += "x**"
                    newStrPoly += str(len(self.polArry)-1-i)
        return newStrPoly
    def __add__(self,newPoly):
        addPoly = [0]
        if(self.length > newPoly.length ):
            for i in range(0,self.length-1,1):
                addPoly.append(0)
            for i in range(-1,-(self.length+1),-1):
                addPoly[i] += self.polArry[i]
            for i in range(-1,-(newPoly.length+1),-1):
                addPoly[i] += newPoly.polArry[i]
        else :
            for i in range(0,newPoly.length-1,1):
                addPoly.append(0)
            for i in range(-1,-(self.length+1),-1):
                addPoly[i] += self.polArry[i]
            for i in range(-1,-(newPoly.length+1),-1):
                addPoly[i] += newPoly.polArry[i]
        
        return polynomial(addPoly,len(addPoly))
    def __mul__(self,newPoly):
        numberMP = self.length + newPoly.length - 1
        mulPoly = []
        for i in range(0,numberMP,1):
            mulPoly.append(0)
        for i in range(self.length-1,-1,-1):
            for j in range(newPoly.length-1,-1,-1):
                index = i + j
                value = newPoly.polArry[j]*self.polArry[i]
                mulPoly[index] += value
        return polynomial(mulPoly,numberMP)  


value1= typeTopolynomial(inputs)
value2= typeTopolynomial(inputs2)

poly1 =  polynomial(value1[0],value1[1])
poly2 =  polynomial(value2[0],value2[1])

print("it is sum :",poly1+poly2)
print("it is mul :",poly1*poly2)
