# Source: https://docs.enate.net/enate-help/portugues/criando-novo-trabalho.md

# Como criar novos trabalhos

O trabalho pode ser criado pelos usuários do Gerenciador de Trabalho de duas maneiras:

1. **A partir do ‘Criar Novo Item de Trabalho’.** Esta opção encontra-se na barra de ferramentas. O agente seleciona um Case ou Ticket para iniciar em um contexto específico do negócio.
2. **A partir da página de ‘Atividade do Contato’**, também conhecida como Página de tratamento de Chamadas. A partir desta página, o agente de serviço primeiro procuraria e encontraria uma pessoa (geralmente alguém ligando para o centro de serviços) e, em seguida, iniciaria um trabalho diretamente para ela, como um ticket ou um case.

## Como criar um novo item de trabalho pelo menu suspenso “Criar novo item de trabalho” <a href="#a-menu-suspenso-criar-novo-item-de-trabalho" id="a-menu-suspenso-criar-novo-item-de-trabalho"></a>

Você pode criar novos trabalhos clicando no link Criar na barra de cabeçalho (imagem do cubo). Isso abrirá uma seção na tela com um menu suspenso que permite iniciar um novo item de trabalho. A hierarquia mostrada no menu suspenso é Empresa, Contrato, Serviço, Grupo de processo (se estiver configurado) e os Casos que podem ser criados.

Os links de entrada aparecem aqui automaticamente para Tickets e Cases quando você cria um processo de ticket ou case no Criador e o ativa. Clicando no link você cria o novo item de trabalho em uma guia separada.

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEhH-dnBbM95bUBf0z%2F-MYEk7maY3OWhZPPG154%2FCreate-Work-Item.gif?alt=media\&token=1d97d13f-88ec-4b2f-b505-dd88d3156538)

{% hint style="info" %}
Nota: Em Modo de Teste, processos que estão no estado de ‘projeto validado’ serão exibidos aqui.
{% endhint %}

## Menu suspenso ‘Iniciar Nova Atividade’ na Página de Atividade do Contato <a href="#b-menu-suspenso-iniciar-nova-atividade-na-pagina-de-atividade-do-contato" id="b-menu-suspenso-iniciar-nova-atividade-na-pagina-de-atividade-do-contato"></a>

Links de entrada gerados automaticamente irão aparecer [na página de Atividade do Contato](https://docs.enate.net/enate-help/portugues/contatos/a-pagina-de-atividade-do-contato).

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEkWZ6buBtuWBZ8N3r%2F-MYEmC7zXzcavCD1pAwt%2FCreate-work-from-contact-activit.gif?alt=media\&token=c4cd6836-a55a-47fb-b302-d94716f09670)

Se você estiver na página de contato de alguém de uma empresa conhecida (ou seja, com escopo definido no nível do cliente), as informações do Cliente não serão exibidas neste link. Uma busca por texto livre irá permitir que você filtre a lista de links.

Os administradores podem controlar se você deseja ver o link de entrada para um determinado processo de Ticket/Case por meio de configurações no Criador.

A criação de um item de trabalho a partir da página de atividade de contato atribuirá automaticamente o contato como o contato principal do item de trabalho.

## Métodos de inicialização <a href="#metodos-de-inicializacao" id="metodos-de-inicializacao"></a>

Há vários métodos pelos quais um item de trabalho pode ser criado. Estes podem ser vistos nos itens de trabalho e utilizados para diversos fins de exibição - por exemplo, para mostrar em colunas de grade ou uso para busca na tela de Visualizações. Os possíveis métodos de inicialização são:

* Fluxo de trabalho – iniciado por outro item de trabalho como parte de um fluxo, por exemplo, uma ação iniciada por um Caso.
* Manual – iniciado pelo Agente no Gerenciador de Trabalho
* Autoatendimento – iniciado pelo recebimento de uma solicitação de autoatendimento
* Robótica – Iniciada pelo Robô RPA
* E-mail – iniciado por e-mail recebido
* Ticket – iniciado por Ticket
* Upload em massa – carregado por meio de arquivo excel de upload em massa
* Agendamento – iniciado automaticamente na data/hora especificada por um cronograma do sistema.
