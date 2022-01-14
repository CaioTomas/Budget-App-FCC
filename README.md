## English description

This is the repo of my solution to the *Budget App* project from the **Scientific Computing with Python** course from freeCodeCamp. The portuguese README is down below.

### Assignment

Complete the `Category` class in `budget.py`. It should be able to instantiate objects based on different budget categories like *food*, *clothing*, and *entertainment*. When objects are created, they are passed in the name of the category. The class should have an instance variable called `ledger` that is a list. The class should also contain the following methods:

* A `deposit` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of `{"amount": amount, "description": description}`.
* A `withdraw` method that is similar to the `deposit` method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return `True` if the withdrawal took place, and `False` otherwise.
* A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
* A `transfer` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return `True` if the transfer took place, and `False` otherwise.
* A `check_funds` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method should be used by both the `withdraw` method and `transfer` method.

When the budget object is printed it should display:
* A title line of 30 characters where the name of the category is centered in a line of `*` characters.
* A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
* A line displaying the category total.

Here is an example of the output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the `Category` class, create a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

The unit tests for this project are in `test_module.py`.

### Development

Write your code in `budget.py`. For development, you can use `main.py` to test your `Category` class. Click the "run" button and `main.py` will run.

### Testing 

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

-------------------------------------------------------

## Descrição em português

Esse é o repositório com a minha solução para o projeto *Budget App* do curso **Scientific Computing with Python** do freeCodeCamp. A tradução que segue abaixo é livre e feita por mim.

### Tarefa

Complete a classe `Category` em `budget.py`. Ela deve ser capaz de instanciar objetos baseada em diferentes categorias de orçamento como *food*, *clothing* e *entertainment*. Quando os objetos são criados, eles são passados no nome da categoria. A classe deve ter uma variável de instância chamada `ledger` que é uma lista. A classe também dever conter os seguintes métodos:

* Um método `deposit` que aceita uma quantidade e uma descrição. Se nenhuma descrição for dada, ele deve retornar uma string vazia por padrão. O método deve dar append na lista ledger na forma `{"amount": amount, "description": description}`.
* Um método `withdraw` que é similar ao método `deposit`, mas a quantidade passada deve ser guardada no ledger como um número negativo. Se não houver fundos o suficiente, nada deve ser acrescentado ao ledger. Esse método deve retornar `True` se a retirada foi feita e `False` caso contrário.
* Um método `get_balance` que retorn o balanço atual da categoria do orçamento baseado nos depósitos e retiradas ocorridas.
* Um método `transfer` que recebe uma quantidade e outra categoria de orçamento como argumentos. O método deve adicionar uma retirada com a quantidade e a descrição "Transfer to [Destination Budget Category]". O método deve então adicionar um depósito em outra categoria do orçamento com a quantidade e a descrição "Transfer from [Source Budget Category]". Se não houver fundos suficientes, nada deve ser acrescentado a nenhum dos ledgers. O método deve retornar `True` se a transferência ocorreu e `False` do contrário.
* Um método `check_funds` que recebe uma quantidade como argumento. Ele retorna `False` se a quantidade é maior que o balanço da categoria do orçamento e `True` caso contrário. Esse método deve ser usado tanto pelo método `withdraw` quanto pelo método `transfer`.

Quando o objeto budget é printado deve ser mostrado:
* Uma linha de título com 30 caracteres, onde o nome da categoria está centralizado em uma linha de `*`.
* Uma lista dos itens no ledger. Cada linha deve mostrar a descrição e a quantidade. Os primeiros 23 caracteres da descrição devem ser mostrado, e em seguida a quantidade. A quantidade deve estar alinhada à direita, com duas casas decimais e no máximo 7 caracteres.
* Uma linha exibindo o total da categoria.

Exemplo de output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Além da classe `Category`, crie umaa função (fora da classe) chamada `create_spend_chart` que recebe uma lista de categorias como argumento. Ela deve retornar uma string que é um gráfico de barras.

O gráfico deve mostrar a porcentagem gasta em cada categoria passada na função. A porcentagem gasta deve ser calculada apenas com retiradas e não com depósitos. No lado esquerdo do gráfico deve haver labels 0 - 100. As "barras" no gráfico devem ser feitas do caracter "o". A altura de cada barra deve ser arredondada para a dezena mais próxima. A linha horizontal abaixo das barras deve ir dois espaços abaixo da barra final. Cada nome de categoria deve ser escrito verticalmente abaixo da barra. Deve haver um título no topo que diz "Percentage spent by category".

Essa função será testada com até quatro categorias.

Observe atentamente o exemplo de output abaixo e garanta que o espaçamento do output está exatamente igual ao exemplo.

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

Os testes unitários para esse projeto estão em `test_module.py`.

### Desenvolvimento

Escreva seu código em `budget.py`. Para o desenvolvimento, você pode usar `main.py` para testar a sua classe `Category`. Clique em "run" e `main.py` rodará.

### Testando 

Importamos os testes de `test_module.py` para `main.py` por conveniência. Os testes rodarão automaticamente sempre que você clicar em "run".

### Submissão

Copie a URL do projeto e submeta-a para o freeCodeCamp.
