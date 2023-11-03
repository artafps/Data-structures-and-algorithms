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


