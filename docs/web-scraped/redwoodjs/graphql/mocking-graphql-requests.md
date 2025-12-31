# Source: https://docs.redwoodjs.com/docs/graphql/mocking-graphql-requests

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [GraphQL](/docs/graphql/index)
-   [Mocking GraphQL Requests]

[Version: 8.8]

On this page

<div>

# Mocking GraphQL Requests

</div>

Testing and building components without having to rely on the API is a good best practice. Redwood makes this possible via `mockGraphQLQuery` and `mockGraphQLMutation`.

The argument signatures of these functions are identical. Internally, they target different operation types based on their suffix.

``` 
mockGraphQLQuery('OperationName', (variables, ) => 
  }
})
```

## The operation name[​](#the-operation-name "Direct link to The operation name") 

The first argument is the [operation name](https://graphql.org/learn/queries/#operation-name); it\'s used to associate mock-data with a query or a mutation:

``` 
query UserProfileQuery 
mockGraphQLQuery('UserProfileQuery', )
```

``` 
mutation SetUserProfile 
mockGraphQLMutation('SetUserProfile', )
```

Operation names should be unique.

## The mock-data[​](#the-mock-data "Direct link to The mock-data") 

The second argument can be an object or a function:

``` 
mockGraphQLQuery('OperationName', (variables, ) => 
  }
})
```

If it\'s a function, it\'ll receive two arguments: `variables` and ``. The `ctx` object allows you to make adjustments to the response with the following functions:

-   `ctx.status(code: number, text?: string)`: set a http response code:

``` 
mockGraphQLQuery('OperationName', (_variables, ) => )
```

\

-   `ctx.delay(numOfMS)`: delay the response

``` 
mockGraphQLQuery('OperationName', (_variables, ) => 
})
```

\

-   `ctx.errors(e: GraphQLError[])`: return an error object in the response:

``` 
mockGraphQLQuery('OperationName', (_variables, ) => ])
})
```

### Typename[​](#typename "Direct link to Typename") 

If using [fragments](/docs/graphql/fragments) it is important to include the `__typename` otherwise Apollo client will not be able to map the mocked data to the fragment attributes.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]note

The `__typename: 'Book' as const` ensures that `'Book'` is considered to be a `type` and not a `string`.

## TypeScript[​](#typescript "Direct link to TypeScript") 

You can get stricter types by passing types when mocking the query, mutation and its variables:

``` 
import type  from 'types/graphql'

mockGraphQLQuery<UserProfileQuery, UserProfileQueryVariables>(
  'UserProfileQuery',
  
)
```

or, you can manually pass your own types:

``` 
mockGraphQLQuery <
  ,
  } >
  ('UserProfileQuery',
  )
```

## Global mock-requests vs local mock-requests[​](#global-mock-requests-vs-local-mock-requests "Direct link to Global mock-requests vs local mock-requests") 

Placing your mock-requests in `"<name>.mock.js"` will cause them to be globally scoped in Storybook, making them available to all stories.

> **All stories?**
>
> In React, it\'s often the case that a single component will have a deeply nested component that perform a GraphQL query or mutation. Having to mock those requests for every story can be painful and tedious.

Using `mockGraphQLQuery` or `mockGraphQLMutation` inside a story is locally scoped and will overwrite a globally-scoped mock-request.

We suggest always starting with globally-scoped mocks.

## Mocking a Cell\'s `QUERY`[​](#mocking-a-cells-query "Direct link to mocking-a-cells-query") 

To mock a Cell\'s `QUERY`, find the file ending with with `.mock.js` in your Cell\'s directory. This file exports a value named `standard`, which is the mock-data that will be returned for your Cell\'s `QUERY`.

UserProfileCell/UserProfileCell.js

``` 
export const QUERY = gql`
  query UserProfileQuery 
  }
`

// UserProfileCell/UserProfileCell.mock.js
export const standard = 
}
```

Since the value assigned to `standard` is the mock-data associated with the `QUERY`, modifying the `QUERY` means you also need to modify the mock-data.

UserProfileCell/UserProfileCell.js

``` 
export const QUERY = gql`
  query UserProfileQuery 
  }
`

// UserProfileCell/UserProfileCell.mock.js
export const standard = 
}
```

> **Behind the scenes**
>
> Redwood uses the value associated with `standard` as the second argument to `mockGraphQLQuery`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/graphql/mocking-graphql-requests.md)