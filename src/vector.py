def sim(q,d): #ngitung similarity dari query sama document  
    dot = dotprod(q,d)
    magq = magvec(q)
    magd = magvec(d)
    kalimag = (magq*magd)
    return dot/kalimag

def dotprod(query,d): #sudah benar
    r = 0
    q = query.keys()
    for i in q:
        x = d.get(i,0)
        r += query[i]*x
    return r
    
def magvec(query): #besar vector
    sum = 0
    q = query.keys()
    for i in q:
        x = query.get(i,0)
        sum += x**2 
    return sum**0.5

def sort(arr,dic): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                dic[j], dic[j+1] = dic[j+1], dic[j] 