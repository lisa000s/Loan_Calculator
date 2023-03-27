import math

integer = int(input())
sigmoid = round(math.exp(integer) / (math.exp(integer) + 1), 2)
print(sigmoid)