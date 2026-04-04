# Source: https://docs.enate.net/enate-help/portugues/processando-uma-acao/enviar-email-e-enviar-email-e-aguardar-acoes.md

# Ações “Enviar e-mail” e “Enviar e-mail e esperar”

### Visão geral

Em uma ação “Enviar e-mail”, o Enate envia automaticamente um e-mail e a ação é imediatamente fechada. O usuário do Gerenciador de Trabalho não precisa fazer nada com esse tipo de ação.

Em uma ação “Enviar e-mail e esperar”, o Enate envia automaticamente um e-mail. Em seguida, a ação é movida para o estado Esperando, até que uma resposta seja recebida. Quando uma resposta tiver sido recebida, a Ação mudará para o estado A Fazer para ser processada.

Os endereços de destinatário, CC e CCO do e-mail são configurados no Criador. Consulte este artigo sobre como configurar ações “Enviar e-mail” no Criador:

{% embed url="<https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab>" %}

Quando o e-mail tiver sido enviado, uma entrada aparecerá na linha do tempo mostrando quando, de quem para quem foi enviado, endereços CC ou CCO, se houver, e o assunto do e-mail e, se você clicar para expandir, o corpo do e-mail.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FsALQaanG3PwdQHe03ivD%2Fimage.png?alt=media&#x26;token=773a6447-5fc5-46fb-8c87-07173771ff7c" alt=""><figcaption></figcaption></figure>

## Exceções

Se for usado um endereço de e-mail de destinatário, CC ou CCO inválido, o e-mail da ação “Enviar e-mail”/”Enviar e-mail e esperar” não será enviada automaticamente e a Ação será movida de volta para a Fila correspondente.

Um aviso aparecerá na linha do tempo:

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FXSt7OEkWu2d453R1jvBa%2Fimage.png?alt=media&#x26;token=98e96900-d53f-44d5-8f9c-ffb0a7a63945" alt=""><figcaption></figcaption></figure>

O proprietário do Caso pode então decidir se deseja enviar manualmente o e-mail e precisará corrigir o endereço de e-mail e adicionar o conteúdo do corpo manualmente. A pessoa proprietária também deve contatar uma pessoa administradora do sistema para alertá-la sobre o problema para que possa corrigir o endereço de e-mail para evitar que outro envio falhe futuramente.
