# (a)
# import numpy as np
# import matplotlib.pyplot as plt
#
# adaboost = np.genfromtxt("AdaBoost_data.csv", delimiter=',')
#
# plt.scatter(adaboost[:, 0], adaboost[:, 1], c=adaboost[:, 2])
# plt.title("Visualization")
# plt.xlabel("x1")
# plt.ylabel("x2")
# plt.show()

# (b)
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("AdaBoost_data.csv", usecols=(0,1), delimiter=',')
label = np.genfromtxt("AdaBoost_data.csv", usecols=2, delimiter=',')
w = np.zeros(len(data[:, 0]))
for i in range(len(data[:, 0])):
    w[i] = 1 / len(data[:, 0])


def classifier(x, temp_w, s, i):
    min_t = 100
    min_count = 100
    for j in range(len(x[:, 0]) - 1):
        count = 0
        t = int((x[j][i] + x[j+1][i]) / 2)
        for k in range(len(x[:, 0])):
            if label[k] != np.sign(s * (x[k][i] - t)):
                count += temp_w[k]
        if count < min_count:
            min_t = t
            min_count = count
    return min_t


def get_error(temp_w, t, s, i):
    J = 0
    for j in range(len(data[:, 0])):
        if label[j] != np.sign(s * (data[j][i] - t)):
            J += w[j]
    e_t = (J / np.sum(temp_w))
    return e_t


def get_alpha(temp_w, t, s, i):
    e_t = get_error(temp_w, t, s, i)
    alpha = (1 / 2) * np.log((1 - e_t) / e_t)
    return alpha


def w_update(temp_w, t, s, i):
    update_w = np.zeros(len(data[:, 0]))
    pos_w = np.zeros(len(data[:, 0]))
    pos = 0
    neg_w = np.zeros(len(data[:, 0]))
    neg = 0
    for j in range(len(data[:, 0])):
        if label[j] == np.sign(s * (data[j][i] - t)):
            pos_w[j] = temp_w[j] * np.exp(-1 * get_alpha(temp_w, t, s, i))
            pos += 1
        else:
            neg_w[j] = temp_w[j] * np.exp(get_alpha(temp_w, t, s, i))
            neg += 1
    z = np.sum(pos_w) + np.sum(neg_w)
    for k in range(len(data[:, 0])):
        if label[k] == np.sign(s * (data[k][i] - t)):
            update_w[k] = pos_w[k] / z
        else:
            update_w[k] = neg_w[k] / z
    return update_w


t1 = classifier(data, w, -1, 0)
w2 = w_update(w, t1, -1, 0)
t2 = classifier(data, w2, -1, 0)
w3 = w_update(w2, t2, -1, 0)
t3 = classifier(data, w3, 1, 1)

e1 = get_error(w, t1, -1, 0)
e2 = get_error(w2, t2, -1, 0)
e3 = get_error(w3, t3, 1, 1)
a1 = get_alpha(w, t1, -1, 0)
a2 = get_alpha(w2, t2, -1, 0)
a3 = get_alpha(w3, t3, 1, 1)

print("a1 =", a1, ", a2 =", a2, ", a3 =", a3)
print("e1 =", e1, ", e2 =", e2, ", e3 =", e3)
print("d0 =", w)
print("d1 =", w2)
print("d2 =", w3)
print("t1 =", t1, ", t2 =", t2, ", t3 =", t3)

error = 0
for j in range(len(data[:, 0])):
    if label[j] == np.sign(-1 * (data[j][0] - t1)) or label[j] == np.sign(-1 * (data[j][0] - t2)) \
            or label[j] == np.sign(data[j][1] - t3):
        error += 1

print("Combined Error:", error)

xvar = np.arange(0, 10)
fig = plt.figure()
plt.subplot(2,2,1).set_title('k=1')
plt.scatter(data[:, 0], data[:, 1], s=1000*w, c=label)
plt.axvline(t1)
plt.ylim(0, 8)

plt.subplot(2,2,2).set_title('k=2')
plt.scatter(data[:,0], data[:, 1], s=1000*w2, c=label)
plt.axvline(t2)
plt.ylim(0, 8)

plt.subplot(2,2,3).set_title('k=3')
plt.scatter(data[:, 0], data[:, 1], s=1000*w3, c=label)
plt.axhline(t3)
plt.ylim(0, 8)

plt.subplot(2,2,4).set_title('Combined')
plt.scatter(data[:, 0], data[:, 1], s=1000*w3, c=label)
plt.axvline(t1)
plt.axvline(t2)
plt.axhline(t3)
plt.ylim(0, 8)
plt.show()