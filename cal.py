def ler_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def calcular():
    print("Calculadora Simples")
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        
        op = input("Digite a opção: ")
        
        if op == "0":
            print("Encerrando a calculadora.")
            break
        
        if op in ["1", "2", "3", "4"]:
            x = ler_numero("Digite o primeiro número: ")
            y = ler_numero("Digite o segundo número: ")
            
            if op == "1":
                resultado = x + y
            elif op == "2":
                resultado = x - y
            elif op == "3":
                resultado = x * y
            elif op == "4":
                if y == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = x / y
            
            print("Resultado:", resultado)
        else:
            print("Opção inválida! Tente novamente.")

calcular()
