# (a)
# import cv2
# img = cv2.imread('UCLA_Bruin.jpg')
# cv2.imshow('Visualization', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # (b)
# # u_init = [[147. 200. 250.]
# #         [  0.   0.   0.]
# #         [137. 141.  57.]
# #         [ 31.  70. 125.]]
# #
# # u = [[203.05552686 216.13657329 216.7668869 ]
# #     [149.15837804 158.20136669 155.55279833]
# #     [144.18720077 151.69300358 146.28917722]
# #     [113.9861382  120.20466861 113.34953944]]
# #
# # J = [1.31125081e+09 1.25912859e+10 1.15830990e+09 7.21232640e+09
# #      0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00
# #       0.00000000e+00 0.00000000e+00]
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2
#
# img = cv2.imread('UCLA_Bruin.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# k = 4
# u = np.zeros((4, 3))
# u[0] = [147, 200, 250]
#
# for i in range(1, k):
#     maxD = 0
#     max_x = 0
#     max_y = 0
#     for j in range(len(img)):
#         for t in range(len(img[0])):
#             diff = []
#             for z in range(0, i):
#                 diff.append(np.linalg.norm(img[j][t] - u[z]))
#             if np.min(diff) > maxD:
#                 maxD = np.min(diff)
#                 max_x = t
#                 max_y = j
#     u[i] = img[max_y][max_x]
# print(u)
#
# r = np.zeros((300, 400, 4))
# jj = np.zeros(10)
# for it in range(10):
#     for j in range(len(img)):
#         for t in range(len(img[0])):
#             diff = []
#             for z in range(k):
#                 diff.append(np.linalg.norm(img[j][t] - u[z]))
#             n = np.argmin(diff)
#             r[j][t][n] = 1
#     n = np.zeros(3)
#     d = 0
#     for i in range(k):
#         for j in range(len(img)):
#             for t in range(len(img[0])):
#                 if r[j][t][i] == 1:
#                     n += img[j][t]
#                     d += 1
#         u[i] = n / d
#     for i in range(k):
#         for j in range(len(img)):
#             for t in range(len(img[0])):
#                 if r[j][t][i] == 1:
#                     jj[i] += np.linalg.norm(img[j][t] - u[i]) ** 2
# print(r)
# print(u)
# print(jj)
# plt.plot(jj)
# plt.ylabel("J")
# plt.xlabel("Number of iterations")
# plt.title("J vs Iterations")
# plt.show()

# (c)
# K = 4:
# J = [1.31125081e+09 1.25912859e+10 1.15830990e+09 7.21232640e+09
#      0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00
#      0.00000000e+00 0.00000000e+00]
# K = 8:
# J = [9.14283468e+08 1.03331878e+10 8.94884000e+08 7.77688189e+09
#     4.10408435e+09 2.00476945e+08 3.56001220e+09 3.54104392e+09
#     0.00000000e+00 0.00000000e+00]
import numpy as np
import cv2
img = cv2.imread('UCLA_Bruin.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

k = 32
u = np.zeros((k, 3))
u[0] = [147, 200, 250]
new_img = img
for i in range(1, k):
    maxD = 0
    max_x = 0
    max_y = 0
    for j in range(len(img)):
        for t in range(len(img[0])):
            diff = []
            for z in range(0, i):
                diff.append(np.linalg.norm(img[j][t] - u[z]))
            if np.min(diff) > maxD:
                maxD = np.min(diff)
                max_x = t
                max_y = j
    u[i] = img[max_y][max_x]

r = np.zeros((300, 400, k))
jj = np.zeros(10)
for it in range(10):
    for j in range(len(img)):
        for t in range(len(img[0])):
            diff = []
            for z in range(k):
                diff.append(np.linalg.norm(img[j][t] - u[z]))
            n = np.argmin(diff)
            r[j][t][n] = 1
    n = np.zeros(3)
    d = 0
    for i in range(k):
        for j in range(len(img)):
            for t in range(len(img[0])):
                if r[j][t][i] == 1:
                    n += img[j][t]
                    d += 1
        u[i] = n / d
    for i in range(k):
        for j in range(len(img)):
            for t in range(len(img[0])):
                if r[j][t][i] == 1:
                    jj[it] += np.linalg.norm((img[j][t] - u[i]), ord=2) ** 2

for i in range(k):
    for j in range(len(img)):
        for t in range(len(img[0])):
            diff = []
            if r[j][t][i] == 1:
                new_img[j][t] = u[i]

print(jj)
new_img = cv2.cvtColor(new_img, cv2.COLOR_RGB2BGR)
cv2.imshow("compressed with k = 16", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
