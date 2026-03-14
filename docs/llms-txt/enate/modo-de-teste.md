# Source: https://docs.enate.net/enate-help/portugues/modo-de-teste.md

# Modo de Teste

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Mudando para o Modo Teste <a href="#a-mudando-para-o-modo-teste" id="a-mudando-para-o-modo-teste"></a>

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Mudando para o Modo Teste <a href="#a-mudando-para-o-modo-teste" id="a-mudando-para-o-modo-teste"></a>

Se sua conta de usuário estiver configurada para permitir o acesso a dados de teste, você poderá alterar o ambiente do Gerenciador de Trabalho para o "Modo teste". Este link está disponível no menu suspenso do usuário à direita da barra de cabeçalho.

## Explicação do modo de teste <a href="#b-explicacao-do-modo-de-teste" id="b-explicacao-do-modo-de-teste"></a>

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2Fjbzp8s2A9yE8RytMQC0w%2Fimage.png?alt=media\&token=e496d7eb-61f0-48ab-8697-923725d8a988)

A partir do momento em que está a executar no modo de teste, você verá apenas os dados de teste; isso permite que você crie e execute itens de trabalho de teste por meio de versões de teste de processos para verificá-los antes de ativar, tudo sem afetar os dados de produção ao vivo.

Como lembrete visual, a barra do cabeçalho fica em vermelho quando você está no modo de teste.

## Definição de diferentes gerentes e membros de filas no modo de teste <a href="#c-definicao-de-diferentes-gerentes-e-membros-de-filas-no-modo-de-teste" id="c-definicao-de-diferentes-gerentes-e-membros-de-filas-no-modo-de-teste"></a>

A funcionalidade do modo de teste permite que você defina um gerente diferente para uma Fila de espera ao executar no modo de teste comparado ao modo ao vivo.

Exemplo: Considere o **Gerente 1,** que tem acesso ao modo ao vivo e é responsável por gerenciar duas filas: **Fila de Financiamento** e fila de **Caso Principal**.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9gm1OMy6tLbgy9Dy%2Fimage.png?alt=media\&token=bf28b64a-3e8e-4c3d-b9a8-66472c51830b)

No modo de teste, as mesmas duas filas podem ser gerenciadas por outro usuário com permissão de líder de equipe e modo de teste – veja o exemplo abaixo em que o **Gerente 2** foi definido para ser o responsável pelas filas no modo de teste.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FgYVUo3EZUNbDogni0hm0%2Fimage.png?alt=media\&token=35dee000-ad77-4422-bbf0-4d93018e9860)

## Alternar Robôs entre os Modos ao vivo e de teste <a href="#d-alternar-robos-entre-os-modos-ao-vivo-e-de-teste" id="d-alternar-robos-entre-os-modos-ao-vivo-e-de-teste"></a>

É possível alternar um robô para que ele possa ser executado no modo de teste ou no modo ao vivo. Especificamente, duas novas atividades foram adicionadas às bibliotecas de atividades para UiPath, Automation Anywhere e BluePrism (e as APIs padrão ajustadas para que possam ser chamadas de maneira geral) como segue

* Definir modo ao vivo
* Definir modo de teste

Essas ações permitem que você alterne um robô entre os estados de teste e ao vivo. Uma vez que um robô tenha sido colocado no modo de teste, as chamadas de atividades posteriores que o robô possa fazer, por exemplo, “Obter mais trabalho” e “Criar Ticket/Caso etc.” ocorrem dentro desse contexto do modo de teste, recebendo e criando apenas itens de trabalho de teste. O robô deve ser alternado de volta para o modo ao vivo uma vez que o processo esteja configurado, de modo que ele possa então criar itens de trabalho ao vivo.

## Contatos de teste - contatos de teste separados no sistema <a href="#e-contatos-de-teste-contatos-de-teste-separados-no-sistema" id="e-contatos-de-teste-contatos-de-teste-separados-no-sistema"></a>

Enate suporta a criação de registros de contato separados no modo de teste, ou seja, quaisquer registros de contato que você criar no modo de teste serão acessíveis apenas para usuários do modo de teste (e contatos criados no modo ao vivo serão acessíveis apenas para usuários do modo ao vivo). Desta forma, é possível garantir que os e-mails dos pacotes de teste não sejam enviados acidentalmente aos usuários da produção, e vice-versa.
