frutas = ['abacaxi','cereja','melão']
print(frutas)
del frutas[0]
print(frutas)

fruta_removida = frutas.pop(1)
print(frutas)
print(fruta_removida)

frutas = ['abacaxi','cereja','melão']
frutas.remove('melão')
print(frutas)