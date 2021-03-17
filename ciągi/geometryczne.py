def nWyraz(a1=1,q=1,n=1):
    an=a1*q**(n-1)
    return (an)
def suma(a1=1,q=1,n=1):
    if q==1:
        s=a1*n
    else:
        s=a1*(1-q**n)/(1-q)
    return (s)