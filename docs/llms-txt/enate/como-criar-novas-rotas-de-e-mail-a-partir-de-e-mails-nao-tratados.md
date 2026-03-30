# Source: https://docs.enate.net/enate-help/portugues/e-mails/e-mails-nao-tratados/como-criar-novas-rotas-de-e-mail-a-partir-de-e-mails-nao-tratados.md

# Como criar novas rotas de e-mail a partir de e-mails não tratados

Como parte de lidar com e-mails não tratados, os usuários agentes podem criar roteamentos de e-mail diretamente pelo Gerenciador de Trabalho. Criar essas regras ajuda a impedir que e-mails equivalentes futuros cheguem como e-mails não tratados, permitindo que um Ticket ou Caso seja criado para eles. Isso reduz os volumes de e-mails não tratados e permite que o trabalho comece mais rápido nesses itens. Para promover mais controle, a possibilidade de usuários criarem novas rotas de e-mail no Gerenciador de Trabalho é uma opção que pode ser desabilitada em “Funções de usuários”, no Criador.

Quando essas regras forem criadas no Gerenciador de Trabalho, elas ficarão ativas instantaneamente, mas usuários administradores no Criador serão notificados quando novas regras de roteamento forem criadas dessa maneira, e elas permanecerão marcadas para atenção até a pessoa administradora indicar que as viu. Administradores ainda podem ajustar ou até desabilitar essas regras depois de avaliá-las.

## Como conceder acesso a usuários do Gerenciador de Trabalho a criar novas rotas de e-mail

O acesso a recurso para poder criar novas rotas de e-mail no Gerenciador de Trabalho é controlado por meio do sistema de Funções de Usuário do Enate, com uma nova opção adicionada à seção “Opções de visualização de e-mails”.

{% hint style="info" %}
Observação: Esse acesso a “Criar rotas de e-mail” mudará para **ATIVADO** para a função de membro padrão da equipe
{% endhint %}

!\[A screenshot of a computer

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FRPSxpjYcFyUovNE31o6F%2F0.jpeg?alt=media>)

## Como criar uma nova rota de e-mail em e-mails não tratados

Ao lidar com um e-mail não tratado na seção de “E-mails não tratados” da Caixa de Entrada de E-mails, se você quiser que o e-mail seja processado em um Ticket/Caso (clicando na opção “Novo item de trabalho”), o seguinte pop-up aparecerá:

!\[A screenshot of a ticket form

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FncvYQZi4ISwdthGhO2gu%2F1.png?alt=media>)

Você pode procurar pela rota de e-mail (que preencherá automaticamente os campos Cliente/Contrato/Serviço/Processo com base nas sugestões do endereço de caixa de entrada selecionado) ou selecionar manualmente. Clicar em Criar nesse momento criará o Ticket ou Caso específico a partir do e-mail normalmente.

No entanto, se você *também* quiser que a mesma coisa aconteça automaticamente de maneira contínua, clique no link “Aplicar a outros e-mails” no rodapé do pop-up antes de clicar em Criar. Se tiver selecionado essa opção, ao clicar em Criar, duas coisas acontecerão:

* Uma pequena mensagem aparecerá confirmando que\
  um novo item de trabalho foi criado.
* Outra tela de pop-up para “Criar nova regra de roteamento de e-mail” aparecerá, onde você pode preencher os outros detalhes da regra de roteamento antes de confirmar a criação.

!\[A screenshot of a computer

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FNKvWNwszrhv5DZ5Tbb20%2F2.png?alt=media>)

Você pode decidir se a rota será do tipo “De” ou “Para”; ou seja,

* “tratar todos os e-mails partindo deste endereço da mesma forma” OU
* “tratar todos os e-mails indo para *esse* endereço da mesma forma”,

e então decidir que endereço de e-mail deve ser usado com isso. O Enate preencherá automaticamente o endereço de e-mail com o endereço relevante associado ao e-mail não processado em que você estava trabalhando.

{% hint style="info" %}
Na seção “Dicas” desse pop-up, há um link que leva o usuário à página de “E-mails não tratados” da ajuda online do Enate, para caso a pessoa precise de mais informações.
{% endhint %}

## Como aplicar a regra a e-mails existentes (execução retroativa)

Além de definir uma regra que lidará com todos os e-mails futuros que correspondam ao padrão definido, você pode também fazer a regra ser executada para todos ou alguns dos e-mails não tratados já existentes que correspondam à regra. Se desejar que isso aconteça, selecione para ativar “Aplicar automaticamente” no rodapé do pop-up.

!\[A white background with black text

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FHU2clxcxSCc0aifzuf9h%2F3.png?alt=media>)

O sistema mostrará quantos e-mails não tratados anteriores correspondem com essa regra; ou seja, quantos serão reprocessados.

**Escolha um intervalo de datas/horas para selecionar quais e-mails não tratados existentes reprocessar.**

Selecionar essa opção abrirá um filtro de data/hora que permite selecionar um subconjunto desses e-mails existentes para executar a regra sobre eles (se, por exemplo, você quiser executar isso somente para e-mails de até uma semana ou um mês atrás, etc.

!\[A screenshot of a email

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FznWzXYkQYqbut8NnQr3r%2F4.png?alt=media>)

Você pode usar a barra deslizante para definir intervalos de datas ou até datas específicas. Ao mudar essa configuração, o sistema refletirá isso atualizando quantos e-mails serão afetados ao executar essa regra.

Quando estiver satisfeito(a) com sua seleção, clique em Criar, e a regra será reexecutada, e os e-mails começarão a ser reprocessados ao tipo de Caso ou Ticket que você especificou.

{% hint style="info" %}
Observação importante: Ao criar uma nova regra de roteamento de e-mail dessa maneira pelo Gerenciador de Trabalho, ela ficará ativa instantaneamente e começará a ser executada para e-mails recebidos subsequentes.
{% endhint %}

## Visibilidade de novas regras de roteamento de e-mail para administradores no Criador

Se novas rotas de e-mail tiverem sido criadas em e-mails não tratados no Gerenciador de Trabalho, usuários administradores verão isso no Criador em um ponto vermelho na seção do ícone de e-mail.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FsKgvGCyz0w8kfXMnKzhp%2F5.png?alt=media)

Ao longo das seções e telas de navegação subsequentes até a página de rotas de e-mail, haverá avisos constantes abaixo das novas regras de roteamento que eles deverão notar.

!\[A screenshot of a computer

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FFHD3aKsnpt4uc5khdvjW%2F6.png?alt=media>)

Ao chegar na página de rotas, os usuários verão um banner notificando sobre as novas rotas de e-mail, bem como quantas existem. Um link permitirá a eles filtrar as rotas a apenas as novas que eles precisam notar.

!\[A close-up of a blue sign

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2F35swK1bSLclU5fifRN4I%2F7.png?alt=media>)

Na própria tabela de rotas, os usuários serão alertados sobre essas novas rotas.

!\[A screenshot of a email

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FYbRxsgwKTOBAz6q2Te9Q%2F8.png?alt=media>)

Os usuários administrativos são incentivados a conferir essas novas regras de roteamento (e falar com os agentes que as criaram\*) para ter certeza de que eles estão satisfeitos com como elas estão funcionando juntamente com as várias outras regras. Eles podem optar por desativar as regras, fazer ajustes ou até excluí-las, se acharem necessário.

Se estiverem satisfeitos com a regra, eles podem desmarcar a notificação de “ajuste”. Eles podem usar o link “Apagar filtro de revisão” no cabeçalho para voltar à visualização normal.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2Fa3SzsHuY6PZodJP1T9mh%2F9.png?alt=media)

\*Você pode visualizar quem criou uma regra de roteamento de e-mail no ícone “Mostrar atividades” no topo do pop-up de detalhes da regra.

!\[A screenshot of a device

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FzhvSGcgpp1mCVMwCIp40%2F10.png?alt=media>)

Clicar nisso mostrará a trilha de auditoria de quem criou e atualizou a regra.

!\[A screenshot of a computer

Description automatically generated]\(<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FQZvXvA20TxjVJyvD10wg%2F11.png?alt=media>)
