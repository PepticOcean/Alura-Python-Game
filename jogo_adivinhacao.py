print("**********************************");
print("Bem-vindo ao jogo de adivinhação");
print("**********************************");

secret_number = 42;

choice = int(input("Digite o seu número: ")); # Transformando o input "String" para "Int"

print("Você digitou o número" , choice);

if(choice == secret_number): 
    print("Você acertou :)");
else:
    if(choice < secret_number):
        print("O número que você digitou é menor do que o número sorteado");
    if(choice > secret_number):
        print("O número que você digitou é maior do que o número sorteado");

print("Fim de Jogo");