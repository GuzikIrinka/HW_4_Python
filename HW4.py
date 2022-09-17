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

#  2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N

import math
pr_num = int(input('Введите число:'))
def func(pr_num):
    while pr_num % 2 == 0:
        print(2)
        pr_num = pr_num / 2
    for i in range (3, int(math.sqrt(pr_num)) + 1,2):
        while(pr_num % i == 0):
            print(i)
            pr_num = pr_num / i
    if pr_num > 2:
        print(pr_num)
func(pr_num)



# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

ex_dann = input('Введите числа через пробел:')
list = []
list = ex_dann.split(' ')
list = [int(ex_dann) for ex_dann in list]
print('исходный список', list)
dubb = [x for i, x in enumerate(list) if x in list[:i]]
print('повтор:', dubb)
list_res = []
for numb in list:
    if numb not in dubb:
        list_res.append(numb)
print(list_res)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random
k= int(input('введите число: '))
s=str()

for poww in range(0,k+1):
  coeff=random.randint(0, 100)
  
  coeff=str(coeff)
  
  if poww==0:
    s=s+coeff+'+'
  else:
   
    if poww==k:
     s=s+coeff+'*x**'+str(poww)+'=0'
    else:
      s=s+coeff+'*x**'+str(poww)+'+'
print(s)
  
    