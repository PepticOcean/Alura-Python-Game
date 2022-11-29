def play():

    print("**********************************");
    print("BEM-VINDO A FORCA:");
    print("**********************************");

    secret_word = "programador".lower();
    right_letters = ["_","_","_","_","_","_","_","_","_","_","_"];
    hanged = False; #variável para saber se o jogador foi enforcado
    correct_word = False;
    errors = 0;
    
    print(right_letters);

    while(hanged != True and correct_word != True):
     
        attempt = str.strip(input("Qual a letra que você deseja utilizar?").lower()); #removendo espaços e deixando tudo minúsculo

        if(attempt in secret_word):
            index = 0;
            for letter in secret_word:
                if(attempt == letter):
                    right_letters[index] = letter;
                    print(right_letters);
                index = index + 1;
        else:
            errors += 1;
        hanged = errors == 6 #Se erros for = 6, a forca acontece e o jogo acaba
        correct_word = "_" not in right_letters; #Se houverem "_" quer dizer que o jogo ainda não foi ganho

    if(correct_word):
        print("Parabéns, você ganhou :)");
    else:
        print("Você perdeu, diga suas últimas palavras:")
        dead = input("Diga algo: ");
        print(dead, "|Foram suas últimas palavras. Fim de jogo|");

if(__name__ == "__main__"):
    play();
