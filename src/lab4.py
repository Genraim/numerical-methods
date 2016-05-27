import math


def func(x):
    return math.sin(math.sqrt((1+ x**2)/3))


def frange(start, stop, step=1, eps=0.000000001):
    res = []
    elem = start
    while (elem <= (stop + eps)):
        res.append(elem)
        elem += step
    return res


def integrate_average_restangles(a, b, step):
    res = 0
    lst = frange(a, b, step)
    #print lst
    #print len(lst)
    for i in range(1, len(lst)):
        arg = (lst[i-1] + lst[i])/2
        res += step * func(arg)
    return res


def pre_integrate_3_8(a, b, step):
    return (step / 8) * (func(a) + 3 * func((2*a + b)/3) + 3 * func((a + 2 * b)/3) + func(b))


def integrate_3_8(a, b, step):
    res = 0
    lst = frange(a, b, step)
    #print len(lst)
    for i in range(1, len(lst)):
        res += pre_integrate_3_8(lst[i-1], lst[i], step)
    return res


def estimation_error_runge(i_h, i_h2, p):
    return (i_h - i_h2)/(2 ** p -1)


print integrate_average_restangles(0.8, 2.2, 0.1)
print estimation_error_runge(integrate_average_restangles(0.8, 2.2, 0.1), integrate_average_restangles(0.8, 2.2, 0.2), 2)
print integrate_average_restangles(0.8, 2.2, 0.05)
print estimation_error_runge(integrate_average_restangles(0.8, 2.2, 0.05), integrate_average_restangles(0.8, 2.2, 0.1), 2)
print integrate_average_restangles(0.8, 2.2, 0.025)
print estimation_error_runge(integrate_average_restangles(0.8, 2.2, 0.025), integrate_average_restangles(0.8, 2.2, 0.05), 2)

print "--------"
print integrate_3_8(0.8, 2.2, 0.1)
print estimation_error_runge(integrate_3_8(0.8, 2.2, 0.1),integrate_3_8(0.8, 2.2, 0.2), 4)
print integrate_3_8(0.8, 2.2, 0.05)
print estimation_error_runge(integrate_3_8(0.8, 2.2, 0.05),integrate_3_8(0.8, 2.2, 0.1), 4)
print integrate_3_8(0.8, 2.2, 0.025)
print estimation_error_runge(integrate_3_8(0.8, 2.2, 0.025),integrate_3_8(0.8, 2.2, 0.05), 4)
# print (func(0.7 * (- math.sqrt(0.6)) + 1.5) * 5 / 9)
# print 0.7 * (func(0.7 * (- math.sqrt(0.6)) + 1.5) * 5 / 9 + func(0.7 * (math.sqrt(0.6)) + 1.5) * 5 / 9 + \
#              func(0.7 * (- math.sqrt(0)) + 1.5) * 8 / 9)
# x = 0.9577
# print math.sin(math.sqrt((1 + x ** 2) / 3))
# print math.sin(1.3117)