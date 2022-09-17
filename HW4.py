# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# d = float(input('Введите число:'))
# i = 0
# while d < 1:
#     i += 1
#     d = d*10
# p = math.pi
# res = round(p, i)
# print(res)

#  2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N

# import math
# pr_num = int(input('Введите число:'))
# def func(pr_num):
#     while pr_num % 2 == 0:
#         print(2)
#         pr_num = pr_num / 2
#     for i in range (3, int(math.sqrt(pr_num)) + 1,2):
#         while(pr_num % i == 0):
#             print(i)
#             pr_num = pr_num / i
#     if pr_num > 2:
#         print(pr_num)
# func(pr_num)








