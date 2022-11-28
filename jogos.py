import forca
import jogo_adivinhacao

print("**********************************");
print("ESCOLHA O SEU JOGO:");
print("**********************************");

print(" | (1) Adivinhação (2) Forca | ")
game = int(input("Selecione o jogo:"));

if(game == 1):
    print("Jogo da Adivinhação");
    jogo_adivinhacao.play();
elif(game == 2):
    print("Jogo da Forca");
    forca.play();