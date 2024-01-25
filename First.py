Patient_number = int(input())
Shirzad_number = int(input())
a = (Patient_number)
b = (Shirzad_number)
c=(a ^ b)
d=bin(c)[2:]
print(d.count('1'))

