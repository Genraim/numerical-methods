__author__ = 'genraim'
import math
sum = 0.1
eps = 0.5 * 10**(-5)
new_sum = sum
counter = 0
res = ((-0.5)/(0.01 * math.log(10, 2)) + (2 * math.sin(0.1))/(math.cos(0.1))**2)
def func(x):
    return 0.5 * math.log10(x) + math.tan(x)
def first_derivative(x):
    return 0.5/(x * math.log2(10)) + 1/(math.cos(x))**2
def second_derivative(x):
    return (-0.5)/(x**2 * math.log2(10) + (2*math.sin(x))/(math.cos(x))**2)
while(True):
    counter += 1
    sum = new_sum
    new_sum -= func(new_sum)/first_derivative(0.1)
    if math.fabs(new_sum - sum) < eps:
        break
print(new_sum, func(new_sum))
print(counter)
counter = 0
x0 = 0.1
x1 = 0.4
new_sum = x1
while(True):
    counter += 1
    sum = new_sum
    new_sum -= (func(new_sum)/(func(new_sum) - func(0.1)))*(new_sum - 0.1)
    if math.fabs(new_sum - sum) < eps:
        break
print(new_sum, func(new_sum))
print(counter)