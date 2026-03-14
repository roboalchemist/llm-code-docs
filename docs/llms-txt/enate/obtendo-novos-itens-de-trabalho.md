# Source: https://docs.enate.net/enate-help/portugues/obtendo-novos-itens-de-trabalho.md

# Obtendo novos itens de trabalho

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc3MQ==>" %}

Clicar no botão ‘Tirar da Fila’ no cabeçalho da tabela da Caixa de Entrada lhe atribuirá uma nova peça de trabalho.

![](https://828797872-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWqMXrK_ZvY1cj8JBqs%2F-MWqRv4hiUBVt6rGJXr3%2Fimage.png?alt=media\&token=0ae54aa3-e15a-4bc0-afd5-26dc5ed9119f)

### Regras de Alocação em Fila de Espera

**Como o sistema determina qual item de trabalho dar a um usuário quando ele clica no botão "Puxar da Fila" na sua caixa de entrada?**

O sistema funciona analisando todos os itens de trabalho não atribuídos de todas as filas a que o usuário está ligado e tem permissões e atribui um novo item de trabalho, priorizando os itens da seguinte forma:

1. Qualquer item de trabalho atualmente ATRASADO (o item mais atrasado primeiro). Se nenhum foi encontrado, então
2. Qualquer item de trabalho que tenha sido rejeitado por um robô. Se nenhum foi encontrado, então
3. Qualquer item de trabalho (item a ser selecionado em breve primeiro).

Nota: As filas definidas para "modo estrito" estão lá para alocar o trabalho estritamente aos robôs. Qualquer usuário humano ligado a tais filas está lá apenas como um retrocesso para itens de trabalho robotizados rejeitados, e não são auto-alocados os itens de trabalho normais e não-rejeitados deles quando se clica em "Puxar da Fila".
