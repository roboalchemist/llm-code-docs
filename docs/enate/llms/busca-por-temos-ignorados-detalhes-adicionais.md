# Source: https://docs.enate.net/enate-help/portugues/anexo/busca-por-temos-ignorados-detalhes-adicionais.md

# Busca por temos ignorados – detalhes adicionais

Como parte dos recursos padrão do Enate, criados para otimizar as pesquisas realizadas pelos usuários, certos termos comumente utilizados são removidos da busca se forem inseridos manualmente. Isso ocorre para garantir uma resposta em tempo hábil, além de impeder que a pesquisa retorne um número muito grande de resultados que acabaria por esconder os retornos desejados pelo usuário. Uma das abordagens utilizadas para isso é o uso de “Listas de Parada”.

## Lista de Parada

Uma lista de parada consiste emu ma lista de palabras comuns padrão,t ais como “e”, “o”, “a”, “eu”, etc., que são ignoradas no processo de busca, visto que retornariam resultados demais.

Abaixo encontra-se uma lista de TODAS as palavras que o Enate irá ignorar – isso não inclui apenas buscas na Busca Rápida, mas também pesquisas realizadas por usuários, por e-mails, Itens de Trabalho, etc. Se você inserir quaisquer dos itens de lista, eles serão ignorados automaticamente na busca por resultados.

{% file src="<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FJNcwVfAkd3mAheAVcmJS%2FEnate%20SQL%20Stop%20List.xlsx?alt=media&token=a0b28715-3b23-4acb-9e1a-90028194aa5a>" %}

Múltiplas Listas de Parada são suportadas por vários idiomas de usuário.

{% hint style="info" %}
Nota: Quando ocorre a busca por Usuários e Emails, a lista em Inglês (Britânico) é sempre utilizada. Para itens de trabalho (Título, Nome do Cliente, Nome do Contrato, Nome do Serviço, Nome do Ticket/Case, etc.) é utilizado o idioma do usuário conectado para buscar a lista de parada. Adicionalmente, perceba que Húngaro não é suportado pela linguagem SQL, de forma que a lista utilizada para usuários húngaros é a em Inglês.
{% endhint %}

## Caracteres ignorados na Busca Rápida

Caracteres específicos são configurados para serem ignorados na Busca Rápida, como “\*”, “?”, “@”, etc. Isso quer dizer, por exemplo, que na busca por cliente.com, as palavras ‘cliente’ e ‘com’ serão pesquisadas. Recomendamos que a combinação de palavras seja colocada entre parênteses para buscar por uma frase específica – provavelmente buscar por “cliente.com” irá retornar os resultados que você deseja.

Abaixo encontra-se uma lista de todos os caracteres  ignorados em pesquisas na Busca Rápida:

{% file src="<https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FMOcQ4WlijRFul9M7VHFT%2FCharacters%20ignored%20in%20Quickfind.pdf?alt=media&token=1db4c324-f93a-4cb2-8315-8ea482e46d1a>" %}
