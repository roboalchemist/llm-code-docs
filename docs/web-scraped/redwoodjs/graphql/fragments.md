# Source: https://docs.redwoodjs.com/docs/graphql/fragments

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [GraphQL](/docs/graphql/index)
-   [Fragments]

[Version: 8.8]

On this page

<div>

# Fragments

</div>

[GraphQL fragments](https://graphql.org/learn/queries/#fragments) are reusable units of GraphQL queries that allow developers to define a set of fields that can be included in multiple queries. Fragments help improve code organization, reduce duplication, and make GraphQL queries more maintainable. They are particularly useful when you want to request the same set of fields on different parts of your data model or when you want to share query structures across multiple components or pages in your application.

## What are Fragments?[​](#what-are-fragments "Direct link to What are Fragments?") 

Here are some key points about GraphQL fragments:

1.  **Reusability**: Fragments allow you to define a set of fields once and reuse them in multiple queries. This reduces redundancy and makes your code more DRY (Don\'t Repeat Yourself).

2.  **Readability**: Fragments make queries more readable by separating the query structure from the actual query usage. This can lead to cleaner and more maintainable code.

3.  **Maintainability**: When you need to make changes to the requested fields, you only need to update the fragment definition in one place, and all queries using that fragment will automatically reflect the changes.

## Basic Usage[​](#basic-usage "Direct link to Basic Usage") 

Here\'s a basic example of how you might use GraphQL fragments in developer documentation:

Let\'s say you have a GraphQL schema representing books, and you want to create a fragment for retrieving basic book information like title, author, and publication year.

``` 
# Define a GraphQL fragment for book information
fragment BookInfo on Book 

# Example query using the BookInfo fragment
query GetBookDetails($bookId: ID!) 
}
```

In this example:

-   We\'ve defined a fragment called `BookInfo` that specifies the fields we want for book information.
-   In the `GetBookDetails` query, we use the `...BookInfo` spread syntax to include the fields defined in the fragment.
-   We also include additional fields specific to this query, such as `description`.

By using the `BookInfo` fragment, you can maintain a consistent set of fields for book information across different parts of your application without duplicating the field selection in every query. This improves code maintainability and reduces the chance of errors.

In developer documentation, you can explain the purpose of the fragment, provide examples like the one above, and encourage developers to use fragments to organize and reuse their GraphQL queries effectively.

## Using Fragments in RedwoodJS[​](#using-fragments-in-redwoodjs "Direct link to Using Fragments in RedwoodJS") 

RedwoodJS makes it easy to use fragments, especially with VS Code and Apollo GraphQL Client.

First, RedwoodJS instructs the VS Code GraphQL Plugin where to look for fragments by configuring the `documents` attribute of your project\'s `graphql.config.js`:

``` 
// graphql.config.js

const  = require('@redwoodjs/internal')

module.exports = ', // 👈 Tells VS Code plugin where to find fragments
}
```

Second, RedwoodJS automatically creates the [fragmentRegistry](https://www.apollographql.com/docs/react/data/fragments/#registering-named-fragments-using-createfragmentregistry) needed for Apollo to know about the fragments in your project without needing to interpolate their declarations.

Redwood exports ways to interact with fragments in the `@redwoodjs/web/apollo` package.

``` 
import  from '@redwoodjs/web/apollo'
```

With `fragmentRegistry`, you can interact with the registry directly.

With `registerFragment`, you can register a fragment with the registry and get back:

``` 

```

which can then be used to work with the registered fragment.

### Setup[​](#setup "Direct link to Setup") 

`yarn rw setup graphql fragments`

See more in [cli commands - setup graphql fragments](/docs/cli-commands#setup-graphql-fragments).

### registerFragment[​](#registerfragment "Direct link to registerFragment") 

To register a fragment, you can simply register it with `registerFragment`.

``` 
import  from '@redwoodjs/web/apollo'

registerFragment(gql`
  fragment BookInfo on Book 
`)
```

This makes the `BookInfo` available to use in your query:

``` 
import type  from 'types/graphql'

import  from '@redwoodjs/web'

import BookInfo from 'src/components/BookInfo'

const GET_BOOK_DETAILS = gql`
  query GetBookDetails($bookId: ID!) 
  }

...

const  = useQuery<GetBookDetails>(GET_BOOK_DETAILS)
```

You can then access the book info from `data` and render:

``` 
`}>
    <h3>Title: </h3>
    <p>by  ()<>
  </div>
)}
```

### fragment[​](#fragment "Direct link to fragment") 

Access the original fragment you registered.

``` 
import  from '@redwoodjs/web/apollo'
```

### typename[​](#typename "Direct link to typename") 

Access typename of fragment you registered.

``` 
import  from '@redwoodjs/web/apollo'
```

For example, with

``` 
# Define a GraphQL fragment for book information
fragment BookInfo on Book 
```

the `typename` is `Book`.

### getCacheKey[​](#getcachekey "Direct link to getCacheKey") 

A helper function to create the cache key for the data associated with the fragment in Apollo cache.

``` 
import  from '@redwoodjs/web/apollo'
```

For example, with

``` 
# Define a GraphQL fragment for book information
fragment BookInfo on Book 
```

the `getCacheKey` is a function where `getCacheKey(42)` would return `Book:42`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

We describe how [cache keys and identifiers](/docs/graphql/caching#identify) are used in more depth in the our [Apollo client cache](/docs/graphql/caching#client-caching) documentation.

### useRegisteredFragment[​](#useregisteredfragment "Direct link to useRegisteredFragment") 

``` 
import  from '@redwoodjs/web/apollo'

const  = registerFragment()
// ...
```

A helper function relies on Apollo\'s [`useFragment` hook](https://www.apollographql.com/docs/react/data/fragments/#usefragment) in Apollo cache.

The useFragment hook represents a lightweight live binding into the Apollo Client Cache. It enables Apollo Client to broadcast specific fragment results to individual components. This hook returns an always-up-to-date view of whatever data the cache currently contains for a given fragment. useFragment never triggers network requests of its own.

This means that once the Apollo Client Cache has loaded the data needed for the fragment, one can simply render the data for the fragment component with its id reference.

Also, anywhere the fragment component is rendered will be updated with the latest data if any of `useQuery` with uses the fragment received new data.

``` 
import type  from 'types/graphql'

import  from '@redwoodjs/web/apollo'

const  = registerFragment(
  gql`
    fragment BookInfo on Book 
  `
)

const Book = (: ) =>  = useRegisteredFragment<Book>(id)

  return (
    complete && (
      <div key=`}>
        <h3>Title: </h3>
        <p>by  ()<>
      </div>
    )
  )
}

export default Book
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

In order to use [fragments](#what-are-fragments) with [unions](/docs/graphql#unions) and interfaces in Apollo Client, you need to tell the client how to discriminate between the different types that implement or belong to a supertype.

Please see how to [generate possible types from fragments and union types](#possible-types-for-unions).

## Possible Types for Unions[​](#possible-types-for-unions "Direct link to Possible Types for Unions") 

In order to use [fragments](#fragments) with [unions](#unions) and interfaces in Apollo Client, you need to tell the client how to discriminate between the different types that implement or belong to a supertype.

You pass a possibleTypes option to the InMemoryCache constructor to specify these relationships in your schema.

This object maps the name of an interface or union type (the supertype) to the types that implement or belong to it (the subtypes).

For example:

``` 
/// web/src/App.tsx

<RedwoodApolloProvider graphQLClientConfig=,
  },
}}>
```

To make this easier to maintain, RedwoodJS GraphQL CodeGen automatically generates `possibleTypes` so you can simply assign it to the `graphQLClientConfig`:

``` 
// web/src/App.tsx

import possibleTypes from 'src/graphql/possibleTypes'

// ...

const graphQLClientConfig = ,
}

<RedwoodApolloProvider graphQLClientConfig=>
```

To generate the `src/graphql/possibleTypes` file, enable fragments in `redwood.toml`:

``` 
[graphql]
  fragments = true
```

## Testing, Storybook and Mock Data[​](#testing-storybook-and-mock-data "Direct link to Testing, Storybook and Mock Data") 

When using fragments with test or Storybook, it is important that you define your mock data correctly.

By including the `__typename` and the GraphQL Type for the mocked data object, you ensure that Apollo Client will handle the information when working with the cache or fragments.

For example, consider the fragment `BookInfo` used by the query `GetBookDetails`.

``` 
import type  from 'types/graphql'

import  from '@redwoodjs/web/apollo'

const  = registerFragment(gql`
  fragment BookInfo on Book 
`)
```

``` 
import type  from 'types/graphql'

import  from '@redwoodjs/web'

import BookInfo from 'src/components/BookInfo'

const GET_BOOK_DETAILS = gql`
  query GetBookDetails($bookId: ID!) 
  }
```

### Mock Data[​](#mock-data "Direct link to Mock Data") 

To satisfy the query as well as the fragment needs your mock data should include the `Book` typename:

``` 
export const standard = ,
}
```

If using [fragments](/docs/graphql/fragments) it is important to include the `__typename` otherwise Apollo client will not be able to map the mocked data to the fragment attributes.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]note

The `__typename: 'Book' as const` ensures that `'Book'` is considered to be a `type` and not a `string`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/graphql/fragments.md)