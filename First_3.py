a=int(input())
b=int(input())
num1=bin(a)[2:]
num2=bin(b)[2:]
num3='0'*(32-len(num1))+num1
num4='0'*(32-len(num2))+num2
num=num4+num3
c=int(input())
values=[]
for i in range(c):
    if c<1 or c>64:
        break
    else:
        value=int(input())
        values.append(value)

output=[]
for value in values:
    if value<0 or value>63:
        break
    else:
        if num[-value-1]=='1':
            output.append('yes')
        elif num[-value-1]=='0':
            output.append('no')
        else:
            pass

for i,result in enumerate(output):
    print(result)
