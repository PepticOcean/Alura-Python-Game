print("**********************************");
print("Bem-vindo ao jogo de adivinhação");
print("**********************************");

secret_number = 42;
maximum_attempts = 3;
current_tempt = 1;

while(current_tempt <= maximum_attempts):
    choice = int(input("Digite o seu número: ")); # Transformando o input "String" para "Int"
    print("Você digitou o número" , choice);
    if(choice == secret_number): 
        print("Você acertou :)");
        break;
    else:
        if(choice < secret_number):
            print("O número que você digitou é menor do que o número sorteado");
            current_tempt += 1;
        if(choice > secret_number):
            print("O número que você digitou é maior do que o número sorteado");
            current_tempt += 1;

print("********************************************************************");
print("FIM DE JOGO (APERTE F5 PARA JOGAR NOVAMENTE");
print("********************************************************************");
