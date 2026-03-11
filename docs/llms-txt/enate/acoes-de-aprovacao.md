# Source: https://docs.enate.net/enate-help/portugues/processando-uma-acao/acoes-de-aprovacao.md

# Ações de aprovação

### O que são ações de aprovação? Como funcionam?

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==?utm_source=gitbook&utm_medium=iframely>" %}

Muitas vezes, dentro dos fluxos de processos de um Caso no Enate há pontos em que pessoas externas (ou seja, pessoas trabalhando fora do Enate, como gerentes dentro da sua empresa ou da de um cliente) precisam aprovar atividades antes que o processo possa continuar. Bons exemplos disso são os processos de pagamento, em que a administração de um cliente precisa aprovar os relatórios antes que o processo possa continuar.

As ações de aprovação do Enate foram criadas especificamente para esses cenários de pedido de aprovação, mas de maneira mais integrada. Assim, esse “ciclo de aprovação” pode ser bem administrado e visível pelo fluxo de atividades no Enate.

### Como ações de aprovação funcionam na execução

Pedidos de aprovação são enviados para agentes que estão trabalhando fora do Enate aprovarem ou rejeitarem.

Existem alguns tipos diferentes de aprovação que afetam como a decisão é tomada:

●        Em um cenário multinível, o e-mail de pedido é enviado para cada novo nível a cada aprovação recebida do anterior, até no máximo três níveis. Se uma pessoa rejeitar o pedido, a aprovação é rejeitada.

●        Em um cenário Paralelo Qualquer, o e-mail do pedido é enviado para todos os aprovadores, e vale a decisão da primeira a responder.

●        Em um cenário Paralelo Todos, o e-mail do pedido é enviado para todos os aprovadores e TODOS eles precisam aprová-lo para que o pedido seja aprovado. Se uma delas rejeitar o pedido, a aprovação é rejeitada.

Se o pedido for aprovado por todas as partes necessárias, a Ação de aprovação será resolvida com sucesso e fechada automaticamente, e nenhum agente do Gerenciador de Trabalho precisará fazer isso manualmente, embora a Ação fechada possa ser visualizada quando desejado ao clicar nela manualmente.

### Exceções - administradas por um agente no Gerenciador de Trabalho

No entanto, existem alguns cenários em que um agente do Gerenciador de Trabalho pode precisar executar atividades necessárias para dar continuidade a uma Ação de aprovação:

●        A aprovação foi rejeitada

●        Nenhum aprovador (ou aprovadores insuficientes) foi determinado automaticamente

#### Pedido de aprovação rejeitado

No cenário em que um pedido de aprovação for rejeitado, a Ação será movida para o estado “A fazer" e por isso precisará ser conduzida por um agente no Gerenciador de Trabalho. Esse agente precisará conferir o motivo da rejeição e decidir como prosseguir. Ele ou ela pode:

1. **Fazer as mudanças necessárias e reenviar o pedido definindo a ação como “Em espera”.** Isso enviará automaticamente o e-mail de pedido de aprovação novamente\*\* e colocará a Ação no estado de “Aguardar por mais informações”, já que estará esperando por uma informação externa (uma resposta de aprovação) ser registrada no sistema antes que a atividade possa prosseguir.
2. **Marcar a Ação como “Não é possível concluir”.** Isso alertará a pessoa proprietária do Caso, que precisará decidir como prosseguir: talvez retrabalhar o Caso ou fechá-lo.
3. **Marcar a Ação como Resolvida,** o que manualmente marcará o pedido como aprovado. O Caso então prosseguirá para a próxima Ação.

{% hint style="info" %}
\*\*Observação: ao enviar outro e-mail de pedido de aprovação, a sequência de aprovação voltará ao começo novamente. Ou seja, todos os aprovadores receberão outro e-mail. Se a pessoa clicar em um dos e-mails enviados anteriormente, verá uma mensagem dizendo que aquele pedido de aprovação específico não é mais válido, pois os detalhes do pedido podem ter mudado.
{% endhint %}

#### Aprovadores insuficientes

No cenário em que um agente precisa adicionar aprovadores, porque um ou mais aprovadores necessários estão em branco (ou precisar fazer mudanças, o que exigirá que o pedido seja enviado novamente), o agente assumirá a ação de aprovação no estado “A fazer”. Depois de fazer os ajustes necessários e/ou preencher os nomes de aprovadores faltantes, o agente precisará colocar a Ação no estado de “Em espera”. Feito isso, o e-mail de pedido de aprovação será enviado automaticamente, e a Ação será colocada no estado “Aguardar por mais informações”, pois estará esperando por informações externas (aprovações) antes de poder prosseguir.

{% hint style="info" %}
Observação: enquanto uma ação de aprovação estiver em “A fazer” ou “Em andamento”, as partes externas que receberem pedidos de aprovação por e-mail NÃO poderão aprovar ou rejeitar o pedido. Em vez disso, a pessoa verá uma mensagem informando que o item em questão está sendo processado no momento. Os agentes do Gerenciador de Trabalho PRECISAM mudar a Ação de volta para o estado “Aguardar por mais informações” se desejarem que a atividade de aprovação recomece.
{% endhint %}

#### Se o pedido de aprovação expirar...

Outro possível cenário é que a Ação de aprovação pode ser fechada automaticamente porque expirou por não ter recebido resposta (ou respostas suficientes) a tempo. Nesse caso, a Ação será definida automaticamente como Resolvida e o Caso continuará. Nenhum agente do Gerenciador de Trabalho precisará assumir uma Ação nesse cenário, embora a Ação fechada possa ser visualizada a qualquer momento clicando nela manualmente.
