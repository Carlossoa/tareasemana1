# 3. Convertir a mayúsculas si la longitud es par, a minúsculas si es impar
convertidas = [s.upper() if len(s) % 2 == 0 else s.lower() for s in strings]
print(convertidas)