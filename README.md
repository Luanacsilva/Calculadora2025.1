Calculadora 2025.1



Calculadora simples em Python que permite realizar operações aritméticas básicas (soma, subtração, multiplicação, divisão) e algumas operações adicionais (exponenciação, módulo, raiz quadrada). O programa foi desenvolvido para ser executado via terminal e inclui tratamento de erros e validação de entrada.

Funcionalidades
Soma
Subtração
Multiplicação
Divisão (com tratamento de divisão por zero)
Exponenciação (x^y)
Módulo (x % y)
Raiz Quadrada (x)
Outros destaques
Suporte a números decimais
O programa utiliza float, permitindo a inserção de valores decimais.

Validação de Entrada
Se o usuário inserir algo que não seja numérico, é exibida uma mensagem de erro e o programa solicita novamente o valor.

Tratamento de Erros

Divisão por zero: exibe mensagem apropriada em vez de encerrar o programa abruptamente.
Exponenciação: caso resulte em valores muito grandes, o Python pode lançar um OverflowError, que também pode ser tratado.
Raiz de número negativo: exibe mensagem de erro quando o valor é negativo.
Loop Interativo
Permite realizar múltiplas operações sem precisar reiniciar o programa.



Requisitos
Python 3.x

Como Usar
Clone o repositório:
git clone https://github.com/Luanacsilva/Calculadora2025.1.git


Acesse o diretório do projeto:
cd Calculadora2025.1


Execute o programa:
python calculadora.py



Estrutura do Projeto
calculadora.py: Arquivo principal contendo a implementação da calculadora.
README.md: Este arquivo com informações e instruções sobre o projeto.
(Outros arquivos, se houver, podem ser adicionados conforme o projeto evolua.)

Melhorias Futuras
Adicionar novas operações matemáticas (fatorial, logaritmos, etc.).
Implementar uma interface gráfica.
Incluir testes unitários para maior robustez do código.
Adicionar suporte a operações mais complexas e funcionalidades extras.




Contribuição
Contribuições são sempre bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para:




Abrir uma issue: descreva o problema ou sugestão.



Enviar um pull request: faça um fork do projeto, implemente a mudança e submeta para análise.




Licença
Este projeto está licenciado sob a MIT License.

