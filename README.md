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
