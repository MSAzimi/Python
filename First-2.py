n=int(input())
m=int(input())
k=int(input())

def sum(n,m):
    while(m!=0):
        a=n&m
        n=n^m
        m=a<<1
    return n
print(sum(n,m))
b=sum(n,m)
if b==k:
    print('YES')
else:
    print('NO')