n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"Soma: {n1 + n2}")
print(f"Diferença: {n1 - n2}")
print(f"Produto: {n1 * n2}")

if n2 != 0:
    print(f"Resto da divisão: {n1 % n2}")
else:
    print("Não é possível calcular o resto da divisão por zero")
