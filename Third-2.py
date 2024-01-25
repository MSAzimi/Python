import re
c=int(input())
values=[]
for i in range(c):
    value=input()
    values.append(value)
lists=[]
for k in values:
    a=re.findall('@(.+)$',k)
    lists.append(a)
new_lists=[]
for j in range(0,len(lists)):
    if lists[j]!=[]:
        new_lists.append(lists[j][0])
    else:
        pass
m=set(new_lists)
n=sorted(m)
for g in n:
    print(g)