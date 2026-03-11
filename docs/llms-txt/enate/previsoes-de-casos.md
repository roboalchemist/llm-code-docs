# Source: https://docs.enate.net/enate-help/portugues/itens-de-trabalho/previsoes-de-casos.md

# Previsões de Casos

## Visão geral

Usuários da versão v2024.1 poderão usar o recurso de previsões para fazer estimativas mais precisas para os esforços dos itens de trabalho, o que permite planejar os recursos necessários melhor.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTY5NTg1MQ==?utm_source=gitbook&utm_medium=iframely>" %}

Em longo prazo, esses dados podem ser coletados e retornados aos usuários administradores para ajustar os temporizadores de esforço estimado e fornecer previsões melhores para volumes de trabalho futuros.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FnYeoNUJ5dTqTOKXw77Un%2Fimage.png?alt=media&#x26;token=06a79af5-c5d3-436e-9833-9c3a917671b1" alt=""><figcaption></figcaption></figure>

## Como usar o recurso de previsões

Quando o recurso de Previsões for habilitado, uma nova guia “Previsão de esforço” aparecerá em Casos no Gerenciador de Trabalho.

Aqui, você verá um resumo do esforço estimado para todo o Caso, um detalhamento do esforço estimado das Ações ou dos Subcasos que compõem o Caso e um detalhamento do esforço estimado das Ações ou dos Subcasos que ainda não foram criados.

## Resumo do esforço de caso

A seção “Resumo do esforço de caso” é onde um usuário pode mudar o tempo estimado para o Caso. Ela também mostra outras métricas úteis para o Caso.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FAkbzlY1WeX2mbgdAmO6c%2Fimage.png?alt=media&#x26;token=19708074-6c24-4828-9fa2-a6e16cfff949" alt=""><figcaption></figcaption></figure>

O esforço “Estimado” mostra o tempo total estimado que o caso levará. Isso pode ser atualizado por uma estimativa mais precisa.

* Essa é a soma do esforço “Estimado” de todo o trabalho criado e das Ações (e Ações de Subcasos) que compõem o Caso e o valor “Esforço para trabalho ainda não criado”.
* O campo mostrará inicialmente o valor manual “Esforço inicial estimado por registro” do Criador (se houver) multiplicado pela quantidade de registros.
  * Se a “Quantidade de registros” for atualizada, o “Esforço estimado” do Caso que não foi atualizado por um usuário do Gerenciador de Trabalho será atualizado para refletir essa mudança.
* Quando o Caso estiver no estado Resolvido ou Fechado, seu esforço estimado não poderá mais ser alterado.
* Tenha em mente que aumentar esse valor aumentará a estimativa “Esforço para trabalho ainda não criado” e vice-versa.
* O esforço “Real” mostra o tempo gasto de fato trabalhando no Caso.
  * É a soma do esforço “Real” de todas as Ações e os Subcasos que compõem o Caso, retirados dos seus respectivos gerenciadores de tempo.
* “Restante estimado” mostra o tempo estimado restante no Caso.
  * Essa é a soma do esforço “Restante estimado” de todas as Ações e Subcasos que compõem o Caso E o tempo restante estimado do trabalho que ainda não foi criado (portanto, ele pode nem sempre ser igual ao esforço Estimado do caso menos o esforço Real do caso).

Mudar o valor “Esforço estimado” de um Caso tem os seguintes efeitos:

* Atualização automática para o valor estimado de “Esforço para trabalho ainda não criado”. Isso é porque o “Esforço estimado”para o Caso é um valor calculado composto da soma do esforço “Estimado” de todo trabalho criado e das Ações (e Ações de Subcasos) que compõem o Caso, e o valor “Esforço para trabalho ainda não criado”.
  * Aumentar o esforço estimado de um Caso também aumenta o valor do “Esforço para trabalho ainda não criado” pelo mesmo valor.
  * Diminuir o esforço estimado de um Caso também diminui o ”Esforço para trabalho ainda não criado” pelo mesmo valor.

## Detalhamento do esforço do trabalho criado

O “Detalhamento do esforço do trabalho criado” é onde um usuário pode mudar o tempo estimado para cada Ação (e Subcasos) individual criada que compõe o Caso. Isso também mostra outras métricas úteis de cada Ação criada (e Subcasos) que compõe o Caso.

Tenha em mente que, quando uma Ação estiver no estado Resolvido ou Fechado, seu esforço estimado não poderá mais ser alterado.

À medida que as Ações (e os Subcasos) são criadas, o esforço estimado para elas é retirado do valor de esforço Estimado da seção “Trabalho ainda não criado” abaixo.

## Detalhamento da ação

Para cada Ação, você verá:

* Um link para cada Ação
* “Esforço estimado”, que mostra o tempo total estimado que a ação levará. Isso pode ser atualizado por uma estimativa mais precisa.
  * O campo mostrará inicialmente o valor manual “Esforço inicial estimado por registro” do Criador multiplicado pela quantidade de registros.
    * Se a “Quantidade de registros” for atualizada, o “Esforço estimado” de quaisquer Ações em andamento que não tiverem sido atualizadas por um usuário do Gerenciador de Trabalho serão atualizadas para refletir essa mudança.
  * Aumentar esse valor diminuirá a estimativa de “Trabalho ainda não criado” e vice-versa e, portanto, pode afetar o esforço total estimado para o caso.
  * Tenha em mente que, quando uma Ação estiver no estado Resolvido ou Fechado, seu esforço estimado não poderá mais ser alterado.
* O esforço “Real” mostra o tempo gasto até agora trabalhando nessa Ação.
  * O valor é retirado do gerenciador de tempo da Ação.
* “Restante estimado” mostra o tempo estimado restante na Ação.
  * Ele é calculado subtraindo o esforço “Real” do esforço “Estimado” da Ação.
* A data-limite da Ação.
  * Você também verá um valor “Início até” se o esforço “Real” for atualmente zero. Esse valor mostra quando é o prazo máximo absoluto em que essa Ação deve começar para ser concluída até a data-limite.
* O status da Ação.

Mudar o valor “Esforço estimado” de uma Ação tem os seguintes efeitos:

* Atualização automática para o valor estimado de “Esforço para trabalho ainda não criado” do Caso.
* Possível atualização automática para o esforço estimado de todo o Caso.

Detalhes:

* Diminuir o esforço estimado de uma Ação aumenta o valor do “Esforço para trabalho ainda não criado” do Caso pelo mesmo valor (mantendo o esforço estimado de todo o Caso o mesmo).
* Aumentar o esforço estimado de uma Ação diminui o valor do “Esforço para trabalho ainda não criado” do Caso pelo mesmo valor. Isso pode ou não afetar o esforço estimado geral do Caso.
  * Se o “Esforço estimado” atualizado de uma Ação não aumentar o suficiente para fazer o valor de “Esforço para trabalho ainda não criado” do Caso chegar a abaixo de 0, o esforço estimado para o Caso não será afetado.
    * Exemplo: digamos que o esforço estimado para a Ação 1 seja 2 horas, o “Esforço para trabalho ainda não criado” estimado seja 1 hora e o esforço estimado para o Caso seja 3. Um usuário decide que a Ação 1 levará 1 hora mais e por isso atualizou o esforço estimado para a Ação 1 de 2 para 3 horas. O “Esforço para trabalho ainda não criado” diminuirá de 1 hora para 0, e o esforço estimado para o Caso não mudará, permanecendo 3 horas.
  * Se o “Esforço estimado” atualizado de uma Ação aumentar o suficiente para fazer o valor de “Esforço para trabalho ainda não criado” do Caso chegar a abaixo de 0, a diferença será adicionada ao “Esforço estimado” para o Caso geral.
    * Exemplo: digamos que um Caso só tem uma Ação criada chamada Ação 1. O esforço estimado para a Ação 1 é 2 horas, o “Esforço para trabalho ainda não criado” estimado é 0 hora e o esforço estimado para o Caso todo é 2 horas. Um usuário decide que a Ação 1 levará 1 hora mais e por isso atualiza o esforço estimado para a Ação 1 de 2 para 3 horas. Como o “Esforço para trabalho ainda não criado” é 0, o esforço estimado para o caso geral aumentará em 1 hora, mudando de 2 para 3 horas.
      * Exemplo 2: digamos que um Caso só tem uma Ação criada chamada Ação 1. O esforço estimado para a Ação 1 é 2 horas, o “Esforço para trabalho ainda não criado” estimado é 1 hora e o esforço estimado para o Caso todo é 3 horas. Um usuário decide que a Ação 1 demorará 2 horas mais e por isso atualiza o esforço estimado da Ação 1 de 2 para 4 horas, fazendo o “Esforço para trabalho ainda não criado” diminuir em 1 hora, de 1 para 0 (diminuindo o máximo possível). A 1 hora “restante” será efetivamente adicionada ao esforço total estimado do Caso, que aumentará em 1 hora, de 3 a 4 horas.

## Detalhamento de subcaso

Se um Subcaso for criado, você verá:

* Um link para o Subcaso se você tiver permissão para acessá-lo (caso contrário, você verá somente o nome e o número de referência do Subcaso sem um link)
* Uma linha “total” do subcaso com o seguinte:
  * O esforço estimado mostra o tempo total estimado que o subcaso levará. Isso pode ser atualizado por uma estimativa mais precisa.
    * Essa é a soma do esforço “Estimado” de todas as Ações criadas e ainda não criadas que compõem o Subcaso.
      * O campo mostrará inicialmente o valor manual “Esforço inicial estimado por registro” do Criador multiplicado pela quantidade de registros.
        * Se a “Quantidade de registros” for atualizada, o “Esforço estimado” do Subcaso que não foi atualizado por um usuário do Gerenciador de Trabalho será atualizado para refletir essa mudança.
      * Quando um Subcaso estiver no estado Resolvido ou Fechado, seu esforço estimado não poderá mais ser alterado.
      * Tenha em mente que aumentar esse valor aumentará a estimativa “Esforço de trabalho ainda não criado” do Subcaso e vice-versa.
  * O esforço “Real” mostra o tempo gasto até agora trabalhando nesse Subcaso.
    * Essa é a soma do esforço “Real” de todas as Ações que compõem o Subcaso, retirados dos seus respectivos gerenciadores de tempo.
  * “Restante estimado” mostra o tempo estimado restante no Subcaso.
    * Essa é a soma do esforço “Restante estimado” de todas as Ações que compõem o Subcaso E do tempo restante estimado do trabalho que ainda não foi criado para o Subcaso (portanto, ele pode nem sempre ser igual ao esforço Estimado do subcaso menos o esforço Real do subcaso).
      * A data-limite do Subcaso.
      * O status do Subcaso.
* Uma linha para cada Ação do Subcaso com o seguinte:
  * O esforço estimado mostra o tempo total estimado que a ação do subcaso levará. Isso pode ser atualizado por uma estimativa mais precisa.
    * O campo mostrará inicialmente o valor manual “Esforço inicial estimado por registro” do Criador multiplicado pela quantidade de registros.
      * Se a “Quantidade de registros” for atualizada, o “Esforço estimado” de quaisquer Ações de Subcaso em andamento que não tiverem sido atualizadas por um usuário do Gerenciador de Trabalho serão atualizadas para refletir essa mudança.
      * Aumentar esse valor diminuirá a estimativa de “Trabalho ainda não criado” do Subcaso e vice-versa e, portanto, pode afetar o esforço total estimado para o subcaso.
      * Quando uma Ação estiver no estado Resolvido ou Fechado, seu esforço estimado não poderá mais ser alterado.
  * O esforço “Real” mostra o tempo gasto até agora trabalhando nessa Ação de Subcaso.
    * O valor é retirado do gerenciador de tempo da Ação do Subcaso.
  * “Restante estimado” mostra o tempo estimado restante na Ação do Subcaso.
    * É calculado subtraindo o esforço “Real” do esforço “Estimado” da Ação do Subcaso.
  * A data-limite da Ação do Subcaso.
    * Você também verá um valor “Início até” se o esforço “Real” for atualmente zero. Esse valor mostra quando é o prazo máximo absoluto em que essa Ação de Subcaso deve começar para ser concluída até a data-limite.
  * O status da Ação de Subcaso.
* Uma linha para “Trabalho de subcaso ainda não criado” com o seguinte:
  * “Esforço estimado” mostra quanto esforço estima-se ser necessário para completar as ações de subcaso que ainda não foram criadas. Isso pode ser atualizado por uma estimativa mais precisa.
    * Mudar a estimativa afetará o esforço estimado para o Subcaso e pode afetar o esforço estimado para o Caso geral

Mudar o valor “Esforço estimado” de uma Ação de Subcaso tem os seguintes efeitos:

* Atualização automática para o valor estimado de “Esforço para trabalho ainda não criado” do Subcaso.
* Possível atualização automática para o esforço estimado de todo o Subcaso.
* Possível atualização automática para o esforço estimado de todo o caso pai.

Detalhes:

* Diminuir o esforço estimado de uma ação de subcaso aumentará o valor de “Esforço para trabalho ainda não criado” pelo mesmo valor (deixando o esforço estimado para o subcaso todo o mesmo e, portanto, não afetando o esforço estimado do Caso pai todo).
* Aumentar o esforço estimado para uma Ação de Subcaso diminui o valor do ”Esforço para trabalho ainda não criado” do Subcaso pelo mesmo valor. Isso pode ou não afetar o esforço estimado geral do Caso.
  * Se o esforço estimado atualizado de uma Ação de Subcaso não aumentar o suficiente para fazer o valor de “Esforço para trabalho ainda não criado” do Subcaso chegar a abaixo de 0, o esforço estimado para o Subcaso não será afetado (e por isso o esforço estimado do Caso pai também não será afetado).
    * Exemplo: digamos que um Subcaso só tem uma Ação criada chamada Ação de Subcaso 1. O esforço estimado para a Ação de Subcaso 1 é 2 horas e o “Esforço para trabalho ainda não criado” estimado é 1 hora, portanto o esforço estimado para o Subcaso é de 3 horas. Um usuário decide que a Ação 1 do Subcaso demorará 1 hora mais e por isso atualiza o esforço estimado da Ação 1 do Subcaso de 2 para 3 horas, fazendo o “Esforço para trabalho ainda não criado” do Subcaso diminuir de 1 hora para 0. O esforço estimado para o Subcaso não mudará, continuando em 3 horas (e portanto o esforço estimado para o Caso pai todo não será afetado).
  * Se o esforço estimado atualizado de uma Ação de Subcaso aumentar o suficiente para fazer o valor de “Esforço para trabalho ainda não criado” do Subcaso chegar a abaixo de 0, a diferença será adicionada ao esforço estimado para o Subcaso geral (e portanto pode afetar o esforço estimado para o Caso pai todo).
    * Exemplo: digamos que um Subcaso só tem uma Ação criada chamada Ação de Subcaso 1. O esforço estimado para a Ação de Subcaso 1 é 2 horas e o “Esforço para trabalho ainda não criado” estimado é 0 hora, portanto o esforço estimado para o Subcaso geral é de 2 horas. Um usuário decide que a Ação de Subcaso 1 levará 1 hora mais e por isso atualiza o esforço estimado para a Ação de Subcaso 1 de 2 para 3 horas. Como o “Esforço para trabalho ainda não criado” do Subcaso é 0, o esforço estimado para o subcaso todo aumentará em 1 hora, mudando de 2 para 3 horas.
      * Se houver tempo suficiente no “Esforço para trabalho ainda não criado” do Caso pai, esse aumento de 1 hora pode ser retirado dele, portanto não haveria impacto sobre o esforço estimado do Caso pai todo.
      * Se não houver tempo suficiente no “Esforço para trabalho ainda não criado” do Caso pai, esse aumento de 1 hora resultará em um aumento no esforço estimado do Caso pai todo.
    * Exemplo 2: digamos que um Subcaso só tenha uma Ação criada chamada Ação de Subcaso 1. O esforço estimado para a Ação de Subcaso 1 é 2 horas e o “Esforço para trabalho ainda não criado” estimado é 1 hora, portanto o esforço estimado para o Subcaso geral é de 3 horas. Um usuário decide que a Ação 1 do Subcaso demorará 2 horas mais e por isso atualiza o esforço estimado da Ação 1 do Subcaso de 2 para 4 horas, fazendo o “Esforço para trabalho ainda não criado” do Subcaso diminuir o máximo possível, nesse caso de 1 hora para 0. A 1 hora “restante” será efetivamente adicionada ao esforço estimado total do Subcaso, que aumentará em 1 hora, de 3 a 4 horas.
      * Se houver tempo suficiente no “Esforço para trabalho ainda não criado” do Caso pai, esse aumento de 1 hora pode ser retirado dele, portanto não haveria impacto sobre o esforço estimado do Caso pai todo.
      * Se não houver tempo suficiente no “Esforço para trabalho ainda não criado” do Caso pai, esse aumento de 1 hora resultará em um aumento no esforço estimado do Caso pai todo.

## Esforço para trabalho ainda não criado

O “Esforço para trabalho ainda não criado” mostra quanto esforço mais estima-se ser necessário para completar as Ações (e Ações de subcaso) que ainda não foram criadas para esse Caso.

Para calcular isso, subtrai-se o esforço estimado por trabalho criado do esforço estimado do Caso. Portanto, aumentar o “Esforço para trabalho ainda não criado” aumentará a estimativa de esforço do Caso geral e vice-versa.

À medida que as Ações (e os Subcasos) são criadas, o esforço estimado para elas é retirado do valor de “Esforço estimado para trabalho ainda não criado”.

Quando o Caso estiver no estado Resolvido ou Fechado, seu “esforço para trabalho ainda não criado” não poderá mais ser alterado.
