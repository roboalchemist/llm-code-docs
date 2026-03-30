# Source: https://docs.enate.net/enate-help/portugues/processando-uma-acao/acionar-acoes-de-api-externas.md

# Ações ‘Acionar API externa’

De forma similar a outros arquetipos de ação, ações ‘Acionar API externa’ podem ser usadas em processos de Case, e são utilizadas quando você precisa se conectar com outro sistema, passando dados a ele e, potencialmente, fazendo com que ele passe dados personalizados atualizados ao Enate.

Para informações de como configurar Ações ‘Acionar API externa’ dê uma olhada nessa seção do [Criador](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab).

Algumas vezes pode ocorrer um atraso quando da espera pela resposta do sistema externo. Quando isso acontece, por exemplo quando a Ação ‘Acionar API Externa’ está aguardando por informações para responder, o card de informações da Ação aparecerá no Gerenciador de Trabalho no estado de ‘Em espera’.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdGu9FLmGCXz8We0NFU%2F-MdGutY8NUSfD_8pOAIn%2Fimage.png?alt=media\&token=5283c5d7-d415-4d8a-8eec-1269c48a5a35)

Quando o sistema externo responde ao Enate com atualização de dados, aparecerá um marcador informando se a ação foi bem sucedida ou não:

#### **Resposta bem sucedida**

Se o sistema responde informando que foi bem sucedido, a ação irá automaticamente para o estado de ‘Fechada’, com o método de resolução ‘Feito com sucesso’.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2F4o1p7QXzqbinedsgRfAD%2Fimage.png?alt=media\&token=b8e10b80-a98d-407b-86b4-0c9d55e20646)

#### **Resposta mal sucedida**

Se o sistema responde informando que não foi bem sucedido, a Ação irá para o estado de ‘A fazer’, com o motivo ‘Atualizado por Integração’. A API externa pode inclusive responder com mais informações sobre o porque não foi bem sucedida. Essa informação aparecerá no card de Informações na seção ‘Motivo da Rejeição’.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2Fzuk8wuyEo0LV7kH0CVET%2Fimage.png?alt=media\&token=18ecfbbb-d686-4c58-8c9b-1e9091f2798e)

Se a Ação não foi bem sucedida porque não completou dentro do tempo definido ([configurado no Criador](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab)), então irá para o estado de ‘A fazer’ com o motivo ‘Tempo esgotado’ e será movida para uma Fila/usuário humano baseado nas regras de alocação configuradas.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FXJBbbiC7mU0t4tG2xA0F%2Fimage.png?alt=media\&token=e7532b72-991c-4013-b6c4-c77be08b9356)

Tais Ações mal sucedidas se comportarão como ações manuais padrão.

{% hint style="info" %}
Note que o proprietário do Case NÃO será notificado destas situações.
{% endhint %}

### **Tentativas Automáticas**

Se a ação não conseguir se conectar ao sistema externo, ela tentará se conectar novamente, de forma automática, por um determinado número de vezes, dependendo da configuração do seu sistema no Criador ([veja mais informações aqui](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)). Você também receberá uma mensagem de erro na Ação informando:

* Quando o erro ocorreu
* Quando o sistema irá tentar estabelecer uma conexão novamente
* Quantas vezes o sistema tentou estabelecer automaticamente uma conexão
* Quantas vezes o sistema irá tentar estabelecer uma conexão.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdGu9FLmGCXz8We0NFU%2F-MdGuwurPHITjyO79XZf%2Fimage.png?alt=media\&token=c935fef7-e004-42f0-967b-b1e6a5d646df)

Você pode tentar estabelecer uma conexão manualmente por aqui também, clicando em ‘Tentar novamente’ na mensagem de erro.

{% hint style="info" %}
Note que quando você faz uma tentativa manual, ela será contada como tentativa e, portanto, será incluída no número que mostra quantas vezes o sistema tentou estabelecer a conexão automaticamente.
{% endhint %}

Se a ação não consegue estabelecer uma conexão após as tentativas automáticas (por exemplo, se você configurou o sistema para tentar novamente de forma automática 5 vezes e após as 5 tentativas ainda não foi possível), ela será movida para o estado de ‘Fechada’ com a resolução ‘Não foi bem sucedida’.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdGu9FLmGCXz8We0NFU%2F-MdGuvESlMx2-Ig31Lvg%2Fimage.png?alt=media\&token=26e5bf52-03b5-40a0-8b02-2556a4513188)

{% hint style="info" %}
Nessa circunstância de falha no estabelecimento de conexão com o sistema externo, será informado ao proprietário do Case, em destaque na seção da Ação da tela do Case, que a Ação foi fechada – não foi bem sucedida.
{% endhint %}

Quando a Ação recebe a informação requerida, ela fechará automaticamente.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2F7DBFjkSK1t7Qi5cKWh3W%2Fimage.png?alt=media\&token=98fcfc04-91e1-4ae3-b4d3-bf864a8194ab)

#### **Ajustando as configurações de tentativa no Criador durante/após tentativas iniciadas**

Se a configuração de tentativa automática no Criador for modificada *após* a tentativa automática do sistema em estabelecer uma conexão com um sistema externo, ocorrerá o seguinte:

Se, por exemplo, a configuração de tentativas for definida para 5 e o sistema tentou estabelecer uma conexão por 5 vezes e falhou, a Ação será movida para o estado de ‘Fechada’ com uma mensagem de erro mostrando a contagem de tentativas 5/5.

Se a configuração de tentativas for alterada para um número maior do que 5, digamos 7, a mensagem de erro mostrará a contagem de tentativas 5/7, mas o sistema NÃO tentará estabelecer uma conexão novamente de forma automática pela 6ª ou 7ª vez já que a ação já se encontra fechada.

No entanto, se a ação ainda não foi movida para o estado de ‘Fechada’ porque não alcançou o número máximo de tentativas (por exemplo, se ocorreram 4 tentativas de estabelecer conexão, de um máximo de 5), o aumento no número de tentativas para 7 significa que ação irá tentar estabelecer uma conexão de forma automática até a 7ª tentativa.

De forma similar, se você reduzir a configuração de tentativas após seu início, por exemplo se você está na 4ª tentativa de 10 e então reduz o máximo para 4, o sistema irá mostrar 4/10 mas será fechado.
