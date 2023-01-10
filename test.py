# import numpy as np

# M=np.zeros((4,4))
# x = 3

# M = ([[1,2,3,4],
#    [5,6,7,8],
#    [9,10,11,12],
#    [13,14,15,16]])

# xlen = len(M[0])
# ylen = len(M[1])

# def binary_search(M,x,j,i):
#     i = len(M[0])
#     j = len(M[1]) 
#     while(jlow <= jhigh):
#         middle = (jlow + jhigh)/2


# # for i in range(4):
# #     for j in range(4):
# #         if M[i][j] == x:
# #             print(i,j)


import numpy as np
M = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
M=np.zeros(len(M))
M = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
max_ele = M[0]

for i in range(len(M)):
    if M[i] > max_ele:
        max_ele = M[i]

histogram = np.zeros((max_ele + 1 ,2))

for j in range(len(M)):
    histogram[M[j]][0] += 1
    histogram[M[j]][1] = j 
    
for k in range(len(M)):
    for l in range(k,len(M)):
        target = M[k] + M[l]
        if target < max_ele:
            if histogram[target][0] == 1 and k!=l:
                print(M[k],M[l],M[int(histogram[target][1])])