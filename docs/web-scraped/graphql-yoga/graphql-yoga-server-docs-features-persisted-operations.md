# Source: https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations

Title: Persisted Operations | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations

Markdown Content:
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#nextra-skip-nav)

On This Page

Persisted Operations
--------------------

Persisted operations is a mechanism for preventing the execution of arbitrary GraphQL operation documents. By default, the persisted operations plugin follows the [the APQ Specification](https://github.com/apollographql/apollo-link-persisted-queries#apollo-engine) for **SENDING** hashes to the server.

However, you can customize the protocol to comply to other implementations e.g. used by [Relay persisted queries](https://relay.dev/docs/guides/persisted-queries/).

change this behavior by overriding the `getPersistedOperationKey` option to support Relay’s specification for example.

Quick Start[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#quick-start)
-------------------------------------------------------------------------------------------------------

Persisted operations requires installing a separate package.

`npm i @graphql-yoga/plugin-persisted-operations`

`pnpm add @graphql-yoga/plugin-persisted-operations`

`yarn add @graphql-yoga/plugin-persisted-operations`

`bun add @graphql-yoga/plugin-persisted-operations`

Persisted operation setup

```
import { createServer } from 'node:http'
import { createSchema, createYoga } from 'graphql-yoga'
import { usePersistedOperations } from '@graphql-yoga/plugin-persisted-operations'
 
const store = {
  ecf4edb46db40b5132295c0291d62fb65d6759a9eedfa4d5d612dd5ec54a6b38: '{__typename}'
}
 
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `
  }),
  plugins: [
    usePersistedOperations({
      getPersistedOperation(sha256Hash: string) {
        return store[sha256Hash]
      }
    })
  ]
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Start your yoga server and send the following request.

Execute persisted GraphQL operation

```
curl -X POST -H 'Content-Type: application/json' http://localhost:4000/graphql \
  -d '{"extensions":{"persistedQuery":{"version":1,"sha256Hash":"ecf4edb46db40b5132295c0291d62fb65d6759a9eedfa4d5d612dd5ec54a6b38"}}}'
 
{"data":{"__typename":"Query"}}
```

As you can see, the persisted operations plugin is able to execute the operation without the need to send the full operation document.

If you now sent a normal GraphQL operation that is not within the store, it will be rejected.

Arbitary GraphQL operation

```
curl -X POST -H 'Content-Type: application/json' http://localhost:4000/graphql \
  -d '{"query": "{__typename}"}'
 
{"errors":[{"message":"PersistedQueryOnly"}]}
```

Extracting client operations[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#extracting-client-operations)
-----------------------------------------------------------------------------------------------------------------------------------------

The recommended way of extracting the persisted operations from your client is to use [GraphQL Code Generator](https://www.graphql-code-generator.com/).

For people not using the client-preset the is also the standalone [`graphql-codegen-persisted-query-ids`](https://github.com/valu-digital/graphql-codegen-persisted-query-ids) plugin for extracting a map of persisted query ids and their corresponding GraphQL documents from your application/client-code in a JSON file.

Example map extracted by GraphQL Code Generator

```
{
  "ecf4edb46db40b5132295c0291d62fb65d6759a9eedfa4d5d612dd5ec54a6b38": "{__typename}",
  "c7a30a69b731d1af42a4ba02f2fa7a5771b6c44dcafb7c3e5fa4232c012bf5e7": "mutation {__typename}"
}
```

This map can then be used to persist the GraphQL documents in the server.

Use JSON file from filesystem as the persisted operation store

```
import { readFileSync } from 'node:fs'
import { createServer } from 'node:http'
import { createSchema, createYoga } from 'graphql-yoga'
import { usePersistedOperations } from '@graphql-yoga/plugin-persisted-operations'
 
const persistedOperations = JSON.parse(readFileSync('./persistedOperations.json', 'utf-8'))
 
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `
  }),
  plugins: [
    usePersistedOperations({
      getPersistedOperation(key: string) {
        return persistedOperations[key]
      }
    })
  ]
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Sending the hash from the client[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#sending-the-hash-from-the-client)
-------------------------------------------------------------------------------------------------------------------------------------------------

The persisted operations plugin follows the [the APQ Specification of Apollo](https://github.com/apollographql/apollo-link-persisted-queries#apollo-engine) for SENDING hashes to the server.

GraphQL clients such `Apollo Client` and `Urql` support that out of the box.

### Urql and GraphQL Code Generator[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#urql-and-graphql-code-generator)

When using the GraphQL Code Generator `client` preset together with urql, sending the hashes is straight-forward using the `@urql/exchange-persisted` package.

Urql Client Configuration

```
import { cacheExchange, createClient } from '@urql/core'
import { persistedExchange } from '@urql/exchange-persisted'
 
const client = new createClient({
  url: 'YOUR_GRAPHQL_ENDPOINT',
  exchanges: [
    cacheExchange,
    persistedExchange({
      enforcePersistedQueries: true,
      enableForMutation: true,
      generateHash: async (_, document) => document['__meta__']['hash']
    })
  ]
})
```

[More information on `@urql/exchange-persisted` on the the urql documentation](https://formidable.com/open-source/urql/docs/advanced/persistence-and-uploads/))

### Apollo Client and GraphQL Code Generator[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#apollo-client-and-graphql-code-generator)

When using the GraphQL Code Generator `client` preset together with Apollo Client, sending the hashes is straight-forward.

Apollo Client Configuration

```
import { ApolloClient, HttpLink, InMemoryCache } from '@apollo/client'
import { createPersistedQueryLink } from '@apollo/client/link/persisted-queries'
 
const link = createPersistedQueryLink({
  generateHash: document => document['__meta__']['hash']
})
 
const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: link.concat(new HttpLink({ uri: '/graphql' }))
})
```

[More information on the Apollo Client documentation](https://www.apollographql.com/docs/apollo-server/performance/apq/#step-2-enable-automatic-persisted-queries)

Using parsed GraphQL documents as AST[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#using-parsed-graphql-documents-as-ast)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

You can reduce the amount of work the server has to do by using the parsed GraphQL documents as AST.

Use parsed GraphQL documents as AST

```
import { parse } from 'graphql'
import {
  PersistedOperationType,
  usePersistedOperations
} from '@graphql-yoga/plugin-persisted-operations'
 
const persistedOperations = {
  'my-key': parse(/* GraphQL */ `
    query {
      __typename
    }
  `)
}
 
const plugin = usePersistedOperations({
  getPersistedOperation(key: string) {
    return persistedOperations[key]
  }
})
```

Skipping validation of persisted operations[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#skipping-validation-of-persisted-operations)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you validate your persisted operations while building your store, we recommend to skip the validation on the server. So this will reduce the work done by the server and the latency of the requests.

Validate persisted operations

```
const plugin = usePersistedOperations({
  //...
  skipDocumentValidation: true
})
```

> Using AST and skipping validations will reduce the amount of work the server has to do, so the requests will have less latency.

Allowing arbitrary GraphQL operations[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#allowing-arbitrary-graphql-operations)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes it is handy to allow non-persisted operations aside from the persisted ones. E.g. you want to allow developers to execute arbitrary GraphQL operations on your production server.

This can be achieved using the `allowArbitraryOperations` option.

Allow arbitrary GraphQL operations

```
const plugin = usePersistedOperations({
  allowArbitraryOperations: request =>
    request.headers.request.headers.get('x-allow-arbitrary-operations') === 'true'
})
```

Use this option with caution!

Using Relay’s Persisted Queries Specification[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#using-relays-persisted-queries-specification)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are using [Relay’s Persisted Queries specification](https://relay.dev/docs/guides/persisted-queries/#example-implemetation-of-relaylocalpersistingjs), you can configure the plugin like below;

Relay Persisted Queries example

```
import { createYoga, createSchema } from 'graphql-yoga'
import { createServer } from 'node:http'
import { usePersistedOperations } from '@graphql-yoga/plugin-persisted-operations'
 
const store = {
  ecf4edb46db40b5132295c0291d62fb65d6759a9eedfa4d5d612dd5ec54a6b38:
    '{__typename}'
}
 
const yoga = createYoga({
    schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `
  }),
  plugins: [
    usePersistedOperations({
      extractPersistedOperationId(params: GraphqlParams & { doc_id?: unknown }) {
        return typeof params.doc_id === 'string' ? params.doc_id : null
      }
      getPersistedOperation(key: string) {
        return store[key]
      },
    }),
  ],
})
 
const server = createServer(yoga)
server.listen(4000, () => {
    console.info('Server is running on http://localhost:4000/graphql')
})
```

Advanced persisted operation id Extraction from HTTP Request[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#advanced-persisted-operation-id-extraction-from-http-request)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can extract the persisted operation id from the request using the `extractPersistedOperationId`

### Query Parameters Recipe[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#query-parameters-recipe)

Extract persisted operation id from query parameters

```
import { createServer } from 'node:http'
import { createSchema, createYoga } from 'graphql-yoga'
import { usePersistedOperations } from '@graphql-yoga/plugin-persisted-operations'
 
const store = {
  ecf4edb46db40b5132295c0291d62fb65d6759a9eedfa4d5d612dd5ec54a6b38: '{__typename}'
}
 
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `
  }),
  plugins: [
    usePersistedOperations({
      getPersistedOperation(sha256Hash: string) {
        return store[sha256Hash]
      },
      extractPersistedOperationId(_params, request) {
        const url = new URL(request.url)
        return url.searchParams.get('id')
      }
    })
  ]
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

### Header Recipe[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#header-recipe)

You can also use the request headers to extract the persisted operation id.

Extract persisted operation id from headers

```
import { createServer } from 'node:http'
import { createSchema, createYoga } from 'graphql-yoga'
import { usePersistedOperations } from '@graphql-yoga/plugin-persisted-operations'
 
const store = {
  ecf4edb46db40b5132295c0291d62fb65d6759a9eedfa4d5d612dd5ec54a6b38: '{__typename}'
}
 
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `
  }),
  plugins: [
    usePersistedOperations({
      getPersistedOperation(sha256Hash: string) {
        return store[sha256Hash]
      },
      extractPersistedOperationId(_params, request) {
        return request.headers.get('x-document-id')
      }
    })
  ]
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

### Path Recipe[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#path-recipe)

You can also the the request path to extract the persisted operation id. This requires you to also customize the GraphQL endpoint. The underlying implementation for the URL matching is powered by the [URL Pattern API](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API).

This combination is powerful as it allows you to use the persisted operation id as it can easily be combined with any type of HTTP proxy cache.

Extract persisted operation id from path

```
import { createServer } from 'node:http'
import { createSchema, createYoga } from 'graphql-yoga'
import { usePersistedOperations } from '@graphql-yoga/plugin-persisted-operations'
 
const store = {
  ecf4edb46db40b5132295c0291d62fb65d6759a9eedfa4d5d612dd5ec54a6b38: '{__typename}'
}
 
const yoga = createYoga({
  graphqlEndpoint: '/graphql/:document_id?',
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `
  }),
  plugins: [
    usePersistedOperations({
      getPersistedOperation(sha256Hash: string) {
        return store[sha256Hash]
      },
      extractPersistedOperationId(_params, request) {
        return request.url.split('/graphql/').pop() ?? null
      }
    })
  ]
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Using an external Persisted Operation Store[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#using-an-external-persisted-operation-store)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

As a project grows the amount of GraphQL Clients and GraphQL Operations can grow a lot. At some point it might become impractible to store all persisted operations in memory.

In such a scenario you can use an external persisted operation store.

You can return a `Promise` from the `getPersistedOperation` function and call any database or external service to retrieve the persisted operation.

For the best performance a mixture of an LRU in-memory store and external persisted operation store is recommended.

Use external persisted operation store

```
import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
import { usePersistedOperations } from '@graphql-yoga/plugin-persisted-operations'
 
const yoga = createYoga({
  plugins: [
    usePersistedOperations({
      async getPersistedOperation(key: string) {
        return await fetch(`https://localhost:9999/document/${key}`).then(res => res.json())
      }
    })
  ]
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Using multiple Persisted Operation Stores[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#using-multiple-persisted-operation-stores)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can vary the persisted operations store you read from by switching based on the request.

An example of this may be to use request headers.

Use parsed GraphQL documents as AST

```
import { parse } from 'graphql'
import {
  PersistedOperationType,
  usePersistedOperations
} from '@graphql-yoga/plugin-persisted-operations'
 
const persistedOperationsStores = {
  ClientOne: {
    'my-key': parse(/* GraphQL */ `
      query {
        __typename
      }
    `)
  }
}
 
const plugin = usePersistedOperations({
  getPersistedOperation(key: string, request: Request) {
    const store = persistedOperationsStores[request.headers.get('client-name')]
    return (store && store[key]) || null
  }
})
```

Customize errors[](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations#customize-errors)
-----------------------------------------------------------------------------------------------------------------

This plugin can throw three different types of errors::

*   `PersistedOperationNotFound`: The persisted operation cannot be found.
*   `PersistedOperationKeyNotFound`: The persistence key cannot be extracted from the request.
*   `PersistedOperationOnly`: An arbitrary operation is rejected because only persisted operations are allowed.

Each error can be customized to change the HTTP status or add a translation message ID, for example.

Customize errors

```
import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
import { usePersistedOperations } from '@graphql-yoga/plugin-persisted-operations'
import { CustomErrorClass } from './custom-error-class'
 
const yoga = createYoga({
  plugins: [
    usePersistedOperations({
      customErrors: {
        // You can change the error message
        notFound: 'Not Found',
        // Or customize the error with a GraphqlError options object, allowing you to add extensions
        keyNotFound: {
          message: 'Key Not Found',
          extensions: {
            http: {
              status: 404
            }
          }
        },
        // Or customize with a factory function allowing you to use your own error class or format
        persistedQueryOnly: () => {
          return new CustomErrorClass('Only Persisted Operations are allowed')
        }
      }
    })
  ]
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```
