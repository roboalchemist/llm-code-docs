# Source: https://www.apollographql.com/docs/apollo-server/api/apollo-server.md

# Source: https://www.apollographql.com/docs/apollo-server.md

# Introduction to Apollo Server

> 📣 **Apollo Server 5 is generally available!**
>
> Apollo Server 5 is a small upgrade focused largely on adjusting which dependency versions are supported. [Upgrading from v4 to v5](https://www.apollographql.com/docs/apollo-server/migration/) usually only takes a few minutes. Because the behavior of Apollo Server has changed minimally between v4 and v5, these docs document both versions.
>
> Still on Apollo Server 3? AS3 has been end-of-life since October 2024. We've got a [full migration guide for upgrading directly from v3 to v5](https://www.apollographql.com/docs/apollo-server/migration-from-v3/). Docs for v3 are [available here](https://www.apollographql.com/docs/apollo-server/v3/).

**Apollo Server is an [open-source](https://github.com/apollographql/apollo-server), spec-compliant GraphQL server** that's compatible with any GraphQL client, including [Apollo Client](https://www.apollographql.com/docs/react). It's the best way to build a production-ready, self-documenting GraphQL API that can use data from any source.

#### You can use Apollo Server as:

* The GraphQL server for a [subgraph](https://www.apollographql.com/docs/apollo-server/using-federation/apollo-subgraph-setup) in a federated supergraph
* An add-on to any new or existing Node.js apps—this includes apps running on [Express](https://www.apollographql.com/docs/apollo-server/api/express-middleware) (including [MERN stack](https://www.apollographql.com/docs/apollo-server/integrations/mern) apps), [AWS Lambda](https://www.npmjs.com/package/@as-integrations/aws-lambda), [Azure Functions](https://www.npmjs.com/package/@as-integrations/azure-functions), [Cloudflare](https://www.npmjs.com/package/@as-integrations/cloudflare-workers), [Fastify](https://www.npmjs.com/package/@as-integrations/fastify), and [more](https://www.apollographql.com/docs/apollo-server/integrations/integration-index)

#### Apollo Server provides:

* **Straightforward setup**, so your client developers can start fetching data quickly
* **Incremental adoption**, enabling you to add features as they're needed
* **Universal compatibility** with any data source, any build tool, and any GraphQL client
* **Production readiness**, enabling you to confidently run your graph in production

#### Ready to try it out?

Get started!
