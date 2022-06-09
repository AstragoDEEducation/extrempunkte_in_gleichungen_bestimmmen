from sympy import *

# Erstelle Variablen
x, y, z = symbols("x y z")

# Gleichung (Gleichungsteil, Ergebnis) AKTUELL FEHLERHAFT
inEq = [2*x**3 + 15*x**2 + 36*x + 12, 0]

# Stellen in der Ausgabe
stellen: int = 6

# Testing Equations:
#
# inEq = [(1/10)*x**3 + 2*x**2 - 4*x - 12, 0]
# L> Works (x1 = -14.27 und x2 = 0.93 --> -4.56 && 4.56)
#
# inEq = [2*x**3 + 15*x**2 + 36*x + 12, 0]
# L> Works (x1 = -3 und x2 = -2 --> -15 && -16)


# Erstelle die erste Ableitung und löse sie
firstDerivative = Eq(diff(inEq[0], x, 1), inEq[1])
firstDerivativeSolved = solve(firstDerivative)

# Liste mit beiden Ableitungen, welche die Werte der 1. Ableitung eingesetzt bekommen und anschließend ausgerechnet werden.
secondDerivativeInsertedAndSolved = []

# Liste mit beiden Punkten
extremePoints = []

# Führe für beide Lösungen der 1. Ableitung aus
for j in firstDerivativeSolved:

    # Erstellen der 2. Ableitung und Einsetzen der Werte der 1. Ableitung:
    secondDerivativeInserted = diff(inEq[0], x, 2)
    secondDerivativeInserted = secondDerivativeInserted.subs(x, j)
    secondDerivativeInsertedAndSolved.append(secondDerivativeInserted)

    # Berrechnung des y-Wertes und Einsetzen des selbigen, sowie des x-wertes
    baseEquation = inEq[0]
    baseEquation = baseEquation.subs(x, j)
    extremePoints.append([j, baseEquation])

# Erstelle Punkt-typen
extremePointType = [None, None]

# Prüfung auf hinreichende Bedingungen für Punkt P
if secondDerivativeInsertedAndSolved[0] < 0:
    extremePointType[0] = ("Hochpunkt")

elif secondDerivativeInsertedAndSolved[0] > 0:
    extremePointType[0] = ("Tiefpunkt")

else:
    extremePointType[0] = ("Sattelpunkt")

# Prüfung auf hinreichende Bedingungen für Punkt Q
if secondDerivativeInsertedAndSolved[1] < 0:
    extremePointType[1] = ("Hochpunkt")

elif secondDerivativeInsertedAndSolved[1] > 0:
    extremePointType[1] = ("Tiefpunkt")

else:
    extremePointType[1] = ("Sattelpunkt")


print("Extrempunkte:".upper())

# Formatierte Ausgabe der Ergebnisse
print(f"P({Float(N(extremePoints[0][0]), stellen)} | {Float(N(extremePoints[0][1]), stellen)}) ist ein {extremePointType[0]} (f''= {Float(N(secondDerivativeInsertedAndSolved[0]), stellen)}).\nQ({Float(N(extremePoints[1][0]), stellen)} | {Float(N(extremePoints[1][1]), stellen)}) ist ein {extremePointType[1]} (f''= {Float(N(secondDerivativeInsertedAndSolved[1]), stellen)}).")


# ================================================================================================================================================================================================


# Erstelle die zweite Ableitung und löse sie
secondDerivative = Eq(diff(inEq[0], x, 2), inEq[1])
secondDerivativeSolved = solve(secondDerivative)

# Liste mit der Ableitung, welche die Werte der 2. Ableitung eingesetzt bekommen und anschließend ausgerechnet werden.
thirdDerivativeInsertedAndSolved = []

# Liste mit dem Punkt
turningPoints = []

# Führe die Lösung der 2. Ableitung aus
for j in secondDerivativeSolved:

    # Erstellen der 3. Ableitung und Einsetzen der Werte der 2. Ableitung:
    thirdDerivativeInserted = diff(inEq[0], x, 3)
    thirdDerivativeInserted = thirdDerivativeInserted.subs(x, j)
    thirdDerivativeInsertedAndSolved.append(thirdDerivativeInserted)

    # Berrechnung des y-Wertes und Einsetzen des selbigen, sowie des x-wertes
    baseEquation = inEq[0]
    baseEquation = baseEquation.subs(x, j)
    turningPoints.append([j, baseEquation])

# Erstelle Punkt-typen
turningPointType = [None, None]

# Prüfung auf hinreichende Bedingungen für Punkt R
if thirdDerivativeInsertedAndSolved[0] < 0:
    turningPointType[0] = ("Links nach Rechts")

elif thirdDerivativeInsertedAndSolved[0] > 0:
    turningPointType[0] = ("Rechts nach Links")

else:
    turningPointType[0] = ("ERROR ERROR ERROR")

print("Wendepunkt:".upper())

# Formatierte Ausgabe Des Ergebnisses
print(f"R({Float(N(turningPoints[0][0]), stellen)} | {Float(N(turningPoints[0][1]), stellen)}) ist ein Wendepunkt von {turningPointType[0]} (f'''= {Float(N(thirdDerivativeInsertedAndSolved[0]), stellen)}).")
