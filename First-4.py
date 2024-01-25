
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            return False

    return True

a,b=map(int,input().split())
count=0
for num in range(a,b+1):
    if is_prime(num):
        count+=1
for num in range(b,a+1):
    if is_prime(num):
        count+=1
if a<0 or a>1000 or b<0 or b>1000:
    print()
else:
    if a<b :
        print('main order - amount: ',count)

    elif a>b:
        print('reverse order - amount: ',count)
    elif a==b:
        if is_prime(num):
            print('main order - amount: ',count-1)
        else:
            print('main order - amount: ',count)
