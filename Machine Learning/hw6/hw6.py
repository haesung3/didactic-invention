# (a)
# import numpy as np
# import matplotlib.pyplot as plt
#
# x1 = np.genfromtxt('data.csv', usecols=0, delimiter=',', dtype=float)
# x2 = np.genfromtxt('data.csv', usecols=1, delimiter=',', dtype=float)
# y = np.genfromtxt('data.csv', usecols=2, delimiter=',', dtype=float)
#
# plt.scatter(x1, x2, c=y)
# plt.title('Plot of data.csv')
# plt.xlabel('x1')
# plt.ylabel('x2')
# plt.show()


# (b)
# P(y = 0) = 0.485
# mu0 = [[ 1.93477872 -2.97498216]]
# mu1 = [[ 5.85647767 -1.11750415]]
# sigma = [[1.11872866 0.45204323]
#         [0.45204323 0.71371048]]
# import numpy as np
#
# x = np.genfromtxt('data.csv', usecols=(0,1), delimiter=',', dtype=float)
# y = np.genfromtxt('data.csv', usecols=2, delimiter=',', dtype=float)
#
# phi = 0
# y_1 = 0
# for i in range(len(y)):
#     if y[i] == 1:
#         y_1 += 1
#
# y_0 = len(y) - y_1
#
# phi = y_0 / len(y)
#
# sigma = np.zeros((2, 2))
# temp_m0 = np.zeros((1,2))
# temp_m1 = np.zeros((1,2))
# cov = np.zeros((2, 2))
#
# for i in range(x.shape[0]):
#     if y[i] == 0:
#         temp_m0 += x[i]
#     elif y[i] == 1:
#         temp_m1 += x[i]
#
# m0 = temp_m0 / y_0
# m1 = temp_m1 / y_1
#
# for i in range(x.shape[0]):
#     if y[i] == 1:
#         cov += (x[i] - m1)*np.transpose(x[i] - m1)
#     if y[i] == 0:
#         cov += (x[i] - m0)*np.transpose(x[i] - m0)
#
# sigma = cov / x.shape[0]
# print("P(y = 0) =", phi)
# print("mu0 =", m0)
# print("mu1 =", m1)
# print("sigma =", sigma)

# (c)
# wT = [[-3.2978957  -0.51377501]]
# b = 11.73604887
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.genfromtxt('data.csv', usecols=(0, 1), delimiter=',', dtype=float)
# x1 = np.genfromtxt('data.csv', usecols=0, delimiter=',', dtype=float)
# x2 = np.genfromtxt('data.csv', usecols=1, delimiter=',', dtype=float)
# y = np.genfromtxt('data.csv', usecols=2, delimiter=',', dtype=float)
#
# phi = 0
# y_1 = 0
# for i in range(len(y)):
#     if y[i] == 1:
#         y_1 += 1
# y_0 = len(y) - y_1
# phi = y_0 / len(y)
# sigma = np.zeros((2, 2))
# temp_m0 = np.zeros((1, 2))
# temp_m1 = np.zeros((1, 2))
# cov = np.zeros((2, 2))
#
# for i in range(x.shape[0]):
#     if y[i] == 0:
#         temp_m0 += x[i]
#     elif y[i] == 1:
#         temp_m1 += x[i]
#
# m0 = temp_m0 / y_0
# m1 = temp_m1 / y_1
#
# for i in range(x.shape[0]):
#     if y[i] == 1:
#         cov += (x[i] - m1)*np.transpose(x[i] - m1)
#     if y[i] == 0:
#         cov += (x[i] - m0)*np.transpose(x[i] - m0)
#
# sigma = cov / x.shape[0]
# wT = (m0 - m1).dot(np.linalg.inv(sigma))
# print(wT)
#
# b = (1/2)*(m1.dot(np.linalg.inv(sigma).dot(np.transpose(m1))) - m0.dot(np.linalg.inv(sigma).dot(np.transpose(m0)))) \
#     - np.log((y_1/len(y))/(y_0/len(y)))
# print(b)
#
# slope = -(b / wT[0][1]) / (b / wT[0])
# y_int = -b / wT[0][1]
# yy = (slope*x) + y_int
# axes = plt.gca()
# axes.set_xlim([-1,10])
# axes.set_ylim([-7,2.5])
# plt.scatter(x1, x2, c=y)
# plt.plot(x, yy, c='blue')
# plt.xlabel('x1')
# plt.ylabel('x2')
# plt.title('data.csv with Decision Boundary')
# plt.show()

# (d)
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from numpy.random import uniform, seed
from matplotlib import cm

x = np.genfromtxt('data.csv', usecols=(0, 1), delimiter=',', dtype=float)
x1 = np.genfromtxt('data.csv', usecols=0, delimiter=',', dtype=float)
x2 = np.genfromtxt('data.csv', usecols=1, delimiter=',', dtype=float)
y = np.genfromtxt('data.csv', usecols=2, delimiter=',', dtype=float)

phi = 0
y_1 = 0
for i in range(len(y)):
    if y[i] == 1:
        y_1 += 1

y_0 = len(y) - y_1
phi = y_0 / len(y)

sigma = np.zeros((2, 2))
temp_m0 = np.zeros((1,2))
temp_m1 = np.zeros((1,2))
cov = np.zeros((2, 2))

for i in range(x.shape[0]):
    if y[i] == 0:
        temp_m0 += x[i]
    elif y[i] == 1:
        temp_m1 += x[i]

m0 = temp_m0 / y_0
m1 = temp_m1 / y_1

for i in range(x.shape[0]):
    if y[i] == 1:
        cov += (x[i] - m1)*np.transpose(x[i] - m1)
    if y[i] == 0:
        cov += (x[i] - m0)*np.transpose(x[i] - m0)

mu = np.zeros(2)
temp_mu0 = 0
temp_mu1 = 0

for i in range(len(y)):
    temp_mu0 += x1[i]
    temp_mu1 += x2[i]

mu[0] = temp_mu0 / len(y)
mu[1] = temp_mu1 / len(y)
sigma = cov / x.shape[0]

def gauss(x,y,Sigma,mu):
    X=np.vstack((x,y)).T
    mat_multi=np.dot((X-mu[None,...]).dot(np.linalg.inv(Sigma)),(X-mu[None,...]).T)
    return  np.diag(np.exp(-1*(mat_multi)))

seed(1234)
npts = 1000
x = uniform(-1, 10, npts)
y = uniform(-7, 2.5, npts)
z = gauss(x, y, sigma, m0)

xi = np.linspace(-1,10,100)
yi = np.linspace(-7,2.5,100)
zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

levels = [0.2, 0.4, 0.6, 0.8, 1.0]
CS = plt.contour(xi, yi, zi, 6, linewidths=0.5, colors='k')
CS = plt.contourf(xi, yi, zi, 6, cmap=cm.Greys_r)
plt.colorbar()
plt.xlim(-1, 10)
plt.ylim(-7, 2.5)
plt.show()
