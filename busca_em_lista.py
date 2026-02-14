lista = ['maçã','banana','cereja','damasco','beterraba','morango','laranja','pera','kiwi']
fruta = input("Escreva uma fruta e confira se ela está na lista: ")
feedback = True or False

for i in lista:
    if i == fruta:
        print("Essa fruta está na lista.")
        feedback = True
    
    else:
        feedback = False
        continue

if feedback == False:
    print("Essa fruta não está na lista.")
