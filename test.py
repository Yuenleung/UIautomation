'''
i = 1
while i < 10:
    a = 1
    while a <= i:
        c = a * i
        print('%s*%s=%s ' % (a, i, c), end='')
        a += 1
    print(end='\n')
    i += 1
'''




'''
#利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序
a = [1, 7, 4, 89, 34, 2]
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)  
'''

'''
a = '* '
b = 4
for i in range(1,6):
    print(' '*b,i*a)
    b =b-1
'''

'''
for Index_row in range(1,6):
    for index_space in range(1,6-Index_row):
        print(" ",end="")
    for Index_col in range(1,Index_row+1):
        print("* ",end="")
    print()
'''
'''
A = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(type(A))
print(list(A.keys()))
B=tuple(list(A.keys()))
print(B)
C = dict(zip(B,(1,2,3,4,5)))
print(type(C))
'''


A1 = zip(('a','b','c','d','e'),(1,2,3,4,5))
print(A1)