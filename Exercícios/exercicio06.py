#Valida o input de uma senha somente se a mesma cumprir todos os requisitos
while True:
    senha = str(input("Digite sua senha : "))
    if senha.islower():
        print("A senha deve ter pelo menos um caractere MAIUSCULO: ")
    elif len(senha) < 7 :
        print("A senha deve ter pelo menos 8 caracteres: ")
    elif senha.isalpha() :
        print("Necessita de um numero: ")
    elif senha.isalnum() :
        print("Necessita de um Caractere especial: ")
    else:
        break