# Source: https://docs.redwoodjs.com/docs/tutorial/chapter2/side-quest

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 2]
-   [Side Quest: How Redwood Works with Data]

[Version: 8.8]

<div>

# Side Quest: How Redwood Works with Data

</div>

Redwood likes GraphQL. We think it\'s the API of the future. Our GraphQL implementation is built with [Apollo](https://www.apollographql.com/) (on the client) and [GraphQL Yoga & Envelop](https://www.graphql-yoga.com) (on the server). Remember in our file system layout, there was a directory `api/src/functions` and a single file in there, `graphql.ts`. If you were to deploy your app to a [serverless](https://en.wikipedia.org/wiki/Serverless_computing) stack (which we will do later in the [Deployment](/docs/tutorial/chapter4/deployment) section), that `graphql.ts` file would be compiled into a serverless function and would become the GraphQL API endpoint. Here\'s how a typical GraphQL query works its way through your app:

![Redwood Data Flow](https://user-images.githubusercontent.com/300/75402679-50bdd180-58ba-11ea-92c9-bb5a5f4da659.png)

The front-end uses [Apollo Client](https://www.apollographql.com/docs/react/) to create a GraphQL payload sent to [GraphQL Yoga](https://www.graphql-yoga.com) and [Envelop](https://www.envelop.dev/docs), which that `graphql.ts` file acts as the entry-point to.

The `*.sdl.ts` files in `api/src/graphql` define the GraphQL [Object](https://www.apollographql.com/docs/tutorial/schema/#object-types), [Query](https://www.apollographql.com/docs/tutorial/schema/#the-query-type) and [Mutation](https://www.apollographql.com/docs/tutorial/schema/#the-mutation-type) types and thus the interface of your API.

Normally you would write a [resolver map](https://www.graphql-tools.com/docs/resolvers) that contains all your resolvers and explains to your GraphQL server how to map them to your SDL. But putting business logic directly in the resolver map would result in a very big file and horrible reusability, so you\'d be well advised to extract all the logic out into a library of functions, import them, and call them from the resolver map, remembering to pass all the arguments through. Ugh, that\'s a lot of effort and boilerplate, and still doesn\'t result in very good reusability.

Redwood has a better way! Remember the `api/src/services` directory? Redwood will automatically import and map resolvers from the corresponding **services** file onto your SDL. At the same time, it allows you to write those resolvers in a way that makes them easy to call as regular functions from other resolvers or services. That\'s a lot of awesomeness to contemplate, so let\'s show an example.

Consider the following SDL JavaScript snippet:

-   JavaScript
-   TypeScript

api/src/graphql/posts.sdl.js

``` 
export const schema = gql`
  type Post 

  type Query 

  input CreatePostInput 

  input UpdatePostInput 

  type Mutation 
`
```

api/src/graphql/posts.sdl.ts

``` 
export const schema = gql`
  type Post 

  type Query 

  input CreatePostInput 

  input UpdatePostInput 

  type Mutation 
`
```

In this example, Redwood will look in `api/src/services/posts/posts.ts` for the following five resolvers:

-   `posts()`
-   `post()`
-   `createPost()`
-   `updatePost()`
-   `deletePost()`

To implement these, simply export them from the services file. They will usually get your data from a database, but they can do anything you want, as long as they return the proper types that GraphQL Yoga expects based on what you defined in `posts.sdl.ts`.

-   JavaScript
-   TypeScript

api/src/services/posts/posts.js

``` 
import  from 'src/lib/db'

export const posts = () => 

export const post = () => ,
  })
}

export const createPost = () => )
}

export const updatePost = () => ,
  })
}

export const deletePost = () => ,
  })
}
```

api/src/services/posts/posts.ts

``` 
import  from 'src/lib/db'
import type  from 'types/graphql'

export const posts: QueryResolvers['posts'] = () => 

export const post: QueryResolvers['post'] = () => ,
  })
}

export const createPost: MutationResolvers['createPost'] = () => )
}

export const updatePost: MutationResolvers['updatePost'] = () => ,
  })
}

export const deletePost: MutationResolvers['deletePost'] = () => ,
  })
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Yoga/Envelop assumes these functions return promises, which `db` (an instance of `PrismaClient`) does. Yoga/Envelop waits for them to resolve before responding with your query results, so you don\'t need to worry about `async`/`await` or mess with callbacks yourself.

You may be wondering why we call these implementation files \"services\". While this example blog doesn\'t get complex enough to show it off, services are intended to be an abstraction **above** single database tables. For example, a more complex app may have a \"billing\" service that uses both a `transactions` table and a `subscriptions` table. Some of the functionality of this service may be exposed via GraphQL, but only as much as you like.

You don\'t have to make each function in your service available via GraphQL---leave it out of your `Query` and `Mutation` types and it won\'t exist as far as GraphQL is concerned. But you could still use it yourself---services are just JavaScript functions so you can use them anywhere you\'d like:

-   From another service
-   In a custom lambda function
-   From a completely separate, custom API

By dividing your app into well-defined services and providing an API for those services (both for internal use **and** for GraphQL), you will naturally start to enforce separation of concerns and increases the maintainability of your codebase.

Back to our data flow: Yoga/Envelop has called the resolver which, in our case, retrieved data from the database. Yoga/Envelop digs into the object and returns only the key/values that were asked for in the GraphQL query. It then packages up the response in a GraphQL payload and returns it to the browser.

If you\'re using a Redwood **cell** then this data will be available to you in your `Success` component ready to be looped through and/or displayed like any other React component.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter2/side-quest.md)