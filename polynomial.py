from tabulate import tabulate

print("polynomial Foramt : 2x**6 + 7x**3 + 3")
f = input("Enter your polynomial :")
partion = f.split("+")
print(partion)
level = 0
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
                arryPolynomial.append(int(partion[j]))
                notfind = False
    if(notfind):
        arryPolynomial.append(0) 
print(arryPolynomial)
