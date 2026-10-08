def missingnumber(a):
    n=len(a)
    expected=n*(n+1)//2
    actual=sum(a)
    return expected-actual
a=[0,1,2,4,5,3,7]
print(missingnumber(a))

