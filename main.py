import sympy

# Erstelle Variablen
x, y, z = symbols("x y z")

# Gleichung (Gleichung, Ergebnis)
inEq = [2*x**3 - 15*x**2 + 36*x + 12, 0]

# Erstelle die erste Ableitung
firstDerivative = Eq(diff(inEq[0], x, 1), inEq[1])

# Liste mit beiden Ableitungen, welche die Werte der 1. Ableitung eingesetzt bekommen und anschließend ausgerechnet werden.
secondDerivativeInsertedAndSolved = []

# Liste mit beiden Punkten
points = []

# Fühhre füe beide Lösungen der 1. Ableitung aus
for j in solve(firstDerivative):

    # Erstellen der 2. Ableitung und Einsetzen der Werte der 1. Ableitung:
    secondDerivative = diff(inEq[0], x, 2)
    secondDerivative = secondDerivative.subs(x, j)
    secondDerivativeInsertedAndSolved.append(secondDerivative)

    # Berrechnung des y-Wertes und Einsetzen des selbigen, sowie des x-wertes
    baseEquation = inEq[0]
    baseEquation = baseEquation.subs(x, j)
    points.append([j, baseEquation])

# Erstelle Punkt-typen
pointType = [None, None]

# Prüfung auf hinreichende Bedingungen für Punkt P
if secondDerivativeInsertedAndSolved[0] < 0:
    pointType[0] = ("Hochpunkt")

elif secondDerivativeInsertedAndSolved[0] > 0:
    pointType[0] = ("Tiefpunkt")

else:
    pointType[0] = ("Sattelpunkt")

# Prüfung auf hinreichende Bedingungen für Punkt Q
if secondDerivativeInsertedAndSolved[1] < 0:
    pointType[1] = ("Hochpunkt")

elif secondDerivativeInsertedAndSolved[1] > 0:
    pointType[1] = ("Tiefpunkt")

else:
    pointType[1] = ("Sattelpunkt")

# Formatierte Ausgabe der Ergebnisse
print(f"P({points[0][0]}|{points[0][1]}) ist ein {pointType[0]} (f''= {secondDerivativeInsertedAndSolved[0]}).\nQ({points[1][0]}|{points[1][1]}) ist ein {pointType[1]} (f''= {secondDerivativeInsertedAndSolved[1]}).")
