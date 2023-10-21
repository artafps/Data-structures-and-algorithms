"""
power by artafp
url : artafp.ir , gethub.com/artafp

"""
class decimalNumber:
    def __init__(self,number) :
        self.correct = number.split(".")[0]
        self.decimal = number.split(".")[1]
    def __str__ (self):
        return f"{self.correct}.{self.decimal}"
    def __add__ (self,decimalN):
        addCorrect = str(int(decimalN.correct)+int(self.correct))
        DN1 ,DN2 = decimalN.decimal,self.decimal
        while(len(DN1) != len(DN2)):
            if(len(DN1)>len(DN2)):
                DN2 += "0"
            if(len(DN2)>len(DN1)):
                DN1 += "0"
        addDecimal = str(int(DN1)+int(DN2)) 
        D = 0
        newAddDecimal = addDecimal
        if(len(addDecimal)>len(DN1)):
            newAddDecimal = ""
            D = 1
            for i in range(1, len(addDecimal), 1):
                newAddDecimal += addDecimal[i]
        return decimalNumber(f"{int(addCorrect)+D}.{newAddDecimal}") 
    def __mul__ (self,decimalN):
        mulSelf = f"{self.correct}{self.decimal}"
        mulDecimalN = f"{decimalN.correct}{decimalN.decimal}"
        mul = str(int(mulDecimalN) * int(mulSelf))
        retMulCorrect = ''
        retMulDecimal = ''
        lenDecimalMUl = len(self.decimal) + len(decimalN.decimal)
        for i in range(0,len(mul)-lenDecimalMUl,1):
            retMulCorrect += mul[i]
        for i in range(len(mul)-lenDecimalMUl,len(mul),1):
            retMulDecimal += mul[i]
        return decimalNumber(f"{retMulCorrect}.{retMulDecimal}") 
    
print("Please enter the numbers correctly")
number1 = input("type number 1 :")
number2 = input("type number 2 :")
newNumberDecimal1 = decimalNumber(number1)
newNumberDecimal2 = decimalNumber(number2)
print("number 1 :",newNumberDecimal1)
print("number 2 :",newNumberDecimal2)
print("sum :",newNumberDecimal1+newNumberDecimal2)
print("mul :",newNumberDecimal1*newNumberDecimal2)
