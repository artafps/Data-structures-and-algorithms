from tabulate import tabulate

n = int(input("The number of rows of the matrix 1 :"))
m = int(input("The number of columns of the matrix 1 :"))
n2 = int(input("The number of rows of the matrix 2 :"))
m2 = int(input("The number of columns of the matrix 2 :"))
def normalToSparse (n,m):
    while n<2 and m<2 :
        n = int(input("The number of rows and columns of the matrix :"))
    matrix = []
    matrixSparse = [[n,m,0]]
    for i in range(0,n,1):
        rows = []
        for j in range(0,m,1):
            print("The row",i ,"of the column",j,":+>")
            inp=int(input())
            if(inp!=0):
                matrixSparse[0][2] += 1
                matrixSparse.append([i,j,inp])
            rows.append(inp)
        matrix.append(rows)
    return matrixSparse        

class saveSparse:
    def __init__(self,val) :
        self.arrMS=val
    def __add__(self,newMS):
        if(self.arrMS[0][0] == newMS.arrMS[0][0]):
            if(self.arrMS[0][1]==newMS.arrMS[0][1]):
                newArrSumSparse=newMS.arrMS
                for i in range(1,len(self.arrMS),1):
                    notFind = True
                    for j in range(1,len(newMS.arrMS),1):
                        
                        if(self.arrMS[i][0] == newMS.arrMS[j][0] and self.arrMS[i][1] == newMS.arrMS[j][1]):
                            newArrSumSparse[i][2] = newMS.arrMS[j][2] +  self.arrMS[i][2]
                            notFind = False
                    if(notFind):
                        newArrSumSparse[0][2] = newArrSumSparse[0][2] + 1
                        newArrSumSparse.append(self.arrMS[i])
                return newArrSumSparse            
            else: 
                return -1
        else: 
            return -1
    # def __mul__(self,newMS):
    #     martrix=newMS.arrMS
    #     if(len(self.arrMS) > len(newMS.arrMS) ):
    #         martrix = self.arrMS
    #     if(self.arrMS[0][0] == newMS.arrMS[0][1]):
    #           arryFinal = [[self.arrMS[0][0] , newMS.arrMS[0][1],0]]
    #           for k in range(1,len(martrix),1):
    #               for k2 in range(1,len(newMS.arrMS),1):
    #                   if(martrix[k][0]==newMS.arrMS[k2][1] and martrix[k][1]== newMS.arrMS[k2][0]):
    #                       arryFinal[0][2] = arryFinal[0][2] + 1
    #                       if(len(arryFinal)<2):
    #                           arryFinal.append([martrix[k][0],newMS.arrMS[k2][1],martrix[k][2]*newMS.arrMS[k2][2]])
    #                       for D in range(1,len(arryFinal),1):   
    #                           if(arryFinal[D][0]==martrix[k][0] and arryFinal[D][1] == newMS.arrMS[k2][1]):
    #                               arryFinal[D][2] += martrix[k][2]*newMS.arrMS[k2][2]        
    #                           else:
    #                               arryFinal.append([martrix[k][0],newMS.arrMS[k2][1],martrix[k][2]*newMS.arrMS[k2][2]]) 
    #           return arryFinal                   
    #     else: 
    #       return -1
    def transpose(self):
        matrisN = [[self.arrMS[0][1],self.arrMS[0][0],self.arrMS[0][2]]]
        for i in range(1,len(self.arrMS),1):
            matrisN.append([self.arrMS[i][1],self.arrMS[i][0],self.arrMS[i][2]])
        return  matrisN   
print("matrix 1")    
matrix = normalToSparse(n,m)
print("matrix 2")
matrix2 = normalToSparse(n2,m2)
clMS1=saveSparse(matrix)
clMS2=saveSparse(matrix2)
sums= clMS1+clMS2
print("is sums matrixSpars")
print(tabulate(sums,tablefmt="grid") )
sumNew = saveSparse(sums)
print("is sums transpose")
print(tabulate(sumNew.transpose(),tablefmt="grid"))

#  tabulate(matrix,tablefmt="grid")


