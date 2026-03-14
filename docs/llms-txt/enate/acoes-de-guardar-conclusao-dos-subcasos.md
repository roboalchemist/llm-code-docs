# Source: https://docs.enate.net/enate-help/portugues/processando-uma-acao/acoes-de-guardar-conclusao-dos-subcasos.md

# Ações 'Aguardar conclusão de Sub Cases’

Uma Ação ‘Aguadar conclusão de Sub Cases’ irá esperar a conclusão de um Sub Case específico para então permitir que o Case mova-se para a próxima Ação.

Você pode identificar uma Ação ‘Aguardar conclusão de Sub Cases’ através do seu card de informações, onde estará escrito ‘Ações esperando conclusão de Sub Case’.

Quando uma Ação ‘Aguardar conclusão de Sub Cases’ é iniciada E o Sub Case relacionado fora iniciado (manualmente ou através da Ação ‘Iniciar Case’), a Ação ‘Aguardar conclusão de Sub Cases’ terá o status de ‘Em espera’.

Uma vez concluído o Sub Case, a Ação ‘Aguardar conclusão de Sub Cases’ será fechada automaticamente.

Você será notificado quanto à isso na linha do tempo.

Se o Sub Case para o qual a Ação ‘Aguardar conclusão de Sub Cases’ está aguardando não estiver disponível – por não ter sido iniciado ou por ter sido concluído anteriormente ao início da Ação – a Ação ‘Aguardar conclusão de Sub Cases’ terá o status de ‘A fazer’ e será atribuída a uma Fila onde um usuário pode recolher a Ação e decidir como proceder.

Se você tentar colocar a Ação ‘Aguardar conclusão de Sub Cases’ no estado de ‘Em espera’, a Ação irá fechar já que o Sub Case em questão não fora iniciado.

Se uma Ação não está no estado ‘Aguardar conclusão de Sub Cases’ e o Sub Case o qual estava esperando for concluído, a mensagem ‘Sub Case concluído’ irá aparecer no card de informações.

Se você conclui manualmente uma Ação ‘Aguardar conclusão de Sub Case’, ela será marcada como concluída mesmo sem a resolução do Sub Case.

{% hint style="info" %}
Note que, se o seu sistema foi configurado para fechar automaticamente uma Ação ‘Aguardar conclusão de Sub Cases’ (veja aqui mais informações sobre como fazer isso) e o Sub Case em questão não estiver disponível – por não ter sido iniciado ou por ter sido concluído anteriormente – a Ação ‘Aguardar conclusão de Sub Cases’ irá automaticamente para o status de Fechada. Você será notificado disso na linha do tempo.
{% endhint %}
