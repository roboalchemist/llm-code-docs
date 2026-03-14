# Source: https://docs.enate.net/enate-help/portugues/contatos/tags-de-contatos.md

# Tags de contatos

Tags de contato são usadas para vincular contatos a itens de trabalho.

## Tags Padrão do Sistema

As tags de Contatos padrão do sistema disponíveis são:

* **Contato principal** – a principal pessoa com quem você está lidando em relação a essa consulta. Só pode haver um contato principal para um item de trabalho. Isso é obrigatório para um Ticket. Dependendo da configuração de um Caso no Criador, isso pode ou não ser obrigatório para um Caso (se estiver definido como obrigatório para o tipo de Caso, também será obrigatório para as Ações do Caso).
* **Solicitante original** – a pessoa que inicialmente levantou a solicitação. Só pode haver um solicitante original para um item de trabalho, e isso é independente da tag Solicitante. O solicitante original ou será automaticamente definido no caso em que um contato válido envia o e-mail que iniciou o item de trabalho, ou a primeira pessoa que for definida manualmente como Solicitante será promovida a “Solicitante original”. A tag “Solicitante original” não pode ser alterada depois de definida, e você não pode remover do item de trabalho o contato marcado como solicitante original.
* **Solicitante** – a pessoa solicitante da consulta. Só pode haver um solicitante para um item de trabalho. Isso é obrigatório para um Ticket. Dependendo da configuração de um Caso no Criador, isso pode ou não ser obrigatório para um Caso (se estiver definido como obrigatório para o tipo de Caso, também será obrigatório para as Ações do Caso).
* **Referido** – a quem se refere o item de trabalho (pode ser diferente dos anteriores). Só pode haver um referido para um item de trabalho.

Muitas vezes, esses três serão a mesma pessoa. Se você marcar outro contato como um desses tipos de relacionamento padrão do sistema, a tag será removida do contato anterior, já que só pode haver um de cada contato padrão do sistema em cada item de trabalho.

Ao adicionar manualmente o primeiro contato a um item de trabalho, ele será definido como “Contato principal”, “Solicitante” e “Referido” por padrão. Você pode reatribuir essas tags para outros usuários manualmente depois.

* CCs - quaisquer outros contatos que possam estar como receptores de cópia uma correspondência. Quando um contato é marcado somente como “com cópia”, ele aparecerá na seção separada CCs (que fica oculta se não houver nenhum contato apenas CC no item de trabalho).

## Como configurar tags padrão adicionais em um registro de contato

Além das tags de contato padrão do sistema (contato principal, referido, CC e solicitante), você pode adicionar mais tags de contato padrão a um registro de contato, tornando o uso das tags de contato nos itens de trabalho mais rápido e fácil.

Exemplo: Se você souber que a “Patrícia da Silva” sempre será a Intermediadora de todos os itens de trabalho em que ela será adicionada como contato, você pode dar ao registro de contato de Patrícia uma tag padrão “Intermediadora”, para que isso seja preenchido automaticamente no item de trabalho, em vez de ter de definir o valor da tag manualmente novamente a cada vez.

A lista de tags padrão disponíveis para escolher é definida no Criador na seção [Configurações gerais >> Tags de contato](https://d.docs.live.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags).

Você pode definir essa tag padrão sempre que adicionar um novo contato ao sistema.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FPzYpdMsKddVKdxMjzdHN%2Fimage.png?alt=media&#x26;token=b84c58ae-2d9a-481c-ab59-c9f40779db56" alt=""><figcaption></figcaption></figure>

Você também pode adicionar a tag aos contatos existentes e editar a tag padrão definida para um contato na página Contatos.

O atributo Tag Padrão também está disponível para editar em massa; ou seja, você pode defini-lo para vários contatos de uma vez só. Basta selecionar os registros de contato na tabela da página Contatos e clicar no botão Editar para acessar a janela pop-up “Edição em massa”.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FCVTJi2NkiNRTmgkqBExG%2Fimage.png?alt=media&#x26;token=4367565b-48fb-47f3-9d0b-f43941879483" alt=""><figcaption></figcaption></figure>

### **Comportamento da tag de contato padrão se definida para não “Permitir vários”**

Se um valor de tag específico não tiver sido definido para “Permitir vários”, somente um contato poderá ter o valor em um item de trabalho. Por exemplo: pode ser que haja somente um contato “Intermediador” em um Ticket. Isso obviamente afeta o uso de tags padrão se dois contatos com a mesma tag padrão “Deve ser único” forem adicionados a um item de trabalho, seja manual ou automaticamente. Nesse cenário, o sistema atribui a tag padrão a somente um contato (e por isso remove a tag padrão dos outros contatos). O sistema atribuirá ao contato já marcado com *outro* valor de tag já existente, na seguinte ordem de prioridade.

* Contato principal
* Solicitante
* Assunto
* CC
* Qualquer outro contato do item de trabalho

### **Notas adicionais sobre discrepâncias de empresa fornecedora com tags de contato**:

* Você não poderá adicionar uma tag padrão a um contato se a empresa à qual ele ou ela estiver atribuído(a) tiver outra empresa fornecedora para a tag padrão.
* Você não poderá enviar um item de trabalho com um contato cuja tag padrão está definida para uma empresa fornecedora diferente da do item de trabalho.

## Uso de tags automáticas de contatos em itens de trabalho

### Contatos preenchidos de um e-mail inicial

**Contatos conhecidos**

Se um e-mail chegar de um endereço associado a um contato já existente no sistema e o contato:

* tiver uma configuração de escopo Global; ou
* tiver uma configuração de escopo Local, mas pertencer à mesma empresa à qual o item de trabalho pertencerá, com base nas regras de roteamento de e-mail

então os detalhes do contato serão preenchidos automaticamente no card Contatos quando o item de trabalho for criado pelo sistema, e ele será marcado automaticamente com as tags “Contato principal”, “Solicitante original” e “Solicitante” do item de trabalho. Além disso, se houver uma tag padrão atribuída a esse contato, ele ou ela também receberá essa tag. No entanto, tenha em mente que você pode editar manualmente as tags depois que o item de trabalho tiver sido criado.

Quando um e-mail chega de um endereço associado a um contato que já consta no sistema, mas ele ou ela tem a configuração de escopo Local e pertence a uma empresa *diferente* da qual o item de trabalho pertencerá, com base nas regras de roteamento de e-mail, os dados do contato NÃO serão preenchidos automaticamente no card Contatos quando o item de trabalho for criado pelo sistema (portanto, não pode ser marcado automaticamente com tags no item de trabalho). Lembre-se que você pode editar manualmente o contato e as tags depois que o item de trabalho tiver sido criado.

#### **Contatos desconhecidos**

*Escopo padrão “Global” ou “Global e Local”*

Ao receber um e-mail de um endereço desconhecidos e:

* a [configuração “Habilitar criação automática de contato” está ativada no Criador](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) e
* seu sistema foi configurado para definir o escopo dos seus contatos externos para "**Global**” ou "**Global e Local**”,

então o contato será criado automaticamente, com escopo Global (ou seja, não será vinculado a nenhuma empresa específica) e seus detalhes serão preenchidos automaticamente no card de contatos quando o item de trabalho for criado pelo sistema. Além disso, a pessoa será automaticamente marcada como contato principal, solicitante original e solicitante do item de trabalho. Como ela já era conhecida antes pelo sistema, não terá uma tag padrão definida. Tenha em mente que você pode editar manualmente as tags depois que o item de trabalho tiver sido criado.

*Escopo “Local” por padrão*

Ao receber um e-mail de um endereço desconhecidos e

* a [configuração “Habilitar criação automática de contato” está ativada no Criador](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) e
* seu sistema foi configurado para definir o escopo dos seus contatos externos para "**Local**”,

então o contato será criado automaticamente, com escopo Local (ou seja, será vinculado a uma empresa específica) e sob a mesma empresa sob a qual o item de trabalho existe. Os detalhes do contato serão preenchidos automaticamente no card Contatos quando o item de trabalho for criado pelo sistema, e ele será marcado automaticamente com as tags “Contato principal”, “Solicitante original” e “Solicitante” do item de trabalho. Como ela já era conhecida antes pelo sistema, não terá uma tag padrão definida. Tenha em mente que você pode editar manualmente as tags depois que o item de trabalho tiver sido criado.

*Criação automática de contato desativada*

Ao receber um e-mail de um endereço desconhecidos e

* a [configuração “Habilitar criação automática de contato” está desativada no Criador](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation),

então o item de trabalho será criado com base nas regras de roteamento de e-mail, mas os detalhes de e-mail do remetente NÃO serão preenchidos automaticamente no card de Contatos quando o item de trabalho for criado pelo sistema (portanto não podendo ser marcado automaticamente ao item de trabalho). Lembre-se que você pode editar manualmente os contatos e as tags depois que o item de trabalho tiver sido criado.

#### Tags de contato preenchidas na página de atividade do contato

Quando um item de trabalho é criado pelo botão “Iniciar item de trabalho” na [página de atividade do contato](https://docs.enate.net/enate-help/portugues/contatos/a-pagina-de-atividade-do-contato), esse contato será marcado automaticamente com as tags “Solicitante original”, “Solicitante”, “Referido” e “Contato principal” do item de trabalho, e a tag padrão do contato também será adicionada (se houver).
