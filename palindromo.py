print("Confira se a palavra é um palíndromo!")
palavra = input("Escreva uma palavra: ")

for i in range(len(palavra)):
    print(palavra[::-1])
    if palavra[::-1] == palavra:
        print("Essa palavra é um palídromo.")
    else:
        print("Essa palavra não é um palíndromo.")

# (nem precisa colocar for i)
# if palavra[::-1] == palavra:
#     print("Essa palavra é um palídromo.")
# else:
#     print("Essa palavra não é um palíndromo.")
