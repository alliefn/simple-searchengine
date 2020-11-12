def sim(q,d): #ngitung similarity dari query sama document  
    dot = dotprod(q,d)
    magq = magvec(q,q)
    magd = magvec(q,d)
    kalimag = (magq*magd)
    return dot/kalimag

def dotprod(q,d): #sudah benar
    r = 0
    for i in q:
        x = d.get(i,0)
        r += q[i]*x
    return r

def magvec(q,v): #besar vector, x = query atau dictionary
    sum = 0
    for i in q:
        x = v.get(i,0)
        sum += x**2 
    return sum**0.5