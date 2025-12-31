# Source: https://docs.redwoodjs.com/docs/graphql/trusted-documents

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [GraphQL](/docs/graphql/index)
-   [Trusted Documents]

[Version: 8.8]

On this page

<div>

# Trusted Documents

</div>

RedwoodJS can be setup to enforce [persisted operations](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations) -- alternatively called [Trusted Documents](https://benjie.dev/graphql/trusted-documents).

Use trusted documents if your GraphQL API is only for your own app (which is the case for most GraphQL APIs) for a massively decreased attack-surface, increased performance, and decreased bandwidth usage.

At app build time, Redwood will extract the GraphQL documents (queries, etc) and make them available to the server. At run time, you must then send \"document id\" or \"hash\" instead of the whole document as the server will only accept requests with a known document id.

This prevents malicious attackers from executing arbitrary GraphQL thus helping with unwanted resolver traversal or information leaking.

See [Configure Trusted Documents](#configure-trusted-documents) for more information and usage instructions.

## Trusted Documents Explained[​](#trusted-documents-explained "Direct link to Trusted Documents Explained") 

When configured to use Trusted Documents, your project will:

1.  When generating types, generate files in `web/src/graphql` needed for persisted aka trusted documents, for example:

``` 
 }",
  "46e9823d95110ebb2ef17ef82fff5c19a468f8a6": "query FindBlogPostQuery($id: Int!)  body createdAt id title } }",
  "421bcffdde84d448ec1a1b30b36eaeb966f00257": "query BlogPostsQuery  body createdAt id title } }",
  "f6ae606548009c2cd4c69b9aecebad0a730ba23d": "mutation DeleteContactMutation($id: Int!)  }",
  "f7d2df28fcf87b0c29d225df79363d1c69159916": "query FindContactById($id: Int!)  }",
  "7af93a7e454d9c59bbb77c14e0c78e99207fd0c6": "query FindContacts  }",
  "e01ad8e899ac908458eac2d1f989b88160a0494b": "query EditContactById($id: Int!)  }",
  "94f51784b918a52e9af64f3c1fd4356903b611f8": "mutation UpdateContactMutation($id: Int!, $input: UpdateContactInput!)  }",
  "da35778949e1e8e27b7d1bb6b2a630749c5d7060": "mutation CreateContactMutation($input: CreateContactInput!)  }",
  "4f880f909a16b7fe15898fe33a2ee26933466719": "query EditPostById($id: Int!)  }",
  "32b9225df81ff7845fedfa6d5c86c5d4a76073d2": "mutation UpdatePostMutation($id: Int!, $input: UpdatePostInput!)  }",
  "daf229dcea085f1beff91102a63c2ba9c88e8481": "mutation CreatePostMutation($input: CreatePostInput!)  }",
  "e3405f6dcb6460943dd604423f0f517bc8318aaa": "mutation DeletePostMutation($id: Int!)  }",
  "43a94ad9a150aa7a7a665c73a931a5b18b6cc28b": "query FindPostById($id: Int!)  }",
  "76308e971322b1ece4cdff75185bb61d7139e343": "query FindPosts  }",
  "287beba179ef2c4448b4d3b150701993eddc07d6": "query BlogPostsQueryTrustedPage  body createdAt id title } }"
}
```

2.  They contain the query and hash that represents and identifies that query
3.  Files with functions to lookup the generated trusted document such as:

``` 
// ...
export function graphql(
  source: '\n  query FindPosts \n  }\n'
): (typeof documents)['\n  query FindPosts \n  }\n']
// ...
export function gql(source: string) 
```

and the generated AST with the hash id in `web/src/graphql/graphql.ts`

``` 
// ...
export const FindPostsDocument = ,
  kind: 'Document',
  definitions: [
    ,
      selectionSet:  },
          ,
            selectionSet:  },
                 },
                 },
                 },
                 },
                 },
              ],
            },
          },
        ],
      },
    },
  ],
} as unknown as DocumentNode<FindPostsQuery, FindPostsQueryVariables>
// ...
```

so that when a query or mutation is made, the web side GraphQL client doesn\'t send the query, but rather **just the hash id** so that the GraphQL Server can lookup the pre-generated query to run.

``` 
,"extensions":}}
```

It does so by adding a `api/src/lib/trustedDocumentsStore.ts` file for use on the GraphQL api side.

``` 
export const store =  }',
  // ...
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

See how the `76308e971322b1ece4cdff75185bb61d7139e343` hash ids match?

Now, when the client requests to make a query for `76308e971322b1ece4cdff75185bb61d7139e343`, the GraphQL server knows to execute the corresponding query associated with that hash.

This means that because queries are pre-generated and the hash ids **must match**, there is no way for any un-trusted or ad-hoc queries to get executed by the GraphQL server.

Thus preventing unwanted queries or GraphQL traversal attacks,

-   Configure RedwoodJS to use Trusted Documents via `redwood.toml`
-   Configure the GraphQL Server

## Configure Trusted Documents[​](#configure-trusted-documents "Direct link to Configure Trusted Documents") 

Below are instructions to manually configure Trusted Documents in your RedwoodJS project.

Alternatively, you can use the `yarn redwood setup graphql trusted-documents` [CLI setup command](/docs/cli-commands#setup-graphql-trusted-docs).

### Configure redwood.toml[​](#configure-redwoodtoml "Direct link to Configure redwood.toml") 

Setting `trustedDocuments` to true will

-   populate `web/src/graphql` files with the pre-generated documents
-   inform Apollo GraphQL client to send the document hashes and not the query itself

``` 
...
[graphql]
  trustedDocuments = true
...
```

### Configure GraphQL Handler[​](#configure-graphql-handler "Direct link to Configure GraphQL Handler") 

As part of GraphQL type and codegen, the `trustedDocumentsStore` is created in `api/src/lib`.

This is the same information that is created in `web/src/graphql/persisted-documents.json` but wrapped in a `store` that can be easily imported and passed to the GraphQL Handler.

#### Store[​](#store "Direct link to Store") 

To enable trusted documents, configure `trustedDocuments` with the store.

``` 
import  from '@redwoodjs/graphql-server'

// ...
import  from 'src/lib/trustedDocumentsStore'

export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  trustedDocuments: ,
  onException: () => ,
})
```

#### Disable[​](#disable "Direct link to Disable") 

You can disable the trustedDocuments `useRedwoodTrustedDocuments` plugin. The `store` is then optional.

``` 
  trustedDocuments: 
```

#### Custom Errors[​](#custom-errors "Direct link to Custom Errors") 

The `persistedQueryOnly` error message defaults to `'Use Trusted Only!'`.

If you\'d like to customize the message when a query is not permitted, you can set the `persistedQueryOnly` configuration setting in `customErrors`:

``` 
  trustedDocuments: ,
  }
```

You can also define a function to returns a `GraphQLError`. This function has access to the `payload`.

``` 
  trustedDocuments: ,
    },
  }
```

In addition to the `persistedQueryOnly` custom error option, you can define error message for:

-   `notFound` - Error to be thrown when the persisted operation is not found
-   `keyNotFound` - Error to be thrown when the extraction of the persisted operation id failed

#### Skipping validation of persisted operations[​](#skipping-validation-of-persisted-operations "Direct link to Skipping validation of persisted operations") 

If you validate your persisted operations while building your store, we recommend to skip the validation on the server. So this will reduce the work done by the server and the latency of the requests.

``` 
  trustedDocuments: 
```

#### Allowing arbitrary GraphQL operations[​](#allowing-arbitrary-graphql-operations "Direct link to Allowing arbitrary GraphQL operations") 

Sometimes it is handy to allow non-persisted operations aside from the persisted ones. E.g. you want to allow developers to execute arbitrary GraphQL operations on your production server.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]Info

To support authentication, the `redwood.currentUser` query is always allowed.

Even if you define `allowArbitraryOperations` the plugin will always check for this request, so you don\'t need to add this check to any custom logic.

This can be achieved using the `allowArbitraryOperations` option.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]Important

Override this option with caution!

For example, you can get a header from the request and allow:

``` 
allowArbitraryOperations: (request) => 
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/graphql/trusted-documents.md)