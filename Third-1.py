import re
x=list(map(str,input().split()))
a=[]
b=[]
def regex(x):
    for i in x:
        t=list(i)
        t.pop(0)
        l=''.join(t)
        a.append(int(*re.findall('[0-9]+',l)))

def reg(x):
    for i in x:
        b.append(re.findall('[^\s]',i))

regex(x)
reg(x)
e=[]
for j in a:
   e.append(int(j))

data_dic=dict(zip(e,b))
sorted_e=sorted(e)
sorted_b=[data_dic[num] for num in sorted_e]
d=[]
for i in range(len(sorted_b)):
    d.append(sorted_b[i][0])
print(''.join(d))



