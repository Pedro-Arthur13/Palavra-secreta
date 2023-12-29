import os
palavra = "segredo"
letras_acertadas = ''#letras acertadas
tentativas = 0 
while True:
    letra_digitada = input("Digite uma letra: ")
    
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue
        
    if letra_digitada in palavra:# se a letra estiver na palavra
        letras_acertadas += letra_digitada# adiciona ela as letras acertadas
        
    palavra_formada = ''#reseta a palavra formada
    for i in palavra:# para cada letra na palavra
        if i in letras_acertadas:# se a letra ja tiver sido descoberda
            palavra_formada += i #adiciona ela a nova palavra
        else: # se não
            palavra_formada += '*'# adiciona '*'
    print(palavra_formada)# printa a palavra formada
    
    tentativas += 1
    if palavra_formada == palavra:
        os.system('cls')#limpar terminal
        break
print(f"Você tentou {tentativas} vezes a palvra era {palavra}")

