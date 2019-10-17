# import numpy as np
# import matplotlib.pyplot as plt
#
# mnist = np.genfromtxt("MNIST3.csv", delimiter=',')
# cov_mnist = np.cov(np.transpose(mnist))
# e_val, e_vec = np.linalg.eig(cov_mnist)
# e_val.sort()
# larges = e_val[-100:]
# larges[::-1].sort()
# plt.plot(larges)
# plt.title("100 Largest Eigenvalues")
# plt.ylabel("Eigenvalues")
# plt.show()
#
# # (b)
# import numpy as np
# import matplotlib.pyplot as plt
#
# mnist = np.genfromtxt("MNIST3.csv", delimiter=',')
# cov_mnist = np.cov(np.transpose(mnist))
#
#
# val, vec = np.linalg.eig(cov_mnist)
#
# print(val)
#
# temp_vec = []
# for i in range(4):
#     temp_vec.append(vec[:, i])
#
# vis1 = np.transpose(np.array(temp_vec[0].reshape(28, 28), dtype=float))
# vis2 = np.transpose(np.array(temp_vec[1].reshape(28, 28), dtype=float))
# vis3 = np.transpose(np.array(temp_vec[2].reshape(28, 28), dtype=float))
# vis4 = np.transpose(np.array(temp_vec[3].reshape(28, 28), dtype=float))
#
# fig = plt.figure()
# plt.subplot(2,2,1)
# plt.imshow(vis1, cmap='gray')
# plt.subplot(2,2,2)
# plt.imshow(vis2, cmap='gray')
# plt.subplot(2,2,3)
# plt.imshow(vis3, cmap='gray')
# plt.subplot(2,2,4)
# plt.imshow(vis4,cmap='gray')
# plt.show()

# (c)
import numpy as np
import matplotlib.pyplot as plt

mnist = np.genfromtxt("MNIST3.csv", delimiter=',')
cov_mnist = np.cov(np.transpose(mnist))

val, vec = np.linalg.eig(cov_mnist)

mean_mnist = np.zeros(784)
for i in range(len(mean_mnist)):
    for j in range(len(mnist)):
        mean_mnist[i] += mnist[j][i]

mean_mnist = (1/400) * mean_mnist


def pcaApproximation(M):
    temp_dim = np.zeros(784)
    temp2_dim = np.zeros(784)
    for k in range(M):
        temp_dim = temp_dim + np.dot(np.dot(mnist[0], vec[:, k]), vec[:, k])
    for t in range(M+1, len(mnist[0])):
        temp2_dim = temp2_dim + np.dot(np.dot(np.transpose(mean_mnist), vec[:, t]), vec[:, t])
    dim = temp_dim + temp2_dim
    return dim


dim1 = pcaApproximation(1)
dim1 = np.real(dim1)
dim10 = pcaApproximation(10)
dim10 = np.real(dim10)
dim50 = pcaApproximation(50)
dim50 = np.real(dim50)
dim250 = pcaApproximation(250)
dim250 = np.real(dim250)
dim0 = pcaApproximation(0)
dim0 = np.real(dim0)

dim1 = np.transpose(dim1.reshape(28, 28))
dim10 = np.transpose(dim10.reshape(28, 28))
dim50 = np.transpose(dim50.reshape(28, 28))
dim250 = np.transpose(dim250.reshape(28, 28))
dim0 = np.transpose(dim0.reshape(28, 28))
print(dim0)

fig = plt.figure()
plt.subplot(2,3,1)
plt.imshow(dim1, cmap='gray')
plt.subplot(2,3,2)
plt.imshow(dim10, cmap='gray')
plt.subplot(2,3,3)
plt.imshow(dim50, cmap='gray')
plt.subplot(2,3,4)
plt.imshow(dim250, cmap='gray')
plt.subplot(2,3,5)
plt.imshow(dim0, cmap='gray')
plt.subplot(2,3,6)
plt.imshow(np.transpose(mnist[0].reshape(28,28)), cmap='gray')
plt.show()


