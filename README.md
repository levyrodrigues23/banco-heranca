# Sistema Bancário Simples com Herança e Polimorfismo

Este projeto é uma simulação de um sistema bancário, desenvolvido em Python para demonstrar conceitos de Programação Orientada a Objetos (POO), incluindo Herança, Polimorfismo e Encapsulamento.

## Funcionalidades

- **Criação de Bancos**: Permite adicionar novos bancos ao sistema de forma interativa.
- **Criação de Contas**: O sistema suporta a criação interativa de três tipos de contas (`ContaCorrente`, `ContaPoupanca` e `ContaInvestimento`) em qualquer banco cadastrado, todas herdando de uma classe abstrata `Conta`.
- **Operações Bancárias**:
  - **Saque**: Cada tipo de conta implementa sua própria lógica de saque, demonstrando polimorfismo.
  - **Depósito**: Funcionalidade comum implementada na classe base.
  - **Transferência**: Demonstra a verificação dinâmica (coerção) para aplicar regras de negócio específicas, como conceder um bônus ao transferir para uma `ContaInvestimento`.
- **Gerenciamento de Contas**: Um banco pode gerenciar múltiplas contas e realizar operações entre elas.

## Conceitos de POO Aplicados

### Herança

- A classe base abstrata `Conta` define a estrutura e o contrato que todas as contas devem seguir.
- As classes `ContaCorrente`, `ContaPoupanca` e `ContaInvestimento` herdam de `Conta`, especializando o comportamento conforme necessário (ex: regras de saque, atributos específicos).

### Polimorfismo

- O método `sacar()` é abstrato em `Conta` e implementado de forma diferente em cada subclasse.
- A classe `Banco` interage com objetos do tipo `Conta` de forma genérica, e o método `sacar()` correto é chamado em tempo de execução, dependendo do tipo real do objeto.

### Polimorfismo na Transferência (Depósito com Bônus)

- A operação de transferência agora demonstra polimorfismo de forma mais completa. Em vez de usar `isinstance()` para verificar o tipo da conta de destino e aplicar um bônus, o método `depositar()` da `ContaInvestimento` foi sobrescrito.
- Isso significa que, ao transferir para uma `ContaInvestimento`, a própria conta se encarrega de aplicar o bônus de 10% ao receber o depósito, sem que a lógica de transferência precise "saber" qual o tipo específico da conta de destino. A decisão é feita em tempo de execução pelo objeto da `ContaInvestimento`.

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Execute o arquivo `main.py` para iniciar o menu interativo:
   ```bash
   python main.py
   ```
3. Siga as opções do menu para criar bancos, criar contas e testar as funcionalidades de saque e transferência.
