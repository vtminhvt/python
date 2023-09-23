m= [5,6,3,99,1,8,7,2,4]

for x in range(1,len(m),1):
    t=m[x] #t=1

    for y in range(x-1,-1,-1):
        if (t<m[y]):
            m[y+1]=m[y]

        if (t>m[y]): 
           m[y+1]=t
           break

        if (y==0):
            m[y]=t
print(m)
            
            
