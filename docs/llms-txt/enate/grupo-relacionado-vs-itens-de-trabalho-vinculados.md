# Source: https://docs.enate.net/enate-help/portugues/trabalhando-com-itens-de-trabalho-vinculados/grupo-relacionado-vs-itens-de-trabalho-vinculados.md

# Grupo Relacionado vs Itens de Trabalho Vinculados

## Grupo de Itens de Trabalho Relacionados

Os itens de trabalho relacionados são um grupo fortemente conectado de itens que, embora se comportem de acordo com sua própria configuração específica, têm um impacto ativo em seu item de trabalho 'pai' - especificamente, o item de trabalho pai não será concluído até que todos os seus 'filhos' tenham concluído.

As comunicações serão compartilhadas automaticamente entre itens de trabalho no grupo relacionado para que estejam sempre visíveis e, quando você responder a um e-mail em um item de trabalho, a resposta poderá ser vista em todos os outros itens de trabalho

Além disso, arquivos, links, defeitos, cards inteligentes e contatos também são compartilhados automaticamente entre todos os itens de trabalho no grupo, portanto, atualizar, por exemplo, um arquivo em um item de trabalho atualizará o arquivo em todos os outros itens de trabalho no grupo relacionado também.

Um Grupo de Itens de Trabalho Relacionados inclui:

* Um Case e suas Ações
* Um Case e seu(s) Sub Case(s).
* O Ticket restante e outros Tickets 'resolvidos' se vários Tickets tiverem sido mesclados
* Um Case ‘filho’ e seu Ticket pai se um Ticket houver sido convertido em Case

{% hint style="info" %}
Observe que para Tickets divididos os arquivos, links, defeitos, cards inteligentes e contatos do pai são para seus Tickets filhos, de forma que atualizar, por exemplo, um arquivo em um item de trabalho não atualizará o arquivo em todos os outros itens do grupo relacionado. No entanto, o Ticket pai, que será movido para um estado de espera, não será concluído até que todos os Tickets 'filhos' sejam concluídos. Observe também que, se o ticket pai receber um e-mail, ele será copiado para os tickets filhos em vez de compartilhado.
{% endhint %}

## Itens de Trabalho Vinculados

Quando os itens de trabalho não têm um impacto ativo um no outro (ou seja, eles não fazem parte de um grupo de itens de trabalho relacionados), mas ainda há uma conexão leve entre eles e você deseja pular rapidamente de um para o outro, você deve usar o recurso Item de Trabalho Vinculado no Enate.

Os itens de trabalho com um relacionamento 'Vinculado' se comportam de acordo com sua própria configuração específica e não precisam esperar que o outro seja concluído antes que eles possam ser concluídos. Você pode vincular facilmente dois ou mais itens de trabalho a qualquer momento e é uma maneira muito útil e flexível de conectar itens livremente para que as pessoas de diferentes departamentos, por exemplo, manterem-se facilmente atualizadas sobre o andamento de outros trabalhos relacionados ao Ticket/Case em que estão trabalhando.

As comunicações também não serão compartilhadas automaticamente entre itens de trabalho vinculados, mas você pode optar por copiar as comunicações de um item de trabalho para um item de trabalho ao qual está vinculado.

Observe que você também tem a opção de compartilhar e-mails entre itens de trabalho vinculados - [veja aqui mais informações sobre como compartilhar e-mails entre itens de trabalho vinculados](https://docs.enate.net/enate-help/portugues/trabalhando-com-itens-de-trabalho-vinculados/compartilhando-emails-entre-itens-de-trabalho-vinculados).

Além disso, os arquivos, links, defeitos, dados personalizados e contatos não serão compartilhados automaticamente ao iniciar um novo item de trabalho vinculado, mas você pode optar por copiá-los. Quaisquer atualizações feitas neles não serão refletidas nos outros itens de trabalho vinculados.

Os itens de trabalho com um relacionamento vinculado serão exibidos na guia 'Trabalho vinculado' em Cases e Tickets.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FYgLWYbAAI6rUAbV30Eau%2F13%20Clicking-on-links-tab.gif?alt=media&#x26;token=9312136e-c44e-4628-b97c-b2efa284e45b" alt=""><figcaption></figcaption></figure>

Usar este tipo de conexão é útil se, por exemplo, a data limite de um Case não depende da conclusão de algum outro trabalho (por exemplo, por um departamento diferente), mas ainda é considerado útil para as pessoas que trabalham em um deles permanecerem cientes da atividade do outro e, mais importante, ter um rápido ponto de acesso ao outro.

Itens de Trabalho podem ser vinculados das seguintes maneiras:

* Um Case ou Ticket iniciado diretamente a partir de um Case ou Ticket existente.
* Adicionando manualmente uma ligação entre um Case/Ticket e outro Ticket ou Case existente. &#x20;
