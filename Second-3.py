number=[]
base=[]
jam=[]
while True:
    a, b = map(int, input().split())
    if a==-1 and b==-1:
        break
    else:
        number.append(a)
        base.append(b)
for i in base:
    if i<2 or i>9:
        print('invalid base!')
        break
else:
    def X(n):
        sum=0
        for i in range(1, n+1):
            if n % i == 0:
                sum=i+sum
        return sum
    for c in number:
        d=X(c)
        jam.append(d)

    def numberToBase(n, b):
        digits = []
        while n:
            digits.append(str(n % b))
            n //= b
        return digits[::-1]
    total=0
    for e in range(0,len(jam)):
        h=numberToBase(jam[e],base[e])
        result=int(''.join(h))
        total+=result

    print(total)