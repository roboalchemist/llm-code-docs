# Source: https://docs.enate.net/enate-help/portugues/processando-um-case/subcasos.md

# Subcasos

## Criando um Sub Case

Um sub case irá comportar-se de acordo com suas configurações específicas, mas seu Case “pai” não será concluído até que os seus sub cases tenham sido concluídos.

Dessa maneira, você só pode criar um Sub Case a partir de um Case existente.

Para criar um novo Sub Case, clique em ‘ + Item de Trabalho”, localizado próximo à seção de guias do Case, e então escolha ‘Sub Case’.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FjlSjpRfToCMvMkr1dtxA%2Fimage.png?alt=media\&token=3f08e16f-196d-4a04-bf3d-a4f35f5a8c95)

Na janela resultante, você pode filtrar para buscar por tipos de processo de Sub Case que deseja criar de duas maneiras:

* buscando pela rota do e-mail – você pode especificar o endereço da caixa de e-mail para a qual as pessoas normalmente enviariam e-mails para criar itens de trabalho. Normalmente uma caixa de e-mail representa uma certa parte do negócio na qual você deseja criar itens de trabalho. Como atalho, criamos uma funcionalidade que permite que você busque pela caixa de E-mail e filtrar para os processos de Sub Case que deseja escolher. Ao selecionar uma Caixa de e-mail, o sistema irá filtrar os resultados para apenas os processos relacionados àquela caixa. &#x20;
* selecionando um Cliente, Contrato, Serviço e um processo de Sub Case para iniciar (aparecerão por padrão se houver apenas uma opção a escolher). Note que o Cliente do Sub Case será preenchido automaticamente de acordo com o Case pai, que é aquele a partir do qual você está criando o Sub Case.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FDHOKyLQhUxFOMWbjFH7J%2Fimage.png?alt=media\&token=0a3e38d7-651a-49cf-99eb-12047fd8c4be)

{% hint style="info" %}
Note que os Sub Cases disponíveis para serem iniciados dependem das permissões definidas no Criador. Adicionalmente, você apenas poderá selecionar um processo de Sub Case a partir de uma rota de e-mail que tenha sido habilitada no Criador ([veja aqui mais informações](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes-detail)). Ainda, você só poderá selecionar um processo de Sub Case no [Modo Teste](https://docs.enate.net/enate-help/portugues/modo-de-teste) se a rota de e-mail para o mesmo houver sido configurada para funcionar no [Modo Teste](https://docs.enate.net/enate-help/portugues/modo-de-teste).
{% endhint %}

Você pode então ajustar as seguintes configurações para o Sub Case:

| Substituir Data-limite | Se o seu sistema foi configurado desta forma ([veja aqui mais informações](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours)), você pode substituir a data-limite do Sub Case que está criando.                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Descrição              | Você pode modificar a descrição do novo Sub Case que está criando                                                                                                                                                                                                                   |
| Cronograma             | Se o seu sistema estiver configurado desta maneira ([veja aqui mais informações](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules)), você deve selecionar um cronograma para o novo Sub Case que está criando. |
| Adicionando contatos   | Você pode adicionar múltiplos contatos diferentes ao novo Sub Case que dividir tags entre eles como quiser.                                                                                                                                                                         |

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FwP7saG4qfRtEiv6dduEX%2Fimage.png?alt=media\&token=052800c1-2c61-4a6f-b6b8-dca99a3560e4)

{% hint style="info" %}
Tenha em mente que Defeitos, Arquivos, Links e Dados Personalizados serão compartilhados automaticamente do Caso Pai para seu novo Subcaso. Comunicações do Caso Pai e seus itens de trabalho relacionados, portanto Ações e Subcasos (se houver) também serão compartilhados com o novo Subcaso. No entanto, tenha em mente que os e-mails não serão compartilhados, mas você pode facilmente vê-los selecionando [“Incluir itens de trabalho relacionados” na linha do tempo](https://docs.enate.net/enate-help/portugues/itens-de-trabalho/secao-principal). Tenha em mente também que atualizar Defeitos, Arquivos, Links, Dados Personalizados ou Comunicações no novo Subcaso também aplicará essas alterações no Caso Pai.
{% endhint %}

Um link para o novo Sub Case aparecerá na [guia de Sub Cases](#guia-sub-cases) e NÃO na [guia Vinculados](#visualizando-itens-de-trabalho-vinculados-a-aba-vinculados).&#x20;

## **Guia Sub Cases**

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8o18I3JZ3nO3hyj0a%2FSub-Cases-Tab.gif?alt=media\&token=bd36ffad-fe23-4381-b5ff-2f74c03a9518)

A guia Sub Cases mostrará as seguintes informações para quaisquer Sub Cases de um Case:

* Ícone do estado atual
* Número de referência do Sub Case e título do Case
* Contagem de Ações – Número de Ações associadas com o dono do Sub Case/ Case (*se definido)*
* Fila – a fila de Cases (*se definida)*
* Data-limite – data-limite do Case
* Ícone para expandir o Sub Case e mostrar suas Ações

## Lógica do número de referência do Sub Case

O número de referência dos Sub Cases pode ser dividido da seguinte maneira:

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FcCssRFsingtDKH13UOxp%2Fimage.png?alt=media\&token=1fb0f7a0-aa80-41bd-9d00-b45555d0876a)
