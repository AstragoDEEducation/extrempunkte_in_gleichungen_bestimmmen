from sympy import *

x, y, z = symbols("x y z")

inEq = [2*x**3 - 15*x**2 + 36*x + 12, 0]

ersteAbleitung = Eq(diff(inEq[0], x, 1), inEq[1])

zweiteAbleitungEingesetzt = []
punkte = []
for j in solve(ersteAbleitung):
    # i = solution of f'(x)

    zweiteAbleitung = diff(inEq[0], x, 2)
    zweiteAbleitung = zweiteAbleitung.subs(x, j)
    zweiteAbleitungEingesetzt.append(zweiteAbleitung)

    eq = inEq[0]
    eq = eq.subs(x, j)
    punkte.append([j, eq])

typ = [None, None]
if zweiteAbleitungEingesetzt[0] < 0:
    typ[0] = ("Hochpunkt")

elif zweiteAbleitungEingesetzt[0] > 0:
    typ[0] = ("Tiefpunkt")

else:
    typ[0] = ("Sattelpunkt")


if zweiteAbleitungEingesetzt[1] < 0:
    typ[1] = ("Hochpunkt")

elif zweiteAbleitungEingesetzt[1] > 0:
    typ[1] = ("Tiefpunkt")

else:
    typ[1] = ("Sattelpunkt")


print(f"P({punkte[0][0]}|{punkte[0][1]}) ist ein {typ[0]} (f'' = {zweiteAbleitungEingesetzt[0]}).\nQ({punkte[1][0]}|{punkte[1][1]}) ist ein {typ[1]} (f'' = {zweiteAbleitungEingesetzt[1]}).")
