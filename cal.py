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
        print("5 - Exponenciação (x^y)")
        print("6 - Módulo (x % y)")
        print("7 - Raiz Quadrada (x)")
        print("0 - Sair")
        
        op = input("Digite a opção: ")
        
        if op == "0":
            print("Encerrando a calculadora.")
            break
        
        # Operações com dois números
        if op in ["1", "2", "3", "4", "5", "6"]:
            x = ler_numero("Digite o primeiro número: ")
            y = ler_numero("Digite o segundo número: ")
            
            try:
                if op == "1":
                    resultado = x + y
                elif op == "2":
                    resultado = x - y
                elif op == "3":
                    resultado = x * y
                elif op == "4":
                    # Verifica divisão por zero
                    resultado = x / y
                elif op == "5":
                    resultado = x ** y
                elif op == "6":
                    # Verifica divisão por zero no módulo
                    resultado = x % y

                print("Resultado:", resultado)

            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
            except OverflowError:
                print("Erro: O resultado é muito grande para ser representado.")
            
        # Operação com apenas um número (raiz quadrada)
        elif op == "7":
            x = ler_numero("Digite o número: ")
            try:
                if x < 0:
                    raise ValueError("Raiz quadrada de número negativo não é suportada.")
                resultado = x ** 0.5
                print("Resultado:", resultado)
            except ValueError as e:
                print(f"Erro: {e}")
        
        else:
            print("Opção inválida! Tente novamente.")

calcular()

























