# Faça o fatorial de um número n
n = int(input("Escreva um número inteiro: "))

fatorial = 1

while n > 1:
    fatorial *= n # fatorial = fatorial * n
    n -= 1 # n = n - 1
print(fatorial)

# fatorial = 1
# for i in range(1,n+1):
#     fatorial *= i

# print(fatorial)

# 1 x 5 = 5
# 5 x 4 = 20
# 20 x 3 = 60
# 60 x 2 = 120
# 120 x 1 = 120