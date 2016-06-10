import numpy as np
import matplotlib.pyplot as plt
import math

start_pos = 0
end_pos = 1
step = 0.01
start_res = 0.1


def func(x, y, der_x=0, der_y=0):
    return {
        0: {
            0: 30 * y * (x - 0.2) * (x - 0.7),
            1: 30 * (x - 0.2) * (x - 0.7),
            2: 0},
        1: {
            0: 30 * y * ((x - 0.7) + (x - 0.2)),
            1: 30 * ((x - 0.7) + (x - 0.2))},
        2: {
            0: 30 * y * 2},
    }[der_x][der_y]


def analytic_solution(x):
    return 0.1 * math.exp(10 * (x ** 3) - 13.5 * (x ** 2) + 4.2 * x)


def euler_method(x, y, step):
    return y + step * func(x, y)


def tayler_method(x, y, step):
    y_der_1 = func(x, y)
    y_der_2 = func(x, y, 1, 0) + func(x, y) * func(x, y, 0, 1)
    y_der_3 = func(x, y, 2, 0) + 2 * func(x, y) * func(x, y, 1, 1) + func(x, y) ** 2 * func(x, y, 0, 2) + \
              func(x, y, 0, 1) * (func(x, y, 1, 0) + func(x, y) * func(x, y, 0, 1))
    return y + step * y_der_1 + y_der_2 * step ** 2 / 2 + y_der_3 * step ** 3 / 6


def simpson_func(xs, ys, y_new, i, step, der=0):
    return {
        0: (- y_new) + ys[i - 1] +
           (func(xs[i + 1], y_new) + 4 * func(xs[i], ys[i]) + func(xs[i - 1], ys[i - 1])) * step / 3,
        1: 1 + (30 * (xs[i + 1] - 0.2) * (xs[i + 1] - 0.7)) * step / 3
    }[der]


def simpson_method(xs, ys, i, step):
    # sum = ys[-1]
    # new_sum = sum
    # eps = 0.000001
    # counter = 0
    # while True:
    #     counter += 1
    #     sum = new_sum
    #     new_sum -= simpson_func(xs, ys, new_sum, i, step) / simpson_func(xs, ys, new_sum, i, step, 1)
    #     print new_sum
    #     if (math.fabs(sum - simpson_func(xs, ys, new_sum, i, step) / simpson_func(xs, ys, new_sum, i, step, 1)) < eps) or counter > 10:
    #         break
    # y_next = new_sum
    # print new_sum
    y_next = (ys[i - 1] + (4 * func(xs[i], ys[i]) + func(xs[i - 1], ys[i - 1])) * step / 3) / (1 - 10 * step * (xs[i + 1] - 0.2) * (xs[i + 1] - 0.7))
    return ys[i - 1] + (func(xs[i + 1], y_next) + 4 * func(xs[i], ys[i]) + func(xs[i - 1], ys[i - 1])) * step / 3


# print np.around((end_pos - start_pos) / step)
xs = np.linspace(start_pos, end_pos, np.around((end_pos - start_pos) / step) + 1)
ys_analytics = [analytic_solution(x) for x in xs]
# ps = plt.subplot(211)


ys_euler = [start_res]
for i in range(0, len(xs) - 1):
    ys_euler.append(euler_method(xs[i], ys_euler[i], step))

ys_tayler = [start_res]
for i in range(0, len(xs) - 1):
    ys_tayler.append((tayler_method(xs[i], ys_tayler[i], step)))

ys_simpson = [start_res]
k_acceleration_1 = step * func(xs[0], ys_simpson[0])
k_acceleration_2 = step * func(xs[0] + step / 2, ys_simpson[0] + k_acceleration_1 / 2)
k_acceleration_3 = step * func(xs[0] + step / 2, ys_simpson[0] + k_acceleration_2 / 2)
k_acceleration_4 = step * func(xs[0] + step, ys_simpson[0] + k_acceleration_3)
ys_simpson.append(
    ys_simpson[0] + (k_acceleration_1 + k_acceleration_2 * 2 + k_acceleration_3 * 2 + k_acceleration_4) / 6)

for i in range(1, len(xs) - 1):
    ys_simpson.append(simpson_method(xs, ys_simpson, i, step))


def font_gen(color='black'):
    return {'family': 'serif',
            'color': color,
            'weight': 'normal',
            'size': 16,
            }

plt.text(0.1, 0.2, 'step:' + str(step), fontdict=font_gen())

plt.plot(xs, ys_analytics, color='red')
plt.text(0.4, 0.2, 'analytic', fontdict=font_gen('red'))

# plt.plot(xs, ys_euler, color='blue')
# plt.text(0.4, 0.19, 'euler', fontdict=font_gen('blue'))

# plt.plot(xs, ys_tayler, color='green')
# plt.text(0.4, 0.18, 'taylor', fontdict=font_gen('green'))

plt.plot(xs, ys_simpson, color='gray')
plt.text(0.4, 0.17, 'simpson', fontdict=font_gen('gray'))

plt.show()

# print("x |", "analytic", "euler", "tayler", "simpson")
# for i in range(len(xs)):
#     print("%.2f" % xs[i], "|", "%.10f;" % ys_analytics[i], "%.10f;" % ys_euler[i], "%.10f;" % ys_tayler[i],
#           "%.10f;" % ys_simpson[i])
