# Source: https://docs.enate.net/enate-help/portugues/busca-rapida/como-a-busca-rapida-funciona-especificidades.md

# Como funciona a busca rápida: detalhes

Uma explicação adicional acerca de como a busca rápida funciona: existem três tipos diferentes de busca ocorrendo em pararelo quando você utiliza a busca rápida:

**1) Busca específica por** **número de referência**. Isso baseia-se no reconhecimento de um formato conhecido do número de referência de itens de trabalho no sistema, e retorna resultados relacionados  a Tickets, Cases, Ações que possuam tal número. Você pode simplesmente digitar a referência, como ‘40308-T’ e o sistema irá reconhecê-la como tal. Você não precisa inserir um código.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FGKRop7fxeJxiq4cOpGMv%2Fimage.png?alt=media\&token=4ba97d0c-9f4b-4d1c-97e1-ccb28bc0152c)

**2) Busca por campos de dados personalizados**. Como descrito acima. O sistema saberá quando realizar esse tipo de busca quando você adicionar um código conhecido, como ‘FN:’. Será realizada a pesquisa por um campo que contenha o valor específico que você inseriu. Veja mais notas sobre o assunto abaixo, em Caracteres Coringa.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FKYmDx2bD3cdA6INO1Ur0%2Fimage.png?alt=media\&token=aba3c821-ba42-44c2-a4da-c01b7ad25adc)

**3) Busca por texto livre para itens de trabalho, comunicações e pessoas** em relação a qualquer coisa que você digitar que não se encaixe nos dois tipos de dados reconhecidos. O sistema de busca por texto livre pesquisa por palavras individuais em vários atributos de itens de trabalho, comunicações e pessoas do sistema, por exemplo: título do item de trabalho, sujeito e corpo do e-mail.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-419833493%2Fuploads%2FXrwdcd5rrtuBwXCqh5Tg%2Fimage.png?alt=media\&token=af854fcd-78a2-42c0-98c9-e6fc03f7c6df)

**4) 'Iniciar com’ – buscando por arquivos** – o sistema usa a lógica ‘começa com’ para buscar por arquivos e adiciona caracteres coringa ao FIM dos textos buscados. Isso significa que quando você busca por um arquivo chamado ‘Processamento da Fatura.docx’, buscar por ‘Fatura’ não irá encontrar o arquivo – buscar por ‘Processamento’ sim.

## Caracteres Coringa para busca livre

Enquanto pesquisa, o sistema irá adicionar um caractere coringa ao FIM do texto de busca, mas não no começo.

Para pesquisas por dados personalizados especificamente, um exemplo do comportamento seria: ao buscar por “p:John Smi”, a pesquisa retornaria o valor “John Smith” no campo ‘pessoa’, enquanto a busca por somente “p:Smith” NÃO retornaria isso.

Resumindo: na busca de dados personalizados, estamos buscando pelo valor específico de um campo, ou o começo do valor. Buscas por texto livre não são *exatamente* assim, já que tal pesquisa irá  tentar encontrar uma correspondência em cada palavra que é inserida na busca, em detrimento de um valor      como um todo.

Caracteres coringa são adicionados ao fim de pesquisas por número de referência também.

### **Utilizando caracteres coringa enquanto digita** <a href="#utilizando-caracteres-coringa-enquanto-digita" id="utilizando-caracteres-coringa-enquanto-digita"></a>

Enquando você digita na Busca Rápida, o sistema irá utilizar caracteres coringa em cada última palavra. Por exemplo, se você está digitando um texto livre: "John retorna prio". O Sistema irá usar de caracteres coringa para completar a última palavra, e retornará resultados com, por exemplo, a palavra ‘prio*ridade*’.

Uma vez que você pressiona a telca de espaço o sistema conclui que você terminou de digitar a palavra e não utiliza desse artifício.

## Outros termos de pesquisa ignorados <a href="#b-outros-termos-de-pesquisa-ignorados" id="b-outros-termos-de-pesquisa-ignorados"></a>

Para manter o desempenho do sistema, os seguintes termos são ignorados das buscas::

* Palavras com 1 a 2 caracteres.
* Palavras na “lista de impedimento” do sistema. São palavras comuns padrão, como “e”, “o”, “eu”, etc., que poderiam retornar resultados em excesso. Consulte aqui a [lista de impedimento completa de palavras que são ignoradas nas buscas](https://docs.enate.net/enate-help/portugues/anexo/busca-por-temos-ignorados-detalhes-adicionais#lista-de-parada) (na busca rápida e em quaisquer outras buscas do sistema).
* Caracteres específicos definidos para serem ignorados, por exemplo: “\*”, “?”, “@”, etc., especificamente na busca rápida. Consulte aqui a [lista completa de caracteres ignorados](https://docs.enate.net/enate-help/portugues/anexo/erros-potenciais-de-validacao-para-a-criacao-de-itens-de-trabalho-em-massa). Isso significa, por exemplo, que, ao buscar por um cliente.com na busca rápida, as palavras “cliente” e “com” seriam buscadas. Sendo assim, recomenda-se colocar essas combinações de palavras entre aspas para buscá-las como uma frase específica. Sendo assim, buscar por “cliente.com” provavelmente retornará os resultados que você procura.

## **Outras coisas a notar na Busca Rápida**

A busca rápida é uma busca voltada para texto. Inserir datas no lugar de texto irá retornar resultados inconsistentes. Use “aspas” onde possível se isso auxiliar na busca por uma sequência de palavras.&#x20;

Use as barras de data para buscar por resultados em períodos específicos.

Quando buscar por múltiplas palavras, a busca utilizará a lógica do ‘E’ ao invés de ‘OU’, por exemplo, retornando itens com as palavras Maçã E Banana E Pêra.

## **Especificidades de buscas por Itens de Trabalho vs Emails**

É importante notar que a Busca Rápida realiza três buscas independentes:

* uma para itens de trabalho (Cases, Ações e Tickets)
* uma para Emails que podem estar relacionados aos itens
* e uma por pessoas.

Um efeito disso é, por exemplo, se você está buscando por combinações de três palavras, como maçã, banana e pêra, a Busca Rápida irá retornar resutlados de quaisquer itens de trabalho onde essas palavras ocorre, e separadamente emails nos quais as três palavras ocorrem. Situações em que duas das três palavras aparecem nos itens de trabalho, e a terceira palavra está apenas associada a um email, não seriam retornadas em nenhuma busca.

Os atributos específicos pelos quais a busca por itens de trabalho é feita são os seguintes:

* Referência do item de trabalho
* Título
* Nome do cliente
* Nome do fornecedor
* Nome do contrato
* Nome do serviço
* Nome da linha de serviço
* Nome do tipo de processo

Os atributos específicos pelos quais a busca por comunicações é feita são os seguintes:

* Título do email
* Corpo do email
* Endereços do email (de, para, Cc, Cco)
* Nota interna (para notas adicionadas no Enate/autoatendimento)
