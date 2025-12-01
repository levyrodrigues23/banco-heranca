# atividade de herança

## Para esta atividade, eu resolvi aplicar os conceitos de herança na atividade de banco. Vou detalhar melhor as mudanças que eu acabei realizando:

### Herança em Conta
> - Apliquei herança na classe Conta, ou seja, existem outras classes como classe ContaCorrente, ContaPoupanca e ContaInvestimento que herdam os atributos da superclasse. Sendo mais direto, eles pegam os métodos também.
>- Além disso, coloquei algumas classes protegidas para facilitar e fiz o uso que vi em um livro específico do property, ou seja, ao inves de implementar os tipicos get e set, o python me permite fazer de uma forma diferente colocando property e depois so chamar o outro método como setter. 
>- Apliquei o super para pegar os atributos da superclasse.
> - Em banco Lista não fiz muitas mudanças, pois não foi necessario aplicar herança nesse sentido.

### Menu
> - Apliquei um menu que puxa os métodos da classe banco, me permitindo executar os comandos de forma tranquila. Eu também coloquei ```if __name__ == "__main__"``` para que eu execute diretamente o main sem executar um print externo, por exemplo com os teste que eu apliquei.

### Eu penso em realizar algumas mudanças futuras aplicando encapsulamento e polimorfismo, mas não consegui pensar em outra forma de ampliar o paradigma de herança senão aplicando a parte das Contas.