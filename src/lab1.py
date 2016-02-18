__author__ = 'genraim'
N = int(input('Please, give number of elements in series: '))
sum0 = 0
sum1 = 0
sum2 = 0
sum3 = 0
pipi_na_6 = 1.6449340668
one_n3 = 1.2020569032
pi4_90 = 1.0823232337
for i in range(1, N+1):
    sum0 += 1/(0.5 * i**2 + 2.7 * i + 0.3)
print(sum0)
sum1 += 2*pipi_na_6
for i in range(1, N+1):
    sum1 -= (5.4 * i + 0.6)/(i**2 * (0.5 * i**2 + 2.7 * i + 0.3))
print(sum1)
sum2 += 2 * pipi_na_6 - 10.8 * one_n3
for i in range(1, N+1):
    sum2 += (57.12 * i**3 + 6.48 * i**2)/(i**5 * (i**2 + 5.4 * i + 0.6))
print(sum2)
sum3 += 2 * pipi_na_6 - 10.8 * one_n3 + 57.12 * pi4_90
for i in range(1, N+1):
    sum3 -= (301.968 * i**6 + 34.272 * i**5)/(i**9 * (i**2 + 5.4 * i + 0.6))
print(sum3)