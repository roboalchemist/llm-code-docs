# Source: https://docs.enate.net/enate-help/portugues/contatos/adicionar-editar-e-excluir-contatos.md

# Adicionar, editar e excluir contatos

## Adicionando Contatos&#x20;

Contatos Externos podem ser criados de diversas formas no Enate.

### 1) Automaticamente a partir de um e-mail recebido&#x20;

O sistema Enate pode ser configurado de forma a criar automaticamente o registro de contatos externos quando da chegada de e-mails que contenham novos endereços de e-mail se a definição[ ‘Ativar Criação Automática de Contatos” estiver ATIVADA no Criador](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation).&#x20;

O sistema irá preencher automaticamente o primeiro e último nome do contato baseado no e-mail. Mais especificamente:&#x20;

* Se há um espaço no nome do e-mail, qualquer coisa antes do primeiro espaço será usada como primeiro nome do contato e qualquer coisa após o espaço será seu ultimo nome. Por exemplo, se o e-mail mostra o nome ‘John Smith’, o primeiro nome do contato será preenchido automaticamente para ‘John’ e o último nome será ‘Smith’.
* Se há uma vírgula, qualquer coisa antes da vírgula será o último nome do contato e qualquer coisa depois da vírgula será o primeiro nome do usuário. Por exemplo, se o e-mail mostra o nome ‘Smith, John’, a último nome do contato será preenchido automaticamente como ‘Smith’, e o primeiro ‘John’.
* Se não é possível o preenchimento com confiança, pelo sistema, do primeiro e último nome, o contato será criado automaticamente sem um primeiro e último nome, e o usuário deverá preencher quando do envio do item de trabalho.&#x20;

A[ companhia definida](#nome-da-empresa-escopo-de-contato-externo) para o contato criado automaticamente dependerá das [configurações de escopo do contato no Criador](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#contact-scope). Se o escopo está configurado como ‘Global’, ou ‘Global e Local’, o contato criado automaticamente terá um escopo Global, ou seja, não relacionado a qualquer empresa específica. Se, por outro lado, o escopo for ‘Local’, o contato criado automaticamente será criado dentro da empresa que criou o item de trabalho existente.&#x20;

### 2) Adicionando um contato individual a partir da página de Gerenciamento de Contatos&#x20;

Você pode adicionar contatos a partir da [página de gerenciamento de contatos](https://docs.enate.net/enate-help/portugues/contatos/pagina-de-gerenciamento-de-contatos) clicando no ícone de Criar Contato e preenchendo os detalhes do contato na janela resultante.&#x20;

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FWtCEmb4lW2FGRQ95l1FO%2F7A%20Adding-Contact-from-Contact-Mana.gif?alt=media&#x26;token=37e0923e-7bdd-4b87-b182-a4a51821386a" alt=""><figcaption></figcaption></figure>

### 3) Importando contatos para a página de Gerenciamento de Contatos a partir de um arquivo do Excel&#x20;

Você pode importar uma lista de contatos a partir de uma planilha do Excel para a [página de gerenciamento de contatos](https://docs.enate.net/enate-help/portugues/contatos/pagina-de-gerenciamento-de-contatos). O modelo fornecido é suportado em todos os idiomas suportados pelo Enate.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FOADFAiPsfbp5EUZGSIIR%2F7A%20Bulk-Adding-Contacts.gif?alt=media&#x26;token=6824426e-7f50-4a3a-80ec-21b170f09266" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
É obrigatório preencher o endereço de e-mail quando da importação de contatos a partir do Excel. Se você não especificar a empresa, o contato será definido como global automaticamente. Veja aqui mais informação sobre [escopo de empresas](#impacto-do-escopo-global-local-na-correspondencia-entre-contato-e-item-de-trabalho).
{% endhint %}

### 4) Adicionando um contato a partir da Busca Rápida&#x20;

Se você estiver buscando por um novo contato que ainda não está inserido no sistema, você pode criar um novo contato a partir da própria [Busca Rápida](https://docs.enate.net/enate-help/portugues/busca-rapida). Navegue até a função de busca por pessoa na Busca Rápida e clique em ‘adicionar um contato’.&#x20;

Quando você clicar em ‘adicionar contato’, o sistema irá decodificar e preencher automaticamente o primeiro nome, último nome e endereço de e-mail. Uma vez preenchidas todas as informações, clique em criar e será redirecionado para a [página de atividade do contato ](https://docs.enate.net/enate-help/portugues/contatos/a-pagina-de-atividade-do-contato)do novo contato.&#x20;

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MbH-BYuK4VLPdtNwqfT%2F-MbHBB9sVuyT_nCkaTfK%2FCreating-a-Contact-from-Quickfin.gif?alt=media\&token=fe49d4ff-b5be-4aee-bbd6-b5aeee0ff1f3)

{% hint style="info" %}
Nota: o endereço de e-mail do contato deve ser único no sistema.
{% endhint %}

### **5)** Adicionando um contato a partir do Card de Contatos de um Item de Trabalho

Você também pode criar um novo contato a partir do [card de contatos](https://docs.enate.net/enate-help/portugues/contatos/card-de-contatos) de um item de trabalho. Quando buscar por um usuário no card de contatos e o mesmo não existir, você pode criar um novo contato clicando na opção ‘Criar Contato’ e preenchendo os detalhes.&#x20;

Se você digitar o endereço de e-mail para o contato, o sistema irá decodificá-lo e preencher automaticamente o primeiro e último nome do contato. Uma vez preenchidas todas as informações, clique em criar e será redirecionado para o item de trabalho.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2Ff4JmjTdBKk6oXjEU2deD%2F7A-Create-Contact-from-Work-Item.gif?alt=media&#x26;token=b5501a21-634b-4c85-83c8-792b585fce9e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note que se você criar um contato no modo teste, o contato apenas estará disponível para testes no sistema.
{% endhint %}

## Criação de contato Automática vs Manual

Você pode visualizar se um contato externo foi criado automaticamente pelo sistema ou manualmente por um usuário observando a coluna ‘Criado automaticamente’ na [página de gerenciamento de contatos](https://docs.enate.net/enate-help/portugues/contatos/pagina-de-gerenciamento-de-contatos). &#x20;

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2F6KCnZdFSN02vRW3FHWkz%2Fimage.png?alt=media\&token=7d879f5a-d65d-4ac6-b077-6bd3de7e666a)

{% hint style="info" %}
Note que quando um contato criado automaticamente é editado, ele não aparecerá mais na coluna ‘Criado Automaticamente’ na [página de gerenciamento de contatos](https://docs.enate.net/enate-help/portugues/contatos/pagina-de-gerenciamento-de-contatos).
{% endhint %}

### Nome da empresa: contato externo como escopo

A depender da configuração no Criador, você terá várias opções quando atribuir uma empresa a um contato externo:

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FeOwoLchmcDSrxFVjl11n%2F7A%20Company-Scope.gif?alt=media&#x26;token=7fe3f700-e955-4933-b766-5781b5265cfc" alt=""><figcaption></figcaption></figure>

* Todas as Empresas/Global
  * Definir como Global significa que contatos externos poderão criar a acessar itens de trabalho para todas as empresas.
  * Isso significa também que usuários do gerenciador de trabalho podem buscar por todos os contatos externos de um item de trabalho.

{% hint style="info" %}
Note que essa configuração está disponível apenas se o Escopo de Contato Externo foi configurado para ‘Global’ ou 'Global e Local' no Criador. Veja [aqui ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#contact-scope)mais informações.
{% endhint %}

* Uma Empresa específica (local)
  * Ao definir o escopo como local, você fará com que o contato externo só possa criar e acessar itens de trabalho apenas da empresa a qual foi associado.
  * Os usuários só poderão adicionar um Contato a um Pacote API se o mesmo estiver na mesma Empresa (ou é uma filial).

{% hint style="info" %}
Tenha em mente que:

1. Só é possível mudar a empresa associada de um contato externo de Todas as empresas/Global para uma determinada empresa (local) se o contato externo não estiver associado a itens de trabalho de várias empresas diferentes. Você pode mudar isso reatribuindo os contatos de um item de trabalho.
2. Para associar contatos externos a Todas as empresas/Global, a coluna Empresa no arquivo de “Criação em massa” deve estar em branco, para que os contatos sejam Globais por padrão.
3. A empresa definida para um contato criado automaticamente dependerá de como você definiu a configuração de escopo dos contatos. Se estiver definida para “Global” ou “Global e Local”, o contato criado automaticamente terá escopo Global; ou seja, não estará associado a nenhuma empresa específica. Se estiver definida para “Local”, o contato criado automaticamente será criado sob a empresa sob a qual o item de trabalho existir.

   .
   {% endhint %}

### **Impacto do escopo Global/Local na correspondência entre Contato e Item de Trabalho**

{% hint style="warning" %}
Note que se um Contato Externo tem escopo local (ou seja, relacionado a uma empresa específica), você não poder adicioná-lo a um item de trabalho de outra empresa. Isso ocorre também para contas de Agente (que devem *sempre* estar relacionadas a uma empresa específica). APENAS contas externas com escopo Global têm a flexibilidade de serem relacionadas como contatos de itens de trabalho de qualquer Cliente.
{% endhint %}

## Editando um Contato

Para editar um contato, vá até a [página de gerenciamento de contatos](https://docs.enate.net/enate-help/portugues/contatos/pagina-de-gerenciamento-de-contatos) e clique duas vezes no contato para abrir a janela pop up de edição.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FaqP6UmRY5uEDzux8rZxG%2F7A%20Editing-a-Contact-in-Contact-Management%20Page.gif?alt=media&#x26;token=dc8c8b42-61e8-438c-af73-40ac6527490e" alt=""><figcaption></figcaption></figure>

Você também pode editar em lote a empresa, fuso horário, localização do escritório, idioma preferido e tag padrão de seus contatos selecionando as caixas de seleção dos contatos - clique no botão Editar e a janela pop-up de Edição em lote aparecerá. Defina os detalhes conforme desejado e clique em Confirmar para salvar as alterações em lote.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FDMipU33jJarjSUrYZpDM%2F7A%20Bulk-Editing-Contacts-in-Conta.gif?alt=media&#x26;token=c08ec3df-34af-4e29-a7fa-8182c3edead1" alt=""><figcaption></figcaption></figure>

## Deletando um Contato

Para deletar um contato, vá até a [página de gerenciamento de contatos](https://docs.enate.net/enate-help/portugues/contatos/pagina-de-gerenciamento-de-contatos) e clique na caixa de seleção do contato e no botão de deletar que aparecerá. Você pode deletar múltiplos contatos de uma vez só.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FCJu7Mc7GWbze68gRBQPU%2F7A%20Deleting-Conacts-from-Contact.gif?alt=media&#x26;token=7dcd35c7-9abf-4631-a69d-104793a4e90a" alt=""><figcaption></figcaption></figure>
