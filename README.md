# p1-Estrutura-de-dados

![uni_vassouras](https://user-images.githubusercontent.com/118143111/228887189-207ea6c6-72aa-4c50-bf97-80c65b7038e9.png)

Curso: Engenharia de Software.

Participantes: Nicolas Vítor C. de Oliveira e Luís Duarte.

Disciplina: Estrutura de Dados.

Período: 3º.

Professor: Márcio Alexandre Dias Garrido.

------------------------------------------------------

Problema e técnica utilizada para resolução:

O desafio consistia em trabalhar com uma matriz 2D, onde era necessário extrair os elementos dos subarrays, organizá-los em ordem alfabética e, ao mesmo tempo, rastrear sua posição original em outra lista (mapper), para posterior plotagem do Big O. Para solucionar o problema, utilizou-se laços duplos para percorrer os elementos dos subarrays e suas respectivas posições. Em seguida, criou-se um dicionário para armazenar as informações coletadas e, por meio de um único laço, adicionaram-se as chaves do dicionário em uma nova lista, a qual foi organizada alfabeticamente utilizando-se novamente laços duplos. Utilizando as chaves da lista ordenada, buscou-se os valores correspondentes no dicionário criado anteriormente, permitindo a criação de uma nova lista com as posições dos elementos.Para realizar a análise do Big O, foram definidos os tamanhos de entrada, os quais consistem basicamente no comprimento do array, sendo divididos em partes do main-array até a sua completude. Para cada um desses tamanhos de entrada, foi calculado o tempo total de execução da respectiva parte do array.Por fim, utilizou-se a biblioteca Matplotlib para a criação e exibição do gráfico.


------------------------------------------------------

Imagens de ao menos 3 partes do código explicando do que se trata o bloco evidenciado:

//Img 1-----------------------------------------------//

![img_1](https://user-images.githubusercontent.com/118143111/228920710-8fad2c74-10f4-4ee3-9d14-7afab1f2ef54.PNG)


Classe com o nome de SubArrIdxPos, que basicamente é o nome mínimo para Sub-array Index e Position, ou seja, vem de uma matriz, nesse caso, 2D. A classe recebe uma matriz e cria uma lista para os elementos e posições do sub-array. São criadas duas listas, uma para os elementos e outra para as posições, ambas do sub-array, para garantir que o output seja exatamente o que foi solicitado.

//Img 1-----------------------------------------------//

//Img 2-----------------------------------------------//

![img_2](https://user-images.githubusercontent.com/118143111/228919993-b9da69c0-d1f2-487f-b63e-59a189cae0a6.PNG)

É um método da classe SubArrIdxPos com o objetivo de pegar os elementos e as posições do sub-array e colocá-los, respectivamente, no dicionário self.item_pos (elemento e posição) e na lista self.items (array 1D) (apenas o elemento).

//Img 2-----------------------------------------------//


//Img 3-----------------------------------------------//

![img_3](https://user-images.githubusercontent.com/118143111/228920042-d4adf971-a8e5-4ac9-93d8-87886cda85f8.PNG)

É um método da classe SubArrIdxPos com o objetivo de associar os valores dos elementos da lista self.items com suas respectivas posições no dicionário. Isso é realizado pegando os valores da posição através da chave que são exatamente os elementos da lista self.items.

//Img 3-----------------------------------------------//


