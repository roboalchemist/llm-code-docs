# Source: https://docs.enate.net/enate-help/portugues/anexo/comportamento-do-sistema-para-determinar-usuarios-responsaveis-proprietarios-e-filas-dos-itens-de-t.md

# Comportamento do sistema para determinar usuários responsáveis, proprietários e filas dos itens de t

Como parte da gestão de Tickets, Casos e Ações nos seus processos de trabalho no Enate, o sistema avalia regularmente a quem o trabalho está atribuído, quem está definido como Proprietário e a qual Fila o item de trabalho está vinculado. Para determinar isso, existem regras detalhadas a serem seguidas.

Antes de conferir essas regras detalhadas, é importante entender o padrão de como essas alocações de itens de trabalho são avaliadas e quando, de fato. Isso funciona da seguinte maneira:

1. Primeiro nós [determinamos QUANDO essas reavaliações ocorreram](#determinar-quando-as-reavaliacoes-ocorrem). Essencialmente, isso ocorre quando algo muda no card de “Status” do item de trabalho.
2. Quando o sistema determina que precisa fazer uma avaliação, nós inicialmente usamos o status/a situação de um item de trabalho para[ determinar quais dos valores de Responsável, Proprietário e Fila precisam ser definidos e quais precisam ser Apagados completamente](#determinar-se-os-valores-responsavel-proprietario-e-fila-precisam-ser-definidos-ou-apagados).
3. [Para os que precisarem de configuração](#como-um-usuario-responsavel-um-proprietario-e-uma-fila-sao-definidos):
   1. Se for necessário definir uma Fila, é simples: basta selecionar a Fila referenciada na regra de Alocação (existem somente dois tipos de regra de alocação de Fila para seguir).
   2. Para o Responsável e o Proprietário, existem mais detalhes: é necessário passar por uma série de regras em uma ordem, parando quando a regra é cumprida e um alvo válido\* é selecionado.

\*[Verificação de validade](#verificacoes-de-validade): como parte da verificação de regra de alocação de Responsável/Proprietário, precisamos determinar se o alvo é válido (existem várias regras de verificação de validade que precisam ser cumpridas). Em caso negativo, continuamos com as regras da parte 3 até um alvo válido ser encontrado.

Agora que o padrão em questão foi descrito, podemos conferir cada conjunto de regras aplicados para as seções 1 a 3 acima e para as verificações de validade de alvo.

## Determinar QUANDO as reavaliações ocorrem

O sistema reavaliará o Usuário Designado, o Proprietário e a Fila sempre que as informações do card de Status mudarem, especificamente:

* o Status mudar
* a Tipo de Espera mudar
* a Data de Acompanhamento Programada mudar
* a data de “Aguardar por mais informações” mudar
* a opção “Aguardando” mudar (somente para Casos)
* o Contexto do Ticket mudar
* a Categoria do Ticket mudar
* o status “Em revisão” mudar
* Novas Informações serem recebidas sobre o item de trabalho
* Um Caso encontrar um problema

## Determinar se os valores Responsável, Proprietário e Fila precisam ser definidos ou apagados

Quando o sistema determina que precisa fazer uma avaliação, nós inicialmente usamos o ESTADO de um item de trabalho para determinar quais dos valores de Responsável, Proprietário e Fila precisam ser definidos e quais precisam ser Apagados completamente. Você pode ver essas informações na tabela abaixo:

| <p><strong>Status/Situação de Item de Trabalho</strong></p><p> </p> | <p><strong>Responsável</strong></p><p> </p> | <p><strong>Proprietário</strong></p><p> </p> | <p><strong>Fila</strong></p><p> </p> |
| ------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------- | ------------------------------------ |
| <p>Fechado</p><p> </p>                                              | <p>Apagar valor</p><p> </p>                 | <p>Apagar valor</p><p> </p>                  | <p>Apagar valor</p><p> </p>          |
| <p>Rascunho</p><p> </p>                                             | <p>Defina um valor</p><p> </p>              | <p>Apagar valor</p><p> </p>                  | <p>Apagar valor</p><p> </p>          |
| <p>Novas informações recebidas</p><p> </p>                          | <p>Defina um valor</p><p> </p>              | <p>Apagar valor</p><p> </p>                  | <p>Defina um valor</p><p> </p>       |
| <p>Atenção Necessária (relevante somente para um Caso)</p><p> </p>  | <p>Defina um valor</p><p> </p>              | <p>Apagar valor</p><p> </p>                  | <p>Defina um valor</p><p> </p>       |
| <p>A Fazer ou Em Andamento para uma Ação ou um Ticket</p><p> </p>   | <p>Defina um valor</p><p> </p>              | <p>Apagar valor</p><p> </p>                  | <p>Defina um valor</p><p> </p>       |
| <p>A Fazer ou Em Andamento para um Caso</p><p> </p>                 | <p>Apagar valor</p><p> </p>                 | <p>Defina um valor</p><p> </p>               | <p>Apagar valor</p><p> </p>          |
| <p>Resolvido ou Esperando</p><p> </p>                               | <p>Apagar valor</p><p> </p>                 | <p>Defina um valor</p><p> </p>               | <p>Apagar valor</p><p> </p>          |

&#x20;

## Como um usuário Responsável, um Proprietário e uma Fila são definidos

* **Filas**: se uma Fila precisar ser definida, é simples: o [método de alocação de fila](https://d.docs.live.net/o/-MMRJw5Faehepj28yGyJ/s/-MWYnDNwe3Cuo4zlGbs5-887967055/~/changes/1591/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method) é executado.
* **Responsável e Proprietário** - Se um Responsável ou Proprietário precisar ser definido, existem alguns detalhes para se ter em mente. É necessário passar por uma série de regras em uma ordem, parando quando a regra é cumprida e um [alvo válido](https://d.docs.live.net/o/-MMRJw5Faehepj28yGyJ/s/-MWYnDNwe3Cuo4zlGbs5-887967055/~/changes/1591/work-manager/work-manager-2021.1/appendix/system-behaviour-for-determining-assignee-owner-and-queue-for-work-items#validity-checks) é selecionado.

Antes de a lista de regras ser executada, existe uma verificação de nível mais alto: se um Responsável/Proprietário estiver definido atualmente, **não modifique o Responsável/Proprietário a menos que a Categoria do Ticket tenha mudado**.

Caso contrário, execute as seguintes regras, na ordem, parando quando um alvo válido for identificado:

1\.      Se a opção “Manter comigo” tiver sido definida em um item de trabalho, o Responsável/Proprietário será definido como o usuário que selecionou “Manter comigo”. Caso contrário, ou caso o usuário resultante seja inválido, então

2\.      Se o usuário Proprietário não estiver em branco, defina Responsável para o mesmo valor. Caso contrário, ou caso o usuário resultante seja inválido, então

<mark style="color:green;">3.      Se o item de trabalho for um Ticket e a categoria do Ticket tiver mudado e, ou o “Tipo de espera” mudou ou o status for Resolvido, o Responsável/Proprietário será definido como o usuário que estiver atualmente atualizando o Ticket. Se não, então</mark>

4\.      Se o item de trabalho não for um Ticket OU for um Ticket (onde a Categoria dele não mudou E temos mais de 2 linhas de histórico de status, ou seja, não está em seu primeiro estado não-rascunho), então:

&#x20;     1\.      Defina o Responsável e o Proprietário para o último usuário/robô a atualizar o item de trabalho. Caso não haja, ou caso o usuário resultante seja inválido, então

&#x20;     2\.      Defina o Responsável/Proprietário para um usuário/robô qualquer anteriormente atribuído em ordem decrescente de quando foi designado. Caso não haja, ou caso o usuário resultante seja inválido, então

&#x20;     3\.      Se a Ação tiver sido iniciada pelo processo de trabalho (ou seja, ad-hoc não manual), definir o Responsável/Proprietário como o último usuário/robô a trabalhar na mesma Ação anteriormente concluída do Caso (ou Revisar a Ação, se estiver em uma revisão). Caso não haja, ou caso o usuário resultante seja inválido, então

5\.      Execute a [Regra de Alocação](https://d.docs.live.net/o/-MMRJw5Faehepj28yGyJ/s/-MWYnDNwe3Cuo4zlGbs5-887967055/~/changes/1591/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours) deste item de trabalho:

&#x20;     1\.      Se a alocação por envio primária estiver configurada para um usuário específico, defina o Responsável/Proprietário para esse usuário. Caso não haja, ou caso o usuário resultante seja inválido, então

&#x20;     2\.      Se a alocação por envio secundária estiver configurada para um usuário específico, defina o Responsável/Proprietário para esse usuário. Caso não haja, ou caso o usuário resultante seja inválido, então

&#x20;     3\.      Se a alocação por envio primária estiver configurada para o Cargo, dos usuários que ocupam esse cargo, defina o Responsável/Proprietário para o usuário com menos itens de trabalho na caixa de entrada. Caso não haja, ou caso o usuário resultante seja inválido, então

&#x20;     4\.      Se a alocação por envio secundária estiver configurada para o Cargo, dos usuários que ocupam esse cargo, defina o Responsável/Proprietário para o usuário com menos itens de trabalho na caixa de entrada. Caso não haja, ou caso o usuário resultante seja inválido, então

6\.      Se o item de trabalho estiver em um Caso, defina o Responsável/Proprietário para o usuário/robô que iniciou o Caso.

## Verificações de validade

Como parte da verificação da regra de alocação de Responsável/Proprietário, temos de determinar se o alvo é válido. Para ser válido, existem várias regras de verificação de validade que ele precisa cumprir. Em caso negativo, continuamos com as regras para definir um Responsável/Proprietário até um alvo válido ser encontrado. As verificações de validade executadas são estas:

* Se o Usuário/Robô não tiver permissão para trabalhar nos itens de trabalho desse tipo (ou seja, Ativo/Em teste), então bloquear
* Se o Usuário/Robô estiver aposentado, então bloquear
* Se o Usuário não tiver permissão, então bloquear (sem verificação de permissão para Robôs)
* Se o Robô estiver suspenso, então bloquear
* Se o Robô tiver executado "Obter mais trabalho” mais de 3 vezes para esse item de trabalho, então bloquear
* Se o usuário selecionado for um Robô e o item de trabalho for uma Ação que está na etapa de Revisão, então bloquear (Robôs não podem executar Revisões)
* Se o usuário selecionado for um Robô e o item de trabalho for uma Ação e nenhuma Robot Farm estiver configurada para a Ação, então bloquear
* Se o usuário selecionado for um Robô e o item de trabalho for uma Ação e o Robô não for membro de uma Robot Farm configurada para a Ação, então bloquear
* Se o usuário selecionado for um Robô e o item de trabalho for um Caso, então bloquear (Robôs não podem ser designados a Casos)
* Se o item de trabalho for um manual com a Ação de Revisão que está na etapa de Revisão e o Usuário tiver executado uma ou mais atualizações enquanto estava na etapa Fazendo, então bloquear (usuários não podem executar revisões em seu próprio trabalho)
* Se o item de trabalho for um manual com a Ação de Revisão que está na etapa Fazendo e o Usuário tiver executado uma ou mais atualizações enquanto estava na etapa Revisão, então bloquear (usuários não podem trabalhar em algo em que tenha feito uma revisão anteriormente)
