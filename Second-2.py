a=input()
inputs=[]
if a!='sum'and a!='average'and a!='min'and a!='max' and a!='gcd'and a!='lcd':
    print('Invalid command')
else:
    while True:
        b = input()
        if b == 'end':
            break
        else:
            inputs.append(b)
    if a=='sum':
        s=[int(x)for x in inputs if x!='end']
        print(sum(s))
    elif a=='average':
        s = [int(x) for x in inputs if x!='end']
        v=(sum(s)/len(inputs))
        print(round(v,2))
    elif a=='min':
        s = [int(x) for x in inputs if x!='end']
        print(min(s))
    elif a=='max':
        s = [int(x) for x in inputs if x!='end']
        print(max(s))

    elif a=='lcd':
        s = [int(x) for x in inputs if x!='end']
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        def lcm(a,b):
            return(a*b)//gcd(a,b)
        def lcm_original(s):
            result=1
            for num in s:
                result=lcm(result,num)
            return result
        print(lcm_original(s))
    elif a=='gcd':
        s = [int(x) for x in inputs if x!='end']
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        def gcd_original(s):
            result=s[0]
            for i in range(1,len(s)):
                result=gcd(result,s[i])
            return result
        print(gcd_original(s))
