# (a)
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.genfromtxt('regression_train.csv', usecols=(0), delimiter=',', dtype=float)
# y = np.genfromtxt('regression_train.csv', usecols=(1), delimiter=',', dtype=float)
#
# plt.scatter(x, y, c='red')
# plt.title("Regression_train")
# plt.xlabel("Input")
# plt.ylabel("Output")
# plt.show()
#

# (b)
# w: [ 2.44640709 -2.81635359]
# J(w): 3.912576405791464

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.genfromtxt('regression_train.csv', usecols=0, delimiter=',', dtype=float)
# y = np.genfromtxt('regression_train.csv', usecols=1, delimiter=',', dtype=float)
#
# x_one = np.ones([x.shape[0], 2])
# x_one[:, 1] = x
#
# gram = np.linalg.inv(np.dot(np.transpose(x_one), x_one))
# w_temp = np.dot(gram, np.transpose(x_one))
#
# w = np.dot(w_temp, y)
#
# l2 = np.linalg.norm(np.dot(x_one, w) - y)
#
# J = np.square(l2)
#
#
# print(w)
# print(J)
#
# for i in range(x.shape[0]):
#     y_predict = w[0] + w[1]*x
#
# plt.scatter(x, y, c='red')
# plt.title("Training data w/ Fitted Line and Data Points")
# plt.xlabel("Input")
# plt.ylabel("Output")
# plt.plot(x, y_predict)
# plt.show()


# (c)
# 0.0407
# iter =  103
# w0 =  [2.43297089]
# w1 =  [-2.789192]
# J(w) =  [3.9136875]

# 0.01
# iter =  363
# w0 =  [2.41824214]
# w1 =  [-2.75941751]
# J(w) =  [3.91712981]

# 0.001
# iter =  2608
# w0 =  [2.35668234]
# w1 =  [-2.63497301]
# J(w) =  [3.95787258]

# 0.0001
# iter =  9999
# w0 =  [1.91573585]
# w1 =  [-1.74358989]
# J(w) =  [5.49356559]

# import numpy as np
#
# x = np.genfromtxt('regression_train.csv', usecols=0, delimiter=',', dtype=float)
# y = np.genfromtxt('regression_train.csv', usecols=1, delimiter=',', dtype=float)
#
# x_one = np.ones([x.shape[0], 2])
# x_one[:, 1] = x
#
# w0 = np.zeros(x_one.shape[1])
# w1 = np.zeros(x_one.shape[1])
# nn = 0.01
#
# J = sum([(w0 + w1*x[i] - y[i])**2 for i in range(len(x))])
#
# for k in range(10000):
#     grad = sum([(w0 + w1*x[i] - y[i]) * x[i] for i in range(len(x))])
#
#     temp0 = w0 - nn * grad
#     temp1 = w1 - nn * grad
#
#     w0 = temp0
#     w1 = temp1
#
#     e = sum([(w0 + w1*x[i] - y[i])**2 for i in range(len(x))])
#
#     if abs(J[0] - e[0]) < 0.0001:
#         break
#
#     J = e
#
# print(k)
# print(J)
# print(w0)
# print(w1)


# (d)
# iter = 0
# w0 =  [0.]
# w1 =  [0.]
# J(w) =  [40.23384741]

# iter =  9
# w0 =  [1.4358061]
# w1 =  [-0.77340127]
# J(w) =  [9.64630623]

# iter =  19
# w0 =  [1.80818327]
# w1 =  [-1.52616998]
# J(w) =  [6.19935337]

# iter =  29
# w0 =  [2.04335025]
# w1 =  [-2.00156523]
# J(w) =  [4.82460907]

# iter =  39
# w0 =  [2.19186501]
# w1 =  [-2.30179112]
# J(w) =  [4.27632136]

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.genfromtxt('regression_train.csv', usecols=0, delimiter=',', dtype=float)
# y = np.genfromtxt('regression_train.csv', usecols=1, delimiter=',', dtype=float)
#
# x_one = np.ones([x.shape[0], 2])
# x_one[:, 1] = x
#
# w0 = np.zeros(1)
# w1 = np.zeros(1)
# nn = 0.0407
#
# J = sum([(w0 + w1*x[i] - y[i])**2 for i in range(len(x))])
#
# for k in range(40):
#     grad0 = sum([(w0 + w1*x[i] - y[i]) for i in range(len(x))])
#     grad1 = sum([(w0 + w1*x[i] - y[i]) * x[i] for i in range(len(x))])
#
#     temp0 = w0 - nn * grad0
#     temp1 = w1 - nn * grad1
#
#     w0 = temp0
#     w1 = temp1
#
#     e = sum([(w0 + w1*x[i] - y[i])**2 for i in range(len(x))])
#
#     if abs(J - e) < 0.0001:
#         break
#
#     J = e
#
# # print("iter = ", k)
# print("w0 = ", w0)
# print("w1 = ", w1)
# print("J(w) = ", J)
#
# for i in range(x.shape[0]):
#     y_predict = w0 + w1 * x
#
# plt.scatter(x, y, c='red')
# plt.plot(x, y_predict)
# plt.xlabel("Input")
# plt.ylabel("Output")
# plt.title("Regression with 40 iterations")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('regression_train.csv', usecols=0, delimiter=',', dtype=float)
y = np.genfromtxt('regression_train.csv', usecols=1, delimiter=',', dtype=float)

x_one = np.ones([x.shape[0], 2])
x_one[:, 1] = x

w = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(x_one), x_one)), np.transpose(x_one)), y)

x_two = np.ones([x.shape[0], 11])
x_two[:, 1] = x
x_two[:, 2] = x**2
x_two[:, 3] = x**3
x_two[:, 4] = x**4
x_two[:, 5] = x**5
x_two[:, 6] = x**6
x_two[:, 7] = x**7
x_two[:, 8] = x**8
x_two[:, 9] = x**9
x_two[:, 10] = x**10

w2 = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(x_two), x_two)), np.transpose(x_two)), y)
print(x_two)
print(w2)

J = np.square(np.linalg.norm(np.dot(x_two, w2) - y))
print(J)

rmse = np.sqrt(J / len(x))
print(rmse)

for i in range(x.shape[0]):
    y_predict = w2[0] + w2[1] * x + (w2[2] * x**2) + (w2[3] * x**3) + (w2[4] * x**5) + (w2[5] * x**5) \
                + (w2[6] * x**6) + (w2[7] * x**7) + (w2[8] * x**8) + (w2[9] * x**9) + (w2[10] * x**10)
#
# for i in range(x.shape[0]):
#     y_predict = w2[0] + w2[1] * x + w2[2] * x**2

print(y_predict)

plt.scatter(x, y, c='red')
plt.plot(x, y_predict)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Regression with 10 iterations")
plt.show()

# 2
# 3.8951779787143193
# 0.441314965682919

# 3
# 1.1933490268629017
# 0.24426921898418777

# 4
# 1.0550834163825074
# 0.22968276125805648

# 5
# 1.0288675930253848
# 0.226811330517832

# 6
# 1.007582519832187
# 0.2244529482800557

# 7
# 0.9881852127414279
# 0.22228193952067135

# 8
# 0.9879952636406667
# 0.2222605749610878

# 9
# 0.8970053995586212
# 0.21177882325183287

# 10
# 0.8962403586195116
# 0.21168849267491036