__author__ = 'genraim'
import math
sum = 0.1
eps = 0.5 * 10**(-5)
new_sum = sum
counter = 0
def func(x):
    return 0.5 * math.log10(x) + math.tan(x)
def first_derivative(x):
    return 0.5/(x * math.log2(10)) + 1/(math.cos(x))**2
def second_derivative(x):
    return (-0.5)/(x**2 * math.log2(10) + (2*math.sin(x))/(math.cos(x))**2)
print("iteration %d;" % counter, "x: %.10f;" % new_sum, "func(x): %.10f" % func(new_sum))
while(True):
    counter += 1
    sum = new_sum
    new_sum -= func(new_sum) / first_derivative(0.1)
    print("iteration %d;" % counter, "x: %.10F;" % new_sum, "func(x): %.10F" % func(new_sum))
    if math.fabs(func(new_sum)/first_derivative(0.1)) < eps:
        break

print("__________")
counter = 0
x0 = 0.1
x1 = 0.4
new_sum = x1
print("iteration %d;" % counter, "x: %.10f;" % new_sum, "func(x): %.10f" % func(new_sum))
while(True):
    counter += 1
    sum = new_sum
    new_sum -= (func(new_sum)/(func(new_sum) - func(0.1)))*(new_sum - 0.1)
    print("iteration %d;" % counter, "x: %.10f;" % new_sum, "func(x): %.10f" % func(new_sum))
    if math.fabs((func(new_sum)*(new_sum-x0))/(func(new_sum)-func(x0))) < eps:
        break
