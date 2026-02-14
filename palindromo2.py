palavra = input("Escreva sua palavra: ")
i = 0
j = len(palavra)-1

# while i < j:
#     i = i + 1
#     j = j - 1
#     if palavra[i] == palavra[j]:
#         print("Essa palavra é um palíndromo.")
#         continue
#     else:
#         print("Essa palavra não é um palíndromo.")
#         break

falso = False
verdadeiro = True

while i < j:
    i = i + 1
    j = j - 1
    if palavra[i] == palavra[j]: verdadeiro
    else: falso
if verdadeiro:
        print("Essa palavra é um palíndromo.")
else:
        print("Essa palavra não é um palíndromo.")
