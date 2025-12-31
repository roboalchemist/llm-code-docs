# Source: https://docs.redwoodjs.com/docs/how-to/mocking-graphql-in-storybook

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Mocking GraphQL in Storybook]

[Version: 8.8]

On this page

<div>

# Mocking GraphQL in Storybook

</div>

## Pre-requisites[​](#pre-requisites "Direct link to Pre-requisites") 

1.  Storybook should be running, start it by running `yarn rw storybook`
2.  Have a Cell, Query, or Mutation that you would like to mock

## Where to put mock-requests[​](#where-to-put-mock-requests "Direct link to Where to put mock-requests") 

1.  Mock-requests placed in a file ending with `.mock.js|ts` are automatically imported and become globally scoped, which means that they will be available in all of your stories.
2.  Mock-requests in a story will be locally scoped and will overwrite globally scoped mocks.

## Mocking a Cell\'s Query[​](#mocking-a-cells-query "Direct link to Mocking a Cell's Query") 

Locate the file ending with `.mock.js` in your Cell\'s folder. This file exports a value named `standard`, which is the mock-data that will be returned for your Cell\'s `QUERY`.

UserProfileCell/UserProfileCell.js

``` 
export const QUERY = gql`
  query UserProfileQuery 
  }
`

// UserProfileCell/UserProfileCell.mock.js
export const standard = ,
}
```

The value assigned to `standard` is the mock-data associated to the `QUERY`, so modifying the `QUERY` means you need to modify the mock-data.

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

> Behind the scenes: Redwood uses the value associated to `standard` as the second argument to `mockGraphQLQuery`.

### GraphQL request variables[​](#graphql-request-variables "Direct link to GraphQL request variables") 

If you want to dynamically modify mock-data based on a queries variables the `standard` export can also be a function, and the first parameter will be an object containing the variables:

UserProfileCell/UserProfileCell.mock.js

``` 
export const standard = (variables) => `,
    },
  }
}
```

## Mocking a GraphQL Query[​](#mocking-a-graphql-query "Direct link to Mocking a GraphQL Query") 

If you\'re not using a Cell, or if you want to overwrite a globally scoped mock, you can use `mockGraphQLQuery`:

Header/Header.stories.js

``` 
export const withReallyLongName = () => 
    }
  })
  return <Header />
}
```

## Mocking a GraphQL Mutation[​](#mocking-a-graphql-mutation "Direct link to Mocking a GraphQL Mutation") 

Use `mockGraphQLMutation`:

UserProfileCell/UserProfileCell.mock.js

``` 
export const standard =
  /* ... */

  mockGraphQLMutation('UpdateUserName', () => ,
    }
  })
```

## Mock-requests that intentionally produce errors[​](#mock-requests-that-intentionally-produce-errors "Direct link to Mock-requests that intentionally produce errors") 

`mockGraphQLQuery` and `mockGraphQLMutation` have access to `ctx` which allows you to modify the mock-response:

``` 
mockGraphQLQuery('UserProfileQuery', (_vars, ) => )
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/mocking-graphql-in-storybook.md)