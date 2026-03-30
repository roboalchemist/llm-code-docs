# Source: https://the-guild.dev/graphql/yoga-server/v4

Title: Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/v4

Markdown Content:
[Skip to Content](https://the-guild.dev/graphql/yoga-server/v4#nextra-skip-nav)

On This Page

**W arning**
This is the documentation for the **old GraphQL Yoga v 4**.

 We recommend upgrading to the latest GraphQL Yoga v5. [Migrate to GraphQL Yoga v5](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v4).

Quick start
-----------

GraphQL Yoga is a batteries-included cross-platform [GraphQL over HTTP spec-compliant](https://github.com/enisdenjo/graphql-http/tree/master/implementations/graphql-yoga) GraphQL server powered by [Envelop](https://envelop.dev/) and [GraphQL Tools](https://graphql-tools.com/) that runs anywhere; focused on easy setup, performance and great developer experience.

Installation[](https://the-guild.dev/graphql/yoga-server/v4#installation)
-------------------------------------------------------------------------

`npm i graphql-yoga graphql`

`pnpm add graphql-yoga graphql`

`yarn add graphql-yoga graphql`

`bun add graphql-yoga graphql`

Schema[](https://the-guild.dev/graphql/yoga-server/v4#schema)
-------------------------------------------------------------

You will need to provide a schema to Yoga, there are many ways to assemble a GraphQL schema, here’s just a few:

Use the `createSchema` function included in Yoga. It actually reuses the [`makeExecutableSchema` from @graphql-tools/schema](https://www.graphql-tools.com/docs/generate-schema).

schema.js

```
import { createSchema } from 'graphql-yoga'
 
export const schema = createSchema({
  typeDefs: /* GraphQL */ `
    type Query {
      hello: String
    }
  `,
  resolvers: {
    Query: {
      hello: () => 'world'
    }
  }
})
```

[`makeExecutableSchema` from @graphql-tools/schema](https://www.graphql-tools.com/docs/generate-schema) is very simple, but powerful. Install it and create a schema.

`npm i @graphql-tools/schema`

`pnpm add @graphql-tools/schema`

`yarn add @graphql-tools/schema`

`bun add @graphql-tools/schema`

schema.js

```
import { makeExecutableSchema } from '@graphql-tools/schema'
 
export const schema = makeExecutableSchema({
  typeDefs: /* GraphQL */ `
    type Query {
      hello: String
    }
  `,
  resolvers: {
    Query: {
      hello: () => 'world'
    }
  }
})
```

[Pothos](https://pothos-graphql.dev/) is a plugin based GraphQL schema builder for TypeScript. Install it and create a schema.

`npm i @pothos/core`

`pnpm add @pothos/core`

`yarn add @pothos/core`

`bun add @pothos/core`

schema.js

```
import SchemaBuilder from '@pothos/core'
 
const builder = new SchemaBuilder({})
 
builder.queryType({
  fields: t => ({
    hello: t.string({
      resolve: () => 'world'
    })
  })
})
 
export const schema = builder.toSchema()
```

Declarative, Code-First GraphQL Schemas for JavaScript/TypeScript through [Nexus GraphQL](https://nexusjs.org/). Install it and create schema.

`npm i nexus`

`pnpm add nexus`

`yarn add nexus`

`bun add nexus`

schema.js

```
import { makeSchema, queryField } from 'nexus'
 
const helloField = queryField('hello', {
  type: 'String',
  resolve: () => 'world'
})
 
export const schema = makeSchema({ types: [helloField] })
```

Code-first type-safe GraphQL schema without codegen or metaprogramming using [gqtx](https://github.com/sikanhe/gqtx). Install it and create schema.

`npm i gqtx`

`pnpm add gqtx`

`yarn add gqtx`

`bun add gqtx`

schema.js

```
import { buildGraphQLSchema, createTypesFactory } from 'gqtx'
 
const t = createTypesFactory()
 
const Query = t.queryType({
  fields: () => [
    t.field({
      name: 'hello',
      type: t.String,
      resolve: () => 'world'
    })
  ]
})
 
export const schema = buildGraphQLSchema({ query: Query })
```

[graphql-js](https://github.com/graphql/graphql-js) is a reference implementation of GraphQL for JavaScript. You should already have it installed, just create schema.

schema.js

```
import { GraphQLObjectType, GraphQLSchema, GraphQLString } from 'graphql'
 
export const schema = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: 'Query',
    fields: {
      hello: {
        type: GraphQLString,
        resolve: () => 'world'
      }
    }
  })
})
```

Server[](https://the-guild.dev/graphql/yoga-server/v4#server)
-------------------------------------------------------------

After you have created a GraphQL schema, simply pass it in to Yoga and liftoff! 🚀

```
import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
import { schema } from './schema'
 
// Create a Yoga instance with a GraphQL schema.
const yoga = createYoga({ schema })
 
// Pass it into a server to hook into request handlers.
const server = createServer(yoga)
 
// Start the server and you're done!
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Visit [`http://localhost:4000/graphql`](http://localhost:4000/graphql) to see Yoga in action.
