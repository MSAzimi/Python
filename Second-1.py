def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i+1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

number = int(input())
result = pascal_triangle(number)
if number>170:
    print()
else:
    for row in result:
        print(*row)
