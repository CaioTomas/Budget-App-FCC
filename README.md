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

## Descri????o em portugu??s

Esse ?? o reposit??rio com a minha solu????o para o projeto *Budget App* do curso **Scientific Computing with Python** do freeCodeCamp. A tradu????o que segue abaixo ?? livre e feita por mim.

### Tarefa

Complete a classe `Category` em `budget.py`. Ela deve ser capaz de instanciar objetos baseada em diferentes categorias de or??amento como *food*, *clothing* e *entertainment*. Quando os objetos s??o criados, eles s??o passados no nome da categoria. A classe deve ter uma vari??vel de inst??ncia chamada `ledger` que ?? uma lista. A classe tamb??m dever conter os seguintes m??todos:

* Um m??todo `deposit` que aceita uma quantidade e uma descri????o. Se nenhuma descri????o for dada, ele deve retornar uma string vazia por padr??o. O m??todo deve dar append na lista ledger na forma `{"amount": amount, "description": description}`.
* Um m??todo `withdraw` que ?? similar ao m??todo `deposit`, mas a quantidade passada deve ser guardada no ledger como um n??mero negativo. Se n??o houver fundos o suficiente, nada deve ser acrescentado ao ledger. Esse m??todo deve retornar `True` se a retirada foi feita e `False` caso contr??rio.
* Um m??todo `get_balance` que retorn o balan??o atual da categoria do or??amento baseado nos dep??sitos e retiradas ocorridas.
* Um m??todo `transfer` que recebe uma quantidade e outra categoria de or??amento como argumentos. O m??todo deve adicionar uma retirada com a quantidade e a descri????o "Transfer to [Destination Budget Category]". O m??todo deve ent??o adicionar um dep??sito em outra categoria do or??amento com a quantidade e a descri????o "Transfer from [Source Budget Category]". Se n??o houver fundos suficientes, nada deve ser acrescentado a nenhum dos ledgers. O m??todo deve retornar `True` se a transfer??ncia ocorreu e `False` do contr??rio.
* Um m??todo `check_funds` que recebe uma quantidade como argumento. Ele retorna `False` se a quantidade ?? maior que o balan??o da categoria do or??amento e `True` caso contr??rio. Esse m??todo deve ser usado tanto pelo m??todo `withdraw` quanto pelo m??todo `transfer`.

Quando o objeto budget ?? printado deve ser mostrado:
* Uma linha de t??tulo com 30 caracteres, onde o nome da categoria est?? centralizado em uma linha de `*`.
* Uma lista dos itens no ledger. Cada linha deve mostrar a descri????o e a quantidade. Os primeiros 23 caracteres da descri????o devem ser mostrado, e em seguida a quantidade. A quantidade deve estar alinhada ?? direita, com duas casas decimais e no m??ximo 7 caracteres.
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

Al??m da classe `Category`, crie umaa fun????o (fora da classe) chamada `create_spend_chart` que recebe uma lista de categorias como argumento. Ela deve retornar uma string que ?? um gr??fico de barras.

O gr??fico deve mostrar a porcentagem gasta em cada categoria passada na fun????o. A porcentagem gasta deve ser calculada apenas com retiradas e n??o com dep??sitos. No lado esquerdo do gr??fico deve haver labels 0 - 100. As "barras" no gr??fico devem ser feitas do caracter "o". A altura de cada barra deve ser arredondada para a dezena mais pr??xima. A linha horizontal abaixo das barras deve ir dois espa??os abaixo da barra final. Cada nome de categoria deve ser escrito verticalmente abaixo da barra. Deve haver um t??tulo no topo que diz "Percentage spent by category".

Essa fun????o ser?? testada com at?? quatro categorias.

Observe atentamente o exemplo de output abaixo e garanta que o espa??amento do output est?? exatamente igual ao exemplo.

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

Os testes unit??rios para esse projeto est??o em `test_module.py`.

### Desenvolvimento

Escreva seu c??digo em `budget.py`. Para o desenvolvimento, voc?? pode usar `main.py` para testar a sua classe `Category`. Clique em "run" e `main.py` rodar??.

### Testando 

Importamos os testes de `test_module.py` para `main.py` por conveni??ncia. Os testes rodar??o automaticamente sempre que voc?? clicar em "run".

### Submiss??o

Copie a URL do projeto e submeta-a para o freeCodeCamp.
