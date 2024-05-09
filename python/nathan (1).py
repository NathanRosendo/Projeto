import random 

numeroSecreto = random.randint(1, 50)

print("Bem vindo ao jogo" , "\n" "Digite um numero de 1 a 50 para adivinhar")

tentativas = 0 

while tentativas <5:
    palpite = int(input("Digite seu palpite"))
    
    if palpite == numeroSecreto:
        print("Voce acertou!")
        break
    elif palpite < numeroSecreto :
        print("Muito baixo")
    else:
        print("Muito alto")
        
    tentativas += 1
    
if tentativas == 5:
    print("Acabarm as tentativas. O numero secreto era:",numeroSecreto)
        # TODO: write code...