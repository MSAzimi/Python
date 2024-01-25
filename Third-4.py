a=[]
def find_pairs(numbers, target):
    pairs_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in pairs_dict:
            a.append(pairs_dict[complement]+i)
        pairs_dict[num] = i


inputs = input().split()
target = int(input())
numbers = list(map(int, inputs))
find_pairs(numbers, target)
sorted_list=sorted(a)
if sorted_list == []:
    print('Not Found!')
else:
    for j in sorted_list:
        print(j)
