x=float(input('ENTER THE VALUE OF X : ' ))
n=int(input('ENTER THE VALUE OF n (FOR X**n) : '))
s=0
for a in range (n+1):
    s+=x**a
print('sum of 1st',n,'terms:',s)
