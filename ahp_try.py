import numpy as np

# ls1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# ls2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# a = np.array(ls1)
# b = np.array(ls2)
# #计算两个矩阵乘法
# c = np.matmul(a, b)
# print(c)
# print(type(c))

standard_num = int(input("Please input the number of standard:"))
plan_num = int(input("Please input the number of plan:"))
ls0 = []

for i in range(standard_num):
    ls0.append([])

for j in range(standard_num):
    for k in range(standard_num):
        if j == k:
            ls0[j].append(1)
        elif j < k:
            num = float(input("Please input the weights:"))
            ls0[j].append(num)
        else:
            ls0[j].append(1 / ls0[k][j])

ls0_1 = []
vector0 = []
for i in ls0:
    s = 1
    for j in i:
        s *= j
    v = s ** (1 / len(i))
    ls0_1.append(v)
s = 0
for i in ls0_1:
    s += i
for i in ls0_1:
    num = i / s
    vector0.append(num)

matrix_standard = np.array(ls0)
matrix_vector0 = np.array(vector0)
matrix = np.matmul(matrix_standard, matrix_vector0)
print(matrix)
