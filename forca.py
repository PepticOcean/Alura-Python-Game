import random;

def play():
    #Se segurar ctrl e passar o mouse em cima da função, você será redirecionado para ela

    welcome(); #exibe a mensagem de "Bem vindo a forca"
    secret_word = read_and_sort(); #lê o arquivo com as palavras e sorteia uma delas (além de estar carregando a var secret_word)
    right_letters = start_right_letters(secret_word); #exibe os marcadores de letras além de exibir a letra certa

    hanged = False; #variável para saber se o jogador foi enforcado
    correct_word = False; #variável para saber se o jogador ganhou o jogo
    errors = 0;
    
    print(right_letters);

    while(hanged != True and correct_word != True):
     
        attempt = str.strip(input("Qual a letra que você deseja utilizar?").lower()); 
        #removendo espaços e deixando tudo minúsculo

        if(attempt in secret_word): #se houver a letra na palavra:
            check_attempt(attempt,right_letters,secret_word);
        else:
            errors += 1;
            hang_draw(errors);

        hanged = errors == 6 #Se erros for = 6, a forca acontece e o jogo acaba
        correct_word = "_" not in right_letters; #Se houverem "_" quer dizer que o jogo ainda não foi ganho 

    if(correct_word):
        win_message();
    else:
        lose_message(secret_word);

#############################################################################################################################

def welcome():

    print("**********************************");
    print("******** BEM-VINDO A FORCA *******");
    print("**********************************");

def read_and_sort():
        with open("palavras.txt", "r", encoding="utf-8") as archive: #abrindo o arquivo em modo leitura e no padrão UTF-8
            words = []
            for string in archive:
                string = string.strip();
                words.append(string);

        choose_words = random.randrange(0, len(words));
        secret_word = words[choose_words].lower();
        return secret_word; #retorna o valor da var para que o restante do código possa ler

def start_right_letters(key):
    return ["_" for letter in key]; #Use o Underline para cada letra dentro da palavra secreta

def check_attempt(attempt, right_letters, secret_word): 
    index = 0;
    for letter in secret_word: #percorre o código em busca da letra
        if(attempt == letter):
            right_letters[index] = letter; #coloca a letra na posição correta
            print(right_letters);
        index = index + 1;    

def hang_draw(errors):
    print("  __________")
    print(" |/          ")

    if(errors == 1):
        print(" |        | ")
        print(" |       (_)")
        print(" |          ")
        print(" |          ")
        print(" |          ")
        print(" |          ")


    if(errors == 2):
        print(" |        | ")
        print(" |       (_)")
        print(" |        | ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
    
    if(errors == 3):
        print(" |        | ")
        print(" |       (_)")
        print(" |       /| ")
        print(" |          ")

    if(errors == 4):
        print(" |        | ")
        print(" |       (_)")
        print(" |       /|\ ")
        print(" |          ")

    if(errors == 5):
        print(" |        | ")
        print(" |       (_)")
        print(" |       /|\ ")
        print(" |         \ ")
    
    if(errors == 6):
        print(" |        | ")
        print(" |       (_)")
        print(" |       /|\ ")
        print(" |       / \ ")

    print(" |          ")
    print("_|__          ")
    
    

def win_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def lose_message(secret_word):
    print("Você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    play();
