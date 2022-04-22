from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0,1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a , b = b, a%b
        x0, x1 = x1 -q*x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p = prod/n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
    
a = [2,3,5] 
n = [5,11,17] 


print(chinese_remainder(n,a))

# Fonte principal: https://medium.com/@fangya.123/chinese-remainder-theorem-with-python-a483de81fbb8

# Outras fontes:
#https://www.youtube.com/watch?v=tcgi_4DRZM0&ab_channel=ProgramadeInicia%C3%A7%C3%A3oCientificadaOBMEP
#https://en.wikipedia.org/wiki/Chinese_remainder_theorem
