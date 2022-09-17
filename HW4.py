# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
d = float(input('Введите число:'))
i = 0
while d < 1:
    i += 1
    d = d*10
p = math.pi
res = round(p, i)
print(res)
