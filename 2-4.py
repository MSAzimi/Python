
def is_valid(x_y,n):
    x,y=x_y
    if 0<=x<n:
        return True
    else:
        return False
def move(d,x,y):
    if d=='R':
        return (x+1,y)
    elif d=='L':
        return (x-1,y)
    elif d=='B':
        #print("" , x , "" , y - 1)
        return (x,y+1)
n=int(input())
moves = []
while True:
    moving = input().strip()
    if moving == 'END':
        break
    moves.append(moving)
b=moves.count('B')
#print(len(moves))
locations=[]
locations.append((0,0))
for i in range(len(moves)):
    if is_valid(move(moves[i],locations[len(locations)-1][0],locations[len(locations)-1][1]),n):
        locations.append(move(moves[i],locations[len(locations)-1][0],locations[len(locations)-1][1]))
rows,columns=locations[len(locations)-1][1],n
#print(rows)
matrix=[([0]*columns) for i in range(rows + 1)]
#print(matrix)
#print(locations)
for i in range(len(locations)):
    #print(locations[i][0])
    #print(locations[i][1])
    matrix[locations[i][1]][locations[i][0]]=1
#print(matrix)
newMatrix = ""
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if matrix[i][j]==0:
            newMatrix += '. '
        else:
            newMatrix += '* '
    if i != len(matrix) - 1:
        newMatrix += '\n'
print(newMatrix)
if locations[len(locations)-1][0]!=n-1:
    print("There's no way out!")
