from sympy import *

x, y, z = symbols("x y z")

inEq = [2*x**3 - 15*x**2 + 36*x + 12, 0]

firstDerivative = Eq(diff(inEq[0], x, 1), inEq[1])

secondDerivativeInsertedAndSolved = []
points = []
for j in solve(firstDerivative):
    # i = solution of f'(x)

    secondDerivative = diff(inEq[0], x, 2)
    secondDerivative = secondDerivative.subs(x, j)
    secondDerivativeInsertedAndSolved.append(secondDerivative)

    baseEquation = inEq[0]
    baseEquation = baseEquation.subs(x, j)
    points.append([j, baseEquation])

pointType = [None, None]
if secondDerivativeInsertedAndSolved[0] < 0:
    pointType[0] = ("Hochpunkt")

elif secondDerivativeInsertedAndSolved[0] > 0:
    pointType[0] = ("Tiefpunkt")

else:
    pointType[0] = ("Sattelpunkt")


if secondDerivativeInsertedAndSolved[1] < 0:
    pointType[1] = ("Hochpunkt")

elif secondDerivativeInsertedAndSolved[1] > 0:
    pointType[1] = ("Tiefpunkt")

else:
    pointType[1] = ("Sattelpunkt")


print(f"P({points[0][0]}|{points[0][1]}) ist ein {pointType[0]} (f'' = {secondDerivativeInsertedAndSolved[0]}).\nQ({points[1][0]}|{points[1][1]}) ist ein {pointType[1]} (f'' = {secondDerivativeInsertedAndSolved[1]}).")
