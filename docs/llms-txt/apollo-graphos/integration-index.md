# Source: https://www.apollographql.com/docs/apollo-server/integrations/integration-index.md

# Apollo Server Integrations

> Are you looking to build a new integration? Or help maintain an existing integration? See [Building Web Framework Integrations for Apollo Server](https://www.apollographql.com/docs/apollo-server/integrations/building-integrations) for step-by-step guidance!

Apollo Server's [`startStandaloneServer`](https://www.apollographql.com/docs/apollo-server/api/standalone) function spins up a basic web server with sensible defaults.  The server is a fully functional GraphQL server supporting all of Apollo Server's GraphQL-level customizations, but it offers minimal opportunities for HTTP-level configuration.

If you need more control over how your GraphQL server speaks HTTP, you should instead use an *integration*. Integrations are packages which connect the Apollo Server API to your favorite web framework.

Apollo maintains an [integration](https://www.apollographql.com/docs/apollo-server/api/express-middleware) between Apollo Server and [Express](https://expressjs.com/), the most popular Node.js web framework. The integration with Express v4 is published as [`@as-integrations/express4`](https://www.npmjs.com/package/@as-integrations/express), and the integration with Express v5 is published as [`@as-integrations/express5`](https://www.npmjs.com/package/@as-integrations/express5). Both packages export the function [`expressMiddleware`](https://www.apollographql.com/docs/apollo-server/api/express-middleware).

> Have you built, or are you maintaining, an Apollo Server integration that isn't listed here? Please [submit a PR](https://github.com/apollographql/apollo-server/blob/main/docs/source/integrations/integration-index.mdx) to be added to this list!

The larger community maintains the following open-source integrations for Apollo Server:

| Web Framework                                                            | Integration Package                                                                                                |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| [AWS Lambda](https://aws.amazon.com/lambda/)                             | [`@as-integrations/aws-lambda`](https://www.npmjs.com/package/@as-integrations/aws-lambda)                         |
| [Azure Functions](https://azure.microsoft.com/en-us/services/functions/) | [`@as-integrations/azure-functions`](https://www.npmjs.com/package/@as-integrations/azure-functions)               |
| [Cloudflare Workers](https://workers.cloudflare.com/)                    | [`@as-integrations/cloudflare-workers`](https://www.npmjs.com/package/@as-integrations/cloudflare-workers)         |
| [Google Functions](https://cloud.google.com/functions)                   | [`@as-integrations/google-cloud-functions`](https://www.npmjs.com/package/@as-integrations/google-cloud-functions) |
| [Fastify](https://fastify.io/)                                           | [`@as-integrations/fastify`](https://www.npmjs.com/package/@as-integrations/fastify)                               |
| [Hapi](https://hapi.dev/)                                                | [`@as-integrations/hapi`](https://www.npmjs.com/package/@as-integrations/hapi)                                     |
| [Koa](https://koajs.com/)                                                | [`@as-integrations/koa`](https://www.npmjs.com/package/@as-integrations/koa)                                       |
| [Next.js](https://nextjs.org/)                                           | [`@as-integrations/next`](https://www.npmjs.com/package/@as-integrations/next)                                     |
| [Nuxt](https://v3.nuxtjs.org/) / [h3](https://github.com/unjs/h3)        | [`@as-integrations/h3`](https://www.npmjs.com/package/@as-integrations/h3)                                         |

> Apollo does not provide official support for the above community-maintained libraries. We cannot guarantee that community-maintained libraries adhere to best practices or that they will continue to be maintained.

For those *building* a new integration library,  we'd like to welcome you (and your repository!) to the [`apollo-server-integrations`](https://github.com/apollo-server-integrations) Github organization alongside other community-maintained Apollo Server integrations. If you participate in our organization, you'll have the option to publish under our community's NPM scope `@as-integrations`, ensuring your integration is discoverable.
