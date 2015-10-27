__author__ = 'genraim'
import math
def count_series(series, N):
    sum = 0
    for i in range(N+1):

print("Please, give number of series: \n[0] is default series, \n[1] is one time accelerated series, \n"
      "[2] is two time accelerated series, \n[3] is three time accelerated series")
series = int(input())
print("Please, give number of elements in series")
N = int(input())
sum = 0
for i in range(N+1):
    if series == 0:
        sum += 1/(0.5*i**2 + 2.7 * i + 0.3)
    elif series == 1:

if series == 0:
    for i in range(N+1):
        sum += 1/(0.5*i**2 + 2.7 * i + 0.3)
elif series == 1:
    for i in range(N+1):
        sum += (9*i + 1)/(i**2 * (0.5 * i**2 + 2.7 * i +0.3))
    sum = sum*0.6 + (math.pi**2 / 3)
elif series == 2:
    for i in range(N+1):
        sum += ((-47.6) * i - 5.4)/(n**3 * (0.5 * i**2 + 2.7 * i +0.3))
    # нужно добавить сумму ряда 1/i**3
elif series == 3:
    for i in range(N+1):
        sum += (251.64 * i + 28.56)/(n**4 * (0.5 * i**2 + 2.7 * i +0.3))
    sum += (-95.2)*(math.pi**4)/90

