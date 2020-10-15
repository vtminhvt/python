def par(m,l,h): 
    i = l 
    j=h-1
    k = m[h] 
  
    while (True):
       while (m[i]<k): i=i+1
       while (m[j]>k): j=j-1
       if (i>=j): break
       m[i],m[j]=m[j],m[i]
       i=i+1
       j=j-1
       
    m[i],m[h]=m[h],m[i]
    return (i) 
  
def QS(arr,l,h):
    st=[]
    p = par( arr, l, h )
    
    st.append(l)
    st.append(p-1)
    st.append(p+1)
    st.append(h)
    print('st=',st)
    while st != []: 
        h=st.pop()
        l=st.pop()
        p = par( arr, l, h )
        print('st=',st)
        if p-1 > l:
            st.append(l)
            st.append(p-1)   
        if p+1 <h:
            st.append(p+1)
            st.append(h)
       
  
m = [4, 3, 5, 1, 2,6,99,-1] 
n = len(m)
print(par(m,0,n-1))
QS(m, 0, n-1) 
print (m)
  

