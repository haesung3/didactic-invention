# from matplotlib import pyplot as plt
# from matplotlib import style
# import numpy as np
#
# x, y = np.genfromtxt('data3.csv', usecols=(0,1), unpack=True, delimiter=',')
# label = np.genfromtxt('data3.csv', usecols=(2), unpack=True, delimiter=',')
#
#
# style.use('ggplot')
#
# plt.title('Data3')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
#
# plt.scatter(x, y, c=label)
#
# plt.show()

# #############
import numpy as np
import matplotlib.pyplot as plt

# fig, ax = plt.subplots(1,2)
data = np.genfromtxt('data2.csv', usecols=(0, 1), delimiter=',', dtype=float)
y = np.genfromtxt('data2.csv', usecols=(2),  delimiter=',', dtype=float)


X_bias = np.ones([data.shape[0], 3])
X_bias[:, 1:3] = data

w = np.zeros([3,1])

n = 0
b = 0.0
index = 0
l = 100

def activation(x):
    return 1 if x >= 1 else -1


def calc_unit_vector(x):
    return x.transpose() / np.sqrt(x.transpose().dot(x))


def calc_hyperplane(X, w):
    return np.ravel([-(w[0] + x * w[1]) / w[2] for x in X])


for _ in range(1000):
    for i in range(X_bias.shape[0]):
        a = activation(w.transpose().dot(X_bias[i]))
        if a != y[i]:
         # Update weights
         w = w + ((y[i] - a) * X_bias[i, :]).reshape(w.shape[0], 1)
         n += 1
         index = i
         # temp_l = np.abs(((w.transpose().dot(X_bias[i])) - w[0] )/ np.sqrt(np.square(X_bias[i][0]) + np.square(X_bias[i][1] + np.square(X_bias[i][2]))))
         # if (temp_l < l):
         #     l = temp_l

print(n)
print(index)
print(w)
print(w[0])

for j in range(data.shape[0]):
    temp_l = np.abs(((w.transpose().dot(X_bias[j]))) / np.sqrt(np.square(X_bias[j][0]) + np.square(X_bias[j][1]) + np.square(X_bias[j][2])))
    if (temp_l < l):
        l = temp_l

result = [w.transpose().dot(x) for x in X_bias]
result_class = [activation(w.transpose().dot(x)) for x in X_bias]

ww = np.linalg.norm(w, 1)
www = np.square(ww)
print(www)

print(n / www)

print(l)

# Calculate unit vector
w = calc_unit_vector(w).transpose()

plt.scatter(data[:, 0], data[:, 1], c=result_class)
plt.title("Data2 with hyperplane")
plt.plot([-1, 1], calc_hyperplane([-1, 1], w), lw=3, c='red')

plt.show()

############

# import numpy as np
# from matplotlib import pyplot as plt
#
# data = np.genfromtxt('data2.csv', usecols=(0, 1), delimiter=',', dtype=float)
# label = np.genfromtxt('data2.csv', usecols=(2), delimiter=',')
#
# X_bias = np.ones([data.shape[0], 3])
# X_bias[:, 1:3] = data
# w = np.zeros([3])
# b = 0.0
# n = 0
# x = 0
# index = 0
#
# def sign(x):
#    return -1 if x < 0 else 1
#
#
# for _ in range(1000):
#     for i in range(X_bias.shape[0]):
#         if sign(w[0]*X_bias[i][0] + w[1]*X_bias[i][1] + w[2]*X_bias[i][2]) != label[i]:
#             w = w + label[i] * X_bias[i]
#             index = i
#             b = label[i] + b
#             w[0] = b
#             n += 1
#
# print(b)
# print(n)
# print(index)
# print(w)
#
# m = (-b) * (w[2] / w[1])
#
# plt.scatter(data[:, 0], data[:, 1], c=label)
# plt.plot( m * X_bias[index], '-')
# plt.show()
