#!usr/bin/env python3

# Entrada do problema
p = 29
ints = [14,6,11]

# Podemos encontrar o valor de "a" pela sugestão do enunciado: como são
# números relativamente pequenos, basta fazer força bruta e achar quais
# dos números entre 1 a p-1, quando elevados ao quadrado mod p, são ou
# não um dos números contido na lista "ints".

print(min(x for x in range(p) if pow(x, 2, p) in ints))
