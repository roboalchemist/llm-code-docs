# Source: https://docs.enate.net/enate-help/portugues/processando-um-ticket/dividindo-um-ticket.md

# Dividir um Ticket

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgzNw==>" %}

Se um ticket contém multiplas solicitações/questões separadas que seriam melhor gerenciadas separadamente você pode dividir o ticket. Clique na guia Dividir na aba Atividade para iniciar a separação:

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FS2Agx4ZFJTgCGNFE1dOm%2Fimage.png?alt=media&#x26;token=97786ecf-44a1-4d2a-b5ea-8cb18eed4093" alt=""><figcaption></figcaption></figure>

A tela por padrão se dividirá em dois tickets. Você pode dividir manualmente em mais tickets. Título, Descrição e Contexto (Cliente >> Categoria de Ticket etc,) são copiados do ticket atual, mas podem ser modificados antes de iniciar a divisão. Você pode escolher manter cada ticket da divisão com você.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FOEX7Lf0g3pnvBYTvJmB9%2Fimage.png?alt=media\&token=d49a2050-3695-4759-8306-420d6cb18037)

Confirme a divisão do ticket clicando em Dividir no Card de Informações:

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FBb6jRTH2fERNPvy3ZqRw%2Fimage.png?alt=media\&token=1184c69d-cb08-4850-8bfb-a4fac65e4f44)

Após a divisão, o ticker original será definico como ‘Aguardando – ticket dividido) e não será mais parte da entrega do serviço (está essencialmente fechado).

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FIUhYWDHrbtkZhpdHxO67%2Fimage.png?alt=media\&token=14ee9523-47e2-4221-b825-eeab8d6de8f6)

A partir do momento em que os tickets divididos estiverem resolvidos, o ticket original será definido como completamente concluído. Por convenção, a data de início do ticket original é copiada para cada ticket resultante.

Para fins de SLA, a data de início do Ticket original é copiada para cada Ticket resultante, e o horário quando o Ticket original foi marcado como Resolvido é calculado como o horário quando o último Ticket em que ele foi dividido é resolvido.

Por exemplo, se o Ticket A foi dividido nos Tickets B e C, e o Ticket B for resolvido em 02-02-2023 à 01:10:00 e o Ticket C for resolvido em 03-02-2023 às 02:00:00, o horário marcado para quando o Ticket A foi Resolvido será 03-02-2023 às 02:00:00.

Você pode cancelar a divisão do ticket a qualquer momento, saindo da aba Dividir (o botão de ação principal no ticket muda de “Dividir”, para que você saiba que não o está dividindo).
