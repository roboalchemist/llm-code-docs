# Source: https://docs.enate.net/enate-help/portugues/processando-uma-acao/acoes-da-abbyy-flexicapture.md

# Ações da ABBYY FlexiCapture

O Enate é capaz de proporcionar integração com o [ABBYY FlexiCapture](https://www.abbyy.com/flexicapture/) - isto é conseguido através do uso de uma ação integrada da ABBYY FlexiCapture (veja [aqui ](https://docs.enate.net/enate-help/integrations/enate-integrations/ocr-integration/abbyy-integration)para obter orientação sobre como criar e configurar este novo tipo de ação).

Quando uma ação da ABBYY Action é executada para um caso, os documentos anexados ao caso podem ser submetidos à ABBYY FlexiCapture para OCR Scanning e os arquivos de saída processados serão devolvidos e automaticamente anexados ao caso.

{% hint style="info" %}
Nota: Somente arquivos com tipos suportados pela ABBYY v12 em diante podem ser enviaods. Clique [aqui](https://help.abbyy.com/en-us/flexicapture/12/standalone_operator/input_formats/) para ver o seguinte link para a lista de formatos suportados pela ABBYY.
{% endhint %}

O sistema mostrará esta mensagem enquanto estiver aguardando que você submeta documentos para o ABBY FlexiCapture para processamento:

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FPh0951cw70OjIzqvsDZR%2Fimage.png?alt=media\&token=5df14ac9-b9ce-4bdc-9734-edabd835abc8)

Você verá a confirmação de quando os documentos foram submetidos com sucesso à ABBYY para processamento:

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2Fu97Q5rhtfRepAgi6sqwg%2Fimage.png?alt=media\&token=5a56c796-fb33-44f0-a85d-c38c545bf533)

Última tentativa é o momento no qual o(s) documento(s) foi enviado para o ABBY FlexiCapture para processamento.

Se os documentos enviados forem de um formato inválido ou se existirem problemas com a formatação do documento em si, o sistema retornará esta mensagem:

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2F5rGsVV7jPPsvnRHrfQij%2Fimage.png?alt=media\&token=41861576-8c12-430f-8517-e84fbeb1037f)

### Tentativas Automáticas

Se ocorrer um problema com o envio do documento, o sistema irá tentar enviar de novo por um determinado número de vezes, dependendo de como o sistema foi configurado no Criador (veja [aqui ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)mais informações).

Se ainda existir um problema com o envio após as tentativas automáticas (por exemplo quando foram definidas 5 tentativas e o sistema não conseguiu estabelecer conexão) a Ação ABBYY irá para o estado de ‘Fechada’.

## Validação

Depois de digitalizar um documento, o ABBYY cria uma pontuação baseada em quão confiante está na qualidade da digitalização. Se a pontuação de confiança estiver acima do limite definido, não é necessária a verificação, e então os dados serão processador e a tarefa concluída. Se a pontuação de confiança estiver abaixo  de um certo limite, é necessária uma verificação humana.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWslty_G4gksJ22CFBo%2Fimage.png?alt=media\&token=8e051fb0-72bd-4144-802f-29c87bc62933)

### Verificação não é necessária

Uma mensagem de status confirmará que a validação humana não é necessária:

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsm0__59qGFBexYyWZ%2Fimage.png?alt=media\&token=a49da588-38c2-4784-b771-a144ada2ec54)

Uma vez concluído o processamento, a Ação ABBYY será fechada. Arquivos exportados serão anexados ao Case e ficarão visíveis no Card de Arquivos.

{% hint style="info" %}
Nota: se Tags de arquivos resultantes foram definidos, então a ABBYY aplicará a tag a todos os arquivos que foram processados, prontos para uso em atividades em seguida.
{% endhint %}

### Verificação humana necessária

O sistema irá alertá-lo se for necessário o uso de verificação humana:

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FIAkVdTHZU8Aq73K2kMcZ%2Fimage.png?alt=media\&token=56f9acf4-07cc-4074-bdb0-eec169076c36)

Além disso, um texto de lembrete será exibido ao lado do status da Ação para reafirmar que a verificação manual deve ser feita na ABBYY antes de continuar.

Clicando no botão "Verificar", você será levado à estação de Verificação da ABBYY onde poderá verificar as digitalizações dos documentos e ajustar as informações conforme for necessário.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FQHAy3EH7ii6hIB7CFeoj%2Fimage.png?alt=media\&token=756fe11a-efb8-4a01-a062-8b094a2d4c76)

{% hint style="info" %}
Nota : Uma conta ABBYY FlexiCapture válida com permissões para realizar verificação no projeto escolhido será necessária para o acesso total.
{% endhint %}

Uma vez conectado, você será apresentado á tela de Verificaçaõ da ABBY FlexiCapture, onde você  poderá rever e ajustar as informações conforme necessário.

A Estação de Verificação é composta por três seções:

1. As páginas individuais do documento a ser digitalizado.
2. Um visão de perto do documento original a ser escaneado.
3. A que foi processado - portanto, a versão digitalizada do documento original.

O texto destacado em amarelo na guia do documento original é informação que a ABBYY não conseguiu ler.  Isto é destacado em vermelho na no arquivo resultante.

Alguns caracteres como o 'i' também podem ser destacados no arquivo resultante se a ABBYY não tiver       certeza sobre a cópia escaneada.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx6MLiLXtXFAmC00W%2Fimage.png?alt=media\&token=adebd784-bdf7-4f4c-b696-4832e40c4ec2)

Uma vez que você tenha finalizado a verificação manual, a tela irá confirmar que isto foi feito, mas chamará atenção para o fato de que de que foi necessária intervenção manual:

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2Fx0VhoVy0v4jTWjl8DgQr%2Fimage.png?alt=media\&token=0dab3630-53c2-4dbd-a0e1-13ebe616008a)

‌Uma vez concluído o processamento, arquivos exportados serão anexados ao Case e ficarão visíveis no [Card de Arquivos](https://docs.enate.net/enate-help/portugues/itens-de-trabalho/card-de-arquivos).

Você pode então marcar a Ação como completa.

{% hint style="info" %}
Nota: se as "tags dos arquivos resultantes” foram definidas, então a ABBYY as aplicará a todos os arquivos processados, prontos para uso nas atividades seguintes.
{% endhint %}
