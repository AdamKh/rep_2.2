import math
import sys

EULER = 0.5772156649015328606
EPS = 10 ** -10

x = float(input("add value for x: "))
if x == 0:
    print("Illegal value of x", file=sys.stderr)
    exit(1)
a = -x ** 2 / 4
S, n = a, 1
while math.fabs(a) > EPS:
    a *= (-1 * x ** 2 * 2 * n) / (2 * (n + 1)) ** 2
    S += a
    n += 1
print(f"Ci({x}) = {EULER + math.log(math.fabs(x)) + S}")