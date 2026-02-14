print('Some os números! Digite 0 para parar.')
n = int(input("Informe um número: "))
total = 0
while n != 0:
    total += n
    n = int(input("Informe outro número: "))
print(f"A soma total dos números é: {total}.")
