# Source: https://docs.enate.net/enate-help/portugues/processando-uma-acao/acao-de-extracao-de-documento.md

# Ação de extração de documento

### Visão geral

O componente de extração de documentos extrai automaticamente os dados relevantes de arquivos anexados a e-mails recebidos, para que esses dados possam ser usados para processar o item de trabalho, o que poupa o tempo e o esforço de seus agentes. Isso também significa que documentos como PDFs podem ser escaneados e usados tanto para iniciar Casos no Enate quanto para formar parte das atividades do processo em andamento.

Quando uma ação de extração de documento é executada para um Caso, os documentos anexados ao caso podem ser enviados para a tecnologia desejada para escaneamento, e os arquivos de saída processados serão retornados e automaticamente anexados ao Caso.

Se a qualquer momento a tecnologia que estiver usando não estiver confiante o bastante sobre o resultado, com base em um limite de confiança, você pode configurar o Enate para instantaneamente transferir o trabalho para um agente para confirmação no Gerenciador de Trabalho, fornecendo a confiabilidade da automação supervisionada por humanos.

Esse componente pode ser ativado pela pessoa que administra a conta na seção do [Marketplace](about:blank) do Criador do Enate.

Assista a este vídeo para saber mais:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

### Como funciona na execução

Quando o Caso é executado no Gerenciador de Trabalho, os dados relevantes de arquivos anexados a e-mails recebidos referentes a ele são automaticamente analisados e extraídos.

Se a tecnologia que estiver usando estiver confiante o suficiente sobre os resultados da extração de dados, essa Ação não precisará ser nem mesmo vista por um usuário humano e será concluída automaticamente, e o Caso continuará com a próxima Ação. A Ação de extração de dados concluída ainda poderá ser visualizada ao clicar nela, mas não precisará ser encaminhada para um usuário humano se envolver.

{% embed url="<https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5x5hGES3lDv4IeonVeVS%2Fimage.png?alt=media&token=d780fad0-e13d-4f09-aab1-92d50045b3b3>" %}

No entanto, se a tecnologia de extração estiver menos confiante sobre o resultado, a Ação será encaminhada para um usuário humano conferir quando ele ou ela selecionar “Obter da fila” na página inicial. Quando um agente abrir a Ação, você verá que ela foi encaminhada para essa pessoa porque precisava ser conferida.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FV6qhrFOKvOSG1ErhVNce%2Fimage.png?alt=media&#x26;token=e432e74f-6bef-496c-a2ca-e025df16c846" alt=""><figcaption></figcaption></figure>

Para fazer isso, basta clicar em “Verificar agora” e rolar a tela até “estação de validação” na Ação, que mostrará a imagem do documento escaneado e a tabela de dados extraídos resultante. Isso permite ver em destaque onde esses níveis de confiança mais baixos estão, conferir essas informações e fazer correções manualmente. Isso pode ser visualizado na mesma página ou expandido em uma tela própria.

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FOcRGIJYedf68RgqEb2Wk%2Fimage.png?alt=media&#x26;token=9f82a3ea-3ae3-46fa-8be1-efa00600c8d4" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nota: Só é possível visualizar um documento de cada vez.
{% endhint %}

<figure><img src="https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FPNTXdjpTmimMBVsIbawU%2Fimage.png?alt=media&#x26;token=5b185e4b-836b-4dd3-a48e-fe6c898b9aa4" alt=""><figcaption></figcaption></figure>

Nesta tela de validação, o agente poderá ver uma cópia digitalizada do arquivo, que pode ter várias páginas, juntamente com duas guias que mostram os dados extraídos.

* A guia Dados extraídos mostra os pares de valores-chave do agente dos dados extraídos, juntamente com o nível de confiança que o EnateAI atribuiu a eles. Os valores podem ser ajustados quando necessário e são salvos assim que o agente clica no botão de atualização para esse valor. Isso definirá o valor de confiança como 100% para essa chave.
* A guia Tabelas mostra todos os dados repetidos que foram selecionados como uma tabela. Você pode usar o botão Excluir para excluir as linhas que não forem necessárias.

Se o agente precisar sair da tela da Estação de Validação a qualquer momento, basta clicar em “Salvar como rascunho” para salvar as alterações feitas em um documento específico.

{% hint style="info" %}
Nota: Se um agente entrar na tela de validação de uma Ação que não esteja atribuída a ele, os dados estarão no modo somente leitura e não poderão ser editados. Para poder editar os dados, o agente deve primeiro atribuir a Ação a si mesmo.
{% endhint %}

Quando um agente estiver satisfeito com os dados, tudo o que ele precisa fazer para enviar os dados atualizados é clicar no botão “Enviar”. O EnateAI concluirá o processamento em segundo plano e atualizará a tela Ação para confirmar quando terminar. O processamento em segundo plano permite que o agente passe para qualquer outro documento que precise de verificação.

Depois que “Enviar” for clicado para o último documento que precisa de validação, a tela Ação será fechada automaticamente. Novamente, o EnateAI está finalizando o processamento em segundo plano e marcará a Ação como Resolvida após um curto período, passando então para Fechada.

*Nota: Sempre que você revisar e atualizar itens de dados, o EnateAI aprenderá e ficará um pouco melhor nas sugestões de extração de dados. Se você perceber que a tecnologia está regularmente apresentando sugestões erradas, fale com sua equipe administrativa sobre a modificação do limite de confiança.*
