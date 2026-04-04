# Source: https://expressjs.com/pt-br/

Title: Express - Node.js framework para aplicações web

URL Source: https://expressjs.com/pt-br/

Markdown Content:
Express - Node.js framework para aplicações web
===============

[](https://expressjs.com/ "Go to homepage")

*   [Primeiros passos](https://expressjs.com/pt-br/starter/installing.html)
    *   [Instalação](https://expressjs.com/pt-br/starter/installing.html)
    *   [Olá mundo](https://expressjs.com/pt-br/starter/hello-world.html)
    *   [Gerador do Express](https://expressjs.com/pt-br/starter/generator.html)
    *   [Roteamento Básico](https://expressjs.com/pt-br/starter/basic-routing.html)
    *   [Arquivos Estáticos](https://expressjs.com/pt-br/starter/static-files.html)
    *   [Mais exemplos](https://expressjs.com/pt-br/starter/examples.html)
    *   [Perguntas mais frequentes](https://expressjs.com/pt-br/starter/faq.html)

*   [Guia](https://expressjs.com/pt-br/guide/routing.html)
    *   [Roteamento](https://expressjs.com/pt-br/guide/routing.html)
    *   [Escrevendo o middleware](https://expressjs.com/pt-br/guide/writing-middleware.html)
    *   [Usando o middleware](https://expressjs.com/pt-br/guide/using-middleware.html)
    *   [Sobrescrevendo a API Express](https://expressjs.com/pt-br/guide/overriding-express-api.html)
    *   [Usando template engines](https://expressjs.com/pt-br/guide/using-template-engines.html)
    *   [Manipulação de erros](https://expressjs.com/pt-br/guide/error-handling.html)
    *   [Depuração](https://expressjs.com/pt-br/guide/debugging.html)
    *   [Express por trás dos proxies](https://expressjs.com/pt-br/guide/behind-proxies.html)
    *   [Migrando para o Express 4](https://expressjs.com/pt-br/guide/migrating-4.html)
    *   [Migrando para o Express 5](https://expressjs.com/pt-br/guide/migrating-5.html)
    *   [Integração com base de dados](https://expressjs.com/pt-br/guide/database-integration.html)

*   [Referência da API](https://expressjs.com/pt-br/5x/api.html)
    *   [5.x](https://expressjs.com/pt-br/5x/api.html)
    *   [4.x](https://expressjs.com/pt-br/4x/api.html)
    *   [3.x (descontinuada)](https://expressjs.com/pt-br/3x/api.html)
    *   [2.x (descontinuada)](https://expressjs.com/2x/)

*   [Tópicos Avançados](https://expressjs.com/pt-br/advanced/developing-template-engines.html)
    *   [Criando template engines](https://expressjs.com/pt-br/advanced/developing-template-engines.html)
    *   [Atualizações de segurança](https://expressjs.com/pt-br/advanced/security-updates.html)
    *   [Melhores práticas de segurança](https://expressjs.com/pt-br/advanced/best-practice-security.html)
    *   [Melhores práticas de desempenho](https://expressjs.com/pt-br/advanced/best-practice-performance.html)
    *   [Verificações de saúde e desligamento](https://expressjs.com/pt-br/advanced/healthcheck-graceful-shutdown.html)

*   [Recursos](https://expressjs.com/pt-br/resources/community.html)
    *   [Comunidade](https://expressjs.com/pt-br/resources/community.html)
    *   [Glossário](https://expressjs.com/pt-br/resources/glossary.html)
    *   [Middleware](https://expressjs.com/pt-br/resources/middleware.html)
    *   [Módulos utilitários](https://expressjs.com/pt-br/resources/utils.html)
    *   [Contribuindo para o Express](https://expressjs.com/pt-br/resources/contributing.html)
    *   [Registros de alterações](https://github.com/expressjs/express/releases)

*   [Suporte](https://expressjs.com/pt-br/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Ultimos post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Todos posts](https://expressjs.com/en/blog/posts.html)
    *   [Escreva um Post](https://expressjs.com/en/blog/write-post.html)

*   [English](https://expressjs.com/en/)
*   [Français](https://expressjs.com/fr/)
*   [Deutsch](https://expressjs.com/de/)
*   [Español](https://expressjs.com/es/)
*   [Italiano](https://expressjs.com/it/)
*   [日本語](https://expressjs.com/ja/)
*   [中文 (简体)](https://expressjs.com/zh-cn/)
*   [繁體中文](https://expressjs.com/zh-tw/)
*   [한국어](https://expressjs.com/ko/)
*   [**Português**](https://expressjs.com/pt-br/)

Este documento pode estar desatualizado em relação à documentação em inglês. Para as últimas atualizações, por favor consulte o [documentação em inglês](https://expressjs.com/en/).

✖

Express[5.2.1](https://github.com/expressjs/express/releases)

Uma estrutura web rápida, flexível e minimalista para aplicativos Node.js
=========================================================================

`$ npm install express --save`

```
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```

*   Express@5.1.0: Agora o Padrão no npm com LTS Timeline

Expresse 5.1.0 agora é o padrão do npm, e estamos introduzindo um cronograma oficial de LTS para as linhas de lançamento v4 e v5. [Confira nosso último blog para obter mais informações.](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Aplicações Web
--------------

 Express é um framework para aplicativos web Node.js, mínimo e flexível que fornece um conjunto robusto de recursos para aplicativos web e móveis. 

APIs
----

Com uma infinidade de métodos utilitários HTTP e middleware à sua disposição, criar uma API robusta é rápido e fácil.

Desempenho
----------

 Express fornece uma fina camada de recursos fundamentais de aplicativos web, sem obscurecer recursos de Node.js que você conhece e ama. 

Middleware
----------

 Express é uma framework de roteamento leve e flexível com recursos centrais mínimos destinados a ser aumentada através do uso de módulos Express [middleware](https://expressjs.com/pt-br/pt-br/resources/middleware.html) . 

[](https://expressjs.com/pt-br/#)

[](https://openjsf.org/ "OpenJS Foundation")
Copyright [OpenJS Foundation](https://openjsf.org/) e Express contributors. Todos os direitos reservados. A [OpenJS Foundation](https://openjsf.org/) possui marcas registradas e utiliza marcas registradas. Para obter uma lista de marcas registradas da [Fundação OpenJS](https://openjsf.org/), por favor veja nossa [Politica de Marca](https://trademark-policy.openjsf.org/) e [Lista de Marcas](https://trademark-list.openjsf.org/). Marcas e logotipos não indicados na lista [de marcas registradas da OpenJS Foundation](https://trademark-list.openjsf.org/) são marcas registradas ou registradas de seus respectivos titulares. O uso deles não implica em nenhuma afiliação ou endosso por eles.

[Termos de Uso](https://terms-of-use.openjsf.org/)[Política de Privacidade](https://privacy-policy.openjsf.org/)[Código de Conduta](https://github.com/expressjs/.github/blob/HEAD/CODE_OF_CONDUCT.md)[Política de Marcas](https://trademark-policy.openjsf.org/)[Política de Segurança](https://github.com/expressjs/express/security/policy)

[](https://github.com/expressjs/express)

[](https://www.youtube.com/channel/UCYjxjAeH6TRik9Iwy5nXw7g)

[](https://x.com/UseExpressJS)

[](https://openjs-foundation.slack.com/archives/C02QB1731FH)

[](https://opencollective.com/express)

[](https://bsky.app/profile/expressjs.bsky.social)

[![Image 1: Preview Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
