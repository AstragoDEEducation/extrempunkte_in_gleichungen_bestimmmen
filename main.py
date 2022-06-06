from sympy import *

x, y, z = symbols("x y z")

# f, g = symbols("f g", cls=Function)

inEq = [2*x**3 - 15*x**2 + 36*x + 12, 0]

values = []
for i in solve(Eq(diff(inEq[0], x, 1), inEq[1])):
    # i = solution of f'(x)
    pass
