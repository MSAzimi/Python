import numpy as np

num_matrices, matrix_size = map(int, input().split())

matrices = []
determinants = []

for i in range (num_matrices):
  matrix=[]
  for _ in range(matrix_size):
    row = list(map(int, input().split()))
    matrix.append(row)
  matrices.append(np.array(matrix))
  determinants.append(np.linalg.det(matrices[i]))
max_index=(0,1)
max_output=np.linalg.det(np.dot(matrices[0],matrices[1]))
a=[]
for i in range(len(matrices)):
    for j in range(i+1,len(matrices)):
        output=np.linalg.det(np.dot(matrices[i],matrices[j]))
        if max_output<output:
            max_output=output
            max_index=(i,j)
            if np.linalg.det(matrices[i])>np.linalg.det(matrices[j]):
                a=np.linalg.inv(np.dot(matrices[i],matrices[j]))
            elif np.linalg.det(matrices[i])<np.linalg.det(matrices[j]):
                a=np.linalg.inv(np.dot(matrices[j],matrices[i]))
            elif np.linalg.det(matrices[i])==np.linalg.det(matrices[j]):
                if i<j :
                    a=np.linalg.inv(np.dot(matrices[i],matrices[j]))
                elif i>j:
                    a=np.linalg.inv(np.dot(matrices[j],matrices[i]))
for row in a:
    for val in row:
        print(f"{val:.3f}",end=" ")
    print()