# Source: https://docs.enate.net/enate-help/portugues/itens-de-trabalho/card-do-gerenciador-de-tempo.md

# Card de Monitoramento de Tempo

## Visão Geral

Para te ajudar a gerenciar atividades de acordo com seus SLAs, o Enate permite que os usuários registrem o tempo gasto para completar os itens de trabalho, tanto como um total geral quanto de cada colaborador que trabalho nele.

O registro de tempo salva o tempo de cada sessão de navegador em que um item está sendo processado. O tempo é registrado sempre que um item de trabalho está aberto na tela, independentemente se está atribuído ao usuário ou não e do estado do item de trabalho. O registro de tempo corre para um só item de trabalho de cada vez em uma sessão de navegador e também para uma guia de item de trabalho quando recebe o foco da guia do navegador. Ele continua correndo mesmo se o navegador estiver minimizado, se a tela do computador for bloqueada, etc.

No cenário em que um item de trabalho A está aberto (com o tempo correndo) e a guia de um item de trabalho posterior B é aberta, o temporizador é pausado no item A e muda para o item B. Alternar entre essas guias de item de trabalho também troca a qual deles o registro de tempo se aplica.

O registro de tempo é pausado quando a guia de item de trabalho é fechada e caso um navegador ou uma máquina expira.

Veja [aqui ](#quando-o-tempo-e-registrado-e-quando-nao)mais detalhes sobre quando o tempo é registrado ou não no card de Registro de Tempo.

{% hint style="info" %}
Nota importante: Clicar diretamente em um e-mail em qualquer guia de visualização de e-mail iniciará o registro de tempo para o item de trabalho e pausará para todas as outras guias de item de trabalho que estivessem contando tempo logo antes disso.
{% endhint %}

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgwNw==>" %}

O card mostra a duração da sessão atual, um total combinado da duração de todas as sessões anteriores, o tempo de referência esperado e, para Ações e Tickets, a previsão de esforço, que o agente do serviço pode alterar, o que pode ser útil para fazer previsões.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FTUauMIT9YAFVSoYl2G5Q%2Fimage.png?alt=media\&token=dc15a2f3-b315-422f-9b96-95e9cdb30072)

{% hint style="info" %}
Nota: Você pode pausar e redefinir o tempo sendo registrado para a sessão atual, independentemente se é a pessoa Responsável pelo item de trabalho ou não.
{% endhint %}

Além disso, você pode editar o tempo das sessões registradas atual e anteriormente, independentemente se é a pessoa Responsável pelo item de trabalho ou não. No entanto, tenha em mente que somente líderes de equipe podem editar o tempo registrado por outros integrantes da equipe, enquanto os integrantes podem editar somente o tempo registrado de suas próprias sessões.

## Visualizando sessões anteriores gravadas&#x20;

Ao expandir o card de monitoramento de tempo, é exibido o tempo gravado de sessões anteriores, bem como quem estava trabalhando no item durante a sessão, qual a duração da mesma e se o tempo de duração gravado foi editado.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FTtA5nlN8rhW1wQKfTknY%2Fimage.png?alt=media\&token=58d2b9b8-7927-40c3-8186-db47e2cb483a)

Clicando no ícone de informação você pode ver a data e hora de gravação da sessão e, se o item de trabalho for um Ticket, qual a categoria atribuída a ele durante a sessão.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2Fg12njOAe1m0IQOBzINPV%2Fimage.png?alt=media\&token=d2efb716-f5ad-4871-ba31-d284485a972f)

## Editando o tempo gravado

Você pode editar o tempo da sessão atual e de sessões anteriores, independentemente de ser ou não o responsável pelo item de trabalho. No entanto, note que apenas líderes da equipe podem editar o tempo gravado por outros membros da sua equipe, enquanto membros da equipe só podem editar o tempo gravado em suas próprias sessões.&#x20;

A edição manual do tempo da tarefa irá salvar o tempo editado **como uma nova linh**a no histórico.&#x20;

Você poderá ver mais informações, incluindo quando e quem realizou a edição quando abrir o card no modo tela cheia.&#x20;

{% hint style="info" %}
Note que os valores de tempo gravados para trabalhos feitos por robôs são do tipo apenas leitura.
{% endhint %}

### Visualizando tempo editado&#x20;

Você pode clicar no item de expandir para abrir o card em tela cheia. Aqui você pode ver a duração da sessão atual, combinada com a duração total de todas as sessões anteriores e, para Ações e Tickets, o tempo esperado para conclusão. Você também pode ver informações mais detalhadas sobre a sessão individual, bem como informações sobre as edições feitas:&#x20;

| Usuário                                            | Quem estava trabalhando no item de trabalho                |
| -------------------------------------------------- | ---------------------------------------------------------- |
| <p> </p><p>Tempo</p>                               | A hora de início e fim e a duração total da sessão gravada |
| Data                                               | A data em que a sessão foi gravada                         |
| Tempo Editado Por                                  | Quem editou por último o tempo gravado da sessão           |
| <p> </p><p>Tempo Editado Para</p>                  | Qual a edição feita no tempo gravado da sessão             |
| <p> </p><p>Data da Edição</p>                      | A data em que a sessão gravada foi editada                 |
| <p> </p><p>Categoria do Ticket (Ticket apenas)</p> | A categoria do Ticket quando a sessão gravada foi editada  |

## Tempo esperado

A expectativa de tempo necessário para concluir o item de trabalho pode ser configurada no Criador para Ações e Tickets. Note que essa informação só será exibida se:&#x20;

* Um valor estimado de esforço houver sido adicionado para a Ação/ Categoria de Ticket no Criador.
* As configurações do sistema “Mostrar gerenciador de tempo” e “Mostrar tempo esperado no gerenciador de tempo” estiverem habilitadas.

## Quando o tempo é registrado e quando não?

O tempo será registrado quando um usuário tiver o item de trabalho aberto e aparecendo na tela. O tempo não será registrado quando o card de Registro de Tempo for pausado. Encontre na tabela abaixo informações mais detalhadas sobre se o tempo é registrado ou não em determinado cenário.

| O item de trabalho está aberto na tela e atribuído a mim/não atribuído a mim                                                                                | O tempo é registrado                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A guia do item de trabalho é fechada                                                                                                                        | O registro de tempo é pausado e a sessão atual de registro é encerrada. Quaisquer novas atividades começarão uma nova sessão de registro de tempo.                                                                                         |
| O usuário seleciona outra guia de item de trabalho                                                                                                          | O registro de tempo do item de trabalho original é pausado enquanto não está aberto na tela, já que outra guia de item de trabalho foi aberta mais recentemente.                                                                           |
| O usuário seleciona novamente a guia do item de trabalho original                                                                                           | O registro de tempo começa novamente como parte da mesma sessão. O registro de tempo do outro item de trabalho (se a guia ainda estiver aberta) é pausado.                                                                                 |
| Redigir um e-mail para um item de trabalho em uma janela avulsa enquanto a guia do item de trabalho ainda está selecionada na janela principal do navegador | O tempo continua sendo registrado                                                                                                                                                                                                          |
| O navegador está minimizado, mas a guia do item de trabalho ainda está selecionada na janela do navegador                                                   | O tempo continua sendo registrado                                                                                                                                                                                                          |
| O computador está bloqueado, mas o Enate ainda está sendo executado e a guia do item de trabalho ainda está aberta na tela                                  | O tempo continua sendo registrado, mas é interrompido se a sessão do Enate expirar                                                                                                                                                         |
| O usuário fecha sua sessão do Enate                                                                                                                         | O registro de tempo é pausado e a sessão atual de registro é encerrada. Uma nova sessão de registro de tempo será iniciada quando o usuário entrar novamente.                                                                              |
| O navegador é fechado de maneira inesperada/o computador desliga de maneira inesperada/a conexão com a Internet é perdida                                   | O sistema do Enate terá um registro do tempo de poll mais recente (dentro dos últimos 3 minutos), e a sessão de registro de tempo atual é encerrada. Uma nova sessão de registro de tempo será iniciada quando o usuário entrar novamente. |

## Informações adicionais acerca do Monitoramento de Tempo

O sistema Enate sempre mantém um registro do tempo gravado automaticamente (ou seja, não editado manualmente). Trata-se do registro do tempo no qual a guia do item de trabalho estava aberta diretamente na tela. Essa informação não é mostrada, mas você pode acessá-la para relatórios. Note que o monitoramento de tempo monitora TODOS os acessos ao item de trabalho, mesmo após sua conclusão. A edição manual do tempo da tarefa irá salvar o tempo editado como uma nova linha no histórico. A caixa ‘tempo na tarefa’ irá mostrar a contagem automática de tempo, desde que você iniciou a edição manual do valor mostrado anteriormente.&#x20;
