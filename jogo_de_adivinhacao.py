import random
numero = random.randint(1,101)
print("Jogo de adivinhação!")
escolha = int(input("Escreva um número de 1 a 100: "))

while escolha != numero:
    if escolha > numero:
        print("O número é menor.")
        escolha = int(input("Escreva um número de 1 a 100: "))
    elif escolha < numero:
        print("O número é maior.")
        escolha = int(input("Escreva um número de 1 a 100: "))

print(f"Você acertou! O número é {numero}.")
