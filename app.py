
def calculadora():                                                   # definindo função principal
    
    while True:                                                      # loop infinito
        print("Calculadora Simples\n")
        print("1. Soma")
        print("2. Subtrai")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        operacao = input("\nSelecione uma opção ou 's' para sair: ") # operacao é a variável com o texto que o usuário digitou

        if operacao == 's' or operacao == 'S':                       # se for 's' ou 'S', sai do loop
            print("\nObrigado por utilizar a Calculadora Simples!\n")
            break                                                    # encerra o loop

        if operacao not in ['1','2','3','4']:                        # verifica se ela não está dentro de uma coleção de opções que eu tenho como válidas
            print("\nOpção inválida, tente novamente.\n")
            continue                                                 # volta na aplicação se a opção for inválida (volta ao loop)
        
        numero_1 = float(input("Primeiro número: "))                 # pega o input do cálculo do usuário e transforma a string
        numero_2 = float(input("Segundo número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("\nO resultado da soma é: ", resultado)
            print()
        elif operacao == '2':                                        # caso contrário se
            resultado = numero_1 - numero_2
            print("\nO resultado da subtração é: ", resultado)
            print()
        elif operacao == '3':                                        # caso contrário se
            resultado = numero_1 * numero_2
            print("\nO resultado da multiplicação é: ", resultado)
            print()
        else:                                                        # caso contrário
            if numero_2 == 0:                                        # caso receba uma divisão por 0, o que não é possível ele retoma o loop
                print("\nDivisões por 0 não são possíveis, tente novamente.\n")
                continue
            else:
                resultado = numero_1 / numero_2
                print("\nO resultado da divisão é: ", resultado)
                print()

calculadora()                                                        # executando a função principal