idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")

if idade >= 18 and idade < 70:
    print("Pode dirigir e comprar bebida alcoólica")
elif idade >= 18:
    print("Pode dirigir e comprar bebida alcoólica")
else:
    print("Não pode dirigir nem comprar bebida alcoólica")