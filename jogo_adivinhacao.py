print("**********************************");
print("Bem-vindo ao jogo de adivinhação");
print("**********************************");

secret_number = 42; # Número sorteado
maximum_attempts = 3; # Número máximo de tentativas
current_atempt = 1; # Tentativa atual

while(current_atempt <= maximum_attempts):

    print("Tentativa atual: {} de {}".format(current_atempt,maximum_attempts));
    choice = int(input("Digite um número de 1 a 100: ")); # Transformando o input "String" para "Int"
    print("Você digitou o número" , choice);


    if(choice < 1 or choice > 100):
        print("Por favor, digite um número entre 1 e 100");
        continue;


    if(choice == secret_number): 
        print("Você acertou :)");
        break;
    else:
        if(choice < secret_number):
            print("O número que você digitou é menor do que o número sorteado");
        if(choice > secret_number):
            print("O número que você digitou é maior do que o número sorteado");
    current_atempt += 1;

print("********************************************************************");
print("FIM DE JOGO (APERTE F5 PARA JOGAR NOVAMENTE");
print("********************************************************************");
